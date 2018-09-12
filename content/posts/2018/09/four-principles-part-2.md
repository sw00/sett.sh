---
title: "Four principles from four people (part 2)"
date: 2018-09-12T19:29:46+02:00
draft: true
tags: ["software-dev", "craft", "principles"]
---

This is the second part of a blog post in which I share four principles that I
picked up from four different people I've been fortunate enough to have
worked with. Part 1 is
[here](/posts/2018/09/four-principles-from-four-people-part-1/).

# Know what you know

This I learnt from my close friend and pair programming buddy with whom I
shared an assortment of (mis)adventures[^adventure] during the year I spent in
Brazil. We'd spend almost every day musing together about every conceivable
thing while breaking builds and getting up to no good. We'd talk about
philosophy, physics, code, politics, transportation, sociology, food, municipal
governance, world history, beer, linguistics, labour law, culture, technology,
tax policy and music. Someone who shared the childlike awe for knowledge and
how strange it is that anything could be something at all.

We worked together on one particularly large, unruly AngularJS
codebase. It was a large project with at least half a dozen squads all
contributing to the same build and the feedback cycle was slow and
expensive[^electric_commander]. One day a change we made introduced a bug which
halted the release for the entire project. I recall it happened a few times and
it was due to our lack of understanding of the nuances in the often inscrutable
JS code we encountered.

At this point, out of frustration, my friend resolved to learn the language
itself from the ground-up. He asked how JS scope worked and to my dismay, I
found that I could not precisely explain it. At this point I had written a lot
of JS, having done front-end webdev all the way from the days of JQuery to
BackboneJS, KnockoutJS and now finally AngularJS. However, I found I had no
true understanding of lexical scope, variable hoisting and how the language
handles _this_. Despite this deficiency, I had gone years of being adequately
quite productive in it[^js]. Except now, in this nontrivial project we regularly
encountered race conditions and unexpected references.

I admired the remarkable need for precise understanding my friend had. He did
not feel comfortable starting a task unless he had a thorough and complete
understanding of the tools we were meant to use. This is because he's a
scientist: he created a programming language for his masters thesis[^age], a
variant of ALGOL that used Portuguese keywords - perfect for teaching young
Brazilian children computer programming. As such, he had the composure and
**grit of a scientist**, a need to fully understand the theory to explain the
observation, whereas up until then I had always favoured pragmatic, exploratory
approaches (poke the thing a few times and see it does anything useful, then
use it everywhere).

The flipside to this approach is that it takes time. And often there is just not enough time. 

[^adventure]: I particularly like that long weekend trip to Uruguay we failed to adequately plan for (of course) and ended up interstate bus-hopping from Chuy all the way to Montevideo. Neither of us spoke Spanish, or had a concrete plan of how to get back i time for work next week except that we'll hopefully find another bus or something.
[^electric_commander]: The CI at that time was a single instance, crumbling old thing shared by the entire organisation. It was also a tightly coupled microservices architecture in that all changes culminated in changes in the UI layer.
[^js]: Sorry. I was _that_ programmer. There is a lot of code I've written that I'm not proud of now.
[^age]: [By the age of 35](https://knowyourmeme.com/memes/by-age-35), every programmer should have created their own programming language.
