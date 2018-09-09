---
title: "Four principles from four people"
date: 2018-09-09T15:43:11+02:00
draft: true
tags: ["software-dev", "principles"]
---

I've had such privilege to have worked with so many different people, in so
many different contexts. Being exposed to such diversity has greatly benefited
me and enriched my world view. But there's also a little bit of everyone I've
internalised - little tools, values and principles for which I am grateful to the people they originate from. 

You get to learn a lot about a person just by pairing with
them on a technical problem or even collaborating on something more
strategic[^euphemism]. You experience their idiosyncracies and philosophy. And
in doing so, a little bit of your own idiosyncracies surface, like looking into
the proverbial "mirror".

Here I'd like to share four principles I picked up from four people that have
had tremendous impact on me and how I approach work. 

# Go fast

Embodied by a certain ridiculously charismatic, Irish-American developer with
the mouth of a sailor[^charismatic], from whom I learnt pretty much most of
everything I know now. Although this principle was not stated so explicitly,
upon reflection I realised a lot of my own approaches to software development
has been deeply influenced if not learnt directly from him. Let's see if I can
lay out the main ideas below:

**Adopt a bias for action**. Not every decision the same impact, so minimise
its cost and overhead. It's perfectly acceptable (and fun) to play
rock-paper-scissors with your pair to make low-impact decisions. This blew my
mind the first time. But I've used this often, though people sometimes find it
unnerving that I make some tech decisions by chance.

What's the thinking behind this? Well, a lot of details in software development
are indeed trivial from a larger perspective. Which test runner should we use?
What should I really name this function? Who cares, they both have minimal
impact _and_ cost little to change. Another thing to understand is that when
starting a new project, feature or change you will be at the _highest level of
ignorance_ such that you might not have the right understanding to competently
choose one over the other: a random choice is just as good as an ignorant
choice[^wrongchoice].

When framed this way, it follows that even making the wrong choice is valuable
because it will reduce your level of ignorance. The trick is reducing the
impact of wrong choices so you're free to make mistakes for learning. There are
techniques and practices you can adopt to achieve this and it's pretty much
what all Agile, Continuous Delivery, Lean and DevOps is about in principle.

**Make feedback a first-class citizen**. Invest heavily in the things that will
give you the right level of information very quickly. On technical level, this
means Test-Driven Development and Automation. Ask yourself: what is the
expected impact of this decision and how do I verify it? Write that automated
test, make friends with your testers and users, push for read access to
environments, send those emails to other teams and managers. This applies to meta-decisions too: retrospectives and one-on-one sessions create a feedback loop for how you're working as a team.

**Leverage the last responsible moment**[^lrm]. You will always have more or
higher grade of information later in time than you do right now. Given this,
your best bet at making an informed decision is later, so all decisions that
can be deferred should be. Seems simple, but I've found the difficulty is
actuall in deciding whether you can afford to defer it. Two things are helpful
in this regard: divide-and-conquer and maximising options. 

The first approach is about investigating whether you can break the decision
down into smaller, low-impact ones. For example, what if you simply load the
data from a flat text file in memory for now instead of committing to a
particular database? The second approach is about making the choices that will
yield you more options. In a way this is closely related to the
divide-and-conquer approach too because the former will likely yield more
options anyway.

# Go slow

There are very few people who are so brilliant and smart that they consistently
and effortlessly outperform everyone else. Give a smart person a task and they
will complete it to perfect specification in very little time. But rarer yet
are people who seem to possess innate wisdom and endless compassion. The
following principle I learnt from someone who embodies the latter, who I
consider a role model and had the tremendous privilege of being mentored by at
first, but then in more official terms as my boss.

To be precise, the principle is better stated: **go as slow as you need to**.
Though it may seem in contradiction to the first principle, it's actually quite
complementary. 

Tasks, goals, missions, objectives. They suffer from a certain effect: that
once they are explicitly declared, they collapse the problem space and
obfuscate the _a priori_ assumptions that were necessary to produce them. 

There are always numerous ways to tackle a problem. One way is to solve the
immediate, first-order situation that you're presented with: if a building's on
fire, use the buckets you have to put it out. 

An alternative is to take a step back and consider the context and processes
that led to its emergence: the building is on fire, replace it with fire-resistant material. This requires a deeper wisdom and discipline than the
first-order "task" oriented thinking[^task]. It is worth taking a detour and
spending the time to consider and work out a strategy to tackling these
second-order problems. The kicker here is that learning a problem takes time to
struggle with it. Something I didn't quite grok for ages because my de facto
urge is feeling pressured to get the result as quickly as possible when presented with a challenge[^frustration].

What does this actually look like in real life? It means, spending the time to
set up Continuous Delivery and path to production[^path] right (including the
time it takes you to learn it). Or putting in effort to position a solid
proposal for project that gives value not just to the client, but to the people
working on it too. It means taking some longer detours to build some
second-order tools to help you produce the first-order thing in higher quality,
but faster later. Learn that new technique, fail and master it. Didn't meet
your sprint commitments? There's always next sprint, really. If something needs
to absolutely be done, then trust that it will need to get done if not now then
later, armed with better understanding and more mastery.

There is tremendous value in going slow.


[^euphemism]: I guess this is a euphemism for making slide decks together.
[^charismatic]: If
[^lrm]: https://blog.codinghorror.com/the-last-responsible-moment/
[^task]: There was a time when I felt very strongly that my worth is tied to how quickly I can tick off boxes and objectives. The problem is that completing tasks quickly doesn't imply that they are valuable or even the right things to do.
[^frustration]: This often leads to Sisyphian cycle of frustration-then-catharsis.
[^path]: This is one of my pet peeves. There have been so many projects that have lacked this basic concept of a "path to production". Oh well, maybe the real path to production was all the friends we made along the way.
