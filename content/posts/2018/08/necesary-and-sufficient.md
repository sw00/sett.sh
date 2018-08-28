---
title: "Critical failure"
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

# The Project
The project itself was replete with problems. In spite of the excellent
technical foundations the original tech leads had laid, the core web
application had been eroded into a ball of mud[^mud] and for various legitimate
reasons nobody understood the current runtime architecture or how it got
deployed to production[^automation].

> "A Big Ball of Mud is a haphazardly structured, sprawling, sloppy,
> duct-tape-and-baling-wire, spaghetti-code jungle. These systems show
> unmistakable signs of unregulated growth, and repeated, expedient
> repair."[^mud]

The client, our product owner, had been using us to bootstrap his startup years
and aggressively chasing growth (i.e. features) without any reprieve for almost
2 years[^agile]. All while leveraging a relatively junior team that suffered
high attrition, breaks in continuity, working in a highly sophisticated tech
stack nobody had any significant experience in[^nonprofit]. There was a lot of
firefighting and the problems seemed serious enough that I was absolutely
terrified of not being able to cope and led me to recommend a complete feature
freeze. But alas, greatness is not achieved by capitulating to the demands of
harsh reality, so feature development was always prioritised above all else.

![Scotty from Star Trek](https://i.imgflip.com/1rojys.jpg#c)

# The Problem
The central part of the system was a few workers applications that would
automatically respond to incoming user messages in real-time or as fast as
possible. In practice this was a bunch of Celery workers subscribed to RabbitMQ
channels making lookups to a MongoDB cluster. These workers were failing to reply to messages.


# The Mechanics of Implication

Implication is a property of our universe. This is quite interesting because this is probably a fundamental property of our universe[^imagine]

$$ A \rightarrow{} B$$

"If A then B."
If A holds, then B holds.

A is sufficient for B.
B is necessary for A.

[^mud]: [Brian Foote and Joseph Yoder, _Big Ball of Mud_. Fourth Conference on Patterns Languages of Programs (PLoP '97/EuroPLoP '97) Monticello, Illinois, September 1997](http://laputan.org/mud/)

[^automation]: The dark side to automation is that it reduces the need for humans to understand what's under the hood. There was a fully automated build and deploy pipeline and infrastructure defined in Puppet that nobody dared to touch for lack of expertise.

[^nonprofit]: The work was originally billed as nonprofit which has a tendency to be viewed as trivial and thus staffed accordingly. Ironically, it was actually the most technically sophisticated project I've ever worked with.

[^agile]: Unfortunately, they'd also been bitten with the Agile bug in the wrong way and seemed to think that it meant no process and spontaneous changing of priorities.

[^imagine]: It's easy to imagine a universe where the laws of physics are different. But not one in which logic doesn't apply.
