---
title: Injections, Surjections and Bijections
tags:
  - functions
  - analysis
  - mathematics
---

# Injections

>[!DEFINITION] Definition: Injection
>
>A [[Functions|function]] $f: X \to Y$ is called **injective** if for each $y \in Y$ there is only one $x\in X$ such that $y = f(x)$.
>

>[!DEFINITION] Definition: Inverse Function
>
>The **inverse function** of an [[Injections, Surjections and Bijections|injection]] $f: X \to Y$ is the [[Functions|function]] $f^{-1}: f(X) \to X$ which to each $y \in Y$ assigns the $x \in X$ for which $y = f(x)$, i.e.
>
>$$
>f^{-1}(f(x)) = x
>$$
>

>[!DEFINITION] Definition: Involution
>
>An **involution** is a [[Functions|function]] $f: X \to Y$ which is its own [[Injections, Surjections and Bijections|inverse function]].
>
>$$
>f(f(x)) = x \qquad \forall x \in X
>$$
>

# Surjections

>[!DEFINITION] Definition: Surjection
>
>A [[Functions|function]] $f: X \to Y$ is called **surjective** if its [[Functions|image]] and [[Functions|codomain]] are equal, i.e. for each $y \in Y$ there is at least one $x \in X$ such that $y = f(x)$.
>

# Bijections

>[!DEFINITION] Definition: Bijection
>
>A [[Functions|function]] $f: X \to Y$ is called **bijective** if it is both [[Injections, Surjections and Bijections|injective]] and [[Injections, Surjections and Bijections|surjective]].
>


![[res/Injection, Surjection, Bijection.svg|Injection, Surjection, Bijection]]