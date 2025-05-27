---
title: Vector Line Integrals
tags:
    - vector-analysis
    - real-analysis
    - analysis
    - mathematics
---

# Vector Line Integrals over Parametric Curves

>[!DEFINITION] Definition: Vector Line Integral
>
>Let $\mathbf{F}: \mathcal{D} \subseteq \mathbb{R}^n \to \mathbb{R}^n$ be a [[Real Vector Field]] and let $\gamma: [a;b] \to \mathbb{R}^n$ be a [[Differentiability of Parametric Curves|differentiable]] [[Parametric Curve]] whose [[Functions|image]] $\gamma([a;b])$ is a [[Sets|subset]] of $\mathcal{D}$.
>
>The **(vector) line integral** of $\mathbf{F}$ over $\gamma$ is the [[Definite Integrals|definite integral]] 
>
>$$
>\int_a^b \mathbf{F}(\gamma(t)) \cdot \gamma'(t) \mathop{\mathrm{d}t},
>$$
>
>where $\cdot$ denotes the [[Real Dot Product|dot product]].
>
>>[!NOTATION]-
>>
>>$$
>>\int_{\gamma} \mathbf{F} \cdot \mathop{\mathrm{d}\mathbf{s}} \qquad \int_{\gamma} \mathbf{F}
>>$$
>>
>>If the [[Functions|image]] of $\gamma$ is a [[Curves#Closed Curves|closed curve]], then we write
>>
>>$$
>>\oint_{\gamma} \mathbf{F} \cdot \mathop{\mathrm{d}\mathbf{s}} \qquad \oint_{\gamma} \mathbf{F}
>>$$
>>
>

## Properties

>[!THEOREM]- Theorem: Vector Line Integral to Scalar Line Integral
>
>Let $\mathbf{F}: \mathcal{D} \subseteq \mathbb{R}^n \to \mathbb{R}^n$ be a [[Real Vector Field]] and let $\gamma: [a;b] \to \mathbb{R}^n$ be a [[Differentiability of Parametric Curves|differentiable]] [[Parametric Curve]] whose [[Functions|image]] $\gamma([a;b])$ is a [[Sets|subset]] of $\mathcal{D}$.
>
>The [[Vector Line Integrals|line integral]] of $\mathbf{F}$ over $\gamma$ is equal to the [[Scalar Line Integrals|line ntegral]] of the [[Real Dot Product|dot product]] of $\mathbf{F}$ with the [[Parametrization|unit tangent vector]] of $\gamma$:
>
>$$
>\int_{\gamma} \mathbf{F} \cdot \mathop{\mathrm{d}\mathbf{s}} = \int_{\gamma} \mathbf{F} \cdot \mathbf{T} \mathop{\mathrm{d}s}
>$$
>
>>[!PROOF]-
>>
>>$$
>>\begin{align*}
>>
>>\int_{\gamma}\mathbf{F}\cdot \mathop{\mathrm{d}\mathbf{s}} & =\int_a^b \mathbf{F}({\gamma}(t)) \cdot{\gamma}^{\prime}(t)dt \\
>>\int_{\gamma}\mathbf{F}\cdot \mathop{\mathrm{d}\mathbf{s}} & =\int_a^b\mathbf{F}({\gamma}(t))\cdot\frac{{\gamma}^{\prime}(t)}{\left\|{\gamma}^{\prime}(t)\right\|}\left\|{\gamma}^{\prime}(t)\right\|dt \\
>>& =\int_a^b\left(\mathbf{F}({\gamma}(t))\cdot\mathbf{T}(t)\right)\left\|{\gamma}^{\prime}(t)\right\| \mathop{\mathrm{d}t} \\
>>& =\int_{\gamma}(\mathbf{F}\cdot\mathbf{T}) \mathop{\mathrm{d}s}
>>
>>\end{align*}
>>$$
>>
>

>[!THEOREM]- Theorem: Linearity of the Vector Line Integral
>
>The [[Vector Line Integrals|vector line integral]] is [[Linear Transformation|linear]]:
>
>$$
>\int_{\gamma} (\lambda\, \boldsymbol{v} +\mu \, \boldsymbol{w})\cdot\mathop{\mathrm{d}\boldsymbol{s}} = \lambda\int_{\gamma} \boldsymbol{v}\cdot\mathop{\mathrm{d}\boldsymbol{s}} + \mu \int_{\gamma} \boldsymbol{w}\cdot \mathop{\mathrm{d}\boldsymbol{s}}
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

# Vector Line Integrals over Geometric Curves

>[!THEOREM] Theorem: Line Integrals over Equivalent Parametrizations
>
>Let $\mathcal{C}$ be a [[Curves#Simple Curves|simple curve]] in $\mathbb{R}^n$, let $\gamma: [a;b] \to \mathbb{R}^n$ and $\varphi: [c;d] \to \mathbb{R}^n$ be [[Curves#Parametrizations|parametrizations]] of $\mathcal{C}$ and let $\mathbf{F}: \mathcal{D} \subseteq \mathbb{R}^n \to \mathbb{R}^n$ be a [[Real Vector Field]].
>
>If $\gamma$ and $\varphi$ are [[Differentiability of Parametric Curves|continuously differentiable]] on $(a;b)$ and $(c;d)$, respectively, and are [[Curves#Equivalence of Parametrizations|equivalent]] up to a [[Differentiability|continuously differentiable]] [[Curves|reparametrization]], then the [[Vector Line Integrals|line integrals]] of $\mathbf{F}$ along $\gamma$ and $\varphi$
>
>-  are equal whenever $\gamma$ and $\varphi$ have the [[Curves#Orientation of Equivalent Parametrizations|same orientation]]
>
>$$
>\int_{\gamma} \mathbf{F} \cdot \mathop{\mathrm{d}\mathbf{s}} = \int_{\varphi} \mathbf{F} \cdot \mathop{\mathrm{d}\mathbf{s}}
>$$
>
>- are equal in magnitude but opposite in sign whenever $\gamma$ and $\varphi$ have [[Curves#Orientation of Equivalent Parametrizations|opposite orientations]]
>
>$$
>\int_{\gamma} \mathbf{F} \cdot \mathop{\mathrm{d}\mathbf{s}} = -\int_{\varphi} \mathbf{F} \cdot \mathop{\mathrm{d}\mathbf{s}}
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

The aforementioned theorem guarantees that the [[Vector Line Integrals|line integrals]] of a [[Real Vector Field|vector field]] $\mathbf{F}$ over [[Differentiability of Parametric Curves|continuously differentiable]] [[Curves#Parametrizations|parametrizations]] of the same [[Curves|curve]] $\mathcal{C}$ which are [[Curves#Equivalence of Parametrizations|equivalent]] up to a [[Differentiability|continuously differentiable]] [[Curves|reparametrization]] are either equal or equal in magnitude but opposite in sign. However, while some [[Curves#Parametrizations|parametrizations]] may be [[Curves#Equivalence of Parametrizations|equivalent]] amongst each other and some other [[Curves#Parametrizations|parametrizations]] may also be [[Curves#Equivalence of Parametrizations|equivalent]] amongst each other, this does not ensure that these groups of [[Curves#Parametrizations|parametrizations]] are *all* [[Curves#Equivalence of Parametrizations|equivalent]]. If we want to define the notion of a line integral over a curve geometrically, we need to determine which equivalence class to consider. A very natural choice is based on the [[Curves#Equivalence of Parametrizations|equivalence of regular injective parametrizations]]. Since these [[Curves#Parametrizatoins|parametrizations]] are [[Injections, Surjections and Bijections|injective]], the absolute value of the [[Vector Line Integrals|line integrals]] of $\mathbf{F}$ over them depend only on the [[Curves|length]] of $\mathcal{C}$ and are thus equal. However, each of these [[Curves#Parametrizations|parametrizations]] still has one of two possible [[Curves#Orientation of Equivalent Parametrizations|orientations]]. This leaves us with two options for defining the line integral of $\mathbf{F}$ over $\mathcal{C}$, none of which is objectively better. 

>[!DEFINITION] Definition: Vector Line Integrals over Curves
>
>Let $\mathbf{F}: \mathcal{D} \subseteq \mathbb{R}^n \to \mathbb{R}^n$ be a [[Real Vector Field]] and let $\mathcal{C} \subseteq \mathcal{D}$ be a [[Curves#Simple Curves|simple curve]] in $\mathbb{R}^n$.
>
>The **line integral** of $\mathbf{F}$ over $\mathcal{C}$ is defined as a [[Vector Line Integrals|line integral]] of $\mathbf{F}$ over any [[Injections, Surjections and Bijections|injective]] [[Curves#Parametrizations|parametrization]] $\gamma: [a;b] \subset \mathbb{R} \to \mathbb{R}^n$ of $\mathcal{C}$ which is [[Differentiability of Parametric Curves|continuously differentiable]] on $(a;b)$ with a non-vanishing [[Differentiability of Parametric Curves|derivative]]:
>
>$$
>\int_{\gamma} \mathbf{F} \cdot \mathop{\mathrm{d}\mathbf{s}}
>$$
>
>>[!NOTATION]
>>
>>$$
>>\int_{\mathcal{C}} \mathbf{F} \cdot \mathop{\mathrm{d}\mathbf{s}}
>>$$
>>
>
>>[!WARNING] Warning: Ambiguity of the Line Integral
>>
>>As explained above, the line integral is *not* uniquely defined. There are two possible values for it depending on the [[Curves#Orientation of Equivalent Parametrizations|orientation]] of $\gamma$ - one positive and one negative. One should always beware which value is relevant to the context.
>>
>