---
title: Convergence of Real Series
tags:
    - convergence
    - real-series
    - real-analysis
---

# Convergence

Since a [[Real Series]] $\displaystyle \sum_{n \in \mathcal{D}} a_n$ is just a [[Real Sequences|real sequence]], the definitions and terminology for convergence of series is the same as those used for [[Convergence of Real Sequences|convergence]] of sequences. What is different, however, is the notation used.

>[!NOTATION] Notation: Convergence of Real Series
>
>If $\displaystyle \sum_{n \in \mathcal{D}} a_n$ [[Convergence of Real Sequences|converges]] to $L$, we write
>
>$$
>\sum_{n \in \mathcal{D}} a_n = L
>$$
>
>Instead of calling $L$ the limit of $\displaystyle \sum_{n \in \mathcal{D}} a_n$, we usually say it is its **value**.
>

# Absolute Convergence

>[!DEFINITION] Definition: Absolute Convergence of Real Series
>
>A [[Real Series]] $\displaystyle \sum_{n \in \mathcal{D}} a_n$ **converges absolutely** to $L$ iff the [[Real Series|series]] $\displaystyle \sum_{n \in \mathcal{D}} |a_n|$ [[Convergence|converges]] to $L$.
>

## Properties

>[!THEOREM]- Theorem: Absolute Convergence $\implies$ Convergence
>
>If a [[Real Series]] is [[Convergence#absolute convergence|absolutely convergent]] towards $L \in \mathbb{C}$, then it is also [[Convergence|convergent]] towards $L$.
>
>>[!PROOF]-
>>
>>TODO
>>
>

# Conditional Convergence

>[!DEFINITION] Definition: Conditional Convergence
>
>A [[Real Series]] is **conditionally convergent** iff it is [[Convergence|convergent]] but not [[Convergence#absolute convergence|absolutely convergent]].
>

## Properties

>[!THEOREM]- The Riemann Series Theorem
>
>Let $(a_n)_{n \in \mathcal{D}}$ be an infinite [[Real Series]].
>
>>[!DEFINITION] Definition: Rearrangement
>>
>>A **rearrangement** of $(a_n)_{n \in \mathcal{D}}$ is another infinite [[Real Series]] $(a_n^{\sigma})_{n \in \mathcal{D}}$ which can be expressed as
>>
>>$$
>>a_{n}^{\sigma} = a_{\sigma (n)}
>>$$
>>
>>for some [[Permutations|permutation]] $\sigma$ of $\mathcal{D}$.
>>
>
>For each $L \in \mathbb{R}$, there exists a rearrangement of $(a_n)_{n \in \mathcal{D}}$ which [[Convergence|converges]] to $L$. There is exist also a rearrangement which [[Convergence|diverges]] to $+\infty$, a rearrangement which [[Convergence|diverges]] to $-\infty$ and a rearrangement which simply [[Convergence|diverges]].
>
>>[!INTUITION]-
>>
>>The terms of every [[Convergence#Conditional Convergence|conditionally convergent]] [[Real Series]] can also be rearranged to produce a sum which is equal to any real number of our choice, or which diverges to infinity or negative infinite or just does not approach any limit, finite or infinite.
>>
>
>>[!PROOF]-
>>
>>TODO
>>
>

# Criteria for Convergence and Divergence

>[!THEOREM]- Theorem: Divergence Test
>
>Let $\displaystyle \sum_{n \in \mathcal{D}} a_n$ be a [[Real Series]].
>
>If the [[Real Sequences|sequence]] $(a_n)_{n \in \mathcal{D}}$ [[Convergence of Real Sequences|diverges]] or its [[Convergence of Real Sequences|limit]] is not zero, then $\displaystyle \sum_{n \in \mathcal{D}} a_n$ [[Convergence of Real Sequences|diverges]].
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM]- Theorem: Minorant Divergence Test
>
>Let $\displaystyle \sum_{n \in \mathcal{D}} a_n$ be a [[Real Series]].
>
>If there exists some [[Convergence|divergent]] [[Real Series]] $\displaystyle \sum_{n \in \mathcal{D}} b_n$ and some integer $N$ such that $0 \le b_n \le a_n$ for all $n \ge N$, then $\displaystyle \sum_{n \in \mathcal{D}} a_n$ also [[Convergence|diverges]].
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM]- Theorem: Majorant Convergence Test
>
>Let $\displaystyle \sum_{n \in \mathcal{D}} a_n$ be a [[Real Series]].
>
>If there exists some [[Convergence|convergent]] [[Real Series]] $\displaystyle \sum_{n \in \mathcal{D}} b_n$ and some integer $N$ such that $|a_n| \le b_n$ for all $n \ge N$, then $\displaystyle \sum_{n \in \mathcal{D}} a_n$ is [[Convergence#absolute convergence|absolutely convergent]].
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM]- Theorem: Quotient Test
>
>Let $\displaystyle \sum_{n \in \mathcal{D}} a_n$ be a [[Real Series]].
>
>If the [[Real Sequences|sequence]] $\left|\frac{a_{n+1}}{a_n}\right|$ [[Convergence of Real Sequences|converges]], then $\displaystyle \sum_{n \in \mathcal{D}} a_n$ is:
>- [[Convergence#absolute convergence|absolutely convergent]] if 
>
>$$
>\displaystyle \lim_{n \to \infty} \left|\frac{a_{n+1}}{a_n}\right| \lt 1
>$$
>
>- [[Convergence|divergent]] if 
>
>$$
>\displaystyle \lim_{n \to \infty} \left|\frac{a_{n+1}}{a_n}\right| \gt 1
>$$
>
>>[!NOTE] 
>>
>>If $\displaystyle \lim_{n \to \infty} \left|\frac{a_{n+1}}{a_n}\right| = 1$, then this theorem is useless.
>>
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM]- Theorem: Square Root Test
>
>Let $\displaystyle \sum_{n \in \mathcal{D}} a_n$ be a [[Real Series]].
>
>If the [[Real Sequences|sequence]] $\sqrt[n]{|a_n|}$ [[Convergence of Real Sequences|converges]], then $\displaystyle \sum_{n \in \mathcal{D}} a_n$ is:
>- [[Convergence#absolute convergence|absolutely convergent]] if 
>
>$$
>\displaystyle \lim_{n \to \infty} \sqrt[n]{|a_n|} \lt 1
>$$
>
>- [[Convergence|divergent]] if 
>
>$$
>\displaystyle \lim_{n \to \infty} \sqrt[n]{|a_n|} \gt 1
>$$
>
>>[!NOTE] 
>>
>>If $\displaystyle \lim_{n \to \infty} \sqrt[n]{|a_n|} = 1$, then this theorem is useless.
>>
>
>>[!PROOF]-
>>
>>TODO
>>
>