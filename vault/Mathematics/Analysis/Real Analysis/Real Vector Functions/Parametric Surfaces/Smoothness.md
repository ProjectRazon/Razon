---
title: Smoothness of Parametric Surfaces
---


>[!DEFINITION] Definition: Smoothness of Parametric Surfaces
>
>Let $s: \mathcal{D} \subseteq \mathbb{R}^2 \to \mathbb{R}^3$ be a [[Parametric Surface]].
>
>We say that $s$ is **smooth at** $\mathbf{a}$ iff it is [[Differentiability of Real Vector Functions|differentiable]] there and its [[Surface Normal Vector|normal vector]] at $\mathbf{a}$ is nonzero.
>
>If $s$ is smooth at every $\mathbf{x}$ in some $S \subseteq \mathbb{R}^2$, then we say that $s$ is **smooth on** $S$. If $S = \mathcal{D}$, then we just say that $s$ is **smooth**.
>

>[!DEFINITION] Definition: Piecewise Smoothness
>
>A **piecewise smooth parametric surface** is a [[Functions of the Real Numbers|function]] $\phi: \mathcal{D} \subseteq \mathbb{R}^2 \to \mathbb{R}^3$ such that $\mathcal{D}$ can be represented as the [[Operations with Collections|union]] of finitely many [[Disjoint Sets]] $\mathcal{D}_1, \dotsc, \mathcal{D}_k$ and $\phi$ can be represented as
>
>$$
>\phi (\mathbf{x}) = 
>\begin{cases}
>
>s_1(\mathbf{x}) \qquad \text{ if } \mathbf{x} \in \mathcal{D}_1 \\
>
>\vdots \\
>
>s_k(\mathbf{x}) \qquad \text{ if } \mathbf{x} \in \mathcal{D}_k
>
>\end{cases}
>$$
>
>where $s_1: \mathcal{D}_1 \to \mathbb{R}^3, \dotsc, s_k: \mathcal{D}_k \to \mathbb{R}^3$ are [[Parametric Surface|parametric surfaces]] which are [[Smoothness|smooth]] except at possibly finitely many places.
>