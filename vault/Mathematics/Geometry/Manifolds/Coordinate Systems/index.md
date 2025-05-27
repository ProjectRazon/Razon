---
title: Coordinate Systems
tags:
  - coordinate-systems
  - manifolds
  - geometry
  - topology
---

# Coordinate Systems on Manifolds

>[!DEFINITION] Definition: Coordinate System
>
>Let $U$ be an [[Topological Spaces|open subset]] of an $n$-[[Manifolds|manifold]] $M$.
>
>A **coordinate system** or **coordinate map** on $U$ is a [[index|homeomorphism]] $\phi: U \to \mathbb{R}^n$ from the [[Topological Subspaces|subspace]] $U$ to an [[Topological Spaces|open subset]] of the [[The Topology of Euclidean Space|Euclidean space]] $\mathbb{R}^n$.
>
>>[!DEFINITION] Definition: Coordinates on a Subset
>>
>>The [[Functions of the Real Numbers|component functions]] $\phi^1, \dotsc, \phi^n: U \to \mathbb{R}$ of $\phi$ are known as **local coordinates** or simply **coordinates** on $U$.
>>
>>>[!NOTATION]-
>>>
>>>The component functions of a coordinate system $\phi$ are usually denoted using superscripts instead of subscripts, i.e. $\phi^1, \dotsc, \phi^n$ instead of $\phi_1, \dotsc, \phi_n$.
>>>
>>
>
>>[!DEFINITION] Definition: Coordinates of a Point
>>
>>Given a point $p \in U$, we call $\phi^k(p)$ the $k$-th **coordinate** of $p$.
>>
>>>[!NOTATION]-
>>>
>>>The coordinates of a point $p$ are usually written together as an $n$-[[Tuples|tuple]]:
>>>
>>>$$
>>>(\phi^1(p), \dotsc, \phi^n(p))
>>>$$
>>>
>>>Oftentimes, we denote the coordinates of $p$ using superscripts in order to make it clear that they are coordinates of some point:
>>>
>>>$$
>>>(p^1, \dotsc, p^n),
>>>$$
>>>
>>>where $p^k = \phi_k(p)$.
>>>
>>
>
>>[!INTUITION]-
>>
>>In its essence, a coordinate system is just a way to identify each point of $U$ with a point (vector) of $\mathbb{R}^n$. More importantly, it is a way to *uniquely* do so, since $\phi$ is a homeomorphism and therefore bijective. No two points of $U$ can correspond to the same vector of $\mathbb{R}^n$ and no two vectors in $\mathbb{R}^n$ can correspond to the same point in $U$. This means that each point $u \in U$ can be uniquely assigned coordinates
>>
>>$$
>>u^1 = \phi_1(u), \dotsc, u^n = \phi_n(u)
>>$$
>>
>>Another useful property of coordinate systems is the fact that they are continuous (since they are homeomorphism by definition). Intuitively, this means that if two points $p$ and $q$ of $U$ are "close", then the [[Euclidean Distance]] between the vectors they correspond to will be small.
>>
>


>[!DEFINITION] Definition: Origin of a Coordinate System
>
>We say that a point $p \in U$ is the **origin** of $\phi$ or that $\phi$ is **centered** at $p$ iff $\varphi(p) = \vec{0}$.
>

>[!DEFINITION] Definition: Global Coordinate System
>
>A [[index|coordinate system]] on an $n$-[[Manifolds|manifold]] $M$ is **global** iff its [[Functions|domain]] is the entirety of $M$.
>
>>[!INTUITION]-
>>
>>A global coordinate system extends to the entire manifold - each point $p \in M$ can be uniquely assigned $n$ coordinates.
>>
>
>>[!WARNING]
>>
>>Most manifolds do *not* admit global coordinate systems because this would require that they are [[Homeomorphic Spaces|homeomorphic]] to $\mathbb{R}^n$.
>>
>

## Charts on Manifolds

>[!DEFINITION] Definition: Chart
>
>Let $M$ be an $n$-[[Manifolds|manifold]].
>
>A **chart** $(U, \phi)$ for $M$ is an [[Topological Spaces|open subset]] $U \subseteq M$ equipped with a [[index|coordinate system]] $\phi: U \to \mathbb{R}^n$ on it.
>
>>[!DEFINITION] Definition: Coordinate Domain
>>
>>We call $U$ the **coordinate domain** of $(U, \phi)$.
>>
>

>[!DEFINITION] Definition: Chart Compatibility
>
>Let $(U_{\alpha}, \phi_{\alpha})$ and $(U_{\beta}, \phi_{\beta})$ be two [[index|charts]] on an $n$-[[Manifolds|manifold]] $M$.
>
>We say that $(U_{\alpha}, \phi_{\alpha})$ and $(U_{\beta}, \phi_{\beta})$ are $C^k$-**compatible** (where $k \in \mathbb{N}_0\cup \{\infty\}$) iff the [[Transition Maps]] between them are $k$-times [[Partial Derivatives of Real Vector Functions|continuously partially differentiable]] or $U_{\alpha} \cap U_{\beta} = \varnothing$. 
>

