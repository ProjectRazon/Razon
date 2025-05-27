>[!DEFINITION] Definition: Orthonormal Basis
>
>An **orthonormal basis** of an [[Inner Product Space]] is an [[Orthogonal Basis]] $B$, where the [[Canonical Norm]] of each basis element is equal to one:
>
>$$
>||\mathbf{v}|| = 1 \qquad \forall \mathbf{v} \in B
>$$
>

>[!THEOREM] Theorem: Vector Representation through an Orthonormal Basis
>
>If $B = \{\mathbf{b}_1, \cdots, \mathbf{b}_n\}$ is an [[Orthonormal Basis]] of an [[Inner Product Space]] $(V,F,+,\cdot)$, then the $i$-th coefficient $c_i$ in the [[Basis|basis representation]] $\mathbf{v} = \sum_{i=1}^n c_i \mathbf{b}_i$ of any $\mathbf{v} \in V$ is the [[Inner Product Space|inner product]] of $\mathbf{v}$ with the $i$-th basis vector $\mathbf{b}_i$:
>
>$$
>c_i = \langle \mathbf{v}, \mathbf{b}_i \rangle
>$$
>
>>[!PROOF]-
>>
>>$$
>>\langle \mathbf{v},\mathbf{b}_i\rangle = c_1 \langle \mathbf{b}_1,\mathbf{b}_i\rangle + \cdots + c_i \langle \mathbf{b}_i,\mathbf{b}_i\rangle + \cdots + c_n \langle \mathbf{b}_n,\mathbf{b}_i\rangle
>>$$
>>
>>Since the basis is orthogonal, $\langle \mathbf{b}_j,\mathbf{b}_i\rangle = 0$ for all $j \ne i$. Moreover, the basis is orthonormal and so $\langle \mathbf{b}_i,\mathbf{b}_i\rangle = ||\mathbf{b}_i||^2 = 1^2 = 1$ which means that
>>
>>$$
>>\langle \mathbf{v},\mathbf{b}_i\rangle = c_1 \underset{0}{\underbrace{\langle \mathbf{b}_1,\mathbf{b}_i\rangle}} + \cdots + c_i \underset{1}{\underbrace{\langle \mathbf{b}_i,\mathbf{b}_i\rangle}} + \cdots + c_n\underset{0}{\underbrace{\langle \mathbf{b}_n,\mathbf{b}_i\rangle}} = c_i
>>$$
>>
>