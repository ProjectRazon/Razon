---
title: The Real Cotangent Function
tags:
  - real-analysis
  - analysis
  - mathematics
---

# The Real Cotangent Function

>[!DEFINITION] Definition: Real Cotangent Function
>
>The **real cotangent function** is defined as the ratio of the [[Real Cosine Function]] to the [[Real Sine Function]].
>
>$$
>\cot(x) \overset{\text{def}}{=} \frac{\cos(x)}{\sin(x)}
>$$
>
>>[!NOTE]
>>
>>The [[Functions|domain]] of the [[Real Cotangent Function]] is $\{x \in \mathbb{R}\mid x\ne k\pi, k \in \mathbb{Z}\}$ because $\sin (k\pi) = 0$ for all $k \in \mathbb{Z}$.
>>
>
>>[!NOTATION]-
>>
>>$$
>>\cot (x) \qquad \mathop{\operatorname{ctg}}(x) \qquad \mathop{\operatorname{cotg}}(x)
>>$$
>>
>

## Properties

>[!THEOREM]- Theorem: Image of the Real Cotangent Function
>
>The [[Functions|image]] of the [[Real Cotangent Function]] is $(-\infty; +\infty)$.
>
>>[!PROOF]-
>>
>>TODO
>>
>


>[!THEOREM]- Theorem: Periodicity of the Real Cotangent Function
>
>The [[Real Cotangent Function]] has a [[Periodicity|period]] of $\pi$. More generally,
>
>$$
>\cot(x + k\pi) = \cot (x) \qquad \forall k \in \mathbb{Z}
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM]- Theorem: Continuity of the Real Cotangent Function
>
>The [[Real Cotangent Function]] is [[Continuity|continuous]] (everywhere it is defined).
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM]- Theorem: Derivative of the Real Cotangent Function
>
>The [[Real Cotangent Function]] is [[Differentiability|differentiable]] (everywhere it is defined) and its [[Differentiability|derivative]] is the negative reciprocal of the square of the [[Real Sine Function]]:
>
>$$
>(\cot x)' = - \frac{1}{\sin^2 x} = -1 - \cot^2 x
>$$
>
>>[!PROOF]-
>>
>>$$
>>(\cot x)' = \left(\frac{\cos x}{\sin x}\right)^\prime = \frac{(\cos x)^\prime \sin x - (\sin x)^\prime \cos x}{\sin^2 x} = \frac{-\sin^2 x -\cos^2 x}{\sin^2 x} = \frac{-(\sin^2 x + \cos^2 x)}{\sin^2 x} = \frac{-1}{\sin^2 x}
>>$$
>>
>