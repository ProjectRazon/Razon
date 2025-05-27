
>[!THEOREM] Theorem: Gradient
>
>Let $f: \mathcal{D} \subseteq \mathbb{R}^n \to \mathbb{R}$ be a [[Real Scalar Field]] and let $\mathbf{a} \in \mathcal{D}$.
>
>If $f$'s [[Directional Derivatives of Real Scalar Fields|directional derivative]] $\partial_{\hat{\mathbf{r}}}f(\mathbf{a})$ along every direction $\hat{\mathbf{r}}$ exists at $\mathbf{a}$, then there exists a unique [[Real Vector|vector]] $\nabla f(\mathbf{a})$, which depends on $\mathbf{a}$ but not on $\hat{\mathbf{r}}$, such that $\partial_{\hat{\mathbf{r}}}f(\mathbf{a})$ is the [[Real Dot Product|dot product]] of $\nabla f(\mathbf{a})$ and $\hat{\mathbf{r}}$:
>
>$$
>(\nabla f(\mathbf{a})) \cdot \hat{\mathbf{r}} = \partial_{\hat{\mathbf{r}}}f(\mathbf{a})
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>
>>[!DEFINITION] Definition: Gradient
>>
>>The [[Real Vector|vector]] $\nabla f(\mathbf{a})$ is known as the **gradient** of $f$ at $\mathbf{a} \in \mathcal{D}$.
>>
>>>[!INTUITION]-
>>>
>>>The gradient at $\mathbf{a}$ shows the directions in which small deviations from $\mathbf{a}$ result in the largest increase and the largest decrease in the value of $f$:
>>>- An infinitesimally small deviation from $\mathbf{a}$ in the direction of $\nabla f(\mathbf{a})$ will result in the greatest possible increase in the value of $f$. If the deviation from $\mathbf{a}$ is in any other direction, then the increase in the value of $f$ will necessarily be smaller (closer to 0).
>>>- An infinitesimally small deviation from $\mathbf{a}$ in the direction of $- \nabla f(\mathbf{a})$ will result in the greatest possible decrease in the value of $f$. If the deviation from $\mathbf{a}$ is in any other direction, then the decrease in the value of $f$ will necessarily be smaller (closer to 0).
>>>
>>
>>>[!NOTATION]-
>>>
>>>$$
>>>\nabla f(\mathbf{a}) \qquad \operatorname{grad} f(\mathbf{a})
>>>$$
>>>
>>
>>>[!NOTE] Note: Gradient as a Function
>>>
>>>If there is no specific $\mathbf{a}$ mentioned, then the term "gradient" usually refers to the entire [[Real Vector Field|vector field]] $\nabla f: \mathcal{D} \to \mathbb{R}^n$ which to each $\mathbf{a}$ assigns $\nabla f(\mathbf{a})$.
>>>
>>
>

>[!THEOREM] Theorem: Gradient in Cartesian Coordinates
>
>Let $f: \mathcal{D} \subseteq \mathbb{R}^n \to \mathbb{R}$ be a [[Real Scalar Field]].
>
>If $f$ is [[Partial Differentiability of Real Scalar Fields|partially differentiable]] with respect to [[Cartesian Coordinate System|Cartesian coordinates]] at $\mathbf{a}$, then the components of its [[Gradient]] there are precisely its [[Partial Derivatives of Real Scalar Fields|partial derivatives]] with respect to [[Cartesian Coordinate System|Cartesian coordinates]] at $\mathbf{a}$:
>
>$$
>\nabla f(\mathbf{a}) = \begin{bmatrix}\frac{\partial f}{\partial x^1} (\mathbf{a}) \\ \vdots \\ \frac{\partial f}{\partial x^n}(\mathbf{a}) \end{bmatrix}
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>