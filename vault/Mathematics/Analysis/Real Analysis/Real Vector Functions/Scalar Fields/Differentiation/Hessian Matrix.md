>[!DEFINITION] Definition: Hessian Matrix
>
>Let $f: \mathcal{D} \subseteq \mathbb{R}^n \to \mathbb{R}$ be a [[Partial Derivatives of Real Scalar Fields|twice partially differentiable]] [[Real Scalar Field]].
>
>The **Hessian matrix** of $f$ is the $n \times n$-[[Square Matrix|matrix]] $H_f$ whose columns are the [[Gradient|gradients]] of $f$'s first order [[Partial Derivatives of Real Scalar Fields|partial derivatives]]:
>
>$$
>H_f \overset{\text{def}}{=} \begin{bmatrix}\vert & \vert & \vert \\ \nabla(\partial_1 f) & \cdots & \nabla(\partial_n f) \\ \vert & \vert & \vert \end{bmatrix} = \begin{bmatrix}\partial_1 \partial_1 f & \cdots & \partial_1\partial_n f \\ \vdots & \ddots & \vdots \\ \partial_n\partial_1 f & \cdots & \partial_n\partial_n f\end{bmatrix}
>$$
>
>>[!NOTATION]-
>>
>>The [[Hessian Matrix]] $H_f$ is different for different $\mathbf{x} \in \mathcal{D}$, since the [[Partial Derivatives of Real Scalar Fields|partial derivatives]] of $f$ depend on $\mathbf{x}$. The [[Hessian Matrix]] at a given $\mathbf{x}_0$ is thus denoted as $H_f(\mathbf{x}_0)$ to make this dependency apparent.
>>
>

>[!THEOREM] Theorem: Symmetry of the Hessian Matrix
>
>Let $f: D \subseteq \mathbb{R}^n \to \mathbb{R}$ be a [[Partial Derivatives of Real Scalar Fields|twice partially differentiable]] [[Real Scalar Field]].
>
>If all [[Partial Derivatives of Real Scalar Fields|second partial derivatives]] of $f$ are also [[Continuity of Real Scalar Fields|continuous]], then the [[Hessian Matrix]] of $f$ is [[Symmetric Matrix|symmetric]] for every $\mathbf{x} \in D$.
>
>>[!PROOF]-
>>
>>This follows directly from [[Symmetry of Second Derivatives|Schwarz's theorem]].
>>
>