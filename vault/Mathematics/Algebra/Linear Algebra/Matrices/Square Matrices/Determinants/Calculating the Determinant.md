>[!ALGORITHM] Algorithm: Calculating the Determinant of a Matrix
>
>To calculate the [[Determinant]] of a [[Square Matrix]] $A\in F^{n\times n}$:
>1. Go through the entries in the first row of $A$ one by one. Multiply the $k$-th entry $A_{1,k}$ with the [[Determinant]] of its [[Cofactor Matrix]] $A_{1,k}$ and alternate the algebraic sign each time - if $k$ is even, place a minus sign before the result. Calculating the [[Determinant]] of the [[Cofactor Matrix]] involves the same process recursively, until a $3\times3$ or $2\times 2$-[[Square Matrix|matrix]] is obtained, at which point one can use the theorems for those.
>
>2. The sum of all results from Step 1 is the [[Determinant]] of $A$.
>
>>[!NOTE] Tips
>>
>>1. Search for a row or column with many rows and exchange it with the first one.
>>2. If the first column contains many zeros, calculate the [[Determinant]] of $A$'s [[Matrix Transposition|transpose]], since they are the same.
>>
>
>>[!EXAMPLE]-
>>
>>$$
>>A = \begin{bmatrix}1 & 2 & 3 & 4 \\ 5 & 6 & 7 & 8 \\ 4 & 3 & 2 & 1 \\ 8 & 7 & 6 & 5\end{bmatrix}
>>$$
>>
>>According to the algorithm
>>
>>$$
>>\det(A) = 1\left|\begin{matrix}6 & 7 & 8 \\ 3 & 2 & 1 \\ 7 & 6 & 5\end{matrix}\right| - 2 \left|\begin{matrix}5 & 7 & 8 \\ 4 & 2 & 1 \\ 8 & 6 & 5\end{matrix}\right| + 3 \left|\begin{matrix}5 & 6 & 8 \\ 4 & 3 & 1 \\ 8 & 7 & 5\end{matrix}\right| - 4 \left|\begin{matrix}5 & 6 & 7 \\ 4 & 3 & 2 \\ 8 & 7 & 6\end{matrix}\right|
>>$$
>> 
>>We must now calculate the determinants of the $3 \times 3$-matrices.
>> 1. For the first matrix:
>> 
>>$$
>>\begin{vmatrix}6 & 7 & 8 \\3 & 2 & 1 \\7 & 6 & 5\end{vmatrix} = 6\begin{vmatrix} 2 & 1 \\ 6 & 5 \end{vmatrix} - 7\begin{vmatrix} 3 & 1 \\ 7 & 5 \end{vmatrix} + 8\begin{vmatrix} 3 & 2 \\ 7 & 6 \end{vmatrix}
>>$$
>>
>>$$
>>= 6 (2 \cdot 5 - 1 \cdot 6) - 7 (3 \cdot 5 - 1 \cdot 7) + 8 (3 \cdot 6 - 2 \cdot 7)
>>$$
>>
>>$$
>>= 6 (10 - 6) - 7 (15 - 7) + 8 (18 - 14)
>>$$
>>
>>$$
>>= 6 \cdot 4 - 7 \cdot 8 + 8 \cdot 4
>>$$
>>
>>$$
>>= 24 - 56 + 32 = 0
>>$$
>>
>>2. For the second matrix:
>> 
>>$$
>>\begin{vmatrix}5 & 7 & 8 \\4 & 2 & 1 \\8 & 6 & 5 \end{vmatrix} = 5\begin{vmatrix}2 & 1 \\6 & 5\end{vmatrix} - 7\begin{vmatrix}4 & 1 \\8 & 5\end{vmatrix} + 8\begin{vmatrix}4 & 2 \\8 & 6\end{vmatrix}
>>$$
>> 
>>$$
>>= 5 (2 \cdot 5 - 1 \cdot 6) - 7 (4 \cdot 5 - 1 \cdot 8) + 8 (4 \cdot 6 - 2 \cdot 8)
>>$$
>> 
>>$$
>>= 5 (10 - 6) - 7 (20 - 8) + 8 (24 - 16)
>>$$
>> 
>>$$
>>= 5 \cdot 4 - 7 \cdot 12 + 8 \cdot 8
>>$$
>> 
>>$$
>>= 20 - 84 + 64 = 0
>>$$
>> 
>> 3. For the third matrix:
>>
>>$$
>>\begin{vmatrix}5 & 6 & 8 \\4 & 3 & 1 \\8 & 7 & 5\end{vmatrix} = 5\begin{vmatrix}3 & 1 \\7 & 5\end{vmatrix} - 6\begin{vmatrix}4 & 1 \\8 & 5\end{vmatrix} + 8\begin{vmatrix}4 & 3 \\8 & 7\end{vmatrix}
>>$$
>>
>>$$
>>= 5 (3 \cdot 5 - 1 \cdot 7) - 6 (4 \cdot 5 - 1 \cdot 8) + 8 (4 \cdot 7 - 3 \cdot 8)
>>$$
>>
>>$$
>>= 5 (15 - 7) - 6 (20 - 8) + 8 (28 - 24)
>>$$
>>
>>$$
>>= 5 \cdot 8 - 6 \cdot 12 + 8 \cdot 4
>>$$
>>
>>$$
>>= 40 - 72 + 32 = 0
>>$$
>> 
>> 4. For the fourth matrix:
>>
>>$$
>>\begin{vmatrix}5 & 6 & 7 \\4 & 3 & 2 \\8 & 7 & 6\end{vmatrix} = 5\begin{vmatrix}3 & 2 \\7 & 6\end{vmatrix} - 6\begin{vmatrix}4 & 2 \\8 & 6\end{vmatrix} + 7\begin{vmatrix}4 & 3 \\8 & 7\end{vmatrix}
>>$$
>>
>>$$
>>= 5 (3 \cdot 6 - 2 \cdot 7) - 6 (4 \cdot 6 - 2 \cdot 8) + 7 (4 \cdot 7 - 3 \cdot 8)
>>$$
>>
>>$$
>>= 5 (18 - 14) - 6 (24 - 16) + 7 (28 - 24)
>>$$
>>
>>$$
>>= 5 \cdot 4 - 6 \cdot 8 + 7 \cdot 4
>>$$
>>
>>$$
>>= 20 - 48 + 28 = 0
>>$$
>> 
>>We see that all determinants are $0$ and so 
>>
>>$$
>>\det(A) = 1 \cdot 0 - 2 \cdot 0 + 3 \cdot 0 - 4 \cdot 0 = 0
>>$$
>> 

>[!THEOREM] Theorem: Determinant of a $2\times 2$-Matrix
>
>The [[Determinant]] of every $2\times 2$-[[Square Matrix|matrix]] $A = \begin{bmatrix}a & b \\ c & d\end{bmatrix}$ is given by
>
>$$
>\det (A) = ad - bc
>$$
>
>>[!PROOF]-
>>
>>By definition
>>
>>$$
>>\left|\begin{matrix}a & b \\ c & d\end{matrix}\right| = a\det(\begin{bmatrix}d\end{bmatrix}) - b\det(\begin{bmatrix}c\end{bmatrix}) = ad - bc
>>$$
>>
>

>[!THEOREM] Theorem: Determinant of a $3\times 3$-Matrix
> 
>The [[Determinant]] of every $3 \times 3$-[[Square Matrix|matrix]] $A = \begin{bmatrix}a & b & c \\ d & e & f \\ g & h & i\end{bmatrix}$ is given by
>
>$$
>\left|\begin{matrix}a & b & c \\ d & e & f \\ g & h & i\end{matrix}\right| = a(ei - fh) - b(di - fg) + c(dh - ge)
>$$
>
>>[!PROOF]-
>>
>>By definition
>>
>>$$
>>\left|\begin{matrix}a & b & c \\ d & e & f \\ g & h & i\end{matrix}\right| = a\left|\begin{matrix}e & f \\ h & i\end{matrix}\right| - b \left|\begin{matrix}d & f \\ g & i\end{matrix}\right| + c \left|\begin{matrix}d & e \\ g & h\end{matrix}\right|
>>$$
>> 
>>The $2\times 2$-determinants can be calculated with the previous theorem.
>>
