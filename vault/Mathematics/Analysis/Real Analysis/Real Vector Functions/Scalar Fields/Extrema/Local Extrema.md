>[!DEFINITION] Definition: Local Minimum
>Let $f: D\subseteq\mathbb{R}^n\to\mathbb{R}$ be a [[Real Scalar Field]].
>
>We say that $f(\vec{x}_0)$ is a **local minimum** of $f$ if there is an [[index|open ball]] $B_\varepsilon (\vec{x}_0)$ around $\vec{x}_0\in D$ where $f(\vec{x}_0)$ is the smallest funtional value.
>
>$$f(\vec{x}_0) \le f(\vec{x}) \qquad \forall \vec{x}\in B_\varepsilon (\vec{x}_0)$$
>
>We say that $\vec{x}_0$ is a **place of a local minimum** for $f$.
>

>[!DEFINITION] Definition: Global Maximum
>Let $f: D\subseteq\mathbb{R}^n\to\mathbb{R}$ be a [[Real Scalar Field]].
>
>We say that $f(\vec{x}_0)$ is a **local maximum** of $f$ if there is an [[index|open ball]] $B_\varepsilon (\vec{x}_0)$ around $\vec{x}_0\in D$ where $f(\vec{x}_0)$ is the greatest funtional value.
>
>$$f(\vec{x}_0) \ge f(\vec{x}) \qquad \forall \vec{x}\in B_\varepsilon (\vec{x}_0)$$
>
>We say that $\vec{x}_0$ is a **place of a local maximum** for $f$.
>

>[!DEFINITION] Definition: Local Extremum
>
>The [[Local Extrema|local minima]] and [[Local Extrema|local maxima]] of a [[Real Scalar Field]] are collectively known as its **local extrema**.
>

>[!THEOREM] Theorem: Finding Local Extrema
>
>Let $f: \mathcal{D} \to \mathbb{R}$ be a [[Real Scalar Field]].
>
>If $f$ has a [[Local Extrema|local extremum]] at $\mathbf{a} \in \mathcal{D}$, then $\mathbf{a}$ is a [[Critical Point]] of $f$.
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Hessian Matrix Criteria for Local Extrema
>
>Let $f: \mathcal{D} \subseteq \mathbb{R}^n \to \mathbb{R}$ be a [[Real Scalar Field]] which is [[Partial Derivatives of Real Scalar Fields|twice continuously partially differentiable]] in [[Cartesian Coordinate System|Cartesian coordinates]] on an [[The Topology of Euclidean Space|open subset]] $\mathcal{D} \subseteq \mathbb{R}^n$.
>
>A [[Critical Point]] $\mathbf{p} \in \mathcal{D}$ is:
>- a place of a [[Local Extrema|local maximum]] if the [[Hessian Matrix]] $H_f(\mathbf{p})$ is [[Definiteness of Real Symmetric Matrices|negative-definite]];
>- a place of a [[Local Extrema|local minimum]] if the [[Hessian Matrix]] $H_f(\mathbf{p})$ is [[Definiteness of Real Symmetric Matrices|positive-definite]];
>- a place of a [[Saddle Point]] if the [[Hessian Matrix]] $H_f(\mathbf{p})$ is [[Definiteness of Real Symmetric Matrices|indefinite]];
>
>
>If the [[Hessian Matrix]] $H_f(\mathbf{p})$ is [[Definiteness of Real Symmetric Matrices|semi-definite]], then it cannot be used to make any predictions.
>
>>[!PROOF]-
>>
>>TODO
>>
>
