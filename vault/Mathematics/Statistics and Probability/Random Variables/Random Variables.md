---
title: Random Variables
tags:
    - probability-theory
    - mathematics
---

# Random Variables

>[!DEFINITION] Definition: Random Variable
>
>Suppose we have an [[Experiments|experiment]] with [[Experiments|sample space]] $\Omega$.
>
>A **random variable** is a [[Functions of the Real Numbers|real-valued function]] $X: \Omega \to \mathbb{R}$.
>
>>[!DEFINITION] Definition: Discrete and Continuous Random Variables
>>
>>If the [[Functions|image]] of $X$ is [[Countable Sets|countable]], then we call $X$ a **discrete random variable**. Otherwise, we call it a **continuous random variable**.
>>
>
>>[!NOTATION]
>>
>>It is typical to denote random variables via capital letters.
>>
>

A random variable is just a way to assign a value to each outcome in the [[Experiments|sample space]] of an [[Experiments|experiment]].

>[!EXAMPLE]-
>
>Consider the experiment of tossing a coin twice. The sample space is $S = \{\mathrm{TT}, \mathrm{HT}, \mathrm{TH}, \mathrm{HH}\}$. One [[Random Variables|random variable]] we could define is the number of heads $X$ which appear in the outcome. We would then have
>
>$$
>\begin{align*}
>X(\mathrm{TT}) = 0 \\
>X(\mathrm{TH}) = 1 \\
>X(\mathrm{HT}) = 1 \\
>X(\mathrm{HH}) = 2
>\end{align*}
>$$
>

## Cumulative Distribution Functions

>[!DEFINITION] Definition: Cumulative Distribution Function (CDF)
>
>The **cumulative distribution function** of a [[Random Variables#Continuous Random Variables|continuous random variable]] $X: \Omega \to \mathbb{R}$ is the [[Functions of the Real Numbers|function]] $F_X: \mathbb{R} \to [0;1]$ which to each $x \in \mathbb{R}$ assigns the [[Probability Spaces|probability]] that $X$ is less than $x$ when the [[Experiments|experiment]] is carried out.
>
>$$
>F_X(x) \overset{\text{def}}{=} P(X \lt x)
>$$
>

>[!THEOREM]- Theorem: Probability in an Interval
>
>The [[Probability Spaces|probability]] that the value of a [[Random Variables#Continuous Random Variables|continuous random variable]] $X$ falls in the interval $[[Random Variables#Cumulative Distribution Functions|a; b)$ is the difference in its [cumulative distribution function]] evaluated at $a$ and $b$:
>
>$$
>P(a \le X \lt b) = F(b) - F(a)
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM]- Theorem: Monotony of the CDF
>
>The [[Random Variables#Cumulative Distribution Functions|cumulative distribution function]] of each [[Random Variables#Continuous Random Variables|continuous random variable]] is [[Monotony|increasing]].
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM]- Theorem: Limits of the CDF
>
>The [[Limits of Real Functions|limits]] of the [[Random Variables#Cumulative Distribution Functions|cumulative distribution function]] $F_X$ of each [[Random Variables#Continuous Random Variables|continuous random variable]] $X$ for $x \to -\infty$ and $x \to +\infty$ are $0$ and $1$, respectively.
>
>$$
>\begin{align*}
>\lim_{x \to -\infty} F_X(x) = 0 \\
>\lim_{x \to +\infty} F_X(x) = 1
>\end{align*}
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

# Discrete Random Variables

>[!DEFINITION] Definition: Discrete Random Variables
>
>A [[Random Variables|random variable]] is **discrete** if and only if its [[Functions|image]] is [[Countable Sets|countable]].
>

Essentially, a [[Random Variables#Discrete Random Variables|discrete random variable]] can take on either finitely many values or it can take on infinitely many values which can be arranged in a [[Real Sequences|real sequence]].

>[!EXAMPLE]-
>
>Consider the experiment of tossing a coin twice. The sample space is $S = \{\mathrm{TT}, \mathrm{HT}, \mathrm{TH}, \mathrm{HH}\}$. One [[Random Variables|random variable]] we could define is the number of heads $X$ which appear in the outcome. We would then have
>
>$$
>\begin{align*}
>X(\mathrm{TT}) = 0 \\
>X(\mathrm{TH}) = 1 \\
>X(\mathrm{HT}) = 1 \\
>X(\mathrm{HH}) = 2
>\end{align*}
>$$
>
>This is a [[Random Variables#Discrete Random Variables|discrete random variable]], since it can take on only three possible values, namely $0$, $1$ and $2$.
>

## Probability Mass Functions

>[!DEFINITION] Definition: Probability Mass Function
>
>The **probability mass function** of a [[Random Variables#Discrete Random Variables|discrete random variable]] $X: \Omega \to \mathbb{R}$ is the [[Functions of the Real Numbers|function]] $p_X: \mathbb{R} \to [0;1]$ which to each possible value $x \in X(\Omega)$ of $X$ assigns the [[Probability Spaces|probability]] that $X$ is equal to $x$ when the [[Experiments|experiment]] is carried out.
>
>$$
>p_X(x) \overset{\text{def}}{=} P(X = x)
>$$
>

>[!DEFINITION] Definition: Support of a Discrete Random Variable
>
>The **support** of a [[Random Variables#Discrete Random Variables|discrete random variable]] $X: \Omega \to \mathbb{R}$ is [[Sets|set]] of all values $x_1, x_2, \dotsc \in \mathbb{R}$ which $X$ can take on with a nonzero probability.
>
>$$
>\{ x \in \mathbb{R} \mid P(X = x) \gt 0\}
>$$
>

>[!DEFINITION] Definition: Mode
>
>A **mode** of a [[Random Variables#Discrete Random Variable|discrete random variable]] $X$ is the [[The Real Numbers|real number]] $m \in \mathbb{R}$ for which the [[Random Variables#Probability Mass Functions|probability mass function]] of $X$ is maximum.
>

# Continuous Random Variable

>[!DEFINITION] Definition: Continuous Random Variable
>
>A [[Random Variables|random variable]] is **continuous** if and only if it is not [[Random Variables#Discrete Random Variables|discrete]] and its [[Random Variables#Cumulative Density Functions|cumulative distribution function]] is [[Differentiability|differentiable]] except for possibly finitely many points where it is [[Continuity|continuous]] but not [[Differentiability|differentiable]].
>

## Probability Density Function

>[!DEFINITION] Definition: Probability Density Function
>
>The **probability density function** of a [[Random Variables#Continuous Random Variables|continuous random variable]] is the [[Differentiability|derivative]] of its [[Random Variables#Cumulative Density Functions|cumulative distribution function]].
>

### Properties

>[!THEOREM]- Theorem: Non-negativity of Probability Density
>
>The [[Random Variables|probability density function]] $f$ of a [[Random Variables#Continuous Random Variables|continuous random variable]] is always non-negative.
>
>$$
>f(x) \ge 0
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
> 

>[!THEOREM]- Theorem: Probability in Interval
>
>The [[Probability Spaces|probability]] that a [[Random Variables#Continuous Random Variables|continuous random variable]] $X$ falls within the interval $[a;b]$ is given by the [[Definite Integrals|definite integral]] of its [[Random Variables|probability density function]] $f$ over $[a;b]$:
>
>$$
>P(a \le X \le b) = \int_{[a;b]} f
>$$
>
>>[!PROOF]-
>>
>>
>>TODO
>

>[!THEOREM]- Theorem: Normalization of Probability Density
>
>The [[Definite Integrals#Improper Integrals|integral]] of the [[Random Variables|probability density function]] $f$ of a [[Random Variables#Continuous Random Variables|continuous random variable]] from $-\infty$ to $+\infty$ is $1$:
>
>$$
>\int_{-\infty}^{+\infty} f = 1
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

# Bibliography