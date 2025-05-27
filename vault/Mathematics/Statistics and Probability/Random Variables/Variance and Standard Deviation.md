---
title: Variance and Standard Deviation
tags:
    - probability-theory
    - mathematics
---


# Variance

>[!DEFINITION] Definition: Variance
>
>The **variance** of a [[Random Variables|random variable]] $X$ is the [[Expectation]] of square of the deviation from $X$'s [[Expectation]]:
>
>$$
>\mathbb{E}[(X - \mathbb{E}[X])^2]
>$$
>
>>[!NOTATION]
>>
>>$$
>>\mathop{\operatorname{Var}} (X) \qquad \sigma^2 \qquad s^2 \qquad V(X) \qquad \mathbb{V}(X)
>>$$
>>
>

>[!TIP] Tip: Discrete Variance
>
>The [[Variance and Standard Deviation|variance]] of a [[Random Variables#Discrete Random Variable|discrete random variable]] $X$ with [[Random Variables#Discrete Random Variable|support]] $S = \{x_1, x_2, \dotsc\}$ and [[Random Variables#Discrete Random Variable|probability mass function]] $p$ is given by the [[Convergence|value]] of the following [[Real Series|series]]:
>
>$$
>\sigma^2 = \sum_{i = 1}^{\infty} p(x_i) \cdot (x_i - \mathbb{E}[X])^2
>$$
>
>If $S$ is finite, then this reduces to a simple sum:
>
>$$
>\sigma^2 = \sum_{i = 1}^{|S|} p(x_i) \cdot (x_i - \mathbb{E}[X])^2
>$$
>

## Properties

>[!THEOREM]- Theorem: Computation Formula for Variance
>
>The [[Variance and Standard Deviation|variance]] of every [[Random Variables|random variable]] $X$ is the difference between the [[Expectation]] of its square and the square of its [[Expectation]]:
>
>$$
>\sigma^2 = \mathbb{E}[X^2] - \mathbb{E}[X]^2
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM]- Theorem: Variance of a Constant
>
>The [[Variance and Standard Deviation|variance]] of a constant [[Random Variables|random variable]] is zero.
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM]- Theorem: Variance of Constant Multiple
>
>The [[Variance and Standard Deviation|variance]] of a constant multiple $\lambda \in \mathbb{R}$ of a [[Random Variables|random variable]] $X$ is equal to the square of $\lambda$ multiplied by the [[Variance and Standard Deviation|variance]] of $X$:
>
>$$
>\mathop{\operatorname{Var}}(\lambda \cdot X) = \lambda^2 \cdot \mathop{\mathrm{Var}}(X)
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM]- Theorem: Variance of Sum and Difference
>
>If $X$ and $Y$ are two [[Random Variables]], then the [[Variance and Standard Deviation|variance]] of their and the [[Variance and Standard Deviation|variance]] of their difference are both equal to the sum of their [[Variance and Standard Deviation|variances]]:
>
>$$
>\begin{align*}
>\mathop{\operatorname{Var}}(X + Y) = \mathop{\operatorname{Var}}(X) + \mathop{\operatorname{Var}}(Y) \\
>\mathop{\operatorname{Var}}(X - Y) = \mathop{\operatorname{Var}}(X) + \mathop{\operatorname{Var}}(Y)
>\end{align*}
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

# Standard Deviation

>[!DEFINITION] Definition: Standard Deviation of a Random Variable
>
>The **standard deviation** of a [[Random Variables|random variable]] $X$ is the square-root of its [[Variance and Standard Deviation#Variance|variance]].
>
>$$
>\sqrt{\mathop{\operatorname{Var}}(X)}
>$$
>
>>[!NOTATION]
>>
>>$$
>>\sigma \qquad \sigma_X \qquad s
>>$$
>>
>