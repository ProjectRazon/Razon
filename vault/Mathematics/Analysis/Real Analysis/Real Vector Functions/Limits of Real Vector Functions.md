>[!DEFINITION] Definition: Limit of a Real Vector Function
>
>Let $f: \mathcal{D} \subseteq \mathbb{R}^m \to \mathbb{R}^n$ be a [[Functions of the Real Numbers|real vector function]] and let $\mathbf{a} \in \mathbb{R}^m$ be an [[Accumulation Point]] of $\mathcal{D}$.
>
>We say that $\mathbf{L} \in \mathbb{R}^n$ is a **limit** of $f$ for $\mathbf{x} \to \mathbf{a}$ iff for each [[The Topology of Euclidean Space|open ball]] $B_{\varepsilon}(\mathbf{L})$ around $\mathbf{L}$ there exists an [[The Topology of Euclidean Space|open ball]] $B_{\delta}(\mathbf{a})$ around $\mathbf{a}$ such that for all $\mathbf{x} \in \mathcal{D}$ different from $\mathbf{a}$,
>
>$$
>\mathbf{x} \in B_{\delta}(\mathbf{a}) \implies f(\mathbf{x}) \in B_{\varepsilon}(\mathbf{L})
>$$
>
>>[!TIP]- Tip: Restatement without Open Balls
>>
>>For the purposes of many proofs, it useful to define the limit without reference to open balls. This is done simply by taking the above definition and replacing every occurrence of "open ball" with the [[index|definition of an open ball]].
>>
>>We say that $\mathbf{L} \in \mathbb{R}^n$ is a **limit** of $f$ for $\mathbf{x} \to \mathbf{a}$ iff for each $\varepsilon \gt 0$, there exists some $\delta \gt 0$ such that for all $\mathbf{x} \in \mathcal{D}$, if $0 \lt ||\mathbf{x} - \mathbf{a}|| \lt \delta$, then $||f(\mathbf{x}) - \mathbf{L}|| \lt \varepsilon$.
>>
>
>>[!NOTATION]-
>>
>>$$
>>\lim_{\mathbf{x} \to \mathbf{a}} f(\mathbf{x}) = \mathbf{L} \qquad f(\mathbf{x}) \overset{\mathbf{x} \to \mathbf{a}}{\to} \mathbf{L}
>>$$
>>
>
>>[!INTUITION]-
>>
>>Suppose we have some fixed point $\mathbf{a} \in \mathbb{R}^m$ and a point $\mathbf{x} \in \mathcal{D}$ which we can move around freely. The limit $\lim_{\mathbf{x}\to\mathbf{a}}f(\mathbf{x})$ tells us what point in $\mathbb{R}^n$ (if any) $f(\mathbf{x})$ approaches as $\mathbf{x}$ gets closer and closer to $\mathbf{a}$. If the limit is $\mathbf{L}$, then no matter how small a sphere $B_{\varepsilon}(\mathbf{L})$ we choose around $\mathbf{L}$, there will always be some sphere $B_{\delta}(\mathbf{a})$ (probably a very small one, too, but nevertheless still containing more than a single point) around $\mathbf{a}$ such that if $\mathbf{x}$ is inside $B_{\delta}(\mathbf{a})$, then $f(\mathbf{x})$ will be inside $B_{\varepsilon}(\mathbf{L})$.
>>
>
>>[!THEOREM] Theorem: Uniqueness of the Limit
>>
>>If $f$ has a [[Limits of Real Vector Functions|limit]] for $\mathbf{x} \to \mathbf{a}$, then this [[Limits of Real Vector Functions|limit]] is unique.
>>
>>>[!PROOF]-
>>>
>>>TODO
>>>
>>
>

## Characterizations

>[!THEOREM] Theorem: Limit via Component Functions
>
>Let $f: D \subseteq \mathbb{R}^m \to \mathbb{R}^n$ be a [[Functions of the Real Numbers|real vector function]] with [[Functions of the Real Numbers|component functions]] $f_1,\cdots, f_n$ and let $\mathbf{a} \in \mathbb{R}^m$.
>
>Then $f$ has a [[Limits of Real Vector Functions|limit]] for $\mathbf{x} \to \mathbf{a}$ if and only if $f_1,\cdots, f_n$ have [[Limits of Real Scalar Fields|limits]] for $\mathbf{x} \to \mathbf{a}$. Moreover,
>
>$$
>\lim_{\mathbf{x} \to \mathbf{a}} f(\mathbf{x}) = 
>
>\begin{bmatrix}
>
>\displaystyle \lim_{\mathbf{x} \to \mathbf{a}} f_1(\mathbf{x}) \\
>
>\vdots \\
>
>\displaystyle \lim_{\mathbf{x} \to \mathbf{a}} f_n(\mathbf{x})
>
>\end{bmatrix}
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

## Properties

>[!THEOREM] Theorem: Linearity of the Limit Operator
>
>If $f, g: \mathcal{D} \subseteq \mathbb{R}^m \to \mathbb{R}^n$ have [[Limits of Real Vector Functions|limits]] for $\mathbf{x} \to \mathbf{a}$, then for all $\lambda, \mu \in \mathbb{R}$
>
>$$
>\lim_{\mathbf{x} \to \mathbf{a}} [\lambda f(\mathbf{x}) + \mu g(\mathbf{x})] = \lambda \lim_{\mathbf{x} \to \mathbf{a}} f(\mathbf{x}) + \mu \lim_{\mathbf{x} \to \mathbf{a}} g(\mathbf{x})
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>