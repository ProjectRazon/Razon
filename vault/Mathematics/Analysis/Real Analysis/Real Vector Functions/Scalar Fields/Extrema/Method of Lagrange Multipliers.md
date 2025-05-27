# Lagrange Multipliers

Lagrange multipliers allow us to determine if a [[Real Scalar Field|function]] subject to some [[Constraints]] has [[Local Extrema]].

>[!THEOREM] Theorem: Lagrange Multipliers
>
>Let $f: \mathcal{D} \subseteq \mathbb{R}^n \to \mathbb{R}$ be a [[Partial Derivatives of Real Scalar Fields|continuously partially differentiable]] [[Real Scalar Field]] and let
>
>$$
>\begin{align*}
>
>g_1(\mathbf{x}) &= c_1 \\
>
>&\vdots \\
>
>g_k(\mathbf{x}) &= c_k
>
>\end{align*}
>$$
>
>be some [[Constraints#^equality-constraint|constraints]], where $g_1, \dotsc, g_k: \mathcal{D} \to \mathbb{R}$ are also [[Partial Derivatives of Real Scalar Fields|continuously partially differentiable]], and let $S \{\mathbf{x} \mid g_1(\mathbf{x}) = c_1 \text{ and } \cdots \text{ and } g_k(\mathbf{x}) = c_k\}$.
>
>If $f\big|_S$ has a [[Extrema|local extremum]] at $\mathbf{a}$ and the [[Gradient|gradients]] $\nabla g_1(\mathbf{a}), \dotsc, \nabla g_k(\mathbf{a})$ are [[Linear Independence|linearly independent]], then $\nabla f(\mathbf{a})$ is a [[Linear Combination]] of $\nabla g_1(\mathbf{a}), \dotsc, \nabla g_k(\mathbf{a})$.
>
>>[!PROOF]-
>>
>>TODO
>>
>
>>[!DEFINITION] Definition: Lagrange Multipliers
>>
>>The coefficients $\lambda_1, \dotsc, \lambda_k$ in the representation 
>>
>>$$
>>\nabla f(\mathbf{a}) = \lambda_1 \nabla g_1(\mathbf{a}) + \cdots + \lambda_k \nabla g_k(\mathbf{a})
>>$$
>>
>>of $\nabla f(\mathbf{a})$ as a [[Linear Combination]] of $\nabla g_1(\mathbf{a}), \dotsc, \nabla g_k(\mathbf{a})$ are known as **Lagrange multipliers**.
>>
>

>[!EXAMPLE]-
>
>TODO
>