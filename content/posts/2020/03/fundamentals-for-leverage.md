---
title: "Leveraging fundamentals"
date: 2020-03-03T21:48:14+02:00
draft: true
---

In my previous [post](/posts/02/the-right-details), I ranted a bit about the state of programming tools based on my struggles working with infrastructure in large-scale systems.
The landscape of infrastructure tooling seems to indicate a response to complexity that doesn't seem effective to me.
The primitives offered up by the tools seem to be quite superficial: still a lot of configuration and incidental details, but now in YAML.
Progress made by incrementalism.

## Lessons from Scientific Research

Last year, I had the immense privilege of attending the International Conference on Accelerator and Large Experimental Physics Control Systems (ICALEPCS 2019).
It was hosted by the Brookhaven National Laboratory, one of the juggernauts of science facilities, boasting no less than 7 Nobel Science Prizes to their name.
Battling jet lag and sleep deprivation, I was struck by a point from one of keynote presentations by associate director Jim Misewich. 
He was presenting an overview of some of the major breakthrough scientific accomplishments that the facility helped with, particularly in imaging technology that allowed scientists to study behaviours of nanomaterials, to imaging individual molecules themselves _during_ reactions.
A particular success story stood out to me, in which the researchers found a way to increase fuel burner efficiency by a tiny margin[^margin] - something in the order of less than 2%.
But while such a marginal improvement didn't seem so impressive, once scaled it would result in trillions of dollars of saved in fuel consumption accross the States, not to mention the positive environmental impact.
It then occurred to me that we get to do this in software every day.


> The building blocks of software development - languages, libraries, and platforms - change significantly every few years. The equivalent in the physical world would be that customers usually add new floors and change the floor-plan once half the building is built and occupied, while the fundamental properties of concrete change every other year.

-- Martin Fowler, [Is High Quality Software Worth The Cost?](https://martinfowler.com/articles/is-quality-worth-cost.html)


[^margin]: Somewhere in the order of less than 2%.
