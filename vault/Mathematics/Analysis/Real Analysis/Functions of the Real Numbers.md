---
title: Functions of the Real Numbers
tags:
  - real-analysis
  - mathematics
  - real-functions
  - analysis
  - vector-analysis
---

# Real-Valued Functions

>[!DEFINITION] Definition: Real-Valued Function
>
>A **real-valued function** is a [[Functions|function]] whose [[Functions|codomain]] are the [[The Real Numbers|real numbers]].
>

>[!DEFINITION] Definition: Operations with Real-Valued Functions
>
>Let $f: \mathcal{D}_f \to \mathbb{R}$ and $g: \mathcal{D}_g \to \mathbb{R}$ be [[Functions of the Real Numbers|real-valued functions]].
>
>We define
>- the **sum** of $f$ and $g$ as $f + g: \mathcal{D}_f \cap \mathcal{D}_g \to \mathbb{R}$ with $(f+g)(x) = f(x) + g(x)$;
>- the **difference** $f - g: \mathcal{D}_f \cap \mathcal{D}_g \to \mathbb{R}$ with $(f-g)(x) = f(x) - g(x)$;
>- the **product** of $f$ and $g$ as $fg: \mathcal{D}_f \cap \mathcal{D}_g \to \mathbb{R}$ with $(fg)(x) = f(x) g(x)$;
>- the **quotient** $f/g: \mathcal{D} \to \mathbb{R}$ with $\mathcal{D} = \{x \in \mathcal{D}_f \cap \mathcal{D}_g \mid g(x) \ne 0\}$ and $(f/g)(x) = \frac{f(x)}{g(x)}$.
>

## Real Functions

>[!DEFINITION] Definition: Real Function
>
>A **real function** is a [[Functions of the Real Numbers|real-valued function]] whose [[Functions|domain]] is a [[Subsets|subset]] of the [[The Real Numbers|real numbers]]:
>
>$$
>f: \mathcal{D} \subseteq \mathbb{R} \to \mathbb{R}
>$$
>

# Real Vector-Valued Functions

>[!DEFINITION] Definition: Real Vector-Valued Function
>
>A **real vector-valued function** $f: D \to \mathbb{R}^n$ is a [[Functions|function]] from an arbitrary [[Sets|set]] $D$ to the [[Real Vector|real vector space]] $\mathbb{R}^n$.
>
>>[!NOTE] Note: Component Functions
>>
>>Every **real vector-valued function** $f: D \to \mathbb{R}^n$ can be described by $n$ [[Functions of the Real Numbers|real-valued functions]] $f_1, \dotsc, f_n: \mathcal{D} \to \mathbb{R}^n$, where $f_k$ is responsible for the $k$-th component of the resulting [[Real Vector|vector]]:
>>
>>$$
>>f(x) = \begin{bmatrix}f_1(x) \\ \vdots \\ f_n(x) \end{bmatrix}
>>$$
>>
>>Hence, $f_1, \dotsc, f_n$ are called the **component functions** of $f$.
>>
>

## Real Vector Functions

>[!DEFINITION] Definition: Vector Function
>
>A **vector function** $f: \mathcal{D} \subseteq \mathbb{R}^m \to \mathbb{R}^n$ is a [[Functions of the Real Numbers|real vector-valued function]] whose [[Functions|domain]] $\mathcal{D}$ is a [[Sets|subset]] of a [[Structure of the Real Vector Space|real vector space]] $\mathbb{R}^m$.
>
>>[!NOTATION]- Notation: Multivariate Notation and Coordinate Representations
>>
>>Strictly speaking, a [[Real Vector Function]] $f$ takes a [[Real Vector|vector]] $\mathbf{p} \in \mathcal{D} \subseteq \mathbb{R}^m$ and outputs another vector $f(\mathbf{p}) \in \mathbb{R}^n$. However, since vectors live as a [[Euclidean Geometry|points]] in [[The Topology of Euclidean Space|Euclidean space]], they can be uniquely represented by [[index|coordinates]].
>>
>>Although the action of $f$ is independent of the choice of [[index|coordinate systems]] for $\mathbb{R}^m$ and $\mathbb{R}^n$ ($\mathbf{p}$ and $f(\mathbf{p})$ are the same vectors, regardless of how we choose to represent them), many definitions involving $f$, such as differentiability and integrability, *do* depend on the choice of a [[index|coordinate system]] for the input space $\mathbb{R}^m$. Indeed, it would be more appropriate to formulate such definitions about the [[Coordinate Representation of Functions|coordinate representations]] of $f$ in the chosen coordinate systems. However, this formality gets very cumbersome very quickly.
>>
>>Hence, if the coordinates of $\mathbf{p}$ in a given coordinate system $\phi$ are $p^1, \dotsc, p^n$, then instead of writing ${}_{(\mathbb{R}^m, \phi)}f(p^1,\dotsc,p^m)$ for the coordinate representation of $f$, we can just write $f(p^1,\dotsc,p^m)$, as long as it is clear which coordinate system we are using. If there is no particular coordinate system specified, then we usually assume that those are [[Cartesian Coordinate System|Cartesian coordinates]].
>>
>>This is why vector functions are often called **multivariate functions**.
>>
>
>>[!NOTE] Note: Component Functions
>>
>>The [[Functions of the Real Numbers|component functions]] of $f$ are [[Real Scalar Field|real scalar fields]].
>>
>

