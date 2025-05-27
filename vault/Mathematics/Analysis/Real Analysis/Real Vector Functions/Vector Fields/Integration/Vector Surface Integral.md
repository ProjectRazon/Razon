>[!DEFINITION] Definition: Vector Surface Integral
>
>Let $\mathbf{F}: \mathcal{D}_{\mathbf{F}} \subseteq \mathbb{R}^3 \to \mathbb{R}^3$ be a [[Real Vector Field]] and let $S: \mathcal{D}_S \subseteq \mathbb{R}^2 \to \mathbb{R}^3$ be a [[Differentiability of Real Vector Functions|differentiable]] [[Parametric Surface]] whose [[Functions|image]] $S(\mathcal{D}_S)$ is a [[Sets|subset]] of $\mathcal{D}_{\mathbf{F}}$.
>
>The **(vector) surface integral** of $f$ over $S$ is the [[Double Integrals|double integral]]
>
>$$
>\iint_{\mathcal{D}_S} \mathbf{F}(S(x,y)) \cdot \mathbf{N}(x,y) \mathop{\mathrm{d}\mathcal{D}_S},
>$$
>
>where $\mathbf{N}$ is the [[Surface Normal Vector|normal vector]] of $S$ and $\cdot$ denotes the [[Real Dot Product|dot product]].
>
>>[!NOTATION]-
>>
>>$$
>>\iint_S \mathbf{F} \qquad \iint_S \mathbf{F} \cdot \mathrm{d}\mathbf{S}
>>$$
>>
>>If $S(\mathcal{D}_S)$ is a [[Closed Surfaces|closed surface]], then a circle can be put through the two integral signs.
>

>[!THEOREM] Theorem: Vector Surface Integral to Scalar Surface Integral
>
>Let $\mathbf{F}: \mathcal{D}_{\mathbf{F}} \subseteq \mathbb{R}^3 \to \mathbb{R}^3$ be a [[Real Vector Field]] and let $S: \mathcal{D}_S \subseteq \mathbb{R}^2 \to \mathbb{R}^3$ be a [[Differentiability of Real Vector Functions|differentiable]] [[Parametric Surface]] whose [[Functions|image]] $S(\mathcal{D}_S)$ is a [[Sets|subset]] of $\mathcal{D}_{\mathbf{F}}$.
>
>The [[Vector Surface Integral]] of $\mathbf{F}$ over $S$ is equal to the [[Scalar Surface Integrals|scalar surface integral]] of the [[Real Dot Product|dot product]] between $\mathbf{F}$ and the [[Surface Normal Vector|unit surface normal]] of $S$.
>
>$$
>\iint_S \mathbf{F} \cdot \mathop{\mathrm{d}\mathbf{S}} = \iint_S \mathbf{F} \cdot \mathbf{n} \mathop{\mathrm{d}S}
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Vector Surface Integrals of Reparameterisations
>
>Let $\mathbf{F}: \mathcal{D}_{\mathbf{F}} \subseteq \mathbb{R}^3 \to \mathbb{R}^3$ be a [[Real Vector Field]] and let $\phi: \mathcal{D}_{\phi} \subseteq \mathbb{R}^2 \to \mathbb{R}^3$ and $\psi: \mathcal{D}_{\psi} \subseteq \mathbb{R}^2 \to \mathbb{R}^3$ be [[Equivalence of Parametric Surfaces|equivalent]] [[Parametric Surface|parametric surfaces]] whose [[Functions|image]] is a [[Sets|subset]] of $\mathcal{D}_{\mathbf{F}}$.
>
>If $\phi$ and $\psi$ have the [[Equivalence of Parametric Surfaces|same orientation]], then the [[Vector Surface Integral|surface integrals]] of $\mathbf{F}$ over $\phi$ and $\psi$ are equal:
>
>$$
>\iint_{\phi} \mathbf{F} = \iint_{\psi} \mathbf{F}
>$$
>
>If $\phi$ and $\psi$ have [[Equivalence of Parametric Surfaces|opposite orientations]], then the [[Vector Surface Integral|surface integrals]] of $\mathbf{F}$ over $\phi$ and $\psi$ are equal in magnitude but differ in algebraic sign:
>
>$$
>\iint_{\phi} \mathbf{F} = -\iint_{\psi} \mathbf{F}
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>


