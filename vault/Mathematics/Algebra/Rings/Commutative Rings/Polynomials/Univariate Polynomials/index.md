---
title: Univariate Polynomials
tags:
  - univariate-polynomials
  - polynomials
  - ring-theory
  - abstract-algebra
  - algebra
  - mathematics
---

# Univariate Polynomials

>[!DEFINITION] Definition: Univariate Polynomial
>
>A **univariate polynomial** is a [[Polynomials|polynomial]] in a single variable.
>
>>[!NOTE]
>>
>>A univariate polynomial has the form
>>
>>$$
>>a_n x^n + \cdots a_{n-1}x^{n-1} + \cdots + a_1 x + a_0
>>$$
>>
>

# Properties

>[!THEOREM] Theorem: Ring of Univariate Polynomials
>
>Let $R$ be a [[index|commutative ring]].
>
>The [[Sets|set]] of all [[index|univariate polynomials]] over $R$ form a commutative ring together with [[Polynomials|polynomial addition]] and [[Polynomials|polynomial multiplication]].
>
>>[!NOTATION]
>>
>>This ring is often denoted as $R[x]$ or $R[X]$.
>>
>
>>[!PROOF]-
>>
>>TODO
>>
>

## Equality

>[!THEOREM] Theorem: Equality of Univariate Polynomials
>
>Let $A(x)$ and $B(x)$ be two [[Polynomials|nonzero]] [[index|polynomials]] over an [[Integral Domain]] with [[Polynomials|degrees]] $\deg(A)$ and $\deg(B)$.
>
>If $A(x)$ and $B(x)$ have the same [[Polynomials|value]] for $\max\{\deg(A), \deg(B)\}+1$ different values for $x$, then $A$ and $B$ are [[Polynomials|equal]].
>
>>[!PROOF]-
>>
>>TODO
>>
>

## Roots

>[!THEOREM] Theorem: Roots of Univariate Polynomials
>
>Let $A(x)$ be a [[index|univariate polynomial]] over a [[index|commutative ring]] $R$.
>
>An element $p \in R$ is a [[Polynomials|root]] of $A$ if and only if $A$ is [[Polynomial Division|divisible]] by $x - p$.
>
>>[!PROOF]-
>>
>>**In the forward direction:** Suppose that $p$ is a root of $A$, i.e. $A(p) = 0$. The [[Polynomial Division|polynomial remainder theorem]] then tells us that the remainder of the division of $A$ by $x-p$ is zero, i.e. $A$ is divisible by $x - p$.
>>
>>**In the backward direction:** Suppose that $A$ is divisible by $x-p$. This means that $A(x) = (x-p)Q(x)$ for some polynomial $Q$. Plugging in $p$ gives us $A(p) = (p - p)Q(p) = 0\cdot Q(p) = 0$ and so $p$ is a root of $A$.
>>
>

>[!THEOREM] Theorem: Number of Roots of Univariate Polynomials
>
>If $P(x)$ is a [[index|polynomial]] $P(x)$ over an [[Integral Domain]], then the maximum number of distinct [[Polynomials|roots]] which $P$ can have is equal its [[Polynomials|degree]] $\deg(P)$.
>
>>[!PROOF]-
>>
>>TODO
>>
>