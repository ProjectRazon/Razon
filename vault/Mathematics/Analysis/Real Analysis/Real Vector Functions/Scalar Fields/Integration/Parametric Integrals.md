


>[!DEFINITION] Definition: Parametric Integrals
>
>Let $f: D \to \mathbb{R}$ be a [[Real Scalar Field]] on a [[TODO|rectangle]] $D = [a;b] \times [c;d]$.
>
>>[!DEFINITION] Definition: Parametric Integral (Type I)
>>
>>Given two [[Functions of the Real Numbers|real functions]] $l,u: [a;b] \to [c;d]$, we define a **parametric integral** $\mathcal{X}: [a;b] \to \mathbb{R}$ as
>>
>>$$
>>\mathcal{X}(x) \overset{\text{def}}{=} \int_{l(x)}^{u(x)} f(x, y) \mathop{\mathrm{d}y}
>>$$
>>
>>>[!NOTE] Note
>>>
>>>For any particular value $x^\ast$ of $x$, the functions $l$ and $u$ result in concrete real numbers $l(x^\ast)$ and $u(x^\ast)$ and the expression $f(x^\ast, y)$ is a concrete [[Functions of the Real Numbers|real function]] of $y$.
>>>
>>
>>>[!EXAMPLE]-
>>>
>>>For $x = 3$, we get
>>>
>>>$$
>>>\mathcal{X}(3) = \int_{l(3)}^{u(3)} f(3,y) \mathop{\mathrm{d}y},
>>>$$
>>>
>>>which is just a regular [[Definite Integrals|definite integral]].
>>>
>>
>
>>[!DEFINITION] Definition: Parametric Integral (Type II)
>>
>>Given two [[Functions of the Real Numbers|real functions]] $l,u: [c;d] \to [a;b]$, we define a **parametric integral** $\mathcal{Y}: [c;d] \to \mathbb{R}$ as
>>
>>$$
>>\mathcal{Y}(y) \overset{\text{def}}{=} \int_{l(y)}^{u(y)} f(x, y) \mathop{\mathrm{d}x}
>>$$
>>
>>>[!NOTE] Note
>>>
>>>For any particular value $y^\ast$ of $y$, the functions $l$ and $u$ result in concrete real numbers $l(y^\ast)$ and $u(y^\ast)$ and the expression $f(x, y^\ast)$ is a concrete [[Functions of the Real Numbers|real function]] of $x$.
>>>
>>
>>>[!EXAMPLE]-
>>>
>>>For $y = 3$, we get
>>>
>>>$$\mathcal{Y}(3) = \int_{l(3)}^{u(3)} f(x,3) \mathop{\mathrm{d}x},$$
>>>
>>>which is just a regular [[Definite Integrals|definite integral]].
>>>
>>
>

>[!THEOREM] Theorem: Continuity of Parametric Integrals
>
>Let $f: R \subset \mathbb{R}^2 \to \mathbb{R}$ be a [[Real Scalar Field]] on some [[TODO|rectangle]] $R = [a;b] \times [c;d]$.
>
>If $f$ is [[Continuity of Real Scalar Fields|continuous]] on $R$, then:
>- the [[Parametric Integrals|parametric integral]] $\int_c^d f(x,y)\mathop{\mathrm{d}y}$ is [[Continuity|continuous]] on $[a;b]$.
>- the [[Parametric Integrals|parametric integral]] $\int_a^b f(x,y)\mathop{\mathrm{d}x}$ is [[Continuity|continuous]] on $[c;d]$.
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Leibniz Integral Rule
>
>Let $f: R \subset \mathbb{R}^2 \to \mathbb{R}$ be a [[Real Scalar Field]] on some [[TODO|rectangle]] $R = [a;b] \times [c;d]$.
>
>If $f$ is [[Partial Derivatives of Real Scalar Fields|continuously partially differentiable]] and $l,u$ are [[Differentiability|continuously differentiable]], then the [[Differentiability|derivatives]] of $f$'s [[Parametric Integrals]] are given by
>
>$$
>\frac{\mathrm{d}}{\mathrm{d}x} \int_{l(x)}^{u(x)} f(x,y) \mathop{\mathrm{d}y} = \int_{l(x)}^{u(x)} \frac{\partial}{\partial x}f(x,y)\mathop{\mathrm{d}y} \,+\, f(x,u(x))\frac{\mathrm{d}}{\mathrm{d}x}u(x) - f(x, l(x))\frac{\mathrm{d}}{\mathrm{d}x}l(x)
>$$
>
>
>$$
>\frac{\mathrm{d}}{\mathrm{d}y} \int_{l(y)}^{u(y)} f(x,y) \mathop{\mathrm{d}x} = \int_{l(y)}^{u(y)} \frac{\partial}{\partial y}f(x,y)\mathop{\mathrm{d}x} \,+\, f(u(y), y)\frac{\mathrm{d}}{\mathrm{d}y}u(y) - f(l(y), y)\frac{\mathrm{d}}{\mathrm{d}x}l(y)
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>