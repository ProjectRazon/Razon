---
title: Line Integrals of Scalar Fields
---

# Scalar Line Integrals over Parametric Curves

>[!DEFINITION] Definition: Line Integral of a Scalar Field
>
>Let $f: \mathcal{D} \subseteq \mathbb{R}^n \to \mathbb{R}$ be a [[Real Scalar Field]] and let $\gamma: [a;b] \to \mathbb{R}^n$ be a [[Parametric Curve]] which is [[Differentiability of Parametric Curves|continuously differentiable]] on $(a;b)$ and whose [[Functions|image]] $\gamma([a;b])$ is a [[Sets|subset]] of $\mathcal{D}$.
>
>The **line integral** of $f$ along $\gamma$ is the [[Definite Integrals|integral]]
>
>$$
>\int_a^b f(\gamma(t))\, ||\dot{\gamma}(t)|| \mathop{\mathrm{d}t}
>$$
>
>>[!NOTATION]
>>
>>$$
>>\int_{\gamma} f \qquad \int_{\gamma} f \mathop{\mathrm{d}s}
>>$$
>>
>>If the [[Functions|image]] of $\gamma$ is a [[Curves|closed curve]], we write
>>
>>$$
>>\oint_{\gamma} f \qquad \oint_{\gamma} f \mathop{\mathrm{d}s}
>>$$
>>
>

## Properties

>[!THEOREM]- Theorem: Linearity of the Scalar Line Integral
>
>The [[Scalar Line Integrals|scalar line integral]] is [[Linear Transformation|linear]]:
>
>$$
>\int_{\gamma} (\lambda\, f +\mu \, g)\mathop{\mathrm{d}s} = \lambda\int_{\gamma} f\mathop{\mathrm{d}s} + \mu \int_{\gamma} g\mathop{\mathrm{d}s}
>$$
>
>>[!PROOF]-
>>
>>$$
>>\begin{align*}\int_\gamma (\lambda\, f +\mu \, g)\mathop{\mathrm{d}s} &=\int_a^b [\lambda\, f(\gamma(t)) +\mu \, g(\gamma(t))]\,||\dot{\gamma}(t)||\mathop{\mathrm{d}t} \\ &=\int_a^b \lambda\, f(\gamma(t))\,||\dot{\gamma}(t)|| +\mu \, g(\gamma(t))\,||\dot{\gamma}(t)||\mathop{\mathrm{d}t} \\ &= \lambda \int_a^b f(\gamma(t)) \, ||\dot{\gamma}(t)|| \mathop{\mathrm{d}t} + \mu \int_a^b g(\gamma(t))\,||\dot{\gamma}(t)||\mathop{\mathrm{d}t} \\ &= \lambda\int_\gamma f\mathop{\mathrm{d}s} + \mu \int_\gamma g\mathop{\mathrm{d}s} \end{align*}
>>$$
>>
>

>[!THEOREM]- Mean value theorem for Scalar Line Integrals
>
>Let $f: \mathcal{D} \subseteq \mathbb{R}^n \to \mathbb{R}$ be a [[Real Scalar Field]] and let $\gamma: [a;b] \to \mathbb{R}^n$ be a [[Differentiability of Parametric Curves|continuously differentiable]] [[Parametric Curve]] whose [[Functions|image]] $\gamma([a;b])$ is a [[Sets|subset]] of $\mathcal{D}$.
>
>If $f$ is [[Continuity of Real Scalar Fields|continuous]], then there exists some $\mathbf{p} \in \gamma([a;b])$ such that the [[Scalar Line Integrals|line integral]] of $f$ along $\gamma$ is
>
>$$
>\int_{\gamma} f = f(\mathbf{p})\cdot L,
>$$
>
>where $L$ is the [[Length]] of $\gamma$.
>
>>[!PROOF]-
>>
>>TODO
>>
>

# Scalar Line Integrals over Geometric Curves

The following theorem makes it possible to provide an unambiguous definition of the line integral of a scalar field over a [[Curves|curve]] in $\mathbb{R}^n$.

>[!THEOREM] Theorem: Line Integrals over Equivalent Parametrizations
>
>Let $\mathcal{C}$ be a [[Curves#Simple Curves|simple curve]] in $\mathbb{R}^n$, let $\gamma: [a;b] \to \mathbb{R}^n$ and $\varphi: [c;d] \to \mathbb{R}^n$ be [[Curves#Parametrizations|parametrizations]] of $\mathcal{C}$ and let $f: \mathcal{D} \subseteq \mathbb{R}^n \to \mathbb{R}$ be a [[Real Scalar Field]].
>
>If $\gamma$ and $\varphi$ are [[Differentiability of Parametric Curves|continuously differentiable]] on $(a;b)$ and $(c;d)$, respectively, and are [[Curves#Equivalence of Parametrizations|equivalent]] up to a [[Differentiability|continuously differentiable]] [[Curves|reparametrization]], then the [[Scalar Line Integrals|line integrals]] of $f$ along $\gamma$ and $\varphi$ are equal.
>
>$$
>\int_{\gamma} f = \int_{\varphi} f
>$$
>
>>[!PROOF]-
>>
>>We will just show this for the case when $\gamma$ and $\varphi$ are *not* piecewise, since the proof is easily generalizable - if $\gamma$ and $\varphi$ *are* piecewise, then one can just apply the following proof to each of their partitions and obtain the same end result after summing the results from each partition.
>>
>>Since $\gamma$ and $\varphi$ parameterise the same curve $\mathcal{C}$, we can [[Curves|reparameterise]] one in the other. More specifically, there exists a [[Injections, Surjections and Bijections|bijection]], [[Differentiability|continuously differentiable function]] $u: [a;b] \to [c;d]$ such that
>>
>>$$
>>\varphi(u(t)) = \gamma (t)
>>$$
>>
>>The [[Differentiation Rules for Curve Parameterisations#^chainrule]] then gives us
>>
>>$$
>>\int_a^b f(\gamma(t))\, ||\dot\gamma (t)||\mathop{\mathrm{d}t} = \int_a^b f(\varphi(u(t)))\, ||\dot\varphi (u(t)) u'(t)|| \mathop{\mathrm{d}t} =  \int_a^b f(\varphi(u(t)))\, ||\dot\varphi (u(t))|| \, |u'(t)|\mathop{\mathrm{d}t}
>>$$
>>
>>If $\gamma$ and $\varphi$ have the [[Curves#^orientation]], then $u(a) = c$ and $u(b) = d$. Since $a \lt b, c \lt d$ and $u$ is bijective, $u$ must be [[Monotony|strictly increasing]], i.e. $|u'(t)| = u'(t)$. We thus have
>>
>>$$
>>\int_a^b f(\varphi(u(t)))\, ||\dot\varphi (u(t))|| \, |u'(t)|\mathop{\mathrm{d}t} = \int_a^b f(\varphi(u(t))) \, ||\dot\varphi (u(t))|| \, u'(t)\mathop{\mathrm{d}t}
>>$$
>>
>>By applying the [[Differentiability|substitution]] $\mathrm{d}u = u' \mathop{\mathrm{d}t}$, we obtain 
>>
>>$$
>>\int_a^b f(\varphi(u(t)))\, ||\dot\varphi (u(t))|| \, u'(t)\mathop{\mathrm{d}t} = \int_c^d f(\varphi(u))\, ||\dot \varphi(u)|| \mathop{\mathrm{d}u}
>>$$
>>
>>$$
>>\int_a^b f(\gamma(t))\, ||\dot\gamma (t)||\mathop{\mathrm{d}t} = \int_c^d f(\varphi(u))\, ||\dot \varphi(u)|| \mathop{\mathrm{d}u}
>>$$
>>
>>We are done with the case where $\gamma$ and $\varphi$ have the same orientation. Now, if $\gamma$ and $\varphi$ have [[Curves#^orientation]], then $u(a) = d$ and $u(b) = c$. Since $a \lt b, c \lt d$ and $u$ is bijective, $u$ must be [[Monotony|strictly decreasing]], i.e. $|u'(t)| = -u'(t)$. We thus have
>>
>>$$
>>\int_a^b f(\varphi(u(t)))\, ||\dot\varphi (u(t))|| \, |u'(t)|\mathop{\mathrm{d}t} = - \int_a^b f(\varphi(u(t)))\, ||\dot\varphi (u(t))|| \, u'(t)\mathop{\mathrm{d}t}
>>$$
>>
>>By applying the substitution $\mathrm{d}u = u' \mathop{\mathrm{d}t}$, we obtain 
>>
>>$$
>>-\int_a^b f(\varphi(u(t)))\, ||\dot\varphi (u(t))|| \, u'(t)\mathop{\mathrm{d}t} = - \int_d^c f(\varphi(u))\, ||\dot \varphi(u)|| \mathop{\mathrm{d}u} = \int_c^d f(\varphi(u))\, ||\dot \varphi(u)|| \mathop{\mathrm{d}u}
>>$$
>>
>>$$
>>\int_a^b f(\gamma(t))\, ||\dot\gamma (t)||\mathop{\mathrm{d}t} = - \int_d^c f(\varphi(u))\, ||\dot \varphi(u)|| \mathop{\mathrm{d}u} = \int_c^d f(\varphi(u))\, ||\dot \varphi(u)|| \mathop{\mathrm{d}u}
>>$$
>>
>>And so the proof is complete.
>>
>

The aforementioned theorem guarantees that [[Scalar Line Integrals|line integrals]] of a [[Real Scalar Field]] over [[Differentiability of Parametric Curves|continuously differentiable]], [[Curves#Equivalence of Parametrizations|equivalent]] [[Curves#Parametrizatoins|parametrizations]] of the same [[Curves#Simple Curves|simple curve]] $\mathcal{C}$ are equal. However, while some [[Curves#Parametrizatoins|parametrizations]] may be [[Curves#Equivalence of Parametrizations|equivalent]] amongst each other and some other [[Curves#Parametrizatoins|parametrizations]] may also be [[Curves#Equivalence of Parametrizations|equivalent]] amongst each other, this does not ensure that the two groups of [[Curves#Parametrizatoins|parametrizations]] are *all* [[Curves#Equivalence of Parametrizations|equivalent]]. But then how do we know which group to choose? Well, a very natural choice is based on the [[Curves#Equivalence of Parametrizations|equivalence of regular injective parametrizations]]. Since these [[Curves#Parametrizatoins|parametrizations]] are [[Injections, Surjections and Bijections|injective]], [[Scalar Line Integrals]] over them depend only on the intrinsic [[Curves#Length|length]] of $\mathcal{C}$ and not on the way these [[Curves#Parametrizatoins|parametrizations]] trace out $\mathcal{C}$.

>[!DEFINITION] Definition: Scalar Line Integrals over Curves
>
>The **line integral** of a [[Real Scalar Field]] $f: \mathcal{D} \subseteq \mathbb{R}^n \to \mathbb{R}$ over a [[Curves#Curves|simple curve]] $\mathcal{C} \subseteq \mathcal{D}$ is defined as the [[Scalar Line Integrals|line integral]] of $f$ over any [[Injections, Surjections and Bijections|injective]] [[Curves#Parametrizations|parametrization]] $\gamma: [a;b] \subset \mathbb{R} \to \mathbb{R}^n$ of $\mathcal{C}$ which is [[Differentiability of Parametric Curves|continuously differentiable]] on $(a;b)$ with a non-vanishing [[Differentiability of Parametric Curves|derivative]]:
>
>$$
>\int_{\gamma} f
>$$
>
>>[!NOTATION]
>>
>>$$
>>\int_{\mathcal{C}} f \qquad \int_{\mathcal{C}} f \mathop{\mathrm{d}s}
>>$$
>
>>[!NOTE] Note: Generalization to Non-Simple Curves
>>
>>If $\mathcal{C}$ is not [[Curves#Simple Curves|simple]] but can be represented as the [[Operations with Collections|union]] $\mathcal{C} = \mathcal{C}_1 \cup \mathcal{C}_2 \cup \cdots \cup \mathcal{C}_{p-1} \cup \mathcal{C}_p$ of finitely many [[Curves#Simple Curves|simple curves]] $\mathcal{C}_1, \dotsc, \mathcal{C}_p$ such that $\mathcal{C}_{k}$ and $\mathcal{C}_{k+1}$ share exactly one point and this point is an [[Curves#Curves with Endpoints|endpoint]] for both $\mathcal{C}_{k}$ and $\mathcal{C}_{k+1}$, then we define the line integral of $\mathcal{f}$ over $\mathcal{C}$ as the sum of the [[Scalar Line Integrals#Scalar Line Integrals over Curves|line integrals]] of $f$ over $\mathcal{C}_1, \dotsc, \mathcal{C}_p$:
>>
>>$$
>>\int_{\mathcal{C}} f = \sum_{i = 1}^p \int_{\mathcal{C}_i} f
>>$$
>>
>>>[!NOTATION] Notation: Line Integrals over Closed Curves
>>>
>>>If $\mathcal{C}$ is [[Curves#Closed Curves|closed]], we denote the line integral of $f$ over $\mathcal{C}$ as one of the following:
>>>
>>>$$
>>>\oint_{\mathcal{C}} f \qquad \oint_{\mathcal{C}} f \mathop{\mathrm{d}s}
>>>$$
>>>
>>
>