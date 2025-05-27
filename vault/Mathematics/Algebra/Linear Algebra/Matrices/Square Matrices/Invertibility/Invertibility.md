>[!DEFINITION] Definition: Invertible Matrix
>
>A [[Square Matrix]] $A \in F^{n \times n}$ is **invertible** if there is a [[Square Matrix]] $A^{-1} \in F^{n \times n}$ such that the [[Matrix Product|matrix products]] $AA^{-1}$ and $A^{-1}A$ are equal to the [[Identity Matrix]] $I_n$.
>
>$$
>AA^{-1} = A^{-1} A = I_n
>$$
>
>The matrices $A$ and $A^{-1}$ are called **inverses** of each other.
>

>[!THEOREM] Theorem: Antidistributivity of Matrix Inversion
>
>[[Invertibility|Matrix inversion]] is antidistributive over [[Matrix Product|matrix products]] - if $A, B \in F^{n \times}$ and their [[Matrix Product|product]] $AB$ are [[Invertibility|invertible]], then:
>
>$$
>(AB)^{-1} = B^{-1} A^{-1}
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Invertible Matrix Theorem
>
>The following statements are equivalent for every [[Square Matrix]] $A \in F^{n \times n}$: 
>- $A$ is [[Invertibility|invertible]].
>- The [[Matrix Transposition|transpose]] of $A$ is [[Invertibility|invertible]].
>- The [[Determinant]] of $A$ is not zero, i.e. $\det(A) \ne 0$.
>- The [[Row Echelon Form|reduced row echelon form]] of $A$ is the [[Identity Matrix]] $I_n$.
>- The [[Augmented Matrix|system of linear equations]] $A \vec{x} = \vec{b}$ has a single [[Solvability of a System of Linear Equations|solution]] for every $\vec{b} \in F^n$.
>- The [[Column Space]] of $A$ is the [[Vector Space of Matrices|vector space]] $F^n$.
>- The [[Row Space]] of $A$ is the [[Vector Space of Matrices|vector space]] $F^{1 \times n}$.
>- The [[Rank]] of $A$ is $n$.
>
>>[!PROOF]-
>>
>>TODO
>>
>