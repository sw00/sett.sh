---
title: "Three Conjectures"
date: 2018-08-07T10:22:06+02:00
draft: true

tags: ['software dev', 'insight']
---

Programming is bloody difficult[^tough]. It demands your full attention and
presence. It's also incredibly rewarding and deeply satisfying. But this is all
premised on having the space and opportunity to practice the craft. To achieve
a state of flow. Based on this, I would like to propose the following:

**Conjecture 1**: Flow is a necessary (but insufficient) condition for
producing working software.

Ultimately, the potential for any dev team to deliver working software is
constrained by their ability to enter the state of flow. Following from this,
is the ability to collaborate and communicate. If you're not optimising for
this, you're severely handicapping your dev efforts. This includes physical
things like how offices are laid out, to more nebulous, difficult things like
ambiguity around decision-making and opaque dependencies.

**Conjecture 2**: The principles of good engineering are at odds with that of
traditional large business operations.

The most _horrifying_ notion. That the activity of software development is
fundamentally incompatible with that of the business. For all our manifestos,
practices, methodologies, technical expertise and tools suddenly rendered
ineffective in the face of a framework built on abject values, at best
orthogonal to craft and engineering. 

The way projects are executed in large organisations do not support engineering
practices and autonomy that is required to build good systems. From how they're
funded to how they're managed. Tech organisations seem to understand this and
leverage organisational culture to get things done. Netflix has "Highly
Aligned, Loosely Coupled"[^netflix] and Spotify has "Squads, Chapters, Tribes
and Guilds". But even more fundamental than how teams are organised is to have
development of components managed and run as **products** instead of
projects[^products_vs_projects].

**Conjecture 3**: Requirements are harmful.

Yes, I'm going there. Requirements are categorically harmful. At worst, they're
an open invitation for people to stop thinking. They give false sense of
security that you're building the right thing that turns into an excuse not to
understand what it is you're building, why and for whom. They're an unfortunate
artifact of the _project_ approach to software development, instead of product.
Burn your requirements documents and allow your BAs to be BAs and spend that
effort on getting your devs to understand stories rather than producing requirements.

[^tough]: I find it no more easier now than when I started roughly 10 years ago.
[^netflix]:
  https://www.slideshare.net/reed2001/culture-1798664/94-Highly_Aligned_Loosely_Coupled_Highly
[^products_vs_projects]:
  https://www.thoughtworks.com/insights/blog/project-vs-product
