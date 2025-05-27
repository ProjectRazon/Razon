---
title: Coordinate Systems for Euclidean Space
tags:
    - coordinate-systems
    - euclidean-geometry
    - geometry
    - mathematics
---

# Coordinate Systems for Euclidean Space

Each [[Real Vector|vector]] $\mathbf{p}$ in the [[The Topology of Euclidean Space|Euclidean space]] $\mathbb{R}^n$ is completely specified by its $n$ components. However, many problems are very difficult or outright impossible to solve if we are doing calculations based on vectors' components. Hence, it is often convenient to specify each $\mathbf{p}$ in some other a way known as a **coordinate system**.

>[!DEFINITION] Definition: Coordinate System for Euclidean Space
>
>A [[index|coordinate system]] $\phi: \mathbb{R}^n \to \mathbb{R}^n$ for the [[The Topology of Euclidean Space|Euclidean space]] $\mathbb{R}^n$ is a [[Continuity of Real Vector Functions|continuous]] [[Real Vector Field|function]] which is [[Injections, Surjections and Bijections|bijective]] onto its [[Functions|image]] and has a continuous [[Continuity of Real Vector Functions|continuous]] [[Injections, Surjections and Bijections|inverse]]. The [[Functions of the Real Numbers|component functions]] of $\phi$ are $n$ [[Real Scalar Field|functions]] $\phi^1, \dotsc, \phi^n: \mathbb{R}^n \to \mathbb{R}$. These functions are known as **coordinates** ***on*** $\mathbb{R}^n$. Given a specific $\mathbf{p} \in \mathbb{R}^n$, the value $p^i = \phi^i (\mathbf{p})$ is known as the $i$-th **coordinate** ***of*** $\mathbf{p}$.
>
>>[!NOTATION]
>>
>>Coordinates are usually denotes using superscripts instead of subscripts: $\phi^1, \dotsc, \phi^n$ and $p^1, \dotsc, p^n$ instead of $\phi_1, \dotsc, \phi_n$ and $p_1, \dotsc, p_n$.
>>
>

>[!INTUITION]
>
>The requirements in the definition of a coordinate system mean that each [[Real Vector|vector]] is identified by a unique combination of coordinates but also ensure that [[Real Vector|vector]] which are closed to each other have coordinates which are close to each other. Essentially, if $\mathbf{p} \ne \mathbf{p}'$, then at least one of $\phi^1(\mathbf{p}), \dotsc, \phi^n(\mathbf{p})$ must be different from $\phi^1(\mathbf{p}'), \dotsc, \phi^n(\mathbf{p}')$. Furthermore, if the [[Euclidean Distance]] between $\mathbf{p}$ and $\mathbf{p}'$ is small, then the differences between $\phi^1(\mathbf{p}), \dotsc, \phi^n(\mathbf{p})$ and $\phi^1(\mathbf{p}'), \dotsc, \phi^n(\mathbf{p}')$, respectively, should be small.
>

## Coordinate Tuples

Although $\phi$ takes in a [[Real Vector|vector]] $\mathbf{p} \in \mathbb{R}^n$ and outputs the [[Real Vector|vector]] $\begin{bmatrix} \phi^1(\mathbf{p}) & \cdots & \phi^n(\mathbf{p}) \end{bmatrix}^{\mathsf{T}}$, we rarely treat its output as such. It is much more common to treat its output as the $n$-[[Tuples|tuple]] $(\phi^1 (\mathbf{p}), \dotsc, \phi^n (\mathbf{p}))$. We just define $\phi$ as a [[Real Vector Field|vector function]] only because it makes formulating the necessary requirements easier. This is, nevertheless, a very important point to make as treating the coordinates a vector falsely lead one to believe that the coordinates of $\mathbf{p} + \mathbf{p}$ are just $\phi^1(\mathbf{p}) + \phi^1 (\mathbf{p}')$, $\dotsc$, $\phi^n (\mathbf{p}) + \phi^n (\mathbf{p}')$. Whilst this might be true in certain coordinate system, it is the exception rather than the rule.

