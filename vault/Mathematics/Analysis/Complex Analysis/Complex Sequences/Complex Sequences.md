---
title: Complex Sequences
tags:
    - complex-sequences
    - complex-analysis
    - mathematics
---

>[!DEFINITION] Definition: Complex Sequence
>
>A **complex sequence** or **sequence of complex numbers** is a [[Complex-Valued Functions|complex-valued function]] $a: \mathcal{D} \subseteq \mathbb{N}_0 \to \mathbb{C}$ whose [[Functions|domain]] $\mathcal{D}$ is either $\mathbb{N}_0$ or a finite [[Sets|subset]] of $\mathbb{N}$ which has the form $\mathcal{D} = \{0,1,2,3,\dotsc, n\}, n \in \mathbb{N}$.
>
>>[!DEFINITION] Definition: Finite and Sequences
>>
>>If $\mathcal{D}$ is nonempty but finite, then we say that $(a_n)_{n \in \mathcal{D}}$ is finite. Otherwise, we say that $(a_n)_{n \in \mathcal{D}}$ is infinite.
>>
>
>>[!NOTATION]-
>>
>>We usually denote $a$ by $(a_n)_{n \in \mathcal{D}}$ or $\{a_n\}_{n \in \mathcal{D}}$. If $\mathcal{D}$ is not really relevant, we can drop it and write just $(a_n)$ or $\{a_n\}$. If $\mathcal{D} = \mathbb{N}_0$ or $\mathcal{D} = \mathbb{N}$, we write $\{a_n\}_{n = 0}^{\infty}$ and $\{a_n\}_{n = 1}^{\infty}$, respectively.
>>
>>Instead of $a(0), a(1), a(2), \dotsc, a(k)$, we write $a_0, a_1, a_2, \dotsc, a_k$.
>>
>

# Equality of Complex Sequences

>[!THEOREM] Theorem: Equality of Complex Sequences
>
>Let $(a_n)_{n \in \mathcal{D}}$ and $(b_n)_{n \in \mathcal{D}}$ be [[Complex Sequences|infinite complex sequences]].
>
>If there exist [[Complex Power Series]] $\sum_{n \in \mathcal{D}} a_n (x - c)^n$ and $\sum_{n \in \mathcal{D}} b_n (x - c)^n$ which have the same center $c \in \mathbb{C}$ and for which there is some $r \gt 0$ such that both series [[Convergence|converge]] and
>
>$$
>\sum_{n \in \mathcal{D}} a_n (x - c)^n = \sum_{n \in \mathcal{D}} b_n (x - c)^n
>$$
>
>when when $|x - c| \lt r$, then $a_n = b_n$ for all $n \in \mathcal{D}$.
>
>>[!PROOF]-
>>
>>TODO
>>
>