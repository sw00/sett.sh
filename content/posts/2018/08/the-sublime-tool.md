---
title: "The Sublime Tool"
date: 2018-08-21T19:23:38+02:00
draft: true
markdown: mmark
tags: ['craft', 'tools', 'software dev']
---
This was initially meant to be a technical post like I promised, but I was faced with several
dilemmas: 

1. Any particular tech I write about will be obsolete by [next
   Tuesday](https://blogs.msdn.microsoft.com/larryosterman/2004/03/30/one-in-a-million-is-next-tuesday/), the standard unit of time it takes for unlikely events to
   occur in computing..
2. There will always be much better resources elsewhere, because
3. I'm not an expert in anything.

So instead of yet another tutorial on test-driven Ansible or the hottest web
framework of the week, I present to you some general ideas with a better shelf-life.

---

I recently finished reading a rather interesting book, [_The Craftsman_ by
Richard Sennett](https://www.goodreads.com/book/show/19075322-the-craftsman).
It had quite a lot of insights that reified some of the intuitions I've been
having about the nature of work, learning, teaching, flow state, craft and
mastery.  Whether explicitly or not, I'd like to unpack some of
the little big ideas in the book here as I digest them over time.

It's impossible to speak of craft without mentioning tools. Tools will form an
essential part of any technical pursuit. But in fact, most of any human
activity will involve a tool of some kind. They're so ubiquitous and obvious
that we take them for granted, but it can be argued that our tools are an
extension of ourselves [^kubrick].

> “When we bring down the hammer we do not feel that its handle has struck our
> palm but that its head has struck the nail\... I have a subsidiary awareness
> of the feeling in the palm of my hand which is merged into my focal awareness
> of my driving in the nail.”

# Fit-for-purpose vs all-purpose

In the book, Sennett reflects on the nature of tools and their role and
significance to the craftsperson. He discovers that tools tend to fall into two
broad categories and have distinct properties. The first is the
_fit-for-purpose_ tool, which yields no ambiguity about how it should be used.
He uses the Phillips head screwdriver as an example, but this notion can be
easily extended to the realm of software development (think
[DSL](https://en.wikipedia.org/wiki/Domain-specific_language)s or GNU
tools). In the abstract, the notion of tools can be expanded to
include shopping lists, agile methodologies or even musical scales.

The thing about _fit-for-purpose_ tools though, is that the very quality that
makes them highly effective is also what makes them inflexible and rigid in
their use. This imbues them with a bias toward singular, goal-oriented
activities. But this is all obvious. It's really why we have the mantra: 
_pick the right tool for the job_.

A far more interesting object in contrast to the _fit-for-purpose_ tool, is the
_all-purpose_ tool. Such a tool is challenging because it's not immediate
obvious how to use it most effectively[^scalpels]. It's often so basic in form that it
seems incomplete but that makes it highly adaptable. It's up to the wielder to
improvise with it, adapting its form to meet the challenges they're facing. Such
a tool can be described as _sublime_: an object simple in form that can seemingly
do anything.

> Getting better at using tools comes to us, in part, when the tools challenge
> us, and this challenge often occurs just because the tools are not
> fit-for-purpose.

An _all-purpose_ tool, by nature, demands a deeper engagement in the act of
using it. Not only that, it demands a nuanced awareness of the situation to
which the tool is applied. It can then be said that it's well suited to open
problems with high uncertainty and ambiguity that direct, mechanical
application cannot solve. 

# Cool story, bro?

"Great, but how is this useful?", you ask. What does it have to do with
software development? Well, let's break it down into simple propositions
about how software is built:

1. The activity of developing software is extremely context-sensitive[^context].
2. The inputs to sofware development are numerous and ambiguous[^ambiguous].

Seeing the connection yet? These insights should should raise a rather
important question: what is the _sublime_, _all-purpose_ tool in software
development? One that's adaptable and not tightly coupled to any tech stack,
context or situation? Such an instrument would be the most valuable thing in a
developer's proverbial toolbox.

I'd hazard that the closest thing to something like that is the _ability to
reason_. **There is no substitute for thinking**. Again, so obvious it seems like 
a cop-out, but it's difficult to understate how much we try to avoid using this 
tool. As individuals, reaching for the newest latest [buzzword] technology and 
as organisations investing millions into agile methodology certifications. The
selective pressure to achieve arbitrary measures of success rather than 
engaging with the things we're trying to produce[^arbitrary].

We also tend to overlook that the sublime tool is not static. It has the
potential to be a precision instrument, like a surgeon's scalpel. It can be
mastered, adapted, improved upon.

# Acquiring precision

I think, to improve is equivalent to being more precise. Precision can't be
acquired if meaning is implicit, hidden and we're lackadaisical in the way we
communicate. Based on this, we can smell that the use of language is a strong
input to quality of thinking. See what I just did there?

So semantics are important. But fluency in language comes with exposure, so I'd
encourage you to read. A lot. Read code, read documentation, read fiction, read
magazines, read comics, film screenplays, cooking recipes, cereal box
ingredients, lease agreements and contracts. And I don't mean this from only in
an Anglo-centric sense. Read in the language that you think in. The benefit
you want to acquire is ultimately richness in thought (knowing a lot of words
is just a second-order effect).

What else? Pointing out the relationship between language and cognition and
telling you to read isn't exactly "precise". True, there are more formal
methods. I think being exposed to Propositional Logic[^logic] is the best hack
to mastering the sublime tool. In fact, I think Propositional Logic is probably
the closest manifestation of a truly "all-purpose" tool. Simple in form and not
immediately obvious in its use, but mastering it yields great benefit in every
sphere of life. And it's not just for developers either. Really, go get your
grandma hooked on Propositional Logic, you won't regret it[^grandma].


[^kubrick]: This idea is stretched to the most profound extent by Kubrick in that single, iconic, brilliant [match cut](https://youtu.be/mI3s5fA7Zhk).
[^scalpels]: Sennett uses the scalpel as an example: early surgeons learnt how to use the new precision instrument only by trial and error.
[^context]: As evidenced by the failure of methodologies like SaFE, SCRUM, etc. to produce consistent repeatable results. No other technical discipline sees such huge variances between input/outputs.
[^ambiguous]: Unlike physical production, which is more-or-less constrained by the natural laws of physics, the building software often more of a social process than it is an engineering discipline. This does not mean we aren't systematic or can't be.
[^arbitrary]: Part of the problem is that we view success as a one-dimensional "thing to be achieved" rather than an ongoing process with no discrete parts. Ironically, this "ends-means" thinking is a big obstacle in producing good work.
[^logic]: A great introductory tutorial: https://brilliant.org/wiki/propositional-logic/
[^grandma]: Realistically though, you should start with people you work with professionally.
