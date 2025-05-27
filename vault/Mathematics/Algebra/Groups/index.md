---
title: Groups
tags:
    - group-theory
    - abstract-algebra
    - algebra
    - mathematics
---

>[!DEFINITION] Definition: Group
>
>A **group** is a [[Monoid]] $(G, \circ)$ which also satisfies the existence of inverse elements: 
>- For each $a \in G$, there exists some $a_{\text{inv}} \in G$ such that $a \circ a_{\text{inv}} = a_{\text{inv}} \circ a = e$, where $e$ is the identity element of the monoid.
>
>>[!THEOREM] Theorem: Uniqueness of Group Inverses
>>
>>Each element of a [[index|group]] has a unique inverse.
>>
>>>[!PROOF]-
>>>
>>>Let $a$ be an element of a [[index|group]] $(G, \circ)$.
>>>
>>>Suppose there are two distinct inverses $a_{\text{inv}}$  and $a_{\text{inv}}'$ of $a$. By definition,
>>>
>>>$$
>>>a \circ a_{\text{inv}} = e
>>>$$
>>>
>>>$$
>>>a \circ a_{\text{inv}}' = e
>>>$$
>>>
>>>Therefore,
>>>
>>>$$
>>>a \circ a_{\text{inv}} = a \circ a_{\text{inv}}'
>>>$$
>>>
>>>We multiply both sides by $a_{\text{inv}}$ on the left and use associativity.
>>>
>>>$$
>>>a_{\text{inv}} \circ a \circ a_{\text{inv}} = a_{\text{inv}} \circ a \circ a_{\text{inv}}'
>>>$$
>>>
>>>$$
>>>(a_{\text{inv}} \circ a) \circ a_{\text{inv}} = (a_{\text{inv}} \circ a) \circ a_{\text{inv}}'
>>>$$
>>>
>>>$$
>>>e \circ a_{\text{inv}} = e \circ a_{\text{inv}}'
>>>$$
>>>
>>>$$
>>>a_{\text{inv}} = a_{\text{inv}}'
>>>$$
>>>
>>
>
>>[!NOTATION]-
>>
>>There are two notations used for groups and both are equivalent.
>>
>>>[!NOTATION]- Additive Notation
>>>
>>>The group operation is denoted by $+$, the identity element by $0$ and the inverse of each $g \in G$ by $-g$. Instead of writing $g + -g$ or $g + (-g)$, we write simply $g-g$.
>>>
>>
>>>[!NOTATION]- Multiplicative Notation
>>>
>>>The group operation is denoted by $\cdot$, the identity element by $1$ and the inverse of each $g \in G$ by $g^{-1}$. We can also write simply $ab$ instead of $a\cdot b$.
>>>
>>
>