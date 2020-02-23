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
Sometimes we take for granted that the work involved in necessary, driven by the inherent nature of large-scale, distributed systems we're working on.
Unfortunately, the world of large-scale, distributed systems is still a very messy space where technology, culture and methodology collides into some supermassive complex, adaptive system of socio-technical interactions.
A multi-dimensional [Jenga](https://en.wikipedia.org/wiki/Jenga) board, if you will.

I try to cope with this by doubling down on first principles. _Easy-isn't-simple_. Keep things _SOLID_. Draw boxes and lines in my mind to model aggregates, properties and relations of the Rube Goldberg machine that produced these\... log lines.
It's difficult to look at all this activity and not feel a little overwhelmed, a bit perplexed and suspicious about where we are and where we're going as an industry and discipline.
And then you see the tools we have been offered up to help us, and then\... despair:

<a href="https://landscape.cncf.io" target="new">![The "landscape" of cloud tools published by the CNCF](/2020/02/img/landscape.png)</a>
<small>The image above illustrates the ecosystem of tools used to build and maintain a modern software system today.</small>

It's difficult to reconcile the picture above with the idea of writing software as a problem solving activity, realised humbly by text-editor and compiler/interpreter. Perhaps this vision was always only a myth. 

My problem partly has to do with the notion of _complexity_. Generally speaking, we can say a system is complex if it consist of interacting parts that are numerous _and_ differentiated. 
Humans can understand this intuitively: something that is more complex is more difficult to reason about.
This heuristic is often superficially applied by software development teams to discuss the merits of an approach or design.

# Accidental or essential?

Of course, when talking about complexity in software we can't get away from the seminal treatment of it from Fred Brooks' "No Silver Bullet" essay. The gist of it is this: 

- there are two kinds of complexity: accidental and essential
- acccidental complexity is a byproduct of the technology we choose to implement a solution
- essential complexity is the byproduct of the problem space (domain)

In practice, I doubt that it can be so neatly separated and there's probably a continuum between the two. However, this has some interesting implications: I think it follows that accidental complexity is more _reducible_[^refactoring] than its counterpart, i.e. it's possible to make things simpler but keep their meaning. 

# So what

Perhaps it's because I've been stuck in the thick of it all for the past year, wrangling configuration in the form of YAML 

# Simple 

- incremental vs fundamental

> Programming today is exactly what you’d expect to get by paying an isolated subculture of nerdy young men to entertain themselves for fifty years. You get a cross between Dungeons & Dragons and Rubik’s Cube, elaborated a thousand-fold. I’m serious: Dungeons & Dragons requires mastery of an encyclopedia of minutiae; Rubik’s Cube is a puzzle requiring abstract mathematical thinking. 



[^refactoring]: In practice, the process of _reducing_ something is synonymous with _refactoring_. 