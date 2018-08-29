---
title: "Critical failure and the Mechanics of Causality"
slug: critical-failure
date: 2018-08-28T17:46:57+02:00
draft: true
markdown: mmark

---

The most critical failure that I've ever experienced on a project happened on
the first week of 2014 and caused recurring outage that lasted a full four
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
any significant experience in[^nonprofit]. There was a lot of firefighting and
the problems seemed serious enough that I was absolutely terrified of not being
able to cope. So armed with a three-page report of about two dozen urgent
items, I recommended a complete feature freeze as my first act as tech lead.
Alas, greatness is not achieved by capitulating to the demands of harsh
reality, so feature development was always prioritised above all else.

![Scotty from Star Trek](https://i.imgflip.com/1rojys.jpg#c)

It was certainly not ideal, but the journey to finding the root cause was not
without some personal cognitive failures (jumping to conclusions are best done
in an excited panic).

The critical part of the system was a few message broker processes that would
respond to incoming user messages fast as possible[^brokers]. In practice this
was a bunch of Celery workers subscribed to RabbitMQ cluster and making lookups
to a MongoDB cluster. Because there was some business logic they needed to
leverage, the workers lived in the same repository as the Django web
application to keep things DRY and were executed by means of configuration
injected (like a good little 12-factor app). These workers were failing to
reply to incoming messages and we didn't know why. Highly critical, and in
certain scenarios a potential life-and-death situation.

The problem was not observed in staging and we hadn't deployed in the past two
weeks.

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

[^imagine]: It's easy to imagine a universe where the laws of physics are different. But not one in which logic doesn't apply.
