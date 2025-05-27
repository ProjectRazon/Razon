>[!DEFINITION] Definition: Linear Independence
>
>Let $\mathbf{v}_1, \cdots, \mathbf{v}_n$ be [[Vector|vectors]] in some [[Vector Space]] $(V,F,+,\cdot$).
>
>We say that $\mathbf{v}_1, \cdots, \mathbf{v}_n$ are **linearly independent** iff
>
>$$
>c_1\mathbf{v}_1 + \cdots + c_n\mathbf{v}_n = \mathbf{0} \implies c_1 = \cdots = c_n = 0
>$$
>
>>[!DEFINITION] Definition: Maximality
>>
>>A [[Sets|set]] of [[Linear Independence|linearly independent]] [[Vector|vectors]] $S = \{ \mathbf{v}_1, \mathbf{v}_2, \cdots \}$ is **maximal** if there is no $\mathbf{v} \in V \setminus S$ such that $S \cup \{ \mathbf{v} \}$ are still [[Linear Independence|linearly independent]]. 
>>
>

>[!THEOREM] Theorem: Size Limit for Linearly Independent Sets
>
>The number of elements in any [[Sets|set]] $I$ of [[Linear Independence|linearly independent]] [[Vector|vectors]] from a [[Spanning Set (Generator|finitely generated]].md) [[Vector Space]] $(V,F,+,\cdot)$ is always less than or equal to the [[Dimension]] of $V$.
>
>$$
>|I| \le \dim(V)
>$$
>
>>[!PROOF]-
>>
>>Let $B = \{\mathbf{b}_1, \cdots, \mathbf{b}_n,\}$ be a [[Basis]] of $V$ and let $I = \{\mathbf{v}_1, \cdots, \mathbf{v}_m\}$ be a [[Sets|set]] of [[Linear Independence|linearly independent]] [[Vector Space|vectors]].
>>
>>According to the [[Steinitz Exchange Lemma]] there are $n-m$ [[Vector Space|vectors]] in $B$ which form a basis with the vectors from $I$. This means that $n-m$ cannot be negative and thus the proof is complete.
>>
>