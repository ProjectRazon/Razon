---
title: The Real Sine Function
tags:
  - real-analysis
  - analysis
  - mathematics
---

# The Real Sine Function

>[!THEOREM] Theorem: Convergence of the Sine Power Series
>
>The [[index|real power series]] $\displaystyle \sum_{n=0}^\infty (-1)^n\frac{x^{2n+1}}{(2n+1)!}$ is [[Convergence|convergent]] for all $x \in \mathbb{R}$.
>
>>[!PROOF]-
>>
>>TODO
>>
>
>>[!DEFINITION] Definition: Real Sine Function
>>
>>The **real sine function** is the [[Real Analytic Functions|real analytic function]] $\sin: \mathbb{R} \to \mathbb{R}$ defined by the [[index|real power series]] $\displaystyle \sum_{n=0}^\infty (-1)^n\frac{x^{2n+1}}{(2n+1)!}$.
>>
>>$$
>>\sin(x) = x - \frac{x^3}{3!}+\frac{x^5}{5!}-\frac{x^7}{7!}+\cdots
>>$$
>>
>>>[!NOTATION]-
>>>
>>>$$
>>>\sin x \qquad \sin (x)
>>>$$
>>>
>>
>

## Properties

>[!THEOREM]- Theorem: Parity of the Real Sine Function
>
>The [[Real Sine Function]] is [[Parity#^odd-function]]:
>
>$$
>\sin(-x) = - \sin(x)
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM]- Theorem: Image of the Real Sine Function
>
>The [[Functions|image]] of the [[Real Sine Function]] is $[-1;1]$.
>
>$$
>\sin(\mathbb{R}) = [-1;1]
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM]- Theorem: Periodicity of the Real Sine Function
>
>The [[Real Sine Function]] has a [[Periodicity|period]] of $2\pi$. More generally,
>
>$$
>\sin (x + 2k\pi) = \sin(x) \qquad \forall k\in\mathbb{Z}
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM]- Theorem: Antiperiodicity of the Real Sine Function
>
>The [[Real Sine Function]] has an [[Periodicity|antiperiod]] of $\pi$. More generally,
>
>$$
>\sin (x + (2k+1) \pi) = -\sin(x) \qquad k \in \mathbb{Z}
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Continuity of the Real Sine Function
>
>The [[Real Sine Function]] is [[Continuity|continuous]] on $\mathbb{R}$.
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM]- Theorem: Derivative of the Real Sine Function
>
>The [[Differentiability|derivative]] of the [[Real Sine Function]] is the [[Real Cosine Function]].
>
>$$
>(\sin x)' = \cos x
>$$
>
>>[!PROOF]-
>>
>>$$
>>\begin{align*}(\sin x)'  &= \lim_{\Delta x\to 0} \frac{\sin (x + \Delta x) - \sin x}{\Delta x} = \lim_{\Delta x\to 0} \frac{2\sin\frac{\Delta x}{2}\cos\frac{2x + \Delta x}{2}}{\Delta x} \\ &= \lim_{\Delta x \to 0}\frac{\sin\frac{\Delta x}{2}}{\frac{\Delta x}{2}}\lim_{\Delta x \to 0} \cos\left(x + \frac{\Delta x}{2}\right) = 1 \cdot \cos x = \cos x\end{align*}
>>$$
>>
>