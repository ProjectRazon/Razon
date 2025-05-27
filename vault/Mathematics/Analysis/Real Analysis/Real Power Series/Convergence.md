---
title: Convergence of Real Power Series
tags:
    - real-power-series
    - real-analysis
    - mathematics
---

# Convergence
>[!DEFINITION] Definition: Convergence and Divergence of Power Series
>
>Let $\displaystyle \sum_{n \in \mathcal{D}} a_n (x-c)^n$ be [[index|real power series]] and let $x^{\ast} \in \mathbb{R}$.
>
>We say that $\displaystyle \sum_{n \in \mathcal{D}} a_n (x-c)^n$
>- **is convergent** or **converges** for $x^{\ast}$ if the resultant [[Real Series]] $\sum_{n \in \mathcal{D}} a_n (x^{\ast} - c)^n$ is [[Convergence|convergent]];
>- **is absolutely convergent** or **converges absolutely** for $x^{\ast}$ if the resultant [[Real Series]] $\sum_{n \in \mathcal{D}} a_n (x^{\ast} - c)^n$ is [[Convergence#absolute convergence|absolutely convergent]];
>- **is divergent** or **diverges** for $x^{\ast}$ if the resultant [[Real Series]] $\sum_{n \in \mathcal{D}} a_n (x^{\ast} - c)^n$ is [[Convergence|divergent]].
>

## Interval of Convergence

>[!THEOREM] Theorem: Interval of Convergence
>
>There are only three possibilities for the [[Convergence]] of every [[index|real power series]] $\displaystyle \sum_{n \in \mathcal{D}} a_n (x - c)^n$:
>- The power series [[Convergence|converges]] only for $x = c$.
>- The power series [[Convergence|converges]] for all $x \in \mathbb{R}$.
>- There exists some $r \gt 0$ such that the power series [[Convergence|converges]] if $x \in (c - r; c + r)$ and [[Convergence|diverges]] if $|x - c| \gt r$. In this case, the power series may or may not [[Convergence|converge]] for $x = c + r$ or $x = c - r$ or both 
>
>>[!PROOF]-
>>
>>TODO
>
>>[!DEFINITION] Definition: Interval of Convergence
>>
>>The [[Sets|set]] of all $x \in \mathbb{R}$ for which a [[index|power series]] $\displaystyle \sum_{n \in \mathcal{D}} a_n (x-c)^n$ [[Convergence|converges]] is known as its **interval of convergence** and if this interval is finite, then we call half of its length the **radius of convergence**.
>>
>>![[res/Interval of convergence.drawio.svg]]
>>
>

### Determining the Interval of Convergence

>[!ALGORITHM] Algorithm: Determining the Interval of Convergence
>
>We are given a [[index|real power series]] $\displaystyle \sum_{n \in \mathcal{D}} a_n (x-c)^n$ and want to determine its [[Convergence|interval of convergence]].
>
>1. Evaluate either one of the [[Convergence of Real Sequences|limits]] $\lim_{n \to \infty} \left| \frac{a_n}{a_{n+1}}\right|$ and $\lim_{n\to \infty} \frac{1}{\sqrt[n]{|a_n|}}$. Choose whichever one is easier to calculate.
>
>2. If the limit is zero, then the power series [[Convergence|converges]] only for $x = c$.
> 
>3. If the limit is $+\infty$, then the power series [[Convergence|converges]] for every $x \in \mathbb{R}$.
>
>4. If the limit is equal to some nonzero $r \in \mathbb{R}$, then the power series [[Convergence|converges]] for $x \in (c - r; c + r)$. However, we also need to check whether it converges for $x = c -r$ and $x = c + r$.
>	-  Evaluate the power series at $x = c - r$. If the resultant [[Real Series|series]] $\sum_{n \in \mathcal{D}} a_n (-r)^n$ is [[Convergence|convergent]], then the power series [[Convergence|converges]] for $x = c - r$ as well.
>	-  Evaluate the power series at $x = c + r$. If the resultant [[Real Series|series]] $\sum_{n \in \mathcal{D}} a_n r^n$ is [[Convergence|convergent]], then the power series [[Convergence|converges]] for $x = c + r$ as well.
>