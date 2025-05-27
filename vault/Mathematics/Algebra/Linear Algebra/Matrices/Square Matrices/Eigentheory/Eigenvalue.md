>[!DEFINITION] Definition: Eigenvalue
>
>Let $A \in F^{n \times n}$ be a [[Square Matrix]].
>
>We say that $\lambda \in F$ is an **eigenvalue** of $A$ if there is a non-zero [[Column Vector|vector]] $\vec{v} \in F^n$ such that
>
>$$
>A \vec{v} = \lambda \vec{v}
>$$
>
>In this case, we also say that $\lambda$ has the [[Eigenvector]] $\vec{v}$.
>
>>[!NOTE]
>>
>>An [[Eigenvalue]] can have multiple [[Eigenvector|eigenvectors]].
>>
>

>[!THEOREM] Theorem: Count of Eigenvalues
>
>A [[Square Matrix]] $A \in F^{n \times n}$ has at most $n$ different [[Eigenvalue|eigenvalues]].
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Algebraic and Geometric Multiplicity
>
>The [[Eigenspace|geometric multiplicity]] and the [[Characteristic Polynomial|algebraic multiplicity]] of every [[Eigenvalue]] $\lambda$ of a [[Square Matrix]] $A \in F^{n \times n}$ obey the following inequality:
>
>$$
>1\le \operatorname{geo}(\lambda)\le \operatorname{alg}(\lambda)
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Sum of the Eigenvalues
>
>The distinct [[Eigenvalue|eigenvalues]] $\lambda_1, \cdots, \lambda_r$ of a [[Square Matrix]] $A \in F^{n \times n}$ and their [[Characteristic Polynomial|algebraic multiplicities]] can be used to calculate the [[Trace]] of $A$:
>
>$$
>\sum_{k=1}^r \lambda_k \cdot \operatorname{alg} (\lambda_k) = \operatorname{Tr}(A)
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Product of the Eigenvalues
>
>The distinct [[Eigenvalue|eigenvalues]] $\lambda_1, \cdots, \lambda_r$ of a [[Square Matrix]] $A \in F^{n \times n}$ and their [[Characteristic Polynomial|algebraic multiplicities]] can be used to calculate the [[Determinant]] of $A$:
>
>$$
>\prod_{k=1}^r \lambda_k^{\operatorname{alg} (\lambda_k)} = \det(A)
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>