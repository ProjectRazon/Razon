---
title: Definite Integrals of Vector Fields
tags:
    - vector-analysis
    - real-analysis
    - analysis
    - mathematics
---

# Integrals over Curves

>[!DEFINITION] Definition: Integrals over Parametric Curves
>
>Let $\mathbf{F}: \mathcal{D} \subseteq \mathbb{R}^n \to \mathbb{R}^n$ be a [[Real Vector Field]] with [[Functions of the Real Numbers|component functions]] $f_1, \dotsc, f_n$ and let $\gamma: [a;b] \subseteq \mathbb{R} \to \mathbb{R}^n$ be a [[Parametric Curve]] with such that $\gamma([a;b]) \subseteq \mathcal{D}$.
>
>The **integral** of $\mathbf{F}$ over $\gamma$ is defined as the [[Real Vector|vector]] whose components are the [[Scalar Line Integrals|line integrals]] of $f_1, \dotsc, f_n$ over $\gamma$:
>
>$$
>\int_{\gamma} \mathbf{F} \overset{\text{def}}{=} \begin{bmatrix} \int_{\gamma} f_1 \\ \vdots \\ \int_{\gamma} f_n \end{bmatrix}
>$$
>

It is also possible to define an integral of a [[Real Vector Field]] over a [[Curves|curve]] which depends only on its geometry and on the way it is traversed by a particular [[Curves#Parametrizations|parametrization]] using the following theorem.

>[!THEOREM] Theorem: Integrals over Equivalent Parametrizations
>
>Let $\mathbf{F}: \mathcal{D} \subseteq \mathbb{R}^n \to \mathbb{R}^n$ be a [[Real Vector Field]], let $\mathcal{C} \subseteq \mathcal{D}$ be a [[Curves|curve]] in $\mathbb{R}^n$ and let $\gamma: [a;b] \subseteq \mathbb{R} \to \mathbb{R}^n$ and $\varphi: [c;d] \subseteq \mathbb{R} \to \mathbb{R}^n$ be [[Curves#Parametrizations|parametrizations]] of $\mathcal{C}$.
>
>If $\gamma$ and $\varphi$ are [[Differentiability of Parametric Curves|continuously differentiable]] on $(a;b)$ and $(c;d)$, respectively, and are [[Curves#Equivalence of Parametrizations|equivalent]] up to a [[Differentiability|continuously differentiable]] [[Curves|reparametrization]], then the [[Definite Integrals#Integrals over Curves|integrals]] of $\mathbf{F}$ over $\gamma$ and $\varphi$ are equal:
>
>$$
>\int_{\gamma} \mathbf{F} = \int_{\varphi} \mathbf{F}
>$$
>
>>[!PROOF]-
>>
>>This is guaranteed by applying the corresponding theorem for [[Scalar Line Integrals#Scalar Line Integrals over Geometric Curves|scalar line integrals]] for each of the component functions.
>>
>

The aforementioned theorem guarantees that the [[Definite Integrals#Integrals over Curves|integrals]] of a [[Real Vector Field|vector field]] $\mathbf{F}$ over [[Differentiability of Parametric Curves|continuously differentiable]] [[Curves#Parametrizations|parametrizations]] of the same [[Curves|curve]] $\mathcal{C}$ which are [[Curves#Equivalence of Parametrizations|equivalent]] up to a [[Differentiability|continuously differentiable]] [[Curves|reparametrization]] are equal. However, while some [[Curves#Parametrizations|parametrizations]] may be [[Curves#Equivalence of Parametrizations|equivalent]] amongst each other and some other [[Curves#Parametrizations|parametrizations]] may also be [[Curves#Equivalence of Parametrizations|equivalent]] amongst each other, this does not ensure that these groups of [[Curves#Parametrizations|parametrizations]] are *all* [[Curves#Equivalence of Parametrizations|equivalent]]. If we want to define the notion of an integral over a curve geometrically, we need to determine which equivalence class to consider. A very natural choice is based on the [[Curves#Equivalence of Parametrizations|equivalence of regular injective parametrizations]]. According to the above theorem, the [[Definite Integrals#Integrals over Curves|integrals]] of $\mathbf{F}$ over these [[Curves#Parametrizatoins|parametrizations]] are all equal and, since they are also [[Injections, Surjections and Bijections|injective]], this value depends only on the [[Curves#Length|length]] of $\mathcal{C}$. 

>[!DEFINITION] Definition: Vector Field Integrals over Curves
>
>The **integral** of a [[Real Vector Field]] $\mathbf{F}$ over a [[Curves|curve]] $\mathcal{C}$ is defined as the [[Definite Integrals#Integrals over Curves|integral]] of $\mathbf{F}$ over any [[Differentiability of Parametric Curves|continuously differentiable]] [[Curves#Parametrizations|parametrization]] $\gamma$ of $\mathcal{C}$ with a non-vanishing [[Differentiability of Parametric Curves|derivative]]
>
>$$
>\int_{\gamma} \mathbf{F}
>$$
>
>>[!NOTATION]
>>
>>$$
>>\int_{\mathcal{C}} \mathbf{F}
>>$$
>>
>

>[!WARNING] Warning: Integrals over Curves vs Vector Line Integrals
>
>[[Definite Integrals#Integrals over Curves|Integrals over curves]] should not be confused with [[Vector Line Integrals]]. At the very least, the former yields a vector, while the latter yields a number. So, remember that the distinction between "integral over a curve" and "line integral" is crucial.
>

# Integrals over Surfaces

TODO

# Integrals over Volumes

TODO

# Higher-Dimensional Integrals

TODO

# Bibliography