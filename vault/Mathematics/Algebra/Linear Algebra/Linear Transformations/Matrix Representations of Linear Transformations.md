>[!THEOREM] Theorem: Matrix Representation of a Linear Transformation
>
>Every [[Linear Transformation]] $T: V \to W$ from the [[Vector Space]] $(V,F,+,\cdot)$ in the [[Vector Space]] $(W,F,+,\cdot)$ can be represented as a [[Matrix]] $M_T\in F^{\dim(W)\times \dim(V)}$.
> 
>Let $B_V$ and $B_W$ be [[Ordered Basis|ordered bases]] of $V$ and $W$, respectively. For every $\mathbf{v}\in V$, we have
> 
>$$
>{}_{B_W} T(\mathbf{v}) = M_T\cdot {}_{B_V}\mathbf{v},
>$$
> 
>where ${}_{B_V}\mathbf{v}$ is the [[Coordinate Vector]] of $\mathbf{v}$ with respect to $B_V$ and ${}_{B_W} T(\mathbf{v})$ is the [[Coordinate Vector]] with respect to $B_W$ of the vector $T(\mathbf{v}) \in W$ which is the result of applying $T$ to $\mathbf{v}$.
>
>>[!WARNING] Warning: Dependence on the Choice of Bases
>>
>>The [[Matrix]] $M_T$ depends on the choice of $B_V$ and $B_W$ - different [[Ordered Basis|bases]] will make the coefficients of $M_T$ different. To make this clear, we usually denote $M_T$ as ${}_{B_{W}}[M_T]_{B_{V}}$.
>>
>

>[!ALGORITHM] Algorithm: Finding the Matrix Representation
>
>Let $(V,F,+,\cdot)$ and $(W,F,+,\cdot)$ be two [[Vector Space|vector spaces]] and let $T: V \to W$ be a [[Linear Transformation]] from $V$ to $W$.
>
>We want to find the [[Matrix Representations of Linear Transformations|matrix representation]] ${}_{B_W}[M_T]$ with respect to the [[Ordered Basis|bases]] of our choice - $B_V = (\mathbf{b}_1^V,\cdots,\mathbf{b}_m^V)$ for $V$ and $B_W = (\mathbf{b}_1^W,\cdots,\mathbf{b}_n^W)$ for $W$. 
> 
>1. Determine the effect of $T$ on the elements of $B_V$, i.e. 
>
>$$\mathbf{w}_1 = T(\mathbf{b}_1^V) \qquad \cdots \qquad \mathbf{w}_m = T(\mathbf{b}_m^V)$$
>
>2. Determine the [[Coordinate Vector]] ${}_{B_W}\mathbf{w}_1,\cdots,{}_{B_W}\mathbf{w}_m$ of $\mathbf{w}_1,\cdots,\mathbf{w}_n$ with respect to $B_W$.
>	- There is no general process for this - it is different for each [[Vector Space]].
>
>3. Construct ${}_{B_W}[M_T]$ by using the [[Coordinate Vector|coordinate vectors]] ${}_{B_W}\mathbf{w}_1,\cdots, {}_{B_W}\mathbf{w}_m$ as its columns:
>
>$$
>{}_{B_W}[M_T]_{B_V} = \begin{bmatrix}\vert & \vert & \vert \\ {}_{B_W}\mathbf{w}_1 & \cdots & {}_{B_W}\mathbf{w}_m \\ \vert & \vert & \vert \end{bmatrix} = \begin{bmatrix}\vert & \vert & \vert \\ {}_{B_W}T(\mathbf{b}_1^V) & \cdots & {}_{B_W}T(\mathbf{b}_m^V) \\ \vert & \vert & \vert \end{bmatrix}
>$$
> 
>>[!EXAMPLE]-
>>
>>TODO
>>
>