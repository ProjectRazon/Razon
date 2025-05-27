---
title: Monomials
tags:
  - polynomials
  - ring-theory
  - abstract-algebra
  - algebra
  - mathematics
---

# Monomials

>[!DEFINITION] Definition: Monomial
>
>A **monomial** over a [[index|commutative ring]] $R$ in the [[TODO|variables]] $x_1, \cdots, x_n$ is an [[Formal Languages|expression]] of the form
>
>$$
>a x_n^{p_n} x_{n-1}^{p_{n-1}}\cdots x_2^{p_2}x_1^{p_1},
>$$
>
>where $a \in R, a \ne 0_R$ and $p_1, \cdots, p_n$ are non-negative [[TODO|integers]].
>
>>[!NOTATION]-
>>
>>If $p_i = 0$, then we do not write $x_i^0$ or $1$, we just do not write anything about $x_i$ at all.
>>
>>If $p_i = 1$, then we write simply $x_i$ instead of $x_i^1$. 
>>
>>We usually use capital Latin letters such as $M$ and $N$ to denote monomials. If we want to be explicit about the variables, we write $M(x_1, \cdots, x_n)$.
>>
>
>>[!DEFINITION] Definition: Coefficient of a Monomial
>>
>>We call $a$ the **coefficient** of the monomial.
>>
>

## Degree

>[!DEFINITION] Definition: Degree of a Monomial
>
>The **degree** of a [[Monomials|monomial]] $M = a x_n^{p_n} x_{n-1}^{p_{n-1}}\cdots x_2^{p_2}x_1^{p_1}$ is $\max \{p_1, \ldots, p_n\}$.
>
>>[!NOTATION]-
>>
>>$$
>>\deg(M)
>>$$
>>
>
>>[!EXAMPLE]-
>>
>>$$
>>\deg(4x^4 y^3 z^5) = 5
>>$$
>>
>>$$
>>\deg(9 y^2 z) = 2
>>$$
>>
>>$$
>>\deg(xy) = 1
>>$$
>>
>

## Equality

>[!DEFINITION] Definition: Equality of Monomials
>
>Two [[Polynomials|monomials]] $M = m x_n^{p_n} x_{n-1}^{p_{n-1}}\cdots x_2^{p_2}x_1^{p_1}$ and $M' = m' x_n^{p_n'} x_{n-1}^{p_{n-1}'}\cdots x_2^{p_2'}x_1^{p_1'}$ are **equal** if $m = m'$ and $p_k = p_k'$ for all $k \in \{1, \cdots, n\}$.
>
>>[!NOTE]
>>
>>The order of the variables $x_1, \cdots, x_n$ is irrelevant.
>>
>
>>[!NOTATION]-
>>
>>$$
>>M = M'
>>$$
>>
>
>>[!EXAMPLE]-
>>
>>$$
>>3x^2 y^3 = 3 y^3 x^2
>>$$
>>
>>$$
>>4x^4 y^2 z = 4 z x^4 y^2
>>$$
>>
>

# Operations

>[!DEFINITION] Definition: Monomial Addition
>
>The sum of two [[Monomials]] $M = m x_n^{p_n} x_{n-1}^{p_{n-1}}\cdots x_2^{p_2}x_1^{p_1}$ and $M' = m' x_n^{p_n} x_{n-1}^{p_{n-1}}\cdots x_2^{p_2}x_1^{p_1}$ is the monomial
>
>$$
>M + M' \overset{\text{def}}{=} (m+m') x_n^{p_n} x_{n-1}^{p_{n-1}}\cdots x_2^{p_2}x_1^{p_1}
>$$
>
>>[!EXAMPLE]-
>>
>>$$
>>2 x^3 y + 3 x^3 y = 5 x^3 y
>>$$
>>
>>$$
>>2.5 x_1^4 x_2^2 y^2 + 1.3 x_1^4 x_2^2 y^2 = 3.8 x_1^4 x_2^2 y^2
>>$$
>>
>

>[!DEFINITION] Definition: Monomial Multiplication
>
>Let $R$ be a [[index|commutative ring]] and let $M = m x_n^{p_n} x_{n-1}^{p_{n-1}}\cdots x_2^{p_2}x_1^{p_1}$ and $M' = m' x_n^{p_n'} x_{n-1}^{p_{n-1}'}\cdots x_2^{p_2'}x_1^{p_1'}$ be two [[Monomials]] over $R$.
>
>The **product** of a $M$ with $M'$ is defined as the monomial
>
>$$
>\begin{align*}MM' \overset{\text{def}}{=} (mm') x_n^{p_n + p_n'} x_{n-1}^{p_{n-1}+p_{n-1}'} \cdots x_2^{p_2 + p_2'}x_1^{p_1 + p_1'}\end{align*}
>$$
>
>>[!INTUITION]-
>>
>>Monomial multiplication is defined in this in order to follow the commutativity and associativity laws for the underlying ring.
>>
>
>>[!EXAMPLE]-
>>
>>$$
>>(3 x^4 y) \cdot (2 x^4 y) = (2\cdot 3) x^{4+4} y^{1 + 1} = 6 x^8 y^2
>>$$
>>
>>$$
>>(11 x^3 y^2 z)\cdot(2 y z^2) = (11 x^3 y^2 z)\cdot( 2 x^0 y z^2) = (11 \cdot 2)(x^{3 + 0} y^{2 + 1} z^{1 + 2}) = 22 x y^3 z^3
>>$$
>>
>>$$
>>(x^3 y)(y z^3) = (x^3 y z^0)(x^0 y z^3) = (1 \cdot 1) (x^{3+0} y^{1+1} z^{0+3}) = x^3 y^2 z^3
>>$$
>>
>