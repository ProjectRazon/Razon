>[!DEFINITION] Definition: Matrix Product
>
>The **matrix product** of a [[Matrix]] $A \in F^{m \times n}$ with a [[Matrix]] $B \in F^{n \times p}$ is another [[Matrix]] $C \in F^{m \times p}$ defined as follows:
>
>$$
>\begin{bmatrix}a_{11} & \cdots & a_{1n} \\ \vdots & \ddots & \vdots \\ a_{m1} & \cdots & a_{mn} \end{bmatrix}\begin{bmatrix}b_{11} & \cdots & b_{1p} \\ \vdots & \ddots & \vdots \\ b_{n1} & \cdots & b_{np} \end{bmatrix}\overset{\text{def}}{=} \begin{bmatrix} c_{11} & \cdots & c_{1p} \\ \vdots & \ddots & \vdots \\ c_{m1} & \cdots & c_{mp}\end{bmatrix},
>$$
>
>where
>
>$$
>c_{ij} \overset{\text{def}}{=} \sum_{k=1}^n a_{ik}b_{kj}
>$$
>
>>[!NOTATION]-
>>
>>$$
>>C = A\times B = A\cdot B = AB
>>$$
>>
>
>>[!TIP]- Tip: Computation of Individual Entries
>>
>>The entry $c_{ij}$ in the $i$-th row and the $j$-th column of the matrix product $C$ is obtained by multiplying the $k$-th entry in the $i$-th row of $A$ with the $k$-th entry in the $j$-th column of $B$ and summing these products.
>>
>
>>[!TIP]- Tip: Requirements for Matrix Multiplication
>>
>>In order for the matrix product $AB$ to be possible, the number of columns in $A$ must be equal to the number of rows in $B$.
>>
>
>>[!TIP]- Tip: Rows and Columns in the Matrix Product
>>
>>The matrix product $AB$ has the same number of rows as $A$ and the same number of columns as $B$.
>>
>

>[!THEOREM] Theorem: Non-Commutativity of the Matrix Product
>
>In general, the [[Matrix Product]] of two [[Matrix|matrices]] is not commutative:
>
>$$
>A\cdot B \ne B \cdot A
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Associativity of the Matrix Product
>
>The [[Matrix Product]] is associative - for all [[Matrix|matrices]] $A \in F^{m\times n}, B \in K^{n\times p}$ and $C \in K^{p\times q}$
>
>$$
>A \cdot (B \cdot C) = (A \cdot B) \cdot C
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Distributivity of the Matrix Product
>
>The [[Matrix Product]] is distributive over addition:
>
>$$
>\begin{align*}
>(A + B)\cdot C &= A\cdot C + B \cdot C \\ A\cdot (B + C) &= A\cdot B + A \cdot C
>\end{align*}
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>>
>