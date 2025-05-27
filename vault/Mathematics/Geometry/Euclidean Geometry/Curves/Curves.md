---
title: Curves
tags:
  - curves
  - euclidean-geometry
  - geometry
  - mathematics
---

# Curves

>[!DEFINITION] Definition: Curve
>
>A **curve** $\mathcal{C}$ in $\mathbb{R}^n$ is a [[Geometric Shapes|geometric figure]] which is the [[Functions|image]] of a nonconstant [[Parametric Curve]] $\gamma$.
>

## Types of Curves

### Curves with Endpoints

>[!DEFINITION] Definition: Endpoints
>
>TODO
>

### Closed Curves

>[!DEFINITION] Definition: Closed Curves
>
>A [[Curves|curve]] is **closed** iff it is [[The Topology of Euclidean Space|compact]] and without [[Manifolds|manifold boundary]].
>

### Simple Curves

>[!DEFINITION] Definition: Simple Curve
>
>A **simple curve** is a [[Curves#Curves|curve]] $\mathcal{C}$ for which there exists an [[Injections, Surjections and Bijections|injective]] [[Curves#Parametrizations|parametrization]] $\gamma: I \subset \mathbb{R} \to \mathbb{R}^n$ on a closed interval $I = [a;b]$ with a [[Continuity of Real Scalar Fields|continuous]] [[Injections, Surjections and Bijections|inverse]].
>
>>[!NOTE]
>>
>>Simples curves are also known as **Jordan arcs**.
>>
>

A [[Curves#Simple Curves|simple curve]] is just a [[Curves#Curves with Endpoints|curve with endpoints]] which does not intersect itself. The existence of a continuous inverse also guarantees that curve is not [[TODO|space-filling]].


# Length

>[!DEFINITION] Definition: Length of Curves
>
>>[!NOTE] Note: Generalization to Non-Simple Curves
>>
>>If a [[Curves#Curves|curve]] $\mathcal{C}$ is not [[Curves#Simple Curves|simple]] but can be represented as the [[Operations with Collections|union]] $\mathcal{C} = \mathcal{C}_1 \cup \mathcal{C}_2 \cup \cdots \cup \mathcal{C}_{n-1} \cup \mathcal{C}_n$ of finitely many [[Curves#Simple Curves|simple curves]] $\mathcal{C}_1, \dotsc, \mathcal{C}_n$ such that $\mathcal{C}_{k}$ and $\mathcal{C}_{k+1}$ share exactly one point and this point lies on their [[Manifolds|manifold boundary]], then we define the length of $\mathcal{C}$ as the sum of the lengths of $\mathcal{C}_1, \dotsc, \mathcal{C}_n$:
>>
>>$$
>>\mathcal{L}(\mathcal{C}) \overset{\text{def}}{=} \sum_{i = 1}^n \mathcal{L}(\mathcal{C}_i)
>>$$
>>
>

>[!THEOREM] Theorem: Length via Line Integral
>
>The [[Curves#Length|length]] of a [[Curves|curve]] $\mathcal{C} \subset \mathbb{R}^n$ is given by the [[Scalar Line Integrals#Scalar Line Integrals over Geometric Curves|line integral]] of $1$ over $\mathcal{C}$.
>
>$$
>\int_{\mathcal{C}} 1 \mathop{\mathrm{d}s}
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

