>[!THEOREM] Theorem: Transforming the Zero Vector
>
>Every [[Linear Transformation]] $T: V \to W$ always transforms the [[Vector Space|zero vector]] $V$ to the zero vector of [[Vector Space|zero vector]]:
>
>$$
>T(\mathbf{0}_V) = \mathbf{0}_W
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Linearity of Composition
>
>The composition $g\circ f: V\to W$ of two [[Linear Transformation|linear transformations]] $f: V \to U$ and $g: U \to W$ is also a [[Linear Transformation]].
>
>>[!PROOF]-
>>
>>$$
>>\begin{align*}g\circ f(\lambda \mathbf{u} +\mu\mathbf{v}) &= g(f(\lambda \mathbf{u} +\mu\mathbf{v}))\\ &= g(\lambda f(\mathbf{u}) + \mu f(\mathbf{v})) \\ &= g(\lambda f(\mathbf{u})) + g(\mu f(\mathbf{v})) \\ &= \lambda g(f(\mathbf{u})) +\mu g(f(\mathbf{v}))\\ &= \lambda g\circ f(\mathbf{u})+\mu g\circ f (\mathbf{v})\end{align*}
>>$$
>>
>

>[!THEOREM] Theorem: Linearity of the Inverse Transformation
>
>If $T$ is a [[Injections, Surjections and Bijections|bijective]] [[Linear Transformation]], then its [[Injections, Surjections and Bijections|inverse]] $T^{-1}$ is also a [[Injections, Surjections and Bijections|bijective]] [[Linear Transformation]].
>
>>[!PROOF]-
>>
>>TODO
>>
>