>[!DEFINITION] Definition: Matrix Transposition
>
>The **transpose** of a [[Matrix]] $A \in F^{m\times n}$ is the [[Matrix]] $A^\mathsf{T} \in F^{n \times m}$ obtained by switching the rows and the columns of $A$, i.e. the $i$-th row (or column) of $A$ is the $i$-th column (or row) of $A^\mathsf{T}$:
>
>$$
>\begin{bmatrix}a_{11} & \cdots & a_{1n} \\ \vdots & \ddots & \vdots \\ a_{m1} & \cdots & a_{mn}\end{bmatrix}^\mathsf{T} \overset{\text{def}}{=} \begin{bmatrix}a_{11} & \cdots & a_{m1} \\ \vdots & \ddots & \vdots \\ a_{1n} & \cdots & a_{mn}\end{bmatrix}
>$$
>
>>[!TIP]
>>
>>The entry in the $i$-th row and the $j$-th column of $A$ is the entry in the $j$-th row and the $i$-th column of $A^\mathsf{T}$.
>>
>
>>[!TIP]
>>
>>The number of rows in $A^\mathsf{T}$ is equal to the number columns in $A$ and the number of columns in $A^\mathsf{T}$ is equal to the number of rows in $A$.
>>
>

>[!THEOREM] Theorem: Distributivity of Transposition
>
>The [[Matrix Transposition]] is distributive over [[Matrix Addition]] and [[Scalar Multiplication]]:
>
>$$
>(A + B)^\mathsf{T} = A^\mathsf{T} + B^\mathsf{T}
>$$
>
>$$
>(\lambda A)^\mathsf{T} = \lambda A^\mathsf{T}
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Antidistributivity of Transposition
>
>The [[Matrix Transposition]] is antidistributive over the [[Matrix Product]]:
>
>$$
>(AB)^\mathsf{T} = B^\mathsf{T} A^\mathsf{T}
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Involution of Transposition
>
>The [[Matrix Transposition]] is an [[Injections, Surjections and Bijections|involution]].
>
>>[!PROOF]-
>>
>>TODO
>>
>