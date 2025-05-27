---
title: The Real Cosine Function
tags:
  - real-analysis
  - analysis
  - mathematics
---

# The Real Cosine Function

>[!THEOREM] Theorem: Convergence of the Cosine Power Series
>
>The [[index|real power series]] $\displaystyle \sum_{n=0}^\infty (-1)^n \frac{x^{2n}}{(2n)!}$ is [[Convergence|convergent]] for all $x \in \mathbb{R}$.
>
>>[!PROOF]-
>>
>>TODO
>>
>
>>[!DEFINITION] Definition: Real Cosine Function
>>
>>The **real cosine function** is the [[Real Analytic Functions|real analytic function]] $\cos: \mathbb{R} \to \mathbb{R}$ defined by the [[index|real power series]] $\displaystyle \sum_{n=0}^\infty (-1)^n \frac{x^{2n}}{(2n)!}$.
>>
>>$$
>>\cos(x) = 1 - \frac{x^2}{2!}+\frac{x^4}{4!}-\frac{x^6}{6!}+\cdots
>>$$
>>
>>>[!NOTATION]-
>>>
>>>$$
>>>\cos x \qquad \cos (x)
>>>$$
>>>
>>
>

## Properties

>[!THEOREM]- Theorem: Parity of the Real Cosine Function
>
>The [[Real Cosine Function]] is [[Parity#^even-function]]:
>
>$$
>\cos(-x) = \cos(x)
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM]- Theorem: Image of the Real Cosine Function
>
>The [[Functions|image]] of the [[Real Cosine Function]] is $[-1;1]$.
>
>$$
>\cos(\mathbb{R}) = [-1;1]
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM]- Theorem: Periodicity of the Real Cosine Function
>
>The [[Real Cosine Function]] has a [[Periodicity|period]] of $2\pi$. More generally,
>
>$$
>\cos (x + 2k\pi) = \cos(x) \qquad \forall k\in\mathbb{Z}$$
>
>>[!PROOF]-
>>
>>TODO
>>
>


>[!THEOREM]- Theorem: Antiperiodicity of the Real Cosine Function
>
>The [[Real Cosine Function]] has an [[Periodicity|antiperiod]] of $\pi$. More generally,
>
>$$
>\cos (x + (2k+1) \pi) = -\cos(x) \qquad k \in \mathbb{Z}
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>


>[!THEOREM]- Theorem: Continuity of the Real Cosine Function
>
>The [[Real Cosine Function]] is [[Continuity|continuous]] on $\mathbb{R}$.
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM]- Theorem: Derivative of the Real Cosine Function
>
>The [[Real Cosine Function]] is [[Differentiability|differentiable]] everywhere and its [[Differentiability|derivative]] is the negative [[Real Sine Function]].
>
>$$
>(\cos x)' = -\sin x
>$$
>
>>[!PROOF]-
>>
>>$$
>>(\cos x)' = \sin\left(\frac{\pi}{2} - x\right)' = \left(\frac{\pi}{2} - x\right)'\cos\left(\frac{\pi}{2} - x\right) = -\cos\left(\frac{\pi}{2} - x\right) = -\sin x
>>$$
>>
>