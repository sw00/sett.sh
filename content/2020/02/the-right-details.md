---
title: "Sweating the Right Details"
date: 2020-02-22T09:29:34+02:00
draft: true
tags: ["programming", "software-developement", "design"]
---

Some things have been bothering me for a while now, about programming as an activity and the software engineering discipline from which it follows.
I've had some false-starts in articulate the insights that I'm grappling for. But let me finally commit to trying, at least.

I've been spending a lot of time with infrastructure in my current role, wrangling automation, troubleshooting environments, configuring and optimising builds.
Operating machinary that pushes buttons and pulls levers on other machines ad infinitum.
In this world the conventional notions of _software design_ and _architecture_ seem to be hidden away in a galaxy of configuration details, sharded between the plethora of YAML files, and smothered under the avalanche of container images, build scripts and orchestration tools.

We often to take for granted that all this work involved is necessary and driven by the inherent nature of large-scale, distributed systems world we're working in.
Unfortunately, this distributed systems world is still a very messy space where technology, culture and methodology coalesces into some supermassive complex, adaptive web of socio-technical interactions.
I tend to think of it as a giant multi-dimensional [Jenga](https://en.wikipedia.org/wiki/Jenga) game.

I try to cope with this by doubling down on first principles. _Easy-isn't-simple_. Keep things _SOLID_. Draw boxes and lines in my mind to model aggregates, properties and relations of the Rube Goldberg machine that produced these\... log lines.
It's difficult to look at all this activity and not feel a little overwhelmed, a bit perplexed and suspicious about where we are and where we're going as an industry and discipline.
And then I see the tools we have been offered up to help us, and then\... despair:

<a href="https://landscape.cncf.io" target="new">![The "landscape" of cloud tools published by the CNCF](/2020/02/img/landscape.png)</a>
<small>The image above illustrates the ecosystem of tools used to build and maintain a modern software system today.</small>

It's difficult to reconcile the picture above with the notion of writing software as a problem solving activity, realised by humble text-editor and compiler/interpreter.
But perhaps this vision was always only a myth, cooked up by well-meaning, rational people in ivory towers.

Still, it raises the question: how _did_ we get here?
This feeling is quite possibly exemplified in the following statement by Jonathan Edwards, a respectable figure in the language design community.

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Programming today is exactly what you’d expect to get by paying an isolated subculture of nerdy young men to entertain themselves for fifty years. You get a cross between Dungeons &amp; Dragons and Rubik’s Cube, elaborated a thousand-fold. <a href="https://t.co/Mug9k7ioIG">https://t.co/Mug9k7ioIG</a></p>&mdash; Jonathan Edwards (@jonathoda) <a href="https://twitter.com/jonathoda/status/1024098312398536704?ref_src=twsrc%5Etfw">July 31, 2018</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

As a nerdy guy who does indeed enjoy Dungeons and Dragons and Rubik's cubes, this struck a chord. But it's not an empty, inflammatory statement, as Mr Edwards expounds further:

>  I’m serious: Dungeons & Dragons requires mastery of an encyclopedia of minutiae; Rubik’s Cube is a puzzle requiring abstract mathematical thinking.

While I don't agree with the entire article, it's a compelling description of sofware development in practice.
Programming, being the most elementary activity in software development, does seem to superficially favour those who have the requisite level of monomania to master these [minutaie](https://stackoverflow.com/questions/26021181/not-enough-entropy-to-support-dev-random-in-docker-containers-running-in-boot2d).
Far more insidious than that, is that it hints at a design philosophy and solution approach that is incrementalist and potentially suffering from [Einstellung](https://en.wikipedia.org/wiki/Einstellung_effect).

I suppose this isn't a novel insight or complaint.
Maybe it's just a rite of passage that all developers must go through: a mid-career crisis that forms a better appreciation for software complexity, after getting burnt for the umpteenth time, finally learning\...
Fortunately, I know there are many movements, practices and tools before that offer an escape to lift us out of "The Tar Pit" and into the realm of deliberate design and problem solving.
Things such as _[Domain Driven Design](https://wiki.c2.com/?DomainDrivenDesign)_, _Functional Reactive Programming_, even _Design Patterns_ and others we can grasp at that offer some salves for our wounds.
But putting them to practice often feels like trying to steer an oil tanker, against its own tremendous momentum.

I'm hopeful that these approaches will win. But not in the same way that Agile has "won".
Software problems cannot be solved by simply playing with stickies and JIRA reports.
These are artifacts and tools of bureaucracy, of managing work from a production-based worldview[^taylorism], and ill-suited for problems of software engineering which is knowledge work.
I've come to believe (cautiously) that the problems of software engineering are fundamentally about dealing with complexity in its many forms.
This requires tools and approaches rooted in design, critical thinking and problem solving - general skills that people excel at when given the chance to be people in their own full complexity.

Generally, I think we're reaching new levels of scale and complexity at which incremental approaches to design are insufficient.
This will force the fore-runners in the field to return to the fundamentals and experiment.
Perhaps the advent of [serverless](https://serverless-stack.com/chapters/what-is-serverless.html) and [deployless](https://thenewstack.io/dark-a-new-programming-language-for-deployless-deployments/) represents the start of this shift.
Hopefully can learn and apply that same philosophy in our own daily work.
Hopefully, reaching for fundamentals can give us more leverage and help us sweat the right details. More on this later.


[^taylorism]: writing software is more like research and design of a new car than assembling that car in a conveyor belt.
