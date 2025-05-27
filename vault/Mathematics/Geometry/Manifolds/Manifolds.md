---
title: Manifolds
tags:
    - manifolds
    - geometry
    - topology
---

# Manifolds

>[!DEFINITION] Definition: Manifold
>
>A **manifold** is a [[Second-Countability Axiom|second-countable]] [[Hausdorff Spaces|Hausdorff space]] which is [[Locally Homeomorphic Spaces|locally homeomorphic]] to a [[The Topology of Euclidean Space|Euclidean space]].
>

>[!THEOREM] Theorem: Invariance of Manifold Dimension
>
>A [[Sets|nonempty]] [[Topological Spaces|topological space]] cannot be [[Locally Homeomorphic Spaces|locally homeomorphic]] to more than one [[The Topology of Euclidean Space|Euclidean space]] - if it is [[Locally Homeomorphic Spaces|locally homeomorphic]] to $\mathbb{R}^n$ and to $\mathbb{R}^m$, then $n = m$.
>
>>[!PROOF]-
>>
>>TODO
>>
>
>>[!DEFINITION] Definition: Dimension of a Manifold
>>
>>The **dimension** of a [[Manifolds|manifold]] is the [[Dimension]] of the [[The Topology of Euclidean Space|Euclidean space]] which it is [[Locally Homeomorphic Spaces|locally homeomorphic]] to.
>>
>>>[!NOTATION]-
>>>
>>> The dimension of a manifold is such a fundamental property that we often denote it as a superscript on the manifold's name. If the manifold is $M$ and its dimension is $n$, we write $M^n$ and call $M$ an $n$-manifold or an $n$-dimensional manifold.
>>>
>>
>

## Manifolds with Boundary

>[!DEFINITION] Definition: Manifold with Boundary
>
>An $n$-dimensional **manifold with boundary** is a [[Second-Countability Axiom|second countable]] [[Hausdorff Spaces|Hausdorff space]] $M$ in which each point has a [[Topological Spaces|neighbourhood]] which is [[Homeomorphic Spaces|homeomorphic]] to the [[The Topology of Euclidean Space|Euclidean space]] $\mathbb{R}^n$ or to the [[Half-Spaces|closed upper half-space]] $\mathbb{H}^n$.
>
>>[!DEFINITION] Definition: Manifold Interior
>>
>>A point $p \in M$ is an **interior point** of $M$ iff $p$ has a [[Topological Spaces|neighbourhood]] which is [[Homeomorphic Spaces|homeomorphic]] to the [[The Topology of Euclidean Space|Euclidean space]] $\mathbb{R}^n$.
>>
>>The **interior** of $M$ is the [[Sets|set]] of all its interior points.
>>
>>>[!NOTATION]
>>>
>>>$$
>>>\operatorname{Int} M
>>>$$
>>>
>>
>
>>[!DEFINITION] Definition: Boundary
>>
>>The **boundary** of $M$ is the [[Complement]] of $M$'s interior in $M$.
>>
>>$$
>>M \setminus \operatorname{Int} M
>>$$
>>
>>>[!NOTATION]
>>>
>>>$$
>>>\partial M
>>>$$
>>>
>>
>>>[!WARNING]
>>>
>>>Despite the name and terminology used, the interior and boundary of a manifold with boundary $M$ are not necessarily the same as its [[Interior, Boundary and Exterior|interior]] and [[Interior, Boundary and Exterior|boundary]] when $M$ is considered a [[Sets|subset]] of some other [[Topological Spaces|topological space]].
>>>
>>
>
