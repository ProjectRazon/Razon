>[!DEFINITION] Definition: Jacobian Matrix
>
>Let $f: \mathcal{D} \subseteq \mathbb{R}^m \to \mathbb{R}^n$ be a [[Partial Derivatives of Real Vector Functions|partially differentiable]] [[Functions of the Real Numbers|real vector function]] with [[Functions of the Real Numbers|component functions]] $f_1,\cdots,f_n$.
>
>The **Jacobian matrix** of $f$ is the $n \times m$-[[Square Matrix|matrix]] whose rows are the [[Gradient|gradients]] of $f_1,\cdots,f_n$:
>
>$$
>\begin{bmatrix} - & (\nabla f_1)^\mathsf{T} & - \\ - & \vdots & - \\ - & (\nabla f_n)^\mathsf{T} & - \end{bmatrix}
>$$
>
>>[!NOTATION]-
>>
>>$$
>>Df \qquad J_f \qquad \mathbf{J}_f
>>$$
>>
>>The coefficients of the [[Jacobian Matrix]] are real numbers and are different for different $\mathbf{x} \in \mathcal{D}$, since the [[Partial Derivatives of Real Vector Functions|partial derivatives]] of $f$ depend on $\mathbf{x}$. To make this clear, the [[Jacobian Matrix]] at a particular $\mathbf{x}_0 \in \mathcal{D}$ is denoted as $Df(\mathbf{x}_0)$.
>>
>