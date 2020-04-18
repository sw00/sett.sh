---
title: "Leveraging fundamentals"
date: 2020-04-18
draft: true
---

In my previous [post](/posts/02/the-right-details), I ranted a bit about the state of programming tools based on my struggles working with infrastructure in large-scale systems.
The general landscape of infrastructure tooling seem to address complexity in ways that don't seem very effective to me.
If the power of tools is to make the complicated tasks simpler, the improvements promised by these tools seems quite superficial: there is still a lot of tweaking incidental details, only in YAML now instead of XML or JSON[^serialisation].
Progress made by incrementalism. And this outcome seems to be even more prevalent in custom software construction.

## Fundamental science research

Last year, I had the immense privilege of attending the International Conference on Accelerator and Large Experimental Physics Control Systems (ICALEPCS 2019).
It was hosted by the Brookhaven National Laboratory, a juggernaut of science facilities, boasting no less than 7 Nobel Science Prizes to their name.
Battling jet lag and sleep deprivation, I was struck by some insights from from one of keynote presentations by Brookhaven's associate director Jim Misewich. 
He was presenting an overview of some of the major breakthrough scientific accomplishments that the facility helped with, particularly in imaging technology that allowed scientists to study behaviours of nanomaterials, to imaging individual molecules themselves so they can be observed _during_ chemical reactions, in-situ!

There was a case which stood out to me, in which the researchers found a way to increase fuel burner efficiency by a tiny margin[^margin] - something in the order of less than 2%.
But while such a marginal improvement didn't seem so impressive on its own, once industrialised and scaled up it would result in trillions of dollars saved in fuel consumption, not to mention the immense positive environmental impact.
Such minor improvements that have a extraordinary consequences at scale is a defining feature of fundamental science research: combining deep expertise at the limits of human knowledge with solid engineering and a billion dollars worth of exprimental equipment to eek out marginal knowledge.
It then occurred to me that we get to do this in software every day.
And for the low price of a bit of upfront effort in problem solving and communication.

This of course, raises the question: what are the things in software construction that gives us such tremendous leverage?

## Fundamental software development

Software is a complex system, especially at the scale of industrial software development.
A lot of activity around software development is focused on making changes that have the intended outcomes and eliminating the unintended ones.
Distributed systems in particular have properties that don't have many analogues in the real world (and unfortunately everything is a distributed system now).
Not so sure? Consider the following:

> The building blocks of software development - languages, libraries, and platforms - change significantly every few years. The equivalent in the physical world would be that customers usually add new floors and change the floor-plan once half the building is built and occupied, while the fundamental properties of concrete change every other year.
<label>-- Martin Fowler, [Is High Quality Software Worth The Cost?](https://martinfowler.com/articles/is-quality-worth-cost.html)</label>

The very thing that makes software unwieldly is what makes so powerful.
A carefully considered change to the fundamentals of a design can give manifold returns for virtually no cost.
Given this potential for almost infinite cost/benefit ratio, is it not valuable to spend a little time in considering the problem space and the holistic design?

Furthermore, I suspect we can reframe the sorts of primitives we use to gain more leverage and expand our solution space.
Instead of processes, network calls and endless maps of configuration values what if we reframed our architecture in terms of _properties_, _relationships_ and _invariants_?
What I'm saying is that the highest leverage we might gain is by getting a little mathematical[^compsci].
Perhaps this regard for first principles should not be relegated to academia and purview of a few Functional Programming gurus, but should be at the core of the software engineering discipline itself.
Fundamental improvements require different assumptions and primitives than the ones we keep reinventing[^management].


[^serialisation]: Never mind that these are serialisation formats and not programming languages so they are limited in expressivity.
[^compsci]: some semblance of this is taught as part of computer science education but I've hardly ever seen such thinking applied in the wild.
[^management]: I also have a bone to pick with the management of software projects not being conducive to such approaches, but I won't get into that here.
