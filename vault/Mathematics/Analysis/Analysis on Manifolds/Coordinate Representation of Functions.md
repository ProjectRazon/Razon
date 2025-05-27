---
title: Coordinate Representation of Functions
tags:
    - analysis-on-manifolds
    - analysis
    - smooth-manifolds
    - mathematics
---

>[!DEFINITION] Definition: Coordinate Representation of a Function
>
>Let $f: M \to \mathbb{R}^n$ be a [[Functions of the Real Numbers|real vector-valued function]] on a $k$-[[Manifolds|manifold]] $M$ and let $(U, \phi)$ be a [[index|chart]] for $M$.
>
>The **coordinate representation** of $f$ on $(U, \phi)$ is the [[Functions of the Real Numbers|real vector function]] ${}_{(U, \phi)}f: \phi(U) \subseteq \mathbb{R}^k \to \mathbb{R}^n$ obtained by the [[Functions of the Real Numbers|compositions]] of $f$ and the [[Injections, Surjections and Bijections|inverse]] of $\phi$.
>
>$$
>{}_{(U, \phi)}f \overset{\text{def}}{=} f \circ \phi^{-1}
>$$
>
>>[!INTUITION]+
>>
>>Although all points on a chart can be uniquely represented by their coordinates, the $f$ does not act on coordinates - it acts on points. Hence, we need a way to convert coordinates to the points they represent before $f$ can be used. This is precisely what $\phi^{-1}$ does. If we are given coordinates $(p^1, \dotsc, p^k)$, we can pass them to $\phi^{-1}$ to obtain the point $p \in U$ which they represent. After having converted the coordinates $(p^1, \dotsc, p^k)$ to the point $p$, we can invoke $f$, i.e. we can obtain the value $f(p)$.
>>
>>The coordinate representation ${}_{(U, \phi)}f$ does all of this in one single step. It takes coordinates $(p^1, \dotsc, p^k)$, converts them to the point $p$ which they represent and then returns the value of $f$ at $p$. 
>>
>