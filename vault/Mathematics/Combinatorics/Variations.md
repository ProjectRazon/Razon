---
title: Variations
tags:
    - combinatorics
    - mathematics
---

# Variations without Repetitions

>[!DEFINITION] Definition: Variation of a Finite Set
>
>Let $S$ be a finite [[Sets|set]].
>
>A **variation** of class $k$ is a [[Permutations|permutation]] of a [[Sets|subset]] of $S$ with $k$ elements.
>
>>[!NOTE] Note: Terminology
>>
>>If $S$ has $n$ elements, we also say a "variation of $n$ elements of class $k$".
>>
>>Variations of class $k$ are unfortunately also called permutations of class $k$.
>>
>
>>[!INTUITION]-
>>
>>A variation of class $k$ is a way to arrange exactly $k$ of the elements of $S$. You can also think of it as a way to choose $k$ elements of $S$ in a specific order. If you pick the same $k$ elements but in a different order, you will have different variations.
>>
>>Since a set does not contain duplicate elements, repetitions are not allowed - you cannot choose the same element from $S$ multiple times in the same variation.
>>
>
>>[!EXAMPLE]-
>>
>>Suppose $S = \{A, B, C, D, E\}$.
>>
>>The following are different variations of class 3:
>>
>>$$
>>(A, D, E) \qquad (E, D, A) \qquad (C, A, E) \qquad (D, B, C) \qquad (B, D, A)
>>$$
>>
>>The following are different variations of class 4:
>>
>>$$
>>(A, D, C, B) \qquad (C, B, A, D) \qquad (E, D, A, B)
>>$$
>>
>>The following are *not* variations:
>>
>>$$
>>(A, A, C, B) \qquad (A, B, C, D, E, C) 
>>$$
>>
>

>[!THEOREM] Theorem: Number of Variations
>
>The total number of [[Variations]] of $n$ elements of class $k$ is 
>
>$$
>n \times (n - 1) \times (n - 2) \times \cdots \times (n - (k - 1))
>$$
>
>It is also given by the ratio of the total number of [[Permutations]] of $n$ elements to the total number of [[Permutations]] of $n-k$ elements.
>
>$$
>\frac{P_n}{P_{n - k}} = \frac{n!}{(n - k)!}
>$$
>
>>[!NOTATION]-
>>
>>$$
>>V_n^k \qquad V_k^n \qquad P_n^k \qquad P_k^n
>>$$
>>
>
>>[!PROOF]-
>>
>>TODO
>>
>

# Variations with Repetition

>[!DEFINITION] Definition: Variation with Repetition
>
>Let $S = \{s_1, \dotsc, s_n\}$ be a [[Sets|set]].
>
>A **variation with repetition** of $S$ of class $k$ is a $k$-[[Tuples|tuple]] of non-necessarily unique elements from $S$.
>
>$$
>(t_1, \dotsc, t_k) \qquad t_i \in S
>$$
>
>>[!EXAMPLE]-
>>
>>Suppose $S = \{1, 2, 3, 4, 5\}$.
>>
>>Some variations $S$ of class $2$ with repetition are
>>
>>$$
>>(1,2) \qquad (2, 1) \qquad (3, 3) \qquad (4, 3) \qquad (1, 5)
>>$$
>>
>>Some variations of $S$ of class $3$ with repetition are
>>
>>$$
>>(1, 1, 4) \qquad (4, 2, 4) \qquad (3, 5, 1) \qquad (2, 2, 2)
>>$$
>>
>>Some variations of $S$ of class $6$ with repetition are
>>
>>$$
>>(1, 2, 3, 4, 5, 1) \qquad (3, 2, 3, 3, 3, 2)
>>$$
>>
>

>[!THEOREM] Theorem: Total Number of Variations with Repetition
>
>If $S$ is a [[Sets|set]] with $n$ elements, then the total number of [[Variations#Variations with Repetition|variations with repetition]] of $S$ of class $k$, denoted by is $n^k$.
>
>$$
>n^k
>$$
>
>>[!NOTATION]
>>
>>Since this number depends only on $n$ and $k$, but not on the elements of $S$, we usually denote it as
>>
>>$$
>>\tilde{V}_n^k
>>$$
>>
>
>>[!PROOF]-
>>
>>TODO
>>
>