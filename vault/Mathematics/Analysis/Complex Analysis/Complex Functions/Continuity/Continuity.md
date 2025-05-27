---
title: Continuity of Complex Functions
tags:
    - continuity
    - complex-functions
    - complex-analysis
    - analysis
    - mathematics
---

# Continuity

>[!DEFINITION] Definition: Continuity of Complex Functions
>
>A [[Complex Functions|complex function]] $f: \mathcal{D} \subseteq \mathbb{C} \to \mathbb{C}$ is **continuous at** $c \in \mathcal{D}$ iff its [[Limits|limit]] for $z \to c$ is equal to its value there.
>
>$$
>\lim_{z \to c} f(z) = f(c)
>$$
>

## Discontinuities

>[!DEFINITION] Definition: Point of Discontinuity
>
>If a [[Complex Functions|complex function]] $f$ is *not* [[Continuity|continuous]] at $c \in \mathbb{C}$, then we call $c$ a **point of discontinuity**.
>

>[!DEFINITION] Definition: Removable Discontinuity
>
>Let $f$ be a [[Complex Functions|complex function]]
>
>A [[Continuity#Discontinuities|point of discontinuity]] $c \in \mathbb{C}$ is a **removable discontinuity** if the [[Limits|limit]] $\lim_{z \to c} f(z)$ exists, but $f$ is not defined at $c$.
>

# Properties

>[!THEOREM]- Theorem: Continuity of the Real and Imaginary Parts
>
>Let $f: \mathcal{D} \subseteq \mathbb{C} \to \mathbb{C}$ be a [[Complex Functions|complex function]]. 
>
>If $f$ is [[Continuity|continuous]] at $z_0 \in \mathbb{C}$, then its [[Complex-Valued Functions|real]] $\operatorname{Re} f$ and [[Complex-Valued Functions|imaginary]] part $\operatorname{Im} f$ are also [[Continuity|continuous]] there.
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM]- Theorem: Continuity of Sum, Product and Division
>
>Let $f$ and $g$ be [[Complex Functions]].
>
>If $f$ and $g$ are [[Continuity|continuous]] at $c \in \mathbb{C}$, then so are
>- $\lambda f + \mu g$ for all $\lambda, \mu \in \mathbb{C}$;
>- $fg$;
>- $f/g$, provided that $g(c) \ne 0$.
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM]- Theorem: Continuity of Composition
>
>Let $f$ and $g$ be [[Complex Functions]].
>
>If $g$ is [[Continuity|continuous]] at $c \in \mathbb{C}$ and $f$ is [[Continuity|continuous]] at $g(c)$, then their [[Composition]] $f\circ g$ is also [[Continuity|continuous]] at $c$.
>
>>[!PROOF]-
>>
>>TODO
>>
>

# Bibliography

1. N. H. Asmar, L. Grafakos, "Analytic Functions," in *Complex Analysis with Applications*, Columbia, MO, USA: Springer, 2018