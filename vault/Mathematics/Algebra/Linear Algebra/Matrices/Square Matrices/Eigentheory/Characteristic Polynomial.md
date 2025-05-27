>[!DEFINITION] Definition: Characteristic Polynomial
>
>The **characteristic polynomial** $p_A(x)$ of a [[Square Matrix]] $A \in F^{n \times n}$ the [[index|univariate polynomial]] obtained through the [[Determinant]] and the [[Identity Matrix]] $I_n$ in the following way:
>
>$$
>p_A(x) \overset{\text{def}}{=} \det(A - x I_n)
>$$
>

>[!THEOREM] Theorem: Degree of the Characteristic Polynomial
>
>The [[Polynomials|degree]] of the [[Characteristic Polynomial]] of a [[Square Matrix]] $A \in F^{n \times n}$ is $n$.
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Finding Eigenvalues
>
>The [[Eigenvalue|eigenvalues]] of a [[Square Matrix]] $A \in F^{n \times n}$ are precisely the roots of its [[Characteristic Polynomial]].
>
>$$
>\det (A - x I_n) = 0
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>
>>[!DEFINITION] Definition: Algebraic Multiplicity
>>
>>If the [[Characteristic Polynomial]] of $A$ has a linear factorisation
>>
>>$$
>>p_A(x) = (x - \lambda_1)^{k_1} \cdots (x - \lambda_r)^{k_r}
>>$$ 
>>
>>over the [[index|field]] $F$, where $\lambda_1,\cdots,\lambda_r \, (r \le n)$ are the distinct [[Eigenvalue|eigenvalues]] of $A$, then we call $k_i$ the **algebraic multiplicity** of $\lambda_i$.
>>
>>>[!NOTATION]-
>>>
>>>$$
>>>\operatorname{alg}(\lambda_i)
>>>$$
>>>
>>
>