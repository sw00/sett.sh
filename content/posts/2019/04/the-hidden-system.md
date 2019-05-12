---
title: "The Hidden System Behind Your Software System"
date: 2019-04-25T20:20:35+02:00
draft: true
tags: ['software-engineering', 'systems']
---

This post is specifically about software development and is cross-posted to dev.to.

April marks my 8th year working in software development. I've been working
professionally in this field for enough time that I finally feel comfortable
enough to call it a career. However, I've always felt that it was not so
much an intentional pursuit as something that I ended up in, given my
idiosyncracies and circumstances. But what else would someone who spent most of
their waking life on a computer from the age of 10 do? Spend too much damned
time hacking away at a computer and some level of competence
emerges[^education]. Said competence can then be put to work as skilled
_expertise_, given the right opportunities and environment.  And thus a career
in "tech" is made.

But then I realised the expertise I've gained is the through the slow
accumulation of incidental knowledge more than anything else. What this means
that a lot of my process resembles that of _intuition_ rather than a deductive,
rational process. Fortunately, intuition gained from experience does tend to be
correct more often than not, but it can also lead to reinforcement of nascent
biases and prone to blind spots.

So, I decided that I need to be more deliberate and rigorous in my thinking by
returning to first principles and to try and articulate what I "feel" better.

# Complexity

I think it's a well known trope that everyone knows by now: software is complex
and the activity of producing valid, useful functionality is complicated and
difficult. And with the advent of dynamic infrastructure and the need to evolve
systems instead of specifying them upfront, we're probably crossing a threshold
that we don't fully understand yet. However, we are likely still experiencing
the paradigm shift that began decades ago when the first two machines exchanged
messages over TCP/IP. There's just _so much more_ of it now.

It's highly likely that if you work in software today, you're dealing with
distributed systems. That is, your system consists of many different parts that
interact with each other across boundaries (processes, network, virtual/physical machines) 
to provide a service or function. We can understand intuitively that complexity 
in a system is unavoidable and emergent whenever we have the following
properties: 

- many parts that combine to form a whole (size/magnitude)
- the parts are different from each other (differentiation)

What are the implications of complexity though? We know generally that
complexity is bad because it makes it harder to reason about the changes we
want to make, making our work as software developers more challenging. This
corresponds with the standard explanation we tend give to non-technical
folk when talking about things like **techincal debt** or **refactoring**.

But what does that even mean? What's the difficulty encountered when making
changes? Complexity in any system makes outcomes harder to predict. This is a
fundamental trait of naturally occuring _complex systems_[^complex_systems]
(weather, climate) and emergent ones (stock markets). And so if we introduce a
change in one side of the equation, we don't know what comes out the other
side. If it's a discrete system, perhaps the combination of all potential
choices is too much for us correct outcome with confidence.

Fortunately, it costs us nothing to simulate the outcome. By _simulate the
outcome_, I mean running the damn thing and giving it input. Think about it. A
program then has no meaningful difference between itself and the
_execution_[^computation] of itself. This is the real value behind the value of
testing.  Testing frees us from having to write rigorous proofs to guarantee
that our software will run correctly, since we can simply run it to prove it
(proof by execution?).

## Complex Systems


# Feedback

Given It is no
longer sufficient to reason about software development as the act of writing
instructions for computers to execute. In practice, nobody thinks of software
development in
this way (I hope).


However, it's worth noting that
we're probably crossing a new threshold of complexity in which everything is
distributed and everything is obsessively "scaled"[^scale]. Unless you're
writing embedded software[^embedded], you're most likely working on a
distributed software system. That is, your software consists of many different components and interacts with them in . I use the term _system_ here in the most general
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

[^education]: Sure some formal education is helpful, but ultimately ability comes about from time spent on it.
[^smell]: http://wiki.c2.com/?CodeSmell
[^complex_systems]: [P. W. Anderson. 1972. More Is Different. Science 177, 4047 (1972), 393–396.](https://www.tkm.kit.edu/downloads/TKM1_2011_more_is_different_PWA.pdf)
[^computation]: Or _computation_ as it's known in the ancient texts.
[^scale]: We're still experiencing the waves of the paradigm shift brought about decades ago, when the first computers were networked together.
[^embedded]: Even then, you'd have to figure out how to package, distribute and deploy your software.
[^cockburn]: https://twitter.com/TotherAlistair/status/1116795119791824896
[^anderson]: More Is Different. (1994). In World Scientific Series in 20th Century Physics: Vol. Volume 7. A Career in Theoretical Physics (pp. 1–4). https://doi.org/10.1142/9789812385123_others01
[^ackoff]: russel ackoff - YouTube. (n.d.). Retrieved April 25, 2019, from https://www.youtube.com/results?search_query=russel+ackoff&page=&utm_source=opensearch
