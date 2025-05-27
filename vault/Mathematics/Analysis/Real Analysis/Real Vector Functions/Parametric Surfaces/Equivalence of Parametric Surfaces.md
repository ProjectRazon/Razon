>[!DEFINITION] Definition: Equivalence of Parametric Surfaces
>
>Let $\phi: \mathcal{D}_{\phi} \subseteq \mathbb{R}^2 \to \mathbb{R}^n$ and $\psi: \mathcal{D}_{\psi} \subseteq \mathbb{R}^2 \to \mathbb{R}^n$ be [[Parametric Surface|parametric surfaces]].
>
>We say that $\phi$ and $\psi$ are **equivalent** if they have the same [[Functions|image]] and there exists a [[Differentiability of Real Vector Functions|differentiable]], [[Injections, Surjections and Bijections|bijective]] [[Real Vector Field]] $h: \mathcal{D}_{\phi} \to \mathcal{D}_{\psi}$ with a [[Differentiability of Real Vector Functions|differentiable]] [[Injections, Surjections and Bijections|inverse]] such that
>
>$$
>\psi \circ h = \phi 
>$$
>
>>[!DEFINITION] Definition: Reparameterisation
>>
>>Equivalent parametric surfaces are also known as **reparameterisations**.
>>
>>>[!DEFINITION] Definition: Smooth Reparameterisation
>>>
>>>We say that $\phi$ and $\psi$ are **smooth reparameterisations** if they are both [[Smoothness|smooth]] and $h$ and $h^{-1}$ are [[Differentiability of Real Vector Functions|continuously differentiable]].
>>>
>>
>

>[!THEOREM] Theorem: Surface Normals of Smooth Parameterisations
>
>If $\phi: \mathcal{D}_{\phi} \subseteq \mathbb{R}^2 \to \mathbb{R}^n$ and $\psi: \mathcal{D}_{\psi} \subseteq \mathbb{R}^2 \to \mathbb{R}^n$ are [[Equivalence of Parametric Surfaces|smooth reparameterisations]], then their [[Surface Normal Vector|surface normal vectors]] $\mathbf{N}_{\psi}$ and $\mathbf{N}_{\phi}$ at each $\mathbf{p} \in \phi(\mathcal{D}_{\phi})$ (or equivalently $\mathbf{p} \in \psi(\mathcal{D}_{\psi})$) are related by
>
>$$
>\mathbf{N}_{\phi} = k(\mathbf{p}) \mathbf{N}_{\psi},
>$$
>
>where $k(\mathbf{p}) \in \mathbb{R}$.
>
>>[!PROOF]-
>>
>>TODO
>>
>