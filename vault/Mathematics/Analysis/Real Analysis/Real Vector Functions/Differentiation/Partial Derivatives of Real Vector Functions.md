>[!DEFINITION] Definition: Partial Derivative of a Real Vector Function
>
>Let $f: \mathcal{D} \subseteq \mathbb{R}^m \to \mathbb{R}^n$ be a [[Functions of the Real Numbers|real vector function]] with [[Functions of the Real Numbers|component functions]] $f_1,\cdots,f_n$ and let $\phi$ be a [[index|coordinate system]] for $\mathbb{R}^m$.
>
>The **partial derivative** of $f$ at $\mathbf{a} \in \mathcal{D}$ with respect to the $i$-th coordinate $\phi^i$ is the [[Real Vector|vector]] whose entries are the [[Partial Derivatives of Real Scalar Fields|partial derivatives]] of $f_1,\cdots,f_n$ with respect to $\phi^i$:
>
>$$
>\begin{bmatrix}\frac{\partial f_1}{\partial \phi^i}(\mathbf{a}) \\ \vdots \\ \frac{\partial f_n}{\partial \phi^i}(\mathbf{a}) \end{bmatrix}
>$$
>
>>[!NOTATION]-
>>
>>$$
>>\frac{\partial f}{\partial \phi^i} (\mathbf{a}) \qquad \left. \frac{\partial f}{\partial \phi^i} \right|_{\mathbf{a}}  \qquad \frac{\partial}{\partial \phi^i} f(\mathbf{a}) \qquad f_{\phi^i} (\mathbf{a})
>>$$
>>
>

>[!DEFINITION] Definition: (Continuous) Partial Differentiability
>
>A [[Functions of the Real Numbers|real vector function]] $f: \mathcal{D} \subseteq \mathbb{R}^m \to \mathbb{R}^n$ is called $k$**-times (continuously) partially differentiable** if all of its $k$-th order [[Partial Derivatives of Real Vector Functions|partial derivatives]] exist (and are [[Continuity of Real Vector Functions|continuous]]) on $\mathcal{D}$. 
>
>If $f$ is $k$-times continuously partially differentiable, then we also say that $f$ is **of class** $C^k$ if $f$.
>
>>[!NOTATION]-
>>
>>$$
>>f \in C^k
>>$$
>>
>
>>[!DEFINITION] Definition: Piecewise (Continuous) Partial Differentiability
>>
>>A [[Functions of the Real Numbers|real vector function]] $f: \mathcal{D} \subseteq \mathbb{R}^m \to \mathbb{R}^n$ is $k$-times **piecewise (continuously) partially differentiable** iff $\mathcal{D}$ can be represented as a [[Disjoint Sets|disjoint]] [[Set Operations|union]] $\mathcal{D} = \mathcal{D}_1 \cup \cdots \cup \mathcal{D}_k$ of finitely many [[Sets|subsets]] $\mathcal{D}_1, \dotsc, \mathcal{D}_k$ of $\mathbb{R}^m$ such that the [[Functions|restrictions]] $f_{\mathcal{D}_1}, \dotsc, f_{\mathcal{D}_k}$ are $k$-times [[Partial Derivatives of Real Vector Functions|(continuously) partially differentiable]].
>>
>
