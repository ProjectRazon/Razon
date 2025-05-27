---
title: Permutations
tags:
    - combinatorics
    - mathematics
---

# Permutations without Repetition

>[!DEFINITION] Definition: Permutation
>
>Let $S$ be a finite [[Sets|set]] with $n$ elements.
>
>A **permutation (without repetition)** of $S$ is an $n$-[[Tuples|tuple]] which contains every element of $S$ exactly once.
>
>>[!INTUITION]-
>>
>>A permutation of $S$ is just a way to arrange all elements of $S$.
>>
>
>>[!EXAMPLE]-
>>
>>Suppose $S = \{A, B, C, D\}$. The following are permutations of $S$:
>>
>>$$
>>(A, B, C, D) \qquad (D, A, C, B) \qquad (B, D, A, C) \qquad (C, B, D, A)
>>$$
>>
>>The following are *not* permutations of $S$: 
>>
>>$$
>>(A, B, D) \qquad (B, C) \qquad (A, B, B, D, C)
>>$$
>>
>

>[!THEOREM] Theorem: Number of Permutations
>
>Let $S$ be a finite [[Sets|set]] with $n$ elements.
>
>The total number of possible permutations of $S$ is
>
>$$
>\prod_{k = 1}^n k = 1 \times 2 \times \cdots \times (n-1) \times n = n!
>$$
>
>>[!NOTATION]-
>>
>>$$
>>P_n
>>$$
>>
>
>>[!PROOF]-
>>
>>We go through the process of constructing a permutation.
>>
>>For the first element of the permutation, we can choose any one of the $n$ elements inside $S$. For the second element of the permutation, we can choose only between the remaining $n - 1$ elements of $S$, since we already chose one element as our first. In general, for the $k$-th element of the permutation, we can choose between $n - (k - 1)$ elements, since at the $k$-th step, we have already filled $k-1$ places of the permutation with elements from $S$. Multiplying these possibilities together, we get the stated result.
>>
>

# Permutations with Repetition

>[!DEFINITION] Definition: Permutation with Repetition
>
>Let $S$ be a [[Multisets|multiset]] with cardinality $k$.
>
>A **permutation with repetition** of $S$ is a $k$-[[Tuples|tuple]] of elements from $S$ in which each element $s_i$ is present as many times as its multiplicity $k_i$.
>
>>[!EXAMPLE]-
>>
>>Let $S = \{3, 3, 4, 5, 5, 5\}$.
>>
>>Some permutations with repetition of $S$ are
>>
>>$$
>>(4, 3, 5, 5, 3, 5) \qquad (5, 3, 4, 5, 5, 3) \qquad (5, 3, 5, 4, 3, 5). 
>>$$
>>
>

>[!THEOREM] Theorem: Total Number of Permutations with Repetition
>
>If $S = \{s_1, \dotsc, s_n\}$ is a [[Multisets|multiset]] with cardinality $k$, then the total number of [[Permutations#Permutations with Repetition|permutations with repetition]] $S$ can be calculated via $k$ and the multiplicity $k_i$ of each element as follows:
>
>$$
>\frac{k!}{k_1! \cdots k_n!}
>$$
>
>>[!NOTATION]
>>
>>Since this number depends only on the cardinality $k$ and multiplicities $k_i$ but does not depend on the elements themselves, we call the above number the **total number of permutations with repetition of class** $k$ and denote it by
>>
>>$$
>>\tilde{P}(k_1, \dotsc, k_n) 
>>$$
>>
>
>>[!PROOF]-
>>
>>TODO
>>
>