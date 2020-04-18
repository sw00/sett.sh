---
title: "Leveraging fundamentals"
date: 2020-03-03T21:48:14+02:00
draft: true
---

In my previous [post](/posts/02/the-right-details), I ranted a bit about the state of programming tools based on my struggles working with infrastructure in large-scale systems.
The general landscape of infrastructure tooling seems to indicate a response to complexity that doesn't seem effective to me.
If the power of tools is to lower the complexity of working working in a domain, the improvements promised by these tools seems quite superficial: there is still a lot of tweaking incidental details, only in YAML now instead of XML or JSON[^serialisation].
Progress made by incrementalism. This kind of approach is even more prevalent in software construction.

## Insights from fundamental science research

Last year, I had the immense privilege of attending the International Conference on Accelerator and Large Experimental Physics Control Systems (ICALEPCS 2019).
It was hosted by the Brookhaven National Laboratory, a juggernaut of science facilities, boasting no less than 7 Nobel Science Prizes to their name.
Battling jet lag and sleep deprivation, I was nonetheless struck by an insight from one of keynote presentations by Brookhaven's associate director Jim Misewich. 
He was presenting an overview of some of the major breakthrough scientific accomplishments that the facility helped with, particularly in imaging technology that allowed scientists to study behaviours of nanomaterials, to imaging individual molecules themselves _during_ reactions.

There was a case which stood out to me, in which the researchers found a way to increase fuel burner efficiency by a tiny margin[^margin] - something in the order of less than 2%.
But while such a marginal improvement didn't seem so impressive one its own, once industrialised and scaled up it would result in trillions of dollars saved in fuel consumption, not to mention the positive environmental impact.
Such minor improvements that have a extraordinary consequences at scale is what fundamental science research is all about: combining deep expertise at the limits of human knowledge with solid engineering and a billion dollars worth of exprimental equipment.
It then occurred to me that we get to do this in software every day, for the price of a bit of upfront effort in exploring a problem space and communication.


> The building blocks of software development - languages, libraries, and platforms - change significantly every few years. The equivalent in the physical world would be that customers usually add new floors and change the floor-plan once half the building is built and occupied, while the fundamental properties of concrete change every other year.

-- Martin Fowler, [Is High Quality Software Worth The Cost?](https://martinfowler.com/articles/is-quality-worth-cost.html)


[^serialisation]: Never mind that these are serialisation formats and not programming languages so they are limited in expressivity.
[^margin]: Somewhere in the order of less than 2%.
