>[!DEFINITION] Definition: Determinant
>
>The **determinant** of a [[Matrix]] $A \in F^{n \times n}$ is an element in $F$ which is calculated recursively from the coefficients of $A$:
>
>$$
>\det(A) = \begin{cases}a_{11}, \text{ if } n = 1 \\ \displaystyle\sum_{i=1}^n (-1)^{1+j}a_{1j}\det(A_{1j}), \text{ if } n\gt 1\end{cases}
>$$
>
>>[!NOTATION]-
>>
>>$$
>>|A| \qquad \det(A)
>>$$
>>
>

>[!THEOREM] Theorem: Distributivity of the Determinant
>
>The [[Determinant]] is distributive over [[Matrix Product|matrix products]]:
>
>$$
>\det(AB) = \det(A) \det(B) = \det(B) \det(A) = \det(BA)
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Determinant of the Transpose
>
>The [[Determinant]] of the [[Matrix Transposition|transpose]] of a $A$ is the same as the [[Determinant]] of $A$.
>
>$$
>\det(A^\mathsf{T}) = \det(A)
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Determinant of the Inverse
>
>If $A$ is [[Invertibility|invertible]], then the [[Determinant]] of $A^{-1}$ is the reciprocal of $A$'s [[Determinant]]:
>
>$$
>\det(A^{-1}) = \frac{1}{\det(A)}
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Determinant of Scalar Multiplication
>
>For the [[Determinant]] of every [[Square Matrix]] $A \in F^{n \times n}$ and every $\alpha \in F$:
>
>$$
>\det(\alpha A) = \alpha^n \det (A)
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>