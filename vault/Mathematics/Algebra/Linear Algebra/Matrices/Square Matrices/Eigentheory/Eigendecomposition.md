>[!DEFINITION] Definition: Diagonalisable Matrix
>
>A [[Square Matrix]] $A \in F^{n \times n}$ is **diagonalisable** if it is [[Matrix Similarity|similar]] to a [[Diagonal Matrix]] $\Lambda \in F^{n \times n}$.
>
>>[!THEOREM] Theorem: Eigendecomposition
>>
>>A [[Square Matrix]] $A \in F^{n \times n}$ is [[Eigendecomposition|diagonalisable]] if and only if it has $n$ [[Linear Independence|linearly independent]] [[Eigenvector|eigenvectors]] $\vec{e}_1, \cdots, \vec{e}_n$.
>>
>>In that case, $A$ can be written as a [[Matrix Product]]
>>
>>$$
>>A = Q\Lambda Q^{-1},
>>$$
>>
>>where the $k$-th column of $Q$ is the $\vec{e}_k$ and $\Lambda = \operatorname{diag}(\lambda_1, \cdots, \lambda_n)$ is the [[Diagonal Matrix]] whose $k$-th diagonal entry is the [[Eigenvalue]] $\lambda_k$ to which $\vec{e}_k$ belongs.
>>
>>>[!PROOF]-
>>>
>>>TODO
>>>
>>
>>>[!DEFINITION] Definition: Eigendecomposition
>>>
>>>The **eigendecomposition** of $A$ is the [[Matrix Product|product]] $Q\Lambda Q^{-1}$.
>>>
>>
>
