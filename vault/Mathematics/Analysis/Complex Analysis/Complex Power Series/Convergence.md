---
title: Convergence of Complex Power Series
tags:
    - convergence
    - complex-power-series
    - complex-analysis
    - mathematics
---

# Convergence

>[!DEFINITION] Definition: Convergence and Divergence of Power Series
>
>Let $\displaystyle \sum_{n \in \mathcal{D}} a_n (x-c)^n$ be [[Complex Power Series]] and let $x^{\ast} \in \mathbb{R}$.
>
>We say that $\displaystyle \sum_{n \in \mathcal{D}} a_n (x-c)^n$
>- **is convergent** or **converges** for $x^{\ast}$ if the resultant [[Complex Series]] $\sum_{n \in \mathcal{D}} a_n (x^{\ast} - c)^n$ is [[Convergence|convergent]];
>- **is absolutely convergent** or **converges absolutely** for $x^{\ast}$ if the resultant [[Complex Series]] $\sum_{n \in \mathcal{D}} a_n (x^{\ast} - c)^n$ is [[Convergence#absolute convergence|absolutely convergent]];
>- **is divergent** or **diverges** for $x^{\ast}$ if the resultant [[Complex Series]] $\sum_{n \in \mathcal{D}} a_n (x^{\ast} - c)^n$ is [[Convergence|divergent]].
>

## Radius of Convergence

>[!THEOREM] Theorem: Radius of Convergence
>
>There are only three possibilities for the [[Convergence]] of every [[Complex Power Series]] $\displaystyle \sum_{n \in \mathcal{D}} a_n (x - c)^n$:
>- The power series [[Convergence|converges]] only for $x = c$.
>- The power series [[Convergence|converges]] for all $x \in \mathbb{C}$.
>- There exists some $r \gt 0$ such that the power series [[Convergence|converges]] if $|x - c| \lt r$ and [[Convergence|diverges]] if $|x - c| \gt r$. If $|x - c| = r$, then the power series may or may not converge and it might do so only for some points but not for others.
>
>![[res/Radius of Convergence.drawio.svg]] 
>
>>[!PROOF]-
>>
>>TODO
>
>>[!DEFINITION] Definition: Radius of Convergence
>>
>>If $r$ exists, then we call it the **radius of convergence**. Furthermore, if the power series converges only for $x = c$, we usually say that the radius of convergence is zero. If the power series converges for all $x \in \mathbb{C}$, then we say that the radius of convergence if infinite.
>>
>

### Determining the Radius of Convergence

>[!ALGORITHM] Algorithm: Determining the Radius of Convergence
>
>We are given a [[Complex Power Series|real power series]] $\displaystyle \sum_{n \in \mathcal{D}} a_n (x-c)^n$ and want to determine its [[Convergence|radius of convergence]].
>
>1. Evaluate either one of the [[Convergence of Real Sequences|limits]] $\lim_{n \to \infty} \left| \frac{a_n}{a_{n+1}}\right|$ and $\lim_{n\to \infty} \frac{1}{\sqrt[n]{|a_n|}}$. Choose whichever one is easier to calculate.
>
>2. If the limit is zero, then the power series [[Convergence|converges]] only for $x = c$.
> 
>3. If the limit is $+\infty$, then the power series [[Convergence|converges]] for every $x \in \mathbb{R}$.
>
>4. If the limit is some nonzero real number, then it is the radius of convergence.
>