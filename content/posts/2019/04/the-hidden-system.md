---
title: "The Hidden System Behind Your Software System"
date: 2019-04-25T20:20:35+02:00
draft: true
tags: ['software-engineering', 'systems']
---
There's something about software development that's been bothering me over
the years. It's kind of an intuition about the process of creating software
that I haven't really been able to articulate or reason about. A common
smell[^smell] that every project and team I've ever worked on has had. Let's 
try and explore this thing below.

# Complexity

I think it's a well known trope that everyone knows by now: software is
complex and writing software even moreso. However, it's worth noting that
we're probably crossing a new threshold of complexity in which everything is
distributed and everything is obsessively "scaled"[^scale]. Unless you're
writing embedded software[^embedded], you're most likely working on a
distributed software system. I use the term _system_ here in the most general
sense: simply a thing that is composed of many other, different things that
relate or interact.

Given this, programming has little to do with specifying instructions
for machines to execute (and it probably hasn't been since the 50s). Rather,
the activity of developing software becomes primarily about what I call
_second-order_ problems: managing changes to different components that relate and
interact with each other in different contexts (e.g. `{write, build, run, release}-time`).

You don't need have a Maths Phd to realise that this leads to a combinatorial
explosion of outcomes for every atomic bit of input/change. So here's the central 
premise/insight of this post:

All the activities, processes, practices, technology, people, everything that
contributes to the development of a software system is itself a system. And
this system is a Complex System.

This is something that's probably featured in any undergraduate Software
Engineering or Systems Engineering textbook (who was paying attention or even
understands this without any exposure/experience).

# On Complex Systems

- More is different[^anderson]
- Russel L. Ackoff[^ackoff]


# Tolerance for Complexity

I've had the privilege to have worked with many different kinds of smart
people. A particular type has fascinated me and is the subject of many
programming myths: the master programmer. This is someone really smart and
highly sought after because their abilities far exceed that of the average or
even "good" developers. I've encountered a handful of them and worked closely
with one or two.

There are two things that initially impressed me. Their ability to be
extraordinarily productive without thinking about a task. Something that
would take me a good week to grok and implement, they would manage in
minutes. Second, their ability to hold a prohibitve (to me) amount of
information and context in their heads. Whereas I tend to rely excessively on
feedback loops, they could reason so far ahead of me that they'd have an
almost complete implementation in their heads without touching the keyboard.

However, some cracks began to show when looking at the situation holistically. When
software is built by only the smartest people with a high tolerance for complexity,
the software system might drift toward complexity. Fortunately, the smart people know this
and actively try to keep it elegant and simple. But the blindspot

[^smell]: http://wiki.c2.com/?CodeSmell
[^scale]: We're still experiencing the waves of the paradigm shift brought about decades ago, when the first computers were networked together.
[^embedded]: Even then, you'd have to figure out how to package, distribute and deploy your software.
[^cockburn]: https://twitter.com/TotherAlistair/status/1116795119791824896
[^anderson]: More Is Different. (1994). In World Scientific Series in 20th Century Physics: Vol. Volume 7. A Career in Theoretical Physics (pp. 1–4). https://doi.org/10.1142/9789812385123_others01
[^ackoff]: russel ackoff - YouTube. (n.d.). Retrieved April 25, 2019, from https://www.youtube.com/results?search_query=russel+ackoff&page=&utm_source=opensearch
