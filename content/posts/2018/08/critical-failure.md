---
title: "Critical failure and the Mechanics of Causality"
slug: critical-failure
date: 2018-08-28T17:46:57+02:00
draft: true
markdown: mmark
tags: ["failure", "software-dev"]

---

The most critical failure that I've ever experienced on a project happened on
the first week of 2014 and caused a recurring outage that lasted a full four
days.

It was my very first large-scale, distributed production system with
multi-national integrations and real-time messaging component. I had been on
the project for 3 months and had inherited the tech lead role which I shared
with a senior colleague who had joined after me. Suffice to say we lost a
lifetime's worth of sleep that week. 

The project itself was replete with problems. In spite of the excellent
technical foundations the original tech leads had laid, the core web
application had been eroded into a (well-tested) ball of mud[^mud] and for
various legitimate reasons nobody understood the current runtime architecture
or how it got deployed to production[^automation].

> "A Big Ball of Mud is a haphazardly structured, sprawling, sloppy,
> duct-tape-and-baling-wire, spaghetti-code jungle. These systems show
> unmistakable signs of unregulated growth, and repeated, expedient
> repair."[^mud]

Our client, the product owner, had been using us to bootstrap his startup and
was aggressively chasing growth (i.e. features) without any reprieve for almost
2 years[^agile]. All while leveraging a relatively junior team that suffered
high attrition, unhealthy levels of priority and context-switching, breaks in
project continuity and working in a highly sophisticated tech stack nobody had
any significant experience in[^nonprofit]. 

There was a lot of firefighting and the problems seemed serious enough that I
was absolutely terrified of not being able to cope. So armed with a three-page
report of about two dozen urgent items, I recommended a complete feature freeze
as my first act as tech lead.  Alas, greatness is not achieved by capitulating
to the demands of harsh reality, so feature development was always prioritised
above all else.

![Scotty from Star Trek](https://i.imgflip.com/1rojys.jpg#c)

It was certainly not ideal, but the journey to finding the root cause was not
without some personal cognitive failures (jumping to conclusions is best done
in an excited panic).

# The technical details
The critical part of the system was a few message broker processes that would
respond directly to incoming user messages fast as possible[^brokers]. In
practice this was a bunch of Celery workers subscribed to queues on a RabbitMQ
cluster and acting on data lookups to a MongoDB cluster. Because there was some
business logic they needed to leverage, the workers lived in the same
repository as the Django web application to keep things DRY. There was actually
more than one type of worker that was differentiated by means of [injected
configuration](https://12factor.net/config). These workers were failing to
reply to incoming messages and we didn't know why. It was highly critical
problem, and in certain cases a potential life-and-death situation.

The issue was not observed in staging and we hadn't deployed in the past two
weeks. It was also clear that that was the usual approaches to debugging[^debugging] could not be applied:

* Production was orders of magnitude larger than staging (thanks MongoDB and
  "Big Data")

I think it had almost reached the 300GB upper bound of the
Linode disk we had provisioned for it. For testing, we had a job regularly sync
a small subset of records from the production cluster to the much smaller
staging instances.

* We couldn't be sure what production actually looked like versus what it was meant to look like. 

There was a collection of Puppet manifests and roles that were mostly
inscrutable due to my lack of experience with its Ruby-esque DSL and Best
practices hadn't quite emerged yet [^puppet]. Also we didn't know when last the
scripts had been run and (to my abject horror) I found lots of dead code and
traces of orphaned configuration on some of the servers themselves. This was
also before the advent of docker and immutable, phoenix servers. In fact it was
everybody's first signficant exposure to Infrastructure as Code[^iac],
including my own[^impostor]. 

So what could be done? Of course, I thought, this is exactly what automated
build & deployment pipelines are for and promptly redeployed the latest trunk
to production. It seemed to resolve the issue, we could see the messages being
picked up and responded to at least until the next hour. And so the pattern
would repeat: deploy, fixed, broken again, deploy, fixed, broken again.

Toward the end of the day, mild panic had set in. We reviewed the code over and
over, ran some production data through staging and observed the output by logs
and queries to Mongo. I dreaded the seemingly inevitable realisation that
something was wrong with the infrastructure itself. Perhaps the Linode, or even
the way RabbitMQ is configured (the two most opaque parts of the system for all
of us). I didn't sleep the first night and spent it looking through RabbitMQ's mailing lists and issues looking for a mention of similar symptoms and perhaps a quick fix.

# The mechanics of causality

Implication is a property of our universe. This is quite interesting because this is probably a fundamental property of our universe[^imagine]

$$ A \rightarrow{} B$$

"If A then B."
If A holds, then B holds.

A is sufficient for B.
B is necessary for A.

[^mud]: [Brian Foote and Joseph Yoder, _Big Ball of Mud_. Fourth Conference on Patterns Languages of Programs (PLoP '97/EuroPLoP '97) Monticello, Illinois, September 1997](http://laputan.org/mud/)

[^automation]: The dark side to automation is that it reduces the need for humans to understand what's under the hood. There was a fully automated build and deploy pipeline and infrastructure defined in Puppet that nobody dared to touch for lack of expertise.

[^nonprofit]: The work was originally billed as non-profit, social impact which has a tendency to be viewed as trivial and thus staffed accordingly. Ironically, it was actually the most technically sophisticated project I've ever worked with in some respects.

[^agile]: Unfortunately, they'd also been bitten with the Agile bug in the wrong way and seemed to think that it meant no process and spontaneous changing of priorities.

[^brokers]: At its peak, this could be up to 400 messages a minute, by 4 generalised service brokers.

[^life-death]: I'm not comfortable sharing but those of you who know me can ask about it in person.

[^debugging]: Try to replicate the problem in another environment, then poke and prod until you find the cause.

[^iac]: Declaring your infrastructure in code so that it can be built and tested automatically just like your application software. There's a whole set of principles and practices to this but think Puppet, Chef, Ansible and you're on the right track.

[^puppet]: For the record, Puppet is my least favourite Config Management tool even years later.

[^impostor]: Compound this with the fact that I had only just learnt what
a message broker even is and had only dealt with NoSQL document data stores in
theory and you have a hot mess of doubt and well-placed impostor syndrome.

[^imagine]: It's easy to imagine a universe where the laws of physics are different. But not one in which logic doesn't apply.
