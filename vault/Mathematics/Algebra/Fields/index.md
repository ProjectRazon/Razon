---
title: Fields
tags:
  - field-theory
  - abstract-algebra
  - algebra
  - mathematics
---

# Fields

> [!DEFINITION] Definition: Field
> 
>A **field** $(F, +, \cdot)$ is an [[Integral Domain]] where each nonzero element has a multiplicative inverse, i.e. for each $a \in F, a\ne 0$ there exists an element $a^{-1} \in F$ such that
>
>$$
>a \cdot a^{-1} = a^{-1} \cdot a = 1
>$$
>
>>[!THEOREM]- Theorem: Uniqueness of Multiplicative Inverses
>>
>>The multiplicative inverse of an element $a$ in a [[Field]] is unique.
>>
>>>[!PROOF]-
>>>
>>>Suppose there were two multiplicative inverses $a^{-1}$ and $a^{-1}{'}$.
>>>
>>>Since $a^{-1}$ is a multiplicative inverse, we have
>>>
>>>$$
>>>a \cdot a^{-1} = 1
>>>$$
>>>
>>>Similarly, since $a^{-1}{'}$ is a multiplicative inverse, we have
>>>
>>>$$
>>>a \cdot a^{-1}{'} = 1
>>>$$
>>>
>>>Combining the two equations, we obtain
>>>
>>>$$
>>>a \cdot a^{-1} = a \cdot a^{-1}{'}
>>>$$
>>>
>>>Multiply both sides by $a^{-1}$ - it does not matter whether we multiply from the left or from the right, since multiplication in integral domains is commutative.
>>>
>>>$$
>>>a^{-1} \cdot (a \cdot a^{-1}) = a^{-1} \cdot (a \cdot a^{-1}{'})
>>>$$
>>>
>>>We now avail ourselves of the associativity of multiplication.
>>>
>>>$$
>>>(a^{-1} \cdot a) \cdot a^{-1} = (a^{-1} \cdot a) \cdot a^{-1}{'}
>>>$$
>>>
>>>$$
>>>1 \cdot a^{-1} = 1 \cdot a^{-1}{'}
>>>$$
>>>
>>>$$
>>>a^{-1} = a^{-1}{'}
>>>$$
>>>
>>
>

## Fields as Vector Spaces

>[!THEOREM] Theorem: Fields as Vector Spaces
>
>Every [[index|field]] $F$ with is a [[Vector Space]] $(F,F,+,\cdot)$ over itself.
>
>>[!PROOF]-
>>
>>TODO
>>
>

# Ordered Fields

>[!DEFINITION] Definition: Ordered Field
>
>An **ordered field** is a [[index|field]] $(F,+,\cdot)$ with a [[Total Order]] $\le$ which for all $a,b,c \in F$ satisfies
>- If $a \le b$, then $a + c \le b + c$;
>- If $0 \le a$ and $0 \le b$, then $0 \le a\cdot b$.
>
>>[!NOTATION]-
>>
>>We write $a \lt b$, if $a \le b$ and $a\ne b$.
>>
>>The notations $b \ge a$ and $b \gt a$ stand for $a \le b$ and $a \lt b$, respectively. 
>>
>