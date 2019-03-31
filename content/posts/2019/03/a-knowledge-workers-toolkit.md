---
title: "A Knowledge Workers Toolkit"
date: 2019-03-25T20:47:54+02:00
tags: ["insight", "software-dev", "philosophy"]
draft: true
---

Knowledge work can have some pretty tricky characteristics that renders it
distinct from physical work. For one, it defies quantification. While chefs,
carpenters and other tradespeople can their efforts take shape into concrete,
material output, the knowledge worker is not so fortunate.

Our raw materials are intangible - what tools could we use to manipulate them?
Likewise, our output can seem quite ephemeral - did the thing we produced
actually add value, by what measure[^value]? Worst of all, our effort[^effort]
is elastic and difficult to wield in a consistent and predictable way.  Effort
spent does not always translate into value extracted. Often something as
nebulous as a change of perspective can yield great benefits of orders of
magnitude, while we can stutter and struggle for days to achieve then next
basic goal[^parkinsons].

Despair. How are we to cope with this and take control of our own faculties?
What tools can we build to apply to our problems? By applying a little
metacognition (thinking about how we're thinking), we can be a bit more
deliberate and perhaps obtain some tools for thought.

# Mental Models

Arguably the closests thing to tools we have are the mental models we employ
when working on a task. This is true is the most general sense, from changing a
tyre to analysing a dataset. We're always using an abstraction to make sense of
the world and using it to make decisions that will give us the outcome we want.
Success depends greatly on how closely the mental model we employ corresponds
to the external world.

All models have limitations, however. They're always bounded approximations
since we're only human and not omiscient: we can't keep the full description of
the universe in our heads. So it's useful to be aware of the limitations and
assumptions of the model we're using. Find the boundaries, so to speak, and we
may expose our own biases.

## Bias

Bias in this case is the tendency for a mental model to favour certain outcomes
when applied in a context. I don't think this is categorically bad, as we're
led to believe.

To reason about this, I like to think of the oft-cited quote by George
Box[^box]:

> "All models are wrong but some are useful."

A cleaver is great at chopping meat but perhaps rather unwieldy for peeling
potatoes. This is because a cleaver has the characteristic of being large and
weighty, with a flat blade edge well suited for a chopping motion. It lacks the
small, sharp, angled blade that is more suited to slicing and peeling.

We can analyse mental models in the same way we do with real tools. It may be
useful to say that they all exhibit at least two types of properties. Ones that
are direct and intentional (by design), but also some properties that are
unintentional and emergent. 

For example, using metaphor of construction to frame how software is created
immediately brings us to think about it as a sequential process. One in which
we lay blocks upon blocks of foundation until we complete a structure.  The
unintentional consquence of this model is that it hides the relationship
between local and global components. Even worse, the metaphor offers no helpful
description of how the software might behave. Its bias is the assumption that
the whole is merely the sum of its parts.


## Characteristics of models

In order to be more mindful of the mental models we're using, it's useful to
know some qualities we may want to evaluate them against[^context]. I've often
used the following to try and explore a problem space:

* **Precision**: does the model have a quality of precision that can be
  tweaked?  Does precision mean being being more specific (semantics) or purely
  in the mathematical/quantitative sense?

* **Fidelity**: is there a threshold of quality we can increase/decrease to
  different things noticable?

* **Topology**: is distance and connectedness important aspects of the model?

* **Boundaries**: are there any delineations between things? Are they strong or
  porous?

* **Temporality**: does time play a central role in interactions? Are events
  sequential or asynchronous?

* **Directionality**: is there a direction in which things go important?

* **Authorship**: do we have direct control on the outcome or can we merely
  direct it by manipulating second-order things?

* **Economics**: is it useful to introduce an element of cost? What should be
  made cheaper or more expensive?

* **Relational**: are there traits that make certain things belong together or
  interact?

These are just some general things that may be useful to think about when
approaching a problem. They are incomplete and this is not an exhaustive list
but I've often found some of them helpful when applied deliberately to a
problem. In future posts, I hope to expand on specific models that I've used to
make sense of phenomena I've encountered in software development. Hopefully,
they will useful or at least entertaining.

[^value]: And does it retain value or will it diminish?

[^effort]: What does it mean to expend effort? Can "effort" be substituted for "attention" or something else?

[^parkinsons]: Chances are, you've probably experienced a fair share of [Parkinson's Law](https://en.wikipedia.org/wiki/Parkinson%27s_law), especially if you work in an office.

[^box]: He was of course referring specifically to statistical models, but I think it can be generalised into "all abstractions are wrong but some are useful".

[^context]: Unfortunately, none of this is ultimately useful without a context, but they offer a good foundation.
