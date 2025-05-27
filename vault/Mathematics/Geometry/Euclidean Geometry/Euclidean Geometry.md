---
title: Euclidean Geometry
tags:
  - euclidean-geometry
  - geometry
  - mathematics
---

# Euclidean Geometry

>[!DEFINITION] Definition: Euclidean Geometry
>
>**Euclidean geometry** is the study of [[Topological Spaces]] which are [[Homeomorphic Spaces|homeomorphic]] to some [[The Topology of Euclidean Space|Euclidean space]].
>

Euclidean geometry considers space as an abstract object, known as a [[Topological Spaces|topological space]]. This object is just a [[Sets|set]] with some special mathematical properties which allow us to rigorously define the notions of distance and "closeness" so that they match with our observations of the physical world.

The "[[Homeomorphic Spaces|homeomorphic]] to some [[The Topology of Euclidean Space|Euclidean space]]" part means that there is a [[Injections, Surjections and Bijections|bijection]] between this [[Sets|set]] and some [[The Topology of Euclidean Space|Euclidean space]] $\mathbb{R}^n$ - in other words, each element (**point**) of the [[Sets|set]] can be uniquely associated with an $n$-dimensional [[Real Vector|real column vector]] $\mathbb{R}^n$. This is very useful because it allows us to apply [[index|real analysis]] to study geometry.

>[!NOTATION]
>
>Points are usually denoted with uppercase Latin letters: $P,Q,K,L,$ etc.
>
>The fact that points can be associated with vectors is so fundamental that we often think of the point and its associated vector as the same thing and write $P = \begin{bmatrix}p_1 & \cdots & p_n\end{bmatrix}^\mathsf{T}$ or more commonly $P = (p_1, \cdots, p_n)$.
>
>

>[!DEFINITION] Definition: Locus of Points
>
>A **locus of points** is any [[Sets|set]] of [[Euclidean Geometry|points]].
>

Once again, points and vectors are so closely related in geometry that we introduce the notion of a vector "pointing" from one point to another.

>[!DEFINITION] Definition: Vector between Points
>
>The vector which "points" from point $P$ to point $Q$, denoted by $\overrightarrow{PQ}$ is the [[Real Vector|difference]] between the [[Real Vector|vector]] associated with $P$ and the [[Real Vector|vector]] associated with $Q$:
>
>$$
>\overrightarrow{PQ} = Q - P
>$$
>

>[!DEFINITION] Definition: Distance between Points
>
>The **distance** between two [[Euclidean Geometry|points]] $P$ and $Q$ is the norm of the [[Euclidean Geometry|vector]] $\overrightarrow{PQ}$ or $\overrightarrow{QP}$:
>
>$$
>d(P, Q) \overset{\text{def}}{=} |\overrightarrow{PQ}| = |\overrightarrow{QP}|
>$$
>