>[!THEOREM] Theorem: Chain Rule for Scalar Fields
>
>Let $f: D \subseteq \mathbb{R}^n \to \mathbb{R}$ be a [[Real Scalar Field]] and let $\mathbf{r}: [a;b] \to D$ be a [[Parametric Curve|curve parameterisation]]. 
>
>If $\mathbf{r}$ is [[Differentiability of Parametric Curves|differentiable]] and $f$ is [[Partial Derivatives of Real Scalar Fields|partially differentiable]], then the [[Differentiability|derivative]] of the [[Composition]] $f \circ \mathbf{r}$ is the [[Real Dot Product|dot product]] of $f$'s [[Gradient]] and $\mathbf{r}$'s derivative.
>
>$$\frac{\mathrm{d}}{\mathrm{d}t} f(\mathbf{r}(t)) = \nabla f(\mathbf{r}(t))\cdot \mathbf{r}'(t)$$
>
>>[!NOTE]
>>
>>The composition $f\circ\mathbf{r}$ is a [[Functions of the Real Numbers|real function]].
>>
>
>>[!PROOF]-
>>
>>TODO
>>
>
>^chainrule
>

>[!THEOREM] Theorem: Product Rule
>
>Let $f, g: \mathcal{D} \subseteq \mathbb{R}^n \to \mathbb{R}$ be [[Real Scalar Field|real scalar fields]].
>
>If $f$ and $g$ are [[Differentiability|differentiable]] at $\mathbf{a} \in \mathcal{D}$, then the product $fg: \mathcal{D} \subseteq \mathbb{R}^n \to \mathbb{R}$ is also [[Differentiability|differentiable]] at $\mathbf{a} \in \mathcal{D}$ with
>
>$$
>\mathop{\mathrm{d}(fg)_{\mathcal{a}}} = g(\mathcal{a})\mathop{\mathrm{d}f_{\mathcal{a}}} + f(\mathcal{a})\mathop{\mathrm{d}g_{\mathcal{a}}}
>$$
>
>>[!IMPORTANT]
>>
>>You should remember that $\mathrm{d}(fg)_{\mathcal{a}}$ is a *function* and so are $\mathop{\mathrm{d}f_{\mathcal{a}}}$ and $\mathop{\mathrm{d}g_{\mathcal{a}}}$
>>
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Quotient Rule
>
>Let $f, g: \mathcal{D} \subseteq \mathbb{R}^n \to \mathbb{R}$ be [[Real Scalar Field|real scalar fields]].
>
>If $f$ and $g$ are [[Differentiability|differentiable]] at $\mathbf{a} \in \mathcal{D}$ and $g(\mathcal{a}) \ne 0$, then the quotient $f/g: \mathcal{D} \subseteq \mathbb{R}^n \to \mathbb{R}$ is also [[Differentiability|differentiable]] at $\mathbf{a} \in \mathcal{D}$ with
>
>$$
>\mathop{\mathrm{d}(f/g)_{\mathcal{a}}} = \frac{g(\mathcal{a})\mathop{\mathrm{d}f_{\mathcal{a}}} - f(\mathcal{a})\mathop{\mathrm{d}g_{\mathcal{a}}}}{g(\mathcal{a})^2}
>$$
>
>>[!IMPORTANT]
>>
>>You should remember that $\mathrm{d}(f/g)_{\mathcal{a}}$ is a *function* and so are $\mathop{\mathrm{d}f_{\mathcal{a}}}$ and $\mathop{\mathrm{d}g_{\mathcal{a}}}$
>>
>
>>[!PROOF]-
>>
>>TODO
>>
>