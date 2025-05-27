>[!ALGORITHM] Algorithm: Gauss-Jordan Elimination
>
>The **Gauss-Jordan elimination** algorithm allows us to determine the solutions of a [[System of Linear Equations]].
>
>1. Notate the [[Augmented Matrix]] $(A|\vec{b})$.
>
>2. Bring $(A|\vec{b})$ into [[Row Echelon Form|reduced row echelon form]] via [[Elementary Row Operations]].
>	- Make the pivot of the $k$-th row equal to $1$ by multiplying the row with an appropriate constant. Then add an appropriate multiple of the $k$-th row to every row below it in order to obtain only $0$s below its pivot.
>	
>3. Examine the solution space of the system:
>	- If a row of the form $\begin{bmatrix}0 & \cdots & 0 \mid \ast\end{bmatrix}$, where $\ast \ne 0$, appears at any step of the process, then the [[System of Linear Equations]] has no solutions.
>	- If the resultant [[Coefficient Matrix]] $A$ has only $1$s on the diagonal and $0$s everywhere else, then system has a unique solution and the last entry in the $k$-th row of the resultant [[Augmented Matrix]] $(A\mid \vec{b})$ is the value for the $k$-th unknown $x_k$.
>	- If the resultant [[Augmented Matrix]] $(A\mid \vec{b})$ has one or more all-zero rows, then the system has infinitely many solutions.
>
>>[!EXAMPLE]-
>>
>>TODO
>>
>