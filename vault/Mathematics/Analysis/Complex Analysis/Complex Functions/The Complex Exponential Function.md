---
title: The Complex Exponential Function
tags:
    - exponentials
    - complex-functions
    - complex-analysis
    - analysis
    - mathematics
---

# The Complex Exponential

>[!THEOREM] Theorem: Complex Exponential
>
>The [[Complex Power Series]]
>
>$$
>\sum_{n = 0}^{\infty} \frac{z^n}{n!} = 1 + \frac{z^1}{1!} +  \frac{z^2}{2!} + \frac{z^3}{3!} + \frac{z^4}{4!} + \cdots
>$$
>
>[[Convergence|converges absolutely]] for all $z \in \mathbb{C}$.
>
>>[!PROOF]-
>>
>>TODO
>>
>
>>[!DEFINITION] Definition: Complex Exponential
>>
>>The [[Complex Functions|complex function]] $\exp: \mathbb{C} \to \mathbb{C}$ defined as
>>
>>$$
>>\exp (z) = \sum_{n = 0}^{\infty} \frac{z^n}{n!}
>>$$
>>
>>is known as the **complex exponential function**.
>>
>>>[!NOTATION]
>>>
>>>$$
>>>\exp z \qquad \exp(z) \qquad \mathrm{e}^z
>>>$$
>>>
>>
>>>[!NOTE]
>>>
>>>The [[Functions|restriction]] of the [[The Complex Exponential Function|complex exponential function]] to $\mathbb{R}$ is the [[The Real Exponential Function|real exponential function]].
>>>
>>
>

## Properties

>[!THEOREM] Theorem: Periodicity of the Complex Exponential
>
>The [[The Complex Exponential Function|complex exponential function]] is [[Periodicity|periodic]] with period $2\pi \mathrm{i}$:
>
>$$
>\exp(z + 2k\pi \mathrm{i}) = \exp (z) \qquad \forall z \in \mathbb{C}, \forall k \in \mathbb{Z}
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Euler's Formula
>
>For every $\varphi \in \mathbb{R}$, the real part of the [[The Complex Exponential Function|complex exponential]] $\mathrm{e}^{\mathrm{i}\varphi}$ is the [[Real Cosine Function|real cosine]] of $\varphi$ and the imaginary part is the [[Real Cosine Function|real sine]] of $\varphi$:
>
>$$
>\mathrm{e}^{\mathrm{i}\varphi} = \cos \varphi + \mathrm{i} \sin \varphi
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Exponent Arithmetic
>
>The [[The Complex Exponential Function|complex exponential]] of a sum is equal to the product of the complex exponentials of its terms:
>
>$$
>\mathrm{e}^{z + w} = \mathrm{e}^z \cdot \mathrm{e}^w \qquad \forall z,w \in \mathbb{C}
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Modulus of the Complex Exponential
>
>For all $z \in \mathbb{C}$, the [[index|modulus]] of the [[The Complex Exponential Function|complex exponential]] of $z$ is the [[The Real Exponential Function|real exponential]] of its real part:
>
>$$
>|\mathrm{e}^z| = \mathrm{e}^{\operatorname{Re}(z)}
>$$
>
>>[!PROOF]-
>>
>>Let $x = \operatorname{Re}(z)$ and $y = \operatorname{Im}(z)$.
>>
>>$$
>>\begin{align*}
>>
>>|\mathrm{e}^z| = \left| \mathrm{e}^{x + \mathrm{i} y} \right| &= \left| \mathrm{e}^{x} \cdot \mathrm{e}^{\mathrm{i} y} \right| \\ &= \left| \mathrm{e}^{x} \cdot \cos y + \mathrm{i} \sin y \right| \\ &= \left| \mathrm{e}^{x} \sqrt{\cos^2 y + \sin^2 y} \right| \\ &= \left|\mathrm{e}^{x} \cdot \sqrt{1}\right| \\ &= \left|\mathrm{e}^{\operatorname{Re}(z)}\right| = \mathrm{e}^{\operatorname{Re}(z)}
>>
>>\end{align*}
>>$$
>>
>