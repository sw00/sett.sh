---
title: "On Complexity"
date: 2020-02-23T12:56:47+02:00
draft: true
---
My problem partly has to do with the notion of _complexity_. Generally speaking, we can say a system is complex if it consist of interacting parts that are numerous _and_ differentiated. 
Humans can understand this intuitively: something that is more complex is more difficult to reason about.
This heuristic is often superficially applied by software development teams to discuss the merits of an approach or design.

# Accidental or essential?

Of course, when talking about complexity in software we can't get away from the seminal treatment of it from Fred Brooks' "No Silver Bullet" essay. The gist of it is this: 

- there are two kinds of complexity: accidental and essential
- acccidental complexity is a byproduct of the technology we choose to implement a solution
- essential complexity is the byproduct of the problem space (domain)

In practice, I doubt that it can be so neatly separated and there's probably a continuum between the two. However, this has some interesting implications: I think it follows that accidental complexity is more _reducible_[^refactoring] than its counterpart, i.e. it's possible to make things simpler but keep their meaning. 

# So what

Perhaps it's because I've been stuck in the thick of it all for the past year, wrangling configuration in the form of YAML 

# Simple 

- incremental vs fundamental

[^refactoring]: In practice, the process of _reducing_ something is synonymous with _refactoring_. 