---
title: Metric Spaces
tags:
  - metric-spaces
  - topology
  - mathematics
---

# Metric

>[!DEFINITION] Definition: Metric
>
>Let $M$ be a [[Sets|set]].
>
>A **metric** on $M$ is a [[Functions of the Real Numbers|real-valued function]] which has the following properties for all $x, y, z \in M$:
>
>- Identity of indiscernibles: $d(x, y) \ge 0$ with $d(x, y) = 0 \iff x = y$
>- Symmetry: $d(x,y) = d(y,x)$
>- Triangle inequality: $d(x,z) \le d(x,y) + d(y,z)$
>
>>[!INTUITION]-
>>
>>A metric on a set can be thought of as a way to define distance between the members of the set.
>> 
>

>[!DEFINITION] Definition: Open Ball
>
>Let $(M, d)$ be a [[index|metric space]].
>
>The **open ball** of radius $r$ around a given $x \in M$ is the [[Sets|set]] of all elements in $M$ which are a [[index|distance]] less than $r$ from $m$.
>
>$$
>\{x \in M \mid d(x, m)  \lt r\}
>$$
>
>>[!NOTATION]-
>>
>>$$
>>B_r(x) \qquad B(x, r)
>>$$
>>
>

# Metric Spaces

>[!DEFINITION] Definition: Metric Space
>
>A **metric space** $(M, d)$ is a [[Sets|set]] $M$ equipped with a [[index|metric]] on it.
>

## The Metric Topology

>[!THEOREM] Theorem: The Metric Topology
>
>Let $(M,d)$ be a [[index|metric space]].
>
>The [[Collections|collection]] of all [[index|open balls]] in $M$ forms a [[index|base]] $(M, \tau_d)$.
>
>>[!PROOF]-
>>
>>TODO
>>
>
>>[!DEFINITION] Definition: Metric Topology
>>
>>The [[Topological Spaces|topology]] $\tau_d$ is known as the **metric topology** induced on $M$ by $d$.
>>
>

>[!TIP] Corollary: Open Sets in the Metric Topology
>
>Let $(S,d)$ be a [[index|metric space]] and let $\tau$ be the [[index|topology]] induced on it by $d$.
>
>A [[Sets|subset]] $U$ of $S$ is [[Topological Spaces|open]] if and only if for each $u \in U$ there exists an [[index|open ball]] $B_\varepsilon (u)$ which is contained entirely in $U$.
>
>>[!PROOF]-
>>
>>This follows directly from [[index|topology generation]].
>>
>

## Properties

>[!THEOREM] Theorem: Metric Spaces are Hausdorff Spaces
>
>Every [[index|metric space]] is a [[Hausdorff Spaces]].
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: First-Countability of Metric Spaces
>
>Every [[index|metric space]] is [[First-Countability Axiom|first countable]].
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Convergence of Sequences in Metric Spaces
>
>Let $(M, d)$ be a [[index|metric space]] with its [[index|metric topology]].
>
>A [[Sequences|sequence]] $(x_n)_{n\in I}$ [[Convergence of Sequences|converges]] to some $l \in M$ if and only if for each [[index|open ball]] $B_\varepsilon(l)$ around $l$, there exists some $N \in I$ such that $x_n \in B_\varepsilon(l)$ for all $n \ge N$.
>
>>[!PROOF]-
>>
>>TODO
>>
>