---
title: "The Right Details"
date: 2020-02-22T09:29:34+02:00
draft: true
tags: ["programming", "software-developement", "design"]
---

Some things have been bothering me for a while now about programming as an activity and the software engineering discipline from which it follows.
It's led to some sleepless nights and false-starts in trying to articulate the insights that I'm grappling at. I don't want to rant, but let me finally commit to trying, at least.

I've been spending a lot of time with infrastructure in my current role, wrangling automation, troubleshooting environments, configuring and optimising builds.
Machines pushing buttons and pulling levers on other machines.
In this world the conventional notions of _software design_ and _architecture_ seem to be hidden in a galaxy of configuration details, sharded amongst the plethora of YAML files, smothered under the avalanche of container images, build scripts and orchestration tools.
Sometimes we simply take for granted that all this work involved is necessary, driven by the inherent nature of large-scale, distributed systems we're working on.
Unfortunately, the world of large-scale, distributed systems is still a very messy space where technology, culture and methodology collides into some supermassive complex, adaptive web of socio-technical interactions.
A multi-dimensional [Jenga](https://en.wikipedia.org/wiki/Jenga) board, if you will.

I try to cope with this by doubling down on first principles. _Easy-isn't-simple_. Keep things _SOLID_. Draw boxes and lines in my mind to model aggregates, properties and relations of the Rube Goldberg machine that produced these\... log lines.
It's difficult to look at all this activity and not feel a little overwhelmed, a bit perplexed and suspicious about where we are and where we're going as an industry and discipline.
And then you see the tools we have been offered up to help us, and then\... despair:

<a href="https://landscape.cncf.io" target="new">![The "landscape" of cloud tools published by the CNCF](/2020/02/img/landscape.png)</a>
<small>The image above illustrates the ecosystem of tools used to build and maintain a modern software system today.</small>

It's difficult to reconcile the picture above with the idea of writing software as a problem solving activity, realised by humble text-editor and compiler/interpreter. Perhaps this vision was always only a myth.

Still, it raises the question: how _did_ we get here? This feeling is perhaps best exemplified in the following statement by Jonathan Edwards, a respectable figure in the language design community.

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Programming today is exactly what you’d expect to get by paying an isolated subculture of nerdy young men to entertain themselves for fifty years. You get a cross between Dungeons &amp; Dragons and Rubik’s Cube, elaborated a thousand-fold. <a href="https://t.co/Mug9k7ioIG">https://t.co/Mug9k7ioIG</a></p>&mdash; Jonathan Edwards (@jonathoda) <a href="https://twitter.com/jonathoda/status/1024098312398536704?ref_src=twsrc%5Etfw">July 31, 2018</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

As a nerdy guy who does indeed enjoy Dungeons and Dragons and Rubik's cubes, this struck a chord. But it's not just an inflammatory post, Mr Edwards expounds further:

>  I’m serious: Dungeons & Dragons requires mastery of an encyclopedia of minutiae; Rubik’s Cube is a puzzle requiring abstract mathematical thinking.

While I don't agree with everything written there, it's definitely seems like a compelling characterisation of sofware development in practice.
Looking back on most of the teams and projects I've been on it does look like a lot of people juggling a lot of minute details that need to come together at parts to form something coherent.
And the way we work seem to superficially favour those who have the requisite level of monomania to master the [minutaie](https://stackoverflow.com/questions/26021181/not-enough-entropy-to-support-dev-random-in-docker-containers-running-in-boot2d).

I suppose this isn't a novel insight or complaint.
Perhaps it's only a rite of passage that all developers must go through, a crisis from a better appreciation of software complexity, in the middle of their careers, after getting burnt for the umpteenth time, finally learning\...
But I know there have been movements, paradigms and tools before that offer an escape to lift us out of the "tar pit" and into the realm of deliberate design and problem solving over toil.
I know things such as _Domain Driven Design_, _Functional Reactive Programming_, _Design Patterns_ and others we can grasp at that offer some salves for our wounds.

I'm hopeful that these approaches will win. But not in the same way that Agile has won.
Software problems cannot be solved by playing with stickies and JIRA reports.
These are artifacts and tools of bureaucracy and ill-suited for problems of engineering.

