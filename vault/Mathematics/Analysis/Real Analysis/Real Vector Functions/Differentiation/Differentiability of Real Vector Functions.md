>[!DEFINITION] Definition: Differentiability of Real Vector Functions
>
>Let $f: \mathcal{D} \to \mathbb{R}^n$ be a [[Functions of the Real Numbers|real vector function]] on an [[The Topology of Euclidean Space|open set]] $\mathcal{D} \subseteq \mathbb{R}^m$ and let $\mathbf{a}$ be an [[Accumulation Point]] of $\mathcal{D}$.
>
>We say that $f$ is **(totally) differentiable at** $\mathbf{a}$ iff there exists some [[Linear Transformation]] $L_a: \mathcal{D} \to \mathbb{R}^n$ (which usually depends on $\mathbf{a}$) such that the following [[Limits of Real Scalar Fields|limit]] is zero.
>
>$$
>\lim_{\mathbf{x} \to \mathbf{a}} \frac{||f(\mathbf{x}) - f(\mathbf{a}) - L_a(\mathbf{x} - \mathbf{a})||}{||\mathbf{x} - \mathbf{a}||} = 0
>$$
>
>In this case, the transformation $L_a$ is known as the **(total) derivative** or **(total) differential** of $f$ at $\mathbf{a}$.
>
>If $f$ is [[Differentiability of Real Vector Functions|differentiable]] at every $\mathbf{a}$ in some $S \subseteq \mathbb{R}^m$, then we say that $f$ is **(totally) differentiable on** $S$. If $S = \mathcal{D}$, we can also just say that $f$ is **(totally) differentiable**. 
>
>>[!NOTATION]-
>>
>>We usually denote $L_{\mathbf{a}}$ as $\mathrm{d}f_{\mathbf{a}}$. If it is clear what $\mathbf{a}$ is, then we can also drop it and write just $\mathrm{d}f$.
>>
>
>>[!THEOREM] Theorem: Uniqueness of the Derivative
>>
>>If $f$ is [[Differentiability of Real Vector Functions|differentiable]] at $\mathbf{a}$, then its [[Differentiability of Real Vector Functions|derivative]] $\mathrm{d}f_{\mathbf{a}}$ is unique.
>>
>>>[!PROOF]-
>>>
>>>
>>>TODO
>>
>

>[!THEOREM] Theorem: Differentiability via Component Functions
>
>A [[Functions of the Real Numbers|real vector function]] $f: \mathcal{D} \subseteq \mathbb{R}^m \to \mathbb{R}^n$ is [[Differentiability of Real Vector Functions|differentiable]] at $\mathbf{a} \in \mathcal{D}$ if and only if its [[Functions of the Real Numbers|component functions]] are [[Differentiability of Real Scalar Fields|differentiable]] there.
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Total Derivative and the Jacobian
>
>Let $f: \mathcal{D} \to \mathbb{R}^n$ be a [[Functions of the Real Numbers|real vector function]] on an [[The Topology of Euclidean Space|open subset]] $\mathcal{D} \subseteq \mathbb{R}^m$ and let $\mathbf{a}$ be an [[Accumulation Point]] of $\mathcal{D}$.
>
>If $f$ is [[Differentiability of Real Vector Functions|differentiable]] at $\mathbf{a}$, then it is [[Partial Derivatives of Real Vector Functions|partially differentiable]] there with respect to [[Cartesian Coordinate System|Cartesian coordinates]] and the [[Matrix Representations of Linear Transformations|matrix representation]] of its [[Differentiability of Real Vector Functions|derivative]] $\mathrm{d}f_{\mathbf{a}}$ (with respect to the [[Standard Basis|standard bases]] of $\mathbb{R}^m$ and $\mathbb{R}^n$) is the [[Jacobian Matrix]] $Df(\mathbf{a})$.
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Continuous Differentiability
>
>Let $f: \mathcal{D} \to \mathbb{R}^n$ be a [[Functions of the Real Numbers|real vector function]] on an [[The Topology of Euclidean Space|open subset]] $\mathcal{D} \subseteq \mathbb{R}^m$ and let $\mathbf{a}$ be an [[Accumulation Point]] of $\mathbf{a}$.
>
>If there exists an [[The Topology of Euclidean Space|open]] [[Topological Spaces|neighbourhood]] $N$ of $\mathbf{a}$ on which the [[Functions|restriction]] $f\big|_{N}$ is [[Partial Derivatives of Real Vector Functions|continuously partially differentiable]] in [[Cartesian Coordinate System|Cartesian coordinates]], then $f$ is [[Differentiability of Real Vector Functions|totally differentiable]] at $\mathbf{a}$.
>
>>[!PROOF]-
>>
>>TODO
>>
>
>>[!DEFINITION] Definition: Continuous Differentiability
>>
>>In this case, we say that $f$ is **continuously differentiable** at $\mathbf{a}$.
>>
>