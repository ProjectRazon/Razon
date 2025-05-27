>[!TIP] Tip: Limit of a Real Scalar Field
>
>Let $f: \mathcal{D} \subseteq \mathbb{R}^n \to \mathbb{R}$ be a [[Real Scalar Field]] and let $\mathbf{a} \in \mathbb{R}^n$ be an [[Accumulation Point]] of $\mathcal{D}$.
>
>A number $L \in \mathbb{R}$ is the [[Limits of Real Vector Functions|limit]] of $f$ for $\mathbf{x} \to \mathbf{a}$ iff for each $\varepsilon \gt 0$ there exists some [[index|open ball]] $B_{\delta}(\mathbf{a})$ around $\mathbf{a}$ such that for all $\mathbf{x} \in \mathcal{D}$
>
>$$
>\mathbf{x} \in B_{\delta}(\mathbf{a}) \implies |f(\mathbf{x}) - L| \lt \varepsilon
>$$
>
>>[!NOTATION]-
>>
>>$$
>>\lim_{\mathbf{x}\to \mathbf{a}} f(\mathbf{x}) = L
>>$$
>>
>

>[!THEOREM] Theorem: Algebraic Properties
>
>Let $f, g: \mathcal{D} \subseteq \mathbb{R}^n \to \mathbb{R}$ be [[Real Scalar Field|real scalar fields]].
>
>If the [[Limits of Real Scalar Fields|limits]] of $f$ and $g$ for $\mathbf{x} \to \mathbf{a}$ exist, then
>
>$$
>\lim_{\mathbf{x} \to \mathbf{a}} [f(\mathbf{x}) g(\mathbf{x})] = \left(\lim_{\mathbf{x} \to \mathbf{a}} f(\mathbf{x}) \right) \cdot \left( \lim_{\mathbf{x} \to \mathbf{a}} g(\mathbf{x}) \right)
>$$
>
>Furthermore, if $g(\mathbf{x}) \ne 0$ for all $\mathbf{x} \in \mathcal{D}$ and $\displaystyle \lim_{\mathbf{x} \to \mathbf{a}} g(\mathbf{x}) \ne 0$, then
>
>$$
>\lim_{ \mathbf{x} \to \mathbf{a} } \frac{ f(\mathbf{x}) }{ g(\mathbf{x}) } = \frac{ \displaystyle \lim_{ \mathbf{x} \to \mathbf{a} } f(\mathbf{x}) }{ \displaystyle \lim_{ \mathbf{x} \to \mathbf{a} } g(\mathbf{x}) }
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>