---
title: Bounds
tags:
  - boundedness
  - orderings
  - set-theory
  - mathematics
---

# Lower Bounds

>[!DEFINITION] Definition: Lower Bound
>
>Let $T$ be a [[Sets|subset]] of a [[Partial Order|partially ordered]] [[Sets|set]] $S$.
>
>An element $l \in S$ is called a **lower bound** of $T$ iff
>
>$$
>l \le t \qquad \forall t\in T
>$$
>

## Infimum

>[!DEFINITION] Definition: Infimum
>
>Let $L$ be the [[Sets|set]] of all [[index|lower bounds]] of $T$.
>
>The **infimum** $\inf (T)$ of $T$ is its smallest [[index|lower bound]].
>
>$$
>\inf (T) \le l \qquad \forall l \in L
>$$
>
>>[!THEOREM] Theorem: Uniqueness of the Infimum
>>
>>The [[Boundedness#infimum|infimum]] of $T$ is unique.
>>
>>>[!PROOF]-
>>>
>>>TODO
>>>
>>
>

# Upper Bounds

>[!DEFINITION] Definition: Upper Bound
>
>Let $T$ be a [[Sets|subset]] of a [[Partial Order|partially ordered]] [[Sets|set]] $S$.
>
>An element $u \in S$ is called an **upper bound** of $T$ iff
>
>$$
>t \le u \qquad \forall t \in T
>$$
>

## Supremum

>[!DEFINITION] Definition: Supremum
>
>Let $U$ be the [[Sets|set]] of all [[index|upper bounds]] of $T$.
>
>The **supremum** $\sup (T)$ of $T$ is its largest [[index|upper bound]].
>
>$$
>u \le \sup (T) \qquad \forall u \in U
>$$
>
>>[!THEOREM] Theorem: Uniqueness of the Supremum
>>
>>The [[Boundedness#supremum|supremum]] of $T$ is unique.
>>
>>>[!PROOF]-
>>>
>>>TODO
>>>
>>
>

# Boundedness

>[!DEFINITION] Definition: Bounded Sets
>
>A [[Partial Order|partially ordered]] [[Sets|set]] is:
>- **bounded above** if it has an [[index#upper bounds|upper bound]];
>- **bounded below** if it has a [[index#lower bounds|lower bound]];
>- **bounded** if it has both an [[index#upper bounds|upper bound]] and a [[index#lower bounds|lower bound]].
>