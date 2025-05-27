---
title: Real Series
tags:
    - real-series
    - real-analysis
    - mathematics
---

# Partial Sums

>[!DEFINITION] Definition: Partial Sum
>
>Let $\{a_n\}_{n \in \mathcal{D}}$ be a [[Real Sequences|real sequence]].
>
>The $k$-th **partial sum** of $\{a_n\}$ is the sum of its first $k$ numbers:
>
>$$
>\sum_{\begin{align*}j &\in \mathcal{D} \\ j &\le k \end{align*}} a_j
>$$
>
>>[!NOTATION]-
>>
>>$$
>>s_k
>>$$
>>
>

# Real Series

Given a [[Real Sequences|real sequence]] $(a_n)_{n \in \mathcal{D}}$, it is apparent that the [[Functions of the Real Numbers|real-valued function]] which maps each $k \in \mathcal{D}$ to the $k$-th [[Real Series#partial sums|partial sum]] of $(a_n)_{n \in \mathcal{D}}$ is itself a [[Real Sequences|real sequence]] $(s_n)_{n \in \mathcal{D}}$.

>[!DEFINITION] Definition: Real Series
>
>A **real series** is the [[Real Sequences|sequence]] of [[Real Series#partial sums|partial sums]] of a [[Real Sequences|real sequence]].
>
>>[!NOTATION]-
>>
>>If the sequence is $(a_n)_{n \in \mathcal{D}}$, then we denote the sequence of its partial sums by $\displaystyle \sum_{n \in \mathcal{D}} a_n$. 
>>
>>When $\mathcal{D} = \mathbb{N}_0$ or $\mathcal{D} = \mathbb{N}$, we write $\displaystyle \sum_{n = 0}^{\infty} a_n$ or $\displaystyle \sum_{n = 1}^{\infty} a_n$, respectively.
>>
>>In the case, when $\mathcal{D} = \mathbb{N} \setminus \{0, 1, \dotsc, p - 1\}$ for some integer $p$, we write $\displaystyle \sum_{n = p}^{\infty} a_n$.
>>
>
