---
title: Real Analytic Functions
tags:
  - analytic-functions
  - real-functions
  - real-analysis
  - analysis
  - mathematics
---

>[!DEFINITION] Definition: Real Analytic Function
>
>A **real analytic function** is a [[Functions of the Real Numbers|real function]] $f: D \to \mathbb{R}$ on an [[Intervals|open interval]] $D \subseteq \mathbb{R}$ for which there exists a [[index|real power series]] $\displaystyle \sum_{n=0}^\infty c_n (x-a)^n$ [[Convergence#^intervalofconvergence]] on $D$ with
>
>$$
>f(x) = \displaystyle \sum_{n=0}^\infty c_n (x-a)^n \qquad \forall x \in D
>$$
>

# Properties

>[!THEOREM]- Theorem: Differentiation of Real Analytic Functions
>
>Every [[Real Analytic Functions|real analytic function]] $f(x) = \displaystyle \sum_{n=0}^\infty c_n (x-a)^n$ is [[Differentiability|differentiable]] on $D$ and its derivative $f'(x)$ is also a real analytic function given by
>
>$$
>f'(x) = \sum_{n=1}^\infty n c_n (x-a)^{n-1}
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM]- Theorem: Antiderivatives of Real Analytic Functions
>
>The [[Antiderivatives]] of any [[Real Analytic Functions|real analytic function]] $f(x) = \displaystyle \sum_{n = 0}^\infty c_n (x-a)^n$ are also real analytic functions and $f$'s [[Antiderivatives|indefinite integral]] is given by
>
>$$
>\int f(x) \mathop{\mathrm{d}x} = C + \sum_{n = 0}^\infty c_n \frac{(x - a)^{n+1}}{n+1}
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>