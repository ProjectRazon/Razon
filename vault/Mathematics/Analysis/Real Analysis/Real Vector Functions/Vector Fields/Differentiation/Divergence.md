# Introduction

In physics, it is often necessary to be able to get a sense of how much a [[Real Vector Field|vector field]] tends to point towards or away from a particular point. This is precisely what divergence tells us. 

# Divergence 

Imagine a [[Real Vector Field|vector field]] $\mathbf{F}$ and some point $\mathbf{p}$ in $\mathbb{R}^3$. To quantify the extent to which $\mathbf{F}$ points towards or away from $\mathbf{p}$, we can construct a sphere $S_r$ of radius $r$ which is centred at $\mathbf{p}$ and then see how much of the field enters and exits through $S_r$. This can be done by using the [[Vector Surface Integral|integral]] of $\mathbf{F}$ over $S_r$, which is equal to $\displaystyle \iint_{S_r} \mathbf{F} \cdot \mathbf{n} \mathop{\mathrm{d}S_r}$, where $\mathbf{n}$ is the [[Surface Normal Vector|unit surface normal]]. 

![[res/Divergence.drawio.svg]]

Recall that the [[Real Dot Product|dot product]] quantifies the extent to which two vectors are oriented in a similar direction. Essentially, at each point of the sphere $S_r$, the dot product $\mathbf{F} \cdot \mathbf{n}$ tells us how aligned $\mathbf{F}$ is with $\mathbf{n}$ there. A positive value means that $\mathbf{F}$ points in a direction which is generally aligned with $\mathbf{n}$, i.e. away from the sphere. Conversely, a negative value means that $\mathbf{F}$ points towards the sphere. The integral is just the sum of these values. If it is positive, then there are more points on the sphere where $\mathbf{F}$ tends to point outwards. If it is negative, then there are more points on the sphere where $\mathbf{F}$ tends to point inwards.

Moreover, as we make the radius $r$ smaller and smaller, the sphere closes in on $\mathbf{p}$. In the limit of $r \to 0$, the part of the field which enters the sphere is essentially the part of the field which points towards $\mathbf{p}$. Similarly, the part of the field which exits the sphere is the part of the field which points away from $\mathbf{p}$.

>[!THEOREM] Theorem: Existence of Divergence
>
>Let $\mathbf{F}: \mathcal{D} \subseteq \mathbb{R}^3 \to \mathbb{R}^3$ be a [[Real Vector Field]] which is [[Differentiability of Real Vector Functions|differentiable]] at $\mathbf{p}$ and let $S_r$ be a [[Parametric Surface]] whose [[Functions|image]] is a sphere of radius $r$ centered at $\mathbf{p}$ such that its [[Surface Normal Vector|normal vector]] is always oriented outwards.
>
>If there exists some [[Topological Spaces|neighbourhood]] of $\mathbf{p}$ where $\mathbf{F}$ is [[Differentiability of Real Vector Functions|continuously differentiable]], then the [[Limits of Real Functions|limit]]
>
>$$
>\lim_{r \to 0^+} \frac{1}{V_r} \iint_{S_r} \mathbf{F} \cdot \mathrm{d}\mathbf{S}_r,
>$$
>
>where $\displaystyle \iint_{S_r} \mathbf{F} \cdot \mathrm{d}\mathbf{S}_r$ is the [[Vector Surface Integral|surface integral]] of $\mathbf{F}$ over $S_r$ and $V_r$ is the volume of $S_r$, exists.
>
>>[!PROOF]-
>>
>>TODO
>>
>
>>[!DEFINITION] Definition: Divergence
>>
>>The **divergence** of $\mathbf{F}$ at $\mathbf{p}$ is defined as precisely
>>
>>$$
>>\lim_{r \to 0^+} \frac{1}{V_r} \iint_{S_r} \mathbf{F} \cdot \mathop{\mathrm{d}\mathbf{S}_r},
>>$$
>>
>>>[!NOTATION]-
>>>
>>>$$
>>>\nabla \cdot \mathbf{F}(\mathbf{p}) \qquad \operatorname{div}\mathbf{F}(\mathbf{p})
>>>$$
>>>
>>
>>
>>>[!NOTE] Note: Divergence as a Function
>>>
>>>When there is no specific $\mathbf{p} \in \mathcal{D}$ mentioned, the term "divergence" is used to refer to the [[Real Scalar Field|scalar field]] $\mathop{\operatorname{div}}\mathbf{F}: \mathcal{D} \to \mathbb{R}$ which maps each $\mathbf{x}$ to its divergence $\nabla \cdot \boldsymbol{v}(\mathbf{x})$.
>>>
>>
>

>[!THEOREM] Theorem: Divergence in Cartesian Coordinates
>
>Let $\boldsymbol{v}: \mathcal{D} \subseteq \mathbb{R}^3 \to \mathbb{R}^3$ be a [[Real Vector Field]] with [[Functions of the Real Numbers|component functions]] $v_1, v_2, v_3$ and let $\mathbf{p} \in \mathbb{R}^3$.
>
>If $\boldsymbol{v}$ is [[Differentiability of Real Vector Functions|continuously differentiable]] at $\mathbf{p}$, then its [[Divergence]] there can be calculated using the [[Partial Derivatives of Real Scalar Fields|partial derivatives]] of $v_1, v_2, v_3$ with respect to [[Cartesian Coordinate System|Cartesian coordinates]]:
>
>$$
>\nabla \cdot \boldsymbol{v} (\mathbf{p}) = \frac{\partial v_1}{\partial x}(\mathbf{p}) + \frac{\partial v_2}{\partial y}(\mathbf{p}) + \frac{\partial v_3}{\partial z}(\mathbf{p})
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

## Properties

>[!THEOREM] Theorem: Linearity of the Divergence
>
>
>
>The [[Divergence]] is [[Linear Transformation|linear]] - for all $\lambda, \mu \in \mathbb{R}$ and all [[Real Vector Field|vector fields]] $\boldsymbol{u}, \boldsymbol{v}$ which are [[Differentiability of Real Vector Functions|differentiable]] at $\mathbf{p} \in \mathbb{R}^3$ we have
>
>$$
>\operatorname{div} (\lambda \boldsymbol{u} + \mu \boldsymbol{v})(\mathbf{p}) = \lambda \operatorname{div} \boldsymbol{u}(\mathbf{p}) + \mu \operatorname{div} \boldsymbol{v}(\mathbf{p})
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>
