---
title: Real Tangent Function
tags:
  - real-analysis
  - analysis
  - mathematics
---

# The Real Tangent Function

>[!DEFINITION] Definition: Real Tangent Function
>
>The **real tangent function** is defined as the ratio of the [[Real Sine Function]] to the [[Real Cosine Function]].
>
>$$
>\tan(x) \overset{\text{def}}{=} \frac{\sin(x)}{\cos(x)}
>$$
>
>>[!NOTE]
>>
>>The [[Functions|domain]] of the [[Real Tangent Function]] is $\{x \in \mathbb{R}\mid x\ne \frac{\pi}{2}+k\pi, k \in \mathbb{Z}\}$ because $\cos (\frac{\pi}{2}+k\pi) = 0$ for all $k \in \mathbb{Z}$.
>>
>
>>[!NOTATION]
>>
>>$$\tan (x) \qquad \mathop{\operatorname{tg}}(x)$$
>>
>

## Properties

>[!THEOREM]- Theorem: Image of the Real Tangent Function
>
>The [[Functions|image]] of the [[Real Tangent Function]] is $(-\infty;+\infty)$.
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM]- Theorem: Periodicity of the Real Tangent Function
>
>The [[Real Tangent Function]] has a [[Periodicity|period]] of $\pi$. More generally,
>
>$$
>\tan(x + k\pi) = \tan (x) \qquad \forall k \in \mathbb{Z}
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM]- Theorem: Continuity of the Real Tangent Function
>
>The [[Real Tangent Function]] is [[Continuity|continuous]] (everywhere it is defined).
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM]- Theorem: Derivative of the Real Tangent Function
>
>The [[Real Tangent Function]] is [[Differentiability|differentiable]] (everywhere it is defined) and its [[Differentiability|derivative]] is the recirpocal of the square of the [[Real Cosine Function]]:
>
>$$
>(\tan x)' = \frac{1}{\cos^2 x} = 1 + \tan^2 x
>$$
>
>>[!PROOF]-
>>
>>$$
>>(\tan x)' = \left(\frac{\sin x}{\cos x}\right)' = \frac{(\sin x)'\cos x - (\cos x)'\sin x}{\cos^2 x} = \frac{\cos^2 x + \sin^2 x}{\cos^2 x} = \frac{1}{\cos^2 x}
>>$$
>>
>