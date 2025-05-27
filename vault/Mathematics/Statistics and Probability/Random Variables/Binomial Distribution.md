---
title: Binomial Distribution
tags:
    - probability-theory
    - mathematics
---

# Binomial Distribution

>[!DEFINITION] Definition: Binomial Distribution
>
>We say that a [[Random Variables#Discrete Random Variable|discrete random variable]] $X$ has a **binomial distribution** if there exist some $n \in \mathbb{N}$ and some [[The Real Numbers|real number]] $p \in [0;1]$ such that
>
>$$
>P(X = k) = \binom{n}{k} p^k (1-p)^{n-k}
>$$
>
>for all $k \in \{0,1,2,\dotsc, n\}$.
>
>>[!NOTE]
>>
>>We often call $n$ and $p$ the parameters of the binomial distribution and say that $X$ is distributed according to the binomial distribution with parameters $n$ and $p$.
>>
>
>>[!NOTATION]
>>
>>$$
>>X \sim \mathop{\operatorname{Bin}}(n, p)
>>$$
>>
>

By far the most common random variable which has a binomial distributions is the following. Consider some [[Experiments|experiment]] $E_1$ with a [[Random Variables|random variable]] $Y$ which is distributed according to a [[Bernoulli Distribution]] with parameter $p$. Now consider the [[Experiments|experiment]] $E_2$ which consists of repeating $n$ times the $E_1$. The [[Random Variables|random variable]] $X$ which denotes the total number of times in which $Y$ was "success" follows the [[Binomial Distribution]] with parameters $n$ and $p$.

## Properties

>[!THEOREM]- Theorem: Cumulative Distribution Function of Binomial Distributions
>
>The [[Random Variables#Cumulative Distribution Function|cumulative distribution function]] of a [[Random Variables|discrete random variable]] $X$ which follows the [[Binomial Distribution]] $\operatorname{Bin}(n,p)$ is given by
>
>$$
>F(x) = \sum_{k = 0}^{\lfloor x \rfloor} \binom{n}{k} p^k (1-p)^{n-k}
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM]- Theorem: Probability Mass Function of Binomial Distributions
>
>The [[Random Variables#Probability Mass Functions|probability mass function]] $p$ of a [[Random Variables#Discrete Random Variables|discrete random variable]] $X$ which follows the [[Binomial Distribution]] $\mathop{\operatorname{Bin}}(n, p)$ is
>
>$$
>p(x) = \begin{cases}\binom{n}{k} p^x (1-p)^{n-x} \qquad \text{if } x \in \{0,1,2,\dotsc,n\} \\ 0 \qquad \text{otherwise}\end{cases}
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM]- Theorem: Mode of Binomial Distributions
>
>The [[Random Variables#Probability Mass Functions|mode(s)]] of a [[Random Variables|discrete random variable]] which follows the [[Binomial Distribution]] $\operatorname{Bin}(n, p)$ is (are):
>-  $\lfloor (n+1)p \rfloor$ if $(n+1)p$ is $0$ or a noninteger;
>- $(n+1)p$ and $(n+1)p - 1$ if $(n+1)p \in \{1, 2, \dotsc, n\}$;
>- $n$ if $(n+1)p = n+1$.
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM]- Theorem: Expectation of Binomial Distributions
>
>The [[Expectation]] of every [[Random Variables|random variable]] $X$ which follows the [[Binomial Distribution]] $\mathop{\operatorname{Bin}}(n,p)$ is given by the product of $n$ and $p$:
>
>$$
>\mathbb{E}(X) = np
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM]- Theorem: Variance of Binomial Distributions
>
>The [[Variance and Standard Deviation|variance]] of every [[Random Variables|random variable]] $X$ which follows the [[Binomial Distribution]] $\mathop{\operatorname{Bin}}(n,p)$ is equal to $np(1-p)$:
>
>$$
>\operatorname{Var}(X) = np(1-p)
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>