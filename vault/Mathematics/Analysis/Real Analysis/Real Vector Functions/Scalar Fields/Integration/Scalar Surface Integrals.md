---
title: Scalar Surface Integrals
tags:
    - vector-analysis
    - real-analysis
    - analysis
    - mathematics
---

# Scalar Surface Integrals over Surface Parametrizations



>[!DEFINITION] Definition: Scalar Surface Integral
>
>Let $f: \mathcal{D}_f \subseteq \mathbb{R}^3 \to \mathbb{R}$ be a [[Real Scalar Field]] and let $S: \mathcal{D}_S \subseteq \mathbb{R}^2 \to \mathbb{R}^3$ be a [[Differentiability of Real Vector Functions|differentiable]] [[Parametric Surface]] whose [[Functions|image]] $S(\mathcal{D}_S)$ is a [[Sets|subset]] of $\mathcal{D}_f$.
>
>The **(scalar) line integral** of $f$ over $S$ is the [[Double Integrals|double integral]]
>
>$$
>\iint_{\mathcal{D}_S} f(S(x,y)) \, ||\mathbf{N}(x,y)|| \mathop{\mathrm{d}\mathcal{D}_S},
>$$
>
>where $\mathbf{N}$ is the [[Surface Normal Vector|normal vector]] of $S$.
>
>>[!NOTATION]-
>>
>>$$
>>\iint_S f \qquad \iint_S f \mathop{\mathrm{d}S}
>>$$
>>
>>If $S(\mathcal{D}_S)$ is a [[Closed Surfaces|closed surface]], then a circle can be put through the two integral signs.
>>
>

>[!THEOREM] Theorem: Surface Integrals of Scalar Fields
>
>Let $f: \mathcal{D} \subseteq \mathbb{R}^3 \to \mathbb{R}$ be a [[Real Scalar Field]] and let $\phi: \mathcal{D}_{\phi} \subseteq \mathbb{R}^2 \to \mathbb{R}^3$ and $\psi: \mathcal{D}_{\psi} \subseteq \mathbb{R}^2 \to \mathbb{R}^3$ be [[Differentiability of Real Vector Functions|differentiable]] [[Parametric Surface|parametric surfaces]] whose [[Functions|images]] are [[Sets|subsets]] of $\mathcal{D}$.
>
>If $\phi$ and $\psi$ are [[Equivalence of Parametric Surfaces|smooth reparameterisations]] and $f$ is [[Continuity of Real Scalar Fields|continuous]], then the [[Scalar Surface Integrals|surface integrals]] of $f$ over $\phi$ and $\psi$ are equal.
>
>$$
>\iint_{\phi} f = \iint_{\psi} f
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>