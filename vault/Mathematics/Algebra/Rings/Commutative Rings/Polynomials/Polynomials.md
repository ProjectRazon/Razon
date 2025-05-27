---
title: Polynomials
tags:
  - polynomials
  - ring-theory
  - abstract-algebra
  - algebra
  - mathematics
---

# Polynomials

>[!DEFINITION] Definition: Polynomial
>
>A **polynomial** over a [[index|commutative ring]] $R$ in the [[TODO|variables]] $x_1, \cdots, x_n$ is an [[Formal Languages|expression]] which can be written as a finite sum of [[Monomials]] in $x_1, \cdots, x_n$.
>
>>[!NOTATION]-
>>
>>We usually use capital Latin letters such as $P$ and $Q$ to denote polynomials. If we want to be explicit about the variables, we write $P(x_1, \cdots, x_n)$.
>>
>
>>[!DEFINITION] Definition: Leading Coefficient
>>
>>The **leading coefficient** of a [[Polynomials|polynomial]] is the [[Monomials|coefficient]] of its highest-[[Monomials|degree]] [[Monomials|monomial]].
>>
>

>[!DEFINITION] Definition: Zero Polynomial
>
>The **zero polynomial** over a [[index|commutative ring]] $R$ in the variables $x_1, \cdots, x_n$ is the [[Polynomials|polynomial]] whose coefficients are all $0$, i.e. 
>
>$$
>\mathcal{Z}(x_1, \cdots, x_n) = 0
>$$
>

## Degree

>[!DEFINITION] Definition: Degree of a Polynomial
>
>The **degree** of a [[Polynomials|nonzero]] [[Polynomials|polynomial]] $P$ is the highest [[Monomials|degree]] amongst its [[Monomials]].
>
>>[!NOTATION]
>>
>>$$
>>\deg(P)
>>$$
>>
>
>>[!EXAMPLE]-
>>
>>$$
>>\deg(3x^3 y + 4z^5 x^3 y^2) = 5
>>$$
>>
>

## Evaluation

>[!DEFINITION] Definition: Evaluation of a Polynomial
>
>Let $P(x_1, \cdots, x_n)$ be a [[Polynomials|polynomial]] over a [[index|commutative ring]] $R$.
>
>The **value** or **evaluation** of $P$ at an $n$-[[Tuples]] $(r_1, \cdots, r_n)$, where $r_1, \cdots, r_n \in R$, is obtained by replacing $x_i$ with $r_i$ and carrying out all ring operations.
>
>>[!NOTATION]
>>
>>$$
>>P(r_1, \cdots, r_n)
>>$$
>>
>

### Roots

>[!DEFINITION] Definition: Root of a Polynomial
>
>The **roots** of a [[Polynomials|polynomial]] $P$ are the [[Polynomial Equations|solutions]] to the [[Polynomial Equations|polynomial equation]] $P = 0$.
>

## Equality

>[!DEFINITION]
>
>Two [[Polynomials]] are **equal** if they are built from the [[Monomials|same]] [[Monomials]].
>
>>[!NOTE]
>>
>>The order of the monomials is irrelevant.
>
>>[!EXAMPLE]-
>>
>>$$
>>4x^2 y z^4 - 3x^3 y + 7z^2 = 7z^2 + 4x^2 y z^4 - 3x^3 y
>>$$
>>
>

>[!THEOREM]- Theorem: Equality of Univariate Polynomials
>
>Let $A(x)$ and $B(x)$ be [[Polynomials]] and let $n$ be equal to the larger of the [[Polynomials#Degree|degrees]] of $A$ and $B$, i.e. $n = \max \{\deg(A), \deg(B)\}$.
>
>If one can find $n+1$ distinct values $x_1, \dotsc, x_{n+1}$ such that the [[Polynomials#Evaluation|evaluations]] $A(x_1), \dotsc, A(x_{n+1})$ are respectively equal to $B(x_1), \dotsc, B(x_{n+1})$, then $A$ and $B$ are [[Polynomials#Equality|equal]].
>
>>[!PROOF]-
>>
>>TODO
>>
>

# Operations

>[!DEFINITION] Definition: Polynomial Addition
>
>TODO
>

>[!DEFINITION] Definition: Polynomial Multiplication
>
>TODO
>