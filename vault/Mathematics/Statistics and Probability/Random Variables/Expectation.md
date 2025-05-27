---
title: Expectation
tags:
    - probability-theory
    - mathematics
---


# Expectation

>[!DEFINITION] Definition: Expectation (Discrete Case)
>
>The **expectation** of a [[Random Variables#Discrete Random Variables|discrete random variable]] $X$ with [[Random Variables#Discrete Random Variables|support]] $S = \{s_1, s_2, \dotsc\}$ and [[Random Variables|probability mass function]] $p$ is the value of the [[Convergence|series]]
>
>$$
>\sum_{i=1}^{\infty} s_i \cdot p(s_i),
>$$
>
>if it exists.
>
>>[!TIP] Note: Finite Support
>>
>>If the [[Random Variables#Discrete Random Variables|support]] $S$ is finite, then the [[Expectation]] of $X$ reduces to the sum
>>
>>$$
>>\sum_{i = 1}^{|S|} s_i \cdot p(s_i)
>>$$
>>
>

>[!DEFINITION] Definition: Expectation (Continuous Case)
>
>The **expectation** of a [[Random Variables#Continuous Random Variables|continuous random variable]] $X$ with [[Random Variables|probability function]] $f$ is the [[Definite Integrals#Improper Integrals|integral]] of $x f(x)$ from $-\infty$ to $+\infty$:
>
>$$
>\int_{-\infty}^{+\infty} x f(x) \mathop{\mathrm{d}x}
>$$
>

>[!NOTATION]
>
>The [[Expectation]] of a [[Random Variables|random variable]] $X$ is usually denoted in one of the following ways:
>
>$$
>EX \qquad \mathrm{E}[X] \qquad \mathrm{E}(X) \qquad \mathbb{E}(X) \qquad \langle X \rangle \qquad \bar{X} \qquad \mu_X
>$$
>

>[!NOTE]
>
>The [[Expectation]] of a [[Random Variables|random variable]] may also be called its **expected value** or **mean**.
>

## Properties

>[!THEOREM]- Theorem: Range of the Expected Value
>
>The [[Expectation]] of a [[Random Variables|random variable]] $X$ always lies between its minimum and maximum value:
>
>$$
>\mathbb{E}[X] \in [\min X; \max X]
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM]- Theorem: Linearity of Expectation
>
>[[Expectation]] is a [[Linear Transformation|linear]] operation - for all [[Random Variables]] $X$ and $Y$ and all $\lambda, \mu \in \mathbb{R}$, we have
>
>$$
>\mathbb{E}[\lambda X + \mu Y] = \lambda \, \mathbb{E}[X] + \mu \, \mathbb{E}[Y]
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM]- Theorem: Law of the Unconscious Statistician (LOTUS)
>
>Let $X$ be a [[Random Variables|random variable]] and let $g: \mathbb{R} \to \mathbb{R}$ be a [[Functions of the Real Numbers|real function]].
>
>If $X$ is [[Random Variables#Discrete Random Variables|discrete]] with [[Random Variables#Discrete Random Variables|support]] $S = \{x_1, x_2, \dotsc \}$ and [[Random Variables#Discrete Random Variables|probability mass function]] $p$, the [[Expectation]] of $g(X)$ is given by the [[Convergence|value]] of the following [[Real Series|series]]:
>
>$$
>\mathbb{E}[g(X)] = \sum_{i} g(x_i) \cdot p(x_i)
>$$
>
>If $X$ is [[Random Variables#Continuous Random Variables|continuous]] with [[Random Variables#Continuous Random Variables|probability density function]] $p$, then the [[Expectation]] of $g(X)$ is given by the following [[Definite Integrals#Improper Integrals|integral]]:
>
>$$
>\mathbb{E}[g(X)] = \int_{-\infty}^{+\infty} g(x) p(x) \mathop{\mathrm{d}x}
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

# Independent Random Variables

>[!DEFINITION] Definition: Independent Random Variables
>
>Two [[Random Variables]] $X$ and $Y$ are **independent** if and only if the [[Experiments|events]] $x \lt X$ and $y \lt Y$ are [[Probability Spaces#Conditional Probability|independent]] for all $x, y \in \mathbb{R}$.
>

## Properties

>[!THEOREM]- Theorem: Expectation of the Product of Independent Random Variables
>
>The [[Expectation]] of the product of two [[Expectation#Independent Random Variables|independent]] [[Random Variables]] $X$ and $Y$ is equal to the product of their [[Expectation|expectations]]:
>
>$$
>\mathbb{E}[X \cdot Y] = \mathbb{E}[X] \cdot \mathbb{E}[Y]
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>