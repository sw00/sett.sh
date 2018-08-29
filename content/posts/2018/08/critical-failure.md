---
title: "Critical failure, deceptive assumptions"
slug: critical-failure
date: 2018-08-28T17:46:57+02:00
draft: true
markdown: mmark
tags: ["failure", "software-dev"]

---

The biggest critical failure that I've ever
experienced on a project happened on the first
week of 2014 and caused a recurring outage that
lasted a full four days.

It was my very first large-scale, distributed
production system with multi-national
integrations and real-time messaging component.
I had been on the project for 3 months and had
inherited the tech lead role which I shared
with a senior colleague who had joined after
me. Suffice to say we lost a lifetime's worth
of sleep that week.

The project itself was replete with problems.
In spite of the excellent technical foundations
the original tech leads had laid, the core web
application had been eroded into a
(well-tested) ball of mud[^mud] and for various
legitimate reasons nobody understood the
current runtime architecture or how it got
deployed to production[^automation].

> "A Big Ball of Mud is a haphazardly
> structured, sprawling, sloppy,
> duct-tape-and-baling-wire, spaghetti-code
> jungle. These systems show unmistakable signs
> of unregulated growth, and repeated,
> expedient repair."[^mud]

Our client, the product owner, had been using
us to bootstrap his startup and was
aggressively chasing growth (i.e. features)
without any reprieve for almost 2
years[^agile]. All while leveraging a
relatively inexperienced team that suffered
high attrition, unhealthy levels of priority
and context-switching, breaks in project
continuity and working in a highly
sophisticated tech stack nobody had any
significant experience in[^nonprofit].

There was a lot of firefighting and the
problems seemed serious enough that I was
absolutely terrified of not being able to cope.
So armed with a rigorous report of about two
dozen urgent "tech debt" items, I recommended a
complete feature freeze as my first act as tech
lead. Alas, greatness is not achieved by
capitulating to the demands of harsh reality,
so feature development was (of course)
prioritised above all else.

![Scotty from Star Trek](https://i.imgflip.com/1rojys.jpg#c)

It was certainly not ideal, but the journey to
finding the root cause was not without some
personal cognitive failures (jumping to
conclusions is best done in an excited panic).

# The technical details

The central part of the system was a few message broker(worker) processes that
would respond directly to incoming user messages fast as possible[^brokers]. In
practice this was a bunch of Celery workers subscribed to queues on a RabbitMQ
cluster and acting on data lookups to a MongoDB cluster. Because there was some
business logic they needed to leverage, the workers lived in the same
repository as the Django web application to keep things DRY. There was actually
more than one type of worker and they were differentiated by means of [injected
configuration](https://12factor.net/config). These workers were failing to
reply to incoming messages and we didn't know why. It was a highly critical
problem, and in certain cases could lead to a potential life-and-death
situation. No pressure.

We couldn't find any issue in staging and we hadn't deployed in the past two
weeks. It was also clear that the usual approaches to debugging[^debugging] could not be applied:

* Production was orders of magnitude larger than staging (thanks MongoDB and
  "big" data)

I think it had almost reached the 300GB upper bound of the
Linode disk we had provisioned for it. For testing, we had a job regularly sync
a small subset of records from the production cluster to the much smaller
staging instances.

* We couldn't be sure what production actually looked like versus what it was
  meant to look like.

There was a collection of Puppet manifests and roles that were mostly
inscrutable due to my lack of experience with its Ruby-esque DSL and best
practices hadn't quite emerged yet [^puppet]. Also we didn't know when last the
scripts had been run and (to my abject horror) I found lots of dead code and
traces of orphaned configuration on some of the servers themselves. This was
also before the advent of docker and immutable, phoenix servers. In fact it was
everybody's first signficant exposure to Infrastructure as Code[^iac],
including my own[^impostor].

# Assume the assumption pose

So what could be done? Of course, I thought, this is exactly what automated
build & deployment pipelines are for and promptly redeployed the latest trunk
to production. It seemed to resolve the issue, we could see the messages being
picked up and responded to\...at least until the afternoon when it stubbornly
reappeared. And so the pattern would repeat: deploy, fixed, broken again,
deploy, fixed, broken again. The definition of insanity.

Toward the end of the day, mild panic had set in. We reviewed the brokers' code
over and over, ran some production data through staging and observed the output
by logs and queries to Mongo. I dreaded the seemingly inevitable realisation
that something was wrong with the infrastructure itself. Perhaps the Linode, or
even the way RabbitMQ is configured causing an edge case bug to appear (the two
most opaque parts of the system for all of us).

I didn't sleep much that night and spent most of it reading up on everything I
possibly could on message queues and brokers. I also looked through RabbitMQ's
mailing lists and issues looking for a mention of similar symptoms and in the
hopes of finding a quick fix. Stackoverflow posts were made. And at some point
I even logged into the Freenode chatroom to ask for assistance.

Day two came around and it was clear to me that we had to pursue the nuclear
option: we needed to rebuild production. This entailed provisioning new Linode
machines and running the dubious Puppet scripts against them, then carefully
teasing apart each Linode box and reconstituting them into the new clusters. I
was also  wary of copying the problem over to the new environment so it was a
manual process of educated _guesswork_ and _intuition_, by poor developers with
the minimal experience in system adminstration. There is no
universe in which this is an even remotely pleasant experience, but we were
forced to learn the system's run state configuration quite intimately and make
best-effort decisions where there were gaps and ambiguities\...

# Too tired to despair

I don't remember all of it, but I believe this took us the next whole day and
half. And it was unsuccessful. To my complete disbelief, the issue had managed
to follow us into a fresh environment. I was too tired to even despair and
mulled over the terrible consequences to come. I mentally prepared myself to
the reality that this might cause the client's company to collapse and I might be losing my job[^job]. So it goes.

Then, as I tried eat my lunch with a dry mouth, fatigued, my thoughts wandered to something I had seen in the codebase during the whole ordeal. Some of the
Celery workers were set to operate on a timer to complete _recurring_ tasks
instead of responding to messages. The purpose of these tasks were to generate
reports from MongoDB records and they were set to run every 5 minutes to
provide an almost real-time statistics. But why couldn't they be in realtime?

Fuck.

The dots finally connected and coalesced into a single phrase I muttererd out
loud: "fuck you, map reduce."

# Two facts, two implications, one conclusion

* Celery uses a backend broker to consume messages _and_ schedule tasks.

  * This means a worker with a scheduled, recurring task is not just a consumer, but pushes messages on to RabbitMQ.

* The processing of reports is a long-running MapReduce across all records in the most populous MongoDB collection.

  * This collection has been growing at a linear rate since the project's first deployment and so too would its running time.

**Conlusion**: The time it took to run the reports had overtaken the scheduling
period. The natural consequence of this was that on average, more tasks were
being created than completed so over time the possibility of completing tasks trended toward zero.

# The solution
The immediate fix was trivial. Increase the
scheduled period to be much longer than the
time it takes to run the report. However, this
was also a result of a flaw in our
configuration there was no separation of
concerns reflected in our RabbitMQ setup. It
might have been an acceptable shortcut to have
all brokers share the same queues in the
beginning, but it wasn't any longer. Lesson
learnt, we gave the long-running workers their
own queues.

But this only kicks the can down the road a
little further. The complete solution was to to
refactor the mapreduce code to operate on a
rolling window of the records instead of the
entire collection. Something I will never
forget now whenever I'm  writing
report-generating code.

---

# The meta-solution

The issue and its solution seems quite
arbitrary in retrospect. Any dev better versed
in RabbitMQ and Celery would have gleaned the
problem immediately by inspecting the RabbitMQ
admin console and its queues. But I wondered if
we could've done better and how I could avoid
dead-ends.

It turns out we can. It's all about being a
little more rigorous and explicit with our
assumptions. Doing so exposes our biases when
debugging and troubleshooting an issue.
If we felt like overachieving, it may also be
helpful to slow down and actually write down:

1. the behaviour we're seeing
2. its potential causes
3. a list of hypotheses (along with observable behaviour that would falsify them)

Godmode would of course be writing this all in
*first-order predicate calculus* and you'd
certainly make Djikstra proud. But having a
general grasp of it should be good enough.

There is however an extremely important idea
that have helped me in my thinking: the
difference between _necessary_ and _sufficient_
conditions.

# The mechanics of causality

In logic there is a notion of _implication_,
which for our intents and purposes can be
regarded as analogous to causality[^causality].

It's often denoted with an arrow like so: $$\rightarrow$$

When we say a condition <div>$$A$$</div> holds.

[^mud]: [Brian Foote and Joseph Yoder, _Big Ball of Mud_. Fourth Conference on Patterns Languages of Programs (PLoP '97/EuroPLoP '97) Monticello, Illinois, September 1997](http://laputan.org/mud/)

[^automation]: The dark side to automation is that it reduces the need for humans to understand what's under the hood. There was a fully automated build and deploy pipeline and infrastructure defined in Puppet that nobody dared to touch for lack of expertise.

[^nonprofit]: The work was originally billed as non-profit, social impact which has a tendency to be viewed as trivial and thus staffed accordingly. Ironically, it was actually the most technically sophisticated project I've ever worked with in some respects.

[^agile]: Unfortunately, they'd also been bitten with the Agile bug in the wrong way and seemed to think that it meant no process and spontaneous changing of priorities.

[^brokers]: At its peak, this could be up to 400 messages a minute, by 4 generalised service brokers.

[^life-death]: I'm not comfortable sharing but those of you who know me can ask about it in person.

[^debugging]: Try to replicate the problem in another environment, then poke and prod until you find the cause.

[^iac]: Declaring your infrastructure in code so that it can be built and tested automatically just like your application software. There's a whole set of principles and practices to this but think Puppet, Chef, Ansible and you're on the right track.

[^puppet]: For the record, Puppet is my least favourite Config Management tool even years later.

[^impostor]: Compound this with the fact that I had only just learnt what a message broker even is and had only dealt with NoSQL document data stores in theory and you have a hot mess of doubt and well-justified impostor syndrome.

[^job]: A crazy thought in retrospect, but I've had many such scenarios throughout my career.

[^imagine]: It's easy to imagine a universe where the laws of physics are different. But not one in which logic doesn't apply.

[^causality]: Be careful though, it's really not the [same thing](https://philosophy.stackexchange.com/questions/24170/causality-vs-implication).
