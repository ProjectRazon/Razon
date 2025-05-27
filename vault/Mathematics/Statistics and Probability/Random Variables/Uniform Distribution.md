---
title: Uniform Distribution
tags:
    - probability-theory
    - mathematics
---

# Discrete Uniform Distribution

>[!DEFINITION] Definition: Discrete Uniform Distribution
>
>We say that a [[Random Variables#Discrete Random Variables|discrete random variable]] $X$ has a **uniform distribution** if its [[Random Variables|support]] $S = \{x_1,\dotsc, x_n\}$ is finite and its [[Random Variables|probability mass function]] $p$ is given by
>
>$$
>p(x) = \begin{cases}\frac{1}{n} \qquad x \in S \\ 0 \qquad \text{otherwise} \end{cases}
>$$
>
>>[!NOTATION]
>>
>>$$
>>X \sim U(n) \qquad X \in U(n)
>>$$
>>
>

# Continuous Uniform Distribution

>[!DEFINITION] Definition: Continuous Uniform Distribution
>
>We say that a [[Random Variables#Continuous Random Variable|continuous random variable]] has a **uniform distribution** on the interval $[a;b]$ (or $(a;b)$) if its [[Random Variables#Cumulative Distribution Functions|cumulative distribution function]] is given by
>
>$$
>F(x) = \begin{cases}0\qquad\text{ if } x \lt a \\ \frac{x-a}{b-a} \hphantom{..} \text{ if } a \le x \le b \\ 1 \qquad \text{ if } x \gt b\end{cases}
>$$
>
>>[!NOTATION]
>>
>>$$
>>X \sim U(a,b) \qquad X \in U(a,b)
>>$$
>>
>

## Properties

>[!THEOREM]- Theorem: Probability Density of Uniform Distributions
>
>The [[Random Variables|probability density function]] of a [[Random Variables#Continuous Random Variable|continuous random variable]] which has the [[Uniform Distribution#Continuous Uniform Distribution|uniform distribution]] $U(a,b)$ is given by
>
>$$
>f(x) = \begin{cases}\frac{1}{b-a} \hphantom{..}\text{ if } a \lt x \lt b \\ 0 \qquad \text{ otherwise }\end{cases}
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>