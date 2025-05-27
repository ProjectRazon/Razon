>[!THEOREM] Gradient Theorem (Fundamental Theorem of Analysis for Line Integrals)
>
>If $\boldsymbol{v}: D \to \mathbb{R}^n$ is the  [[Conservative Vector Field|gradient field]] of a [[Real Scalar Field|scalar field]] $f: D\to\mathbb{R}$ on an [[index#^opensets|open subset]] $D \subseteq \mathbb{R}^n$, then its [[Vector Line Integrals|line integral]] over a [[Differentiability of Parametric Curves|piecewise continuously differentiable]] [[Parametric Curve|curve parameterisation]] $\gamma: [a;b] \to D$ can be calculated as
>
>$$
>\int_\gamma \boldsymbol{v} \cdot \mathop{\mathrm{d}\boldsymbol{s}} = f(\gamma (b)) - f(\gamma (a))
>$$
>
>>[!PROOF]-
>>
>>By definition
>>
>>$$
>>\int_\gamma \boldsymbol{v} \cdot \mathop{\mathrm{d}\boldsymbol{s}} = \int_a^b \boldsymbol{v}(\gamma(t)) \cdot \gamma'(t) \mathop{\mathrm{d}t} = \int_a^b \nabla  f(\gamma(t)) \cdot \gamma'(t) \mathop{\mathrm{d}t}
>>$$
>>
>>The [[Differentiation Rules for Scalar Fields#^chainrule|chain rule for scalar fields]] tells us that the integrand is the derivative of $f(\gamma (t))$:
>>
>>$$
>>\frac{\mathrm{d}}{\mathrm{d}t} f(\gamma (t)) = \nabla  f(\gamma(t)) \cdot \gamma'(t)
>>$$
>>
>>$$
>>\int_a^b \nabla  f(\gamma(t)) \cdot \gamma'(t) \mathop{\mathrm{d}t} = \int_a^b \frac{\mathrm{d}}{\mathrm{d}t} f(\gamma (t)) \mathop{\mathrm{d}t}
>>$$
>>
>>The [[The Fundamental Theorem of Real Analysis|fundamental theorem of real analysis]] then gives us
>>
>>$$
>>\int_a^b \frac{\mathrm{d}}{\mathrm{d}t} f(\gamma (t)) \mathop{\mathrm{d}t} = f(\gamma(t))\Big|_a^b = f(\gamma(b)) - f(\gamma(a))
>>$$
>>
>

>[!THEOREM] Theorem: Path Independence of Line Integrals of Conservative Vector Fields
>
>A [[Real Vector Field]] $\boldsymbol{v}: D\subseteq \mathbb{R}^n \to \mathbb{R}^n$ is [[Conservative Vector Field|conservative]] if and only if its [[Vector Line Integrals|line integrals]] over all [[Curves|simple curves]] with [[Partial Derivatives of Real Vector Functions|piecewise continuously differentiable]] [[Curves|reparameterisations]] $\gamma_1: [a;b] \to \mathbb{R}^n$ and $\gamma_2: [a;b] \to \mathbb{R}^n$ (i.e. $\gamma_1(a) = \gamma_2(a)$ and $\gamma_1(b) = \gamma_2(b)$) are equal.
>
>$$
>\int_{\gamma_1} \boldsymbol{v}\cdot \mathop{\mathrm{d}\boldsymbol{s}} = \int_{\gamma_2} \boldsymbol{v}\cdot \mathop{\mathrm{d}\boldsymbol{s}}
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Line Integrals of Conservative Vector Fields over Closed Curves
>
>A [[Continuity of Real Vector Functions|continuous]] [[Real Vector Field|vector field]] $\boldsymbol{v}: D\subseteq \mathbb{R}^n \to \mathbb{R}^n$ is [[Conservative Vector Field|conservative]] if and only if its [[Vector Line Integrals|line integral]] over every [[Curves|closed curve]] $\mathcal{C} \subseteq D$ is always zero.
>
>$$
>\oint_\mathcal{C} \boldsymbol{v} \cdot \mathop{\mathrm{d}\boldsymbol{s}} = 0
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>