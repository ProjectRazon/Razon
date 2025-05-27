---
title: Parametrization
tags:
  - vector-analysis
  - real-analysis
  - analysis
  - euclidean-geometry
  - geometry
  - mathematics
---

# Parametrizations

>[!DEFINITION] Definition: Curve Parametrization
>
>A **parametrization** of a [[Curves#Curves|curve]] $\mathcal{C}$ in $\mathbb{R}^n$ is a [[Continuity of Real Vector Functions|continuous]] [[Functions of the Real Numbers|function]] $\gamma: I \subseteq \mathbb{R} \to \mathbb{R}^n$ on an [[The Topology of Euclidean Space|interval]] $I$ whose [[Functions|image]] is $\mathcal{C}$.
>
>$$
>\gamma(I) = \mathcal{C}
>$$
>
>>[!NOTE] Note: Parametric Curves
>>
>>Parametrizations are often called **parametric curves**.
>>
>

The same [[Curves#Curves|curve]] can have many different [[Curves#Parametrizations|parametrizations]].

>[!EXAMPLE]- Example: Different Parametrizations of the Same Curve
>
>TODO
>

More over, not all parametrizations are created equal. A single curve can have multiple parametrizations but some of them will be more useful than others because they have certain properties. 

## Tangent Vectors

[[Differentiability of Parametric Curves|Differentiable]] [[Parametrization#Parametrizations|parametrizations]] allows us to define the notion of "tangentiality" for [[Curves]].

>[!DEFINITION] Definition: Tangent Vector
>
>Let $\gamma: I \subseteq \mathbb{R} \to \mathbb{R}^n$ be a [[Parametrization|curve parametrization]] which is [[Differentiability of Parametric Curves|differentiable]] at $t \in I$.
>
>The **tangent vector** of $\gamma$ at $t$ is the [[Differentiability of Parametric Curves|derivative]] $\dot{\gamma}(t)$ of $\gamma$ there.
>
>>[!NOTE]
>>
>>The tangent vector is also known as $\gamma$'s **velocity** and its magnitude as $\gamma$'s **speed**.
>>
>
>>[!DEFINITION] Definition: Unit Tangent Vector
>>
>>The **unit tangent vector** is the [[Unit Vector]] obtained from the [[Parametrization#Tangent Vectors|tangent vector]]:
>>
>>$$
>>\frac{1}{||\dot{\gamma}(t)||}\dot{\gamma}(t)
>>$$
>>
>>>[!NOTATION]
>>>
>>>$$
>>>\mathbf{T}(t)
>>>$$
>>>
>>
>

It is apparent from the above definition that there is no unique [[Parametrization#Tangent Vectors|tangent vector]] which is intrinsic to a [[Curves|curve]]'s geometry. Instead, tangent vectors depend on the [[Parametrization#Parametrizations|parametrization]] in question. However, it turns out that the [[Parametrization#Tangent Vectors|tangent vectors]] of all [[Parametrization#Parametrizations|parametrizations]] at the same point, if they exist, are collinear.

>[!THEOREM] Theorem: Collinearity of Tangent Vectors
>
>Let $\mathcal{C}$ be a [[Curves|curve]] in $\mathbb{R}^n$ and let $\gamma: I_{\gamma} \subseteq \mathbb{R} \to \mathbb{R}^n$ and $\varphi: I_{\varphi} \subseteq \mathbb{R} \to \mathbb{R}^n$ be [[Parametrization#Parametrizations|parametrizations]] of $\mathcal{C}$. Let $\mathbf{p} \in \mathcal{C}$ and let $t \in I_{\gamma}$ and $s \in I_{\varphi}$ be such that $\gamma(t) = \mathbf{p}$ and $\varphi(s) = \mathbf{p}$.
>
>If $\gamma$ is [[Differentiability of Parametric Curves|differentiable]] at $t$ and $\varphi$ is [[Differentiability of Parametric Curves|differentiable]] at $s$, then there exists some $\lambda \in \mathbb{R}$ such that
>
>$$
>\dot{\gamma}(t) = \lambda \, \dot{\varphi}(s)
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

The above theorem tells us that all [[Parametrization#Tangent Vectors|tangent vectors]] at a point of a [[Curves|curve]] line on a [[Straight Line]]

>[!DEFINITION] Definition: Tangent Line
>
>The **tangent line** to a [[Curves|curve]] $\mathcal{C}$ at $\mathbf{p} \in \mathcal{C}$ is the [[Straight Line]]
>
>$$
>\{ \mathbf{p} + k \mathbf{t} \mid k \in \mathbb{R} \},
>$$
>
>where $\mathbf{t}$ is any non-zero [[Parametrization#Tangent Vectors|tangent vector]] of a [[Parametrization#Parametrizations|parametrization]] of $\mathcal{C}$ at $\mathbf{p}$.
>

## Normal Vectors

>[!DEFINITION] Definition: Normal Vector
>
>Let $\gamma: I \subseteq \mathbb{R} \to \mathbb{R}^n$ be a [[Parametrization|curve parametrization]] which is twice [[Differentiability of Parametric Curves|differentiable]] at $t \in I$.
>
>The **normal vector** of $\gamma$ at $t$ is the [[Differentiability of Parametric Curves|derivative]] of its [[Parametrization#Tangent Vectors|tangent vector]] there, i.e. $\gamma$'s second [[Differentiability of Parametric Curves|derivative]] $\ddot{\gamma}(t)$.
>
>>[!DEFINITION] Definition: Unit Normal Vector
>>
>>The **unit normal vector** is the [[Unit Vector]] obtained from $\gamma$'s [[Parametrization#Normal Vectors|normal vector]]:
>>
>>$$
>>\frac{1}{||\dot{\mathbf{T}}(t)||}\dot{\mathbf{T}}(t)
>>$$
>>
>>>[!NOTATION]
>>>
>>>$$
>>>\mathbf{N}(t)
>>>$$
>>>
>>
>

## Binormal Vectors

>[!DEFINITION] Definition: Binormal Vector
>
>Let $\gamma: I \subseteq \mathbb{R} \to \mathbb{R}^3$ be a [[Parametrization|curve parametrization]] which is twice [[Differentiability of Parametric Curves|differentiable]] at $t \in I$.
>
>
>The **binormal vector** of $\gamma$ at $t$ is the [[Real Cross Product|cross product]] of its [[Parametrization#Tangent Vectors|unit tangent vector]] and its [[Parametrization#Normal Vectors|unit normal vector]] at $t$:
>
>$$
>\mathbf{T}(t) \times \mathbf{N}(t)
>$$
>
>>[!NOTATION]
>>
>>$$
>>\mathbf{B}(t)
>>$$
>>
>

# Equivalence of Parametrizations

>[!DEFINITION] Definition: Reparametrization
>
>Let $\mathcal{C}$ be a [[Curves#Curves|curve]] in $\mathbb{R}^n$ and let $\gamma: I_{\gamma} \subseteq \mathbb{R} \to \mathbb{R}^n$ and $\varphi: I_{\varphi} \subseteq \mathbb{R} \to \mathbb{R}^n$ be [[Parametric Curve|parametrizations]] of $\mathcal{C}$.
>
>A **reparametrization** between $\gamma$ and $\varphi$ is a [[Injections, Surjections and Bijections|bijective]] [[Functions of the Real Numbers|function]] $h_{I_{\gamma} \to I_{\varphi}}: I_{\gamma} \to I_{\varphi}$ with [[Injections, Surjections and Bijections|inverse]] $h_{I_{\varphi} \to I_{\gamma}}: I_{\varphi} \to I_{\gamma}$ such that
>
>$$
>\begin{align*}
>\gamma(t) = \varphi(h_{I_{\gamma} \to I_{\varphi}}(t)) \qquad \forall t \in I_{\gamma} \\
>\varphi(t) = \gamma(h_{I_{\varphi} \to I_{\gamma}}(t)) \qquad \forall t \in I_{\varphi}
>\end{align*}
>$$
>
>>[!NOTE]
>>
>>This is the most general definition for reparametrization. However, it is quite common to require that both $h_{I_{\gamma} \to I_{\varphi}}$ and $h_{I_{\varphi} \to I_{\gamma}}$ have additional properties such as [[Continuity]], [[Differentiability|continuous differentiability]] or [[Differentiability|smoothness]]. In this case, when we say that a reparametrization has some property, we mean that both $h_{I_{\gamma} \to I_{\varphi}}$ and $h_{I_{\varphi} \to I_{\gamma}}$ have this property.
>>
>

>[!DEFINITION] Definition: Equivalence of Parametrizations
>
>Let $\mathcal{C}$ be a [[Curves#Curves|curve]] in $\mathbb{R}^n$.
>
>Two [[Parametric Curve|parametrizations]] $\gamma: I_{\gamma} \subseteq \mathbb{R} \to \mathbb{R}^n$ and $\varphi: I_{\varphi} \subseteq \mathbb{R} \to \mathbb{R}^n$ of $\mathcal{C}$ are **equivalent** if and only if there exists a [[Parametrization#Equivalence of Parametrizations|reparametrization]] between them.
>
>>[!NOTE] Note
>>
>>This is the most general definition of equivalence for parametrizations. However, sometimes we require that such a [[Parametrization#Equivalence of Parametrizations|reparametrization]] also has additional properties such as [[Continuity]], [[Differentiability|continuous differentiability]] or [[Differentiability|smoothness]]. In this case, we say that $\gamma$ and $\varphi$ are "equivalent up to a PROPERTY reparametrization" such as "equivalent up to a continuous reparametrization" or "equivalent up to a smooth reparametrization".
>>
>

>[!THEOREM] Theorem: Equivalence of Regular Injective Parametrizations
>
>Let $\gamma: I_{\gamma} \subseteq \mathbb{R} \to \mathbb{R}^n$ and $\varphi: I_{\varphi} \subseteq \mathbb{R} \to \mathbb{R}^n$ be [[Curves#Parametrizations|parametrizations]] of the same [[Curves#Curves|curve]] $\mathcal{C}$.
>
>If $\gamma$ and $\varphi$ are $C^1$-[[TODO|regular]] (i.e. [[Differentiability of Parametric Curves|continuously differentiable]] with a non-vanishing [[Differentiability of Parametric Curves|derivative]]) and [[Injections, Surjections and Bijections|injective]], then they are [[Curves#Equivalence of Parametrizations|equivalent]] up to a [[Differentiability|continuously differentiable]] [[Curves#Equivalence of Parametrizations|reparametrization]].
>
>>[!PROOF]-
>>
>>TODO
>>
>

### Orientation

[[Differentiability of Parametric Curves|Continuously differentiable]] [[Curves#Parametrizations|parametrizations]] which are [[Curves#Equivalence of Parametrizations|equivalent]] up to a [[Differentiability|continuously differentiable]] [[Curves#Equivalence of Parametrizations|reparametrization]] with a non-vanishing [[Differentiability|derivative]] exhibit a nice property which allows us to define orientations for them.

>[!THEOREM] Theorem: Unit Tangent Vectors of Equivalent Parametrizations
>
>Let $\gamma: I_{\gamma} \subseteq \mathbb{R} \to \mathbb{R}^n$ and $\gamma: I_{\gamma} \subseteq \mathbb{R} \to \mathbb{R}^n$ be two [[Curves#Parametrizations|parametrizations]] of the same [[Curves#Curve|curve]] $\mathcal{C}$.
>
>If $\gamma$ and $\varphi$ are [[Differentiability of Parametric Curves|differentiable]] with non-vanishing [[Differentiability of Parametric Curves|derivatives]] and are also [[Curves#Equivalence of Parametrizations|equivalent]] up to a [[Differentiability|continuously differentiable]] [[Curves#Equivalence of Parametrizations|reparametrization]] $\{h_{I_{\gamma} \to I_{\varphi}}, h_{I_{\varphi} \to I_{\gamma}}\}$ with a non-vanishing [[Differentiability|derivative]], then exactly one of the following is true for their [[Parametrization|unit tangent vectors]]:
>
>- Case (I): $\mathbf{T}_{\varphi}(t) = \mathbf{T}_{\gamma}(h_{I_{\varphi} \to I_{\gamma}}(t))$ for all $t \in I_{\varphi}$
>- Case (II): $\mathbf{T}_{\varphi}(t) = -\mathbf{T}_{\gamma}(h_{I_{\varphi} \to I_{\gamma}}(t))$ for all $t \in I_{\varphi}$
>
>>[!PROOF]-
>>
>>By definition, we have $\varphi(t) = \gamma(h_{I_{\varphi} \to I_{\gamma}}(t))$. The [[Differentiation Rules for Curve Parameterisations|chain rule]] gives us
>>
>>$$
>>\varphi'(t) = \gamma'(h_{I_{\varphi} \to I_{\gamma}}(t)) \cdot h_{I_{\varphi} \to I_{\gamma}}'(t).
>>$$
>>
>>The [[Parametrization|unit tangent vector]] $\mathbf{T}_{\varphi}$ of $\varphi$ is given by $\frac{\varphi'}{||\varphi'||}$ which combined with the above yields
>>
>>$$
>>\mathbf{T}_{\varphi}(t) = \frac{\varphi'(t)}{||\varphi'(t)||} = \frac{\gamma'(h_{I_{\varphi} \to I_{\gamma}}(t)) \cdot h_{I_{\varphi} \to I_{\gamma}}'(t)}{||\gamma'(h_{I_{\varphi} \to I_{\gamma}}(t)) \cdot h_{I_{\varphi} \to I_{\gamma}}'(t)||}.
>>$$
>>
>>We can use the property of the norm to transform the above expression into the following:
>>
>>$$
>>\mathbf{T}_{\varphi}(t) = \frac{h_{I_{\varphi} \to I_{\gamma}}'(t)}{|h_{I_{\varphi} \to I_{\gamma}}'(t)|} \frac{\gamma'(h_{I_{\varphi} \to I_{\gamma}}(t))}{||\gamma'(h_{I_{\varphi} \to I_{\gamma}}(t))||} = \frac{h_{I_{\varphi} \to I_{\gamma}}'(t)}{|h_{I_{\varphi} \to I_{\gamma}}'(t)|} \mathbf{T}_{\gamma}(h_{I_{\varphi} \to I_{\gamma}}(t)).
>>$$
>>
>>Since $h_{I_{\varphi} \to I_{\gamma}}'(t)$ is [[Differentiability|continuously differentiable]] with a non-vanishing [[Differentiability|derivative]], it must be the case that either $h_{I_{\varphi} \to I_{\gamma}}'(t) \gt 0$ or $h_{I_{\varphi} \to I_{\gamma}}'(t) \lt 0$ for all $t \in I_{\varphi}$. Moreover, we notice that $\frac{h_{I_{\varphi} \to I_{\gamma}}'(t)}{|h_{I_{\varphi} \to I_{\gamma}}'(t)|}$ is $1$ if and only if $h_{I_{\varphi} \to I_{\gamma}}'(t) \gt 0$ and $\frac{h_{I_{\varphi} \to I_{\gamma}}'(t)}{|h_{I_{\varphi} \to I_{\gamma}}'(t)|}$ is $-1$ if and only if $h_{I_{\varphi} \to I_{\gamma}}'(t) \lt 0$ and so either $\frac{h_{I_{\varphi} \to I_{\gamma}}'(t)}{|h_{I_{\varphi} \to I_{\gamma}}'(t)|} = 1$ for all $t \in I_{\varphi}$ or $\frac{h_{I_{\varphi} \to I_{\gamma}}'(t)}{|h_{I_{\varphi} \to I_{\gamma}}'(t)|} = -1$ or $t \in I_{\varphi}$.
>>
>
>>[!DEFINITION] Definition: Orientation of Parametrizations
>>
>>We say that $\gamma$ and $\varphi$ have
>>- the **same orientation** in the first case;
>>- **opposite orientations** in the second case.
>>
>>>[!NOTE] Note: Preserving and Reversing Orientation
>>>
>>>We might also say that $\gamma$ and $\varphi$ are equivalent up to an
>>>- **orientation-preserving** reparametrization in the first case;
>>>- **orientation-reversing** reparametrization in the second case;
>>>
>>
>



Intuitively, the above theorem tells us that, under the specified conditions, the unit tangent vectorof one parametrization at each point on the curve is always either equal or exactly opposite to the unit tangent vector of the other parametrization at the same point.

![[res/Unit Tangent Vectors of Equivalent Parametrizations.svg]]

# Bibliography

