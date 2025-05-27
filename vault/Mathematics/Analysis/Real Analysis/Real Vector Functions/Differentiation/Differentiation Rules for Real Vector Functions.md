>[!THEOREM] Theorem: Linearity of Differentiation
>
>Let $f,g: \mathcal{D} \subseteq \mathbb{R}^m \to \mathbb{R}^n$ be [[Functions of the Real Numbers|real vector functions]].
>
>If $f$ and $g$ are both [[Differentiability of Real Vector Functions|differentiable]] at $\mathbf{a} \in \mathcal{D}$, then for all $\lambda, \mu \in \mathbb{R}$, the [function] $\lambda f + \mu g$ is also [[Differentiability of Real Vector Functions|differentiable]] there with
>
>$$
>\mathop{\mathrm{d}(\lambda f + \mu g)_{\mathbf{a}}} = \lambda \mathop{\mathrm{d}f_{\mathbf{a}}} + \mu \mathop{\mathrm{d}g_{\mathbf{a}}}
>$$
>
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Chain Rule
>
>Let $g: \mathcal{D} \subseteq \mathbb{R}^m \to \mathbb{R}^n$ be a [[Functions of the Real Numbers|real vector function]] on an [[The Topology of Euclidean Space|open set]] $\mathcal{D}$ such that the [[Functions|image]] $g(\mathcal{D})$ is also [[The Topology of Euclidean Space|open]] and let $f: g(\mathcal{D}) \subseteq \mathbb{R}^n \to \mathbb{R}^p$.
>
>If $g$ is [[Differentiability of Real Vector Functions|differentiable]] at $\mathbf{a} \in \mathcal{D}$ and $f$ is [[Differentiability of Real Vector Functions|differentiable]] at $g(\mathbf{a})$, then the [[Composition]] $f \circ g: \mathcal{D} \subseteq \mathbb{R}^m \to \mathbb{R}^p$ is also [[Differentiability of Real Vector Functions|differentiable]] at $\mathbf{a}$ with
>
>$$
>\mathop{\mathrm{d}(f\circ g)_{\mathbf{a}}} = \mathop{\mathrm{d}f_{\mathbf{g(a)}}} \circ \mathop{\mathrm{d}g_{\mathbf{a}}}
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>