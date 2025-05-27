>[!ALGORITHM] Algorithm: Matrix Inversion
>
>To find the [[Invertibility|inverse]] of an [[Invertibility|invertible]] [[Square Matrix|matrix]] $A \in F^{n \times n}$:
>1. Notate an $n\times 2n$-[[Matrix]] $(A\mid I_n)$ by sticking the [[Identity Matrix]] $I_n$ to the right of $A$.
>2. Perform [[Gauss-Jordan Elimination]] on $(A \mid I_n)$. If $A$ is indeed [[Invertibility|invertible]], the final result will be $(I_n \mid A^{-1})$.
>
>>[!EXAMPLE]-
>>
>>Let's find the inverse of $A = \begin{bmatrix}6 & 8 & 3 \\ 4 & 7 & 3 \\ 1 & 2 & 1\end{bmatrix}$. Notate
>>
>>$$
>>[A\mid I_3] = \left[\begin{array}{ccc|ccc}6 & 8 & 3 & 1 & 0 & 0\\ 4 & 7 & 3 & 0 & 1 & 0 \\ 1 & 2 & 1 & 0 & 0 & 1\end{array}\right]
>>$$
>>
>>Perform [[Gauss-Jordan Elimination]]
>>
>>$$
>>\left[\begin{array}{ccc|ccc}6 & 8 & 3 & 1 & 0 & 0\\ 4 & 7 & 3 & 0 & 1 & 0 \\ 1 & 2 & 1 & 0 & 0 & 1\end{array}\right] \approx \left[\begin{array}{ccc|ccc}1 & 2 & 1 & 0 & 0 & 1 \\ 6 & 8 & 3 & 1 & 0 & 0\\ 4 & 7 & 3 & 0 & 1 & 0 \end{array}\right] \approx \left[\begin{array}{ccc|ccc}1 & 2 & 1 & 0 & 0 & 1 \\ 0 & -4 & -3 & 1 & 0 & -6\\ 0 & -1 & -1 & 0 & 1 & -4 \end{array}\right]
>>$$
>>
>>$$
>>\left[\begin{array}{ccc|ccc}1 & 2 & 1 & 0 & 0 & 1 \\ 0 & -4 & -3 & 1 & 0 & -6\\ 0 & -1 & -1 & 0 & 1 & -4 \end{array}\right] \approx \left[\begin{array}{ccc|ccc}1 & 0 & -1 & 0 & 2 & -7 \\ 0 & 1 & 1 & 0 & -1 & 4\\ 0 & 0 & 1 & 1 & -4 & 10 \end{array}\right] \approx \left[\begin{array}{ccc|ccc}1 & 0 & 0 & 1 & -2 & 3 \\ 0 & 1 & 0 & -1 & 3 & -6\\ 0 & 0 & 1 & 1 & -4 & 10 \end{array}\right]
>>$$
>>
>>$$
>>A^{-1} = \begin{bmatrix}1 & -2 & 3 \\ -1 & 3 & -6 \\ 1 & -4 & 10\end{bmatrix}
>>$$
>>
>

>[!THEOREM] Theorem: Inverting $2\times2$-Matrices
>
>A $2\times 2$-[[Square Matrix|matrix]] $A = \begin{bmatrix}a & b \\ c & d\end{bmatrix}$ is [[Invertibility|invertible]] if and only if
>
>$$
>ad - bc \ne 0
>$$
>
>If $A$ is [[Invertibility|invertible]], then
>
>$$
>A^{-1} = \frac{1}{ad-bc}\begin{bmatrix}d & -b \\ -c & a\end{bmatrix}
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>