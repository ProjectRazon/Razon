>[!DEFINITION] Definition: Partial Derivative of a Real Scalar Field
>
>Let $f: \mathcal{D} \to \mathbb{R}$ be a [[Real Scalar Field]] on an [[The Topology of Euclidean Space|open subset]] $\mathcal{D} \subseteq \mathbb{R}^n$, let $\phi: \mathcal{D} \to \mathbb{R}^n$ be a [[index|coordinate system]] on $\mathcal{D}$ and let $a^1 = \phi^1(\mathbf{a}), \dotsc, a^n = \phi^n(\mathbf{a})$ be the coordinates of some $\mathbf{a} \in \mathcal{D}$ in $\phi$.
>
>The **partial derivative** of $f$ at $\mathbf{a}$ with respect to the $i$-th coordinate $\phi^i$ is the [[Limits of Real Functions|limit]]
>
>$$
>\lim_{h\to 0} \frac{f(a^1, \dotsc, a^i + h, \dotsc, a^n) - f(a^1, \dotsc, a^i, \dotsc, a^n)}{h},
>$$
>
>>[!NOTATION]-
>>
>>Most commonly, the partial derivative of $f$ at $\mathbf{a}$ with respect to the $i$-th coordinate $\phi^i$ is denoted as:
>>
>>$$
>>\frac{\partial}{\partial \phi^i} (\mathbf{a}) \qquad  \frac{\partial f}{\partial \phi^i} f(\mathbf{a}) \qquad \left. \frac{\partial f}{\partial \phi^i}\right|_{\mathbf{a}} \qquad f_{\phi^i}(\mathbf{a})
>>$$
>>
>>If the coordinate system is evident from context, we can also write $\partial_i f(\mathbf{a})$.
>>
>
>>[!NOTE] Note: Partial Derivative as a Function
>>
>>When there is no specific $\mathbf{a} \in \mathcal{D}$ mentioned, the term "partial derivative" refers to the the [[Real Scalar Field|function]] $\frac{\partial f}{\partial \phi^i} : \mathcal{D} \to \mathbb{R}$ which to each $\mathbf{x} \in \mathcal{D}$ assigns the [[Partial Derivatives of Real Scalar Fields|partial derivative]] of $f$ at $\mathbf{a}$ with respect to the coordinate $\phi^i$.
>>
>

>[!NOTE] Note: Orders of Partial Derivatives
>
>An $n$-th order partial derivative of $f$ is a partial derivative of $f$'s $(n-1)$-th partial derivative function.
>


