>[!DEFINITION] Continuity of a Real Vector Function
>
>Let $f: \mathcal{D} \subseteq \mathbb{R}^m \to \mathbb{R}^n$ be a [[Functions of the Real Numbers|real vector function]].
>
>We say that $f$ is **continuous at** $\mathbf{a} \in \mathcal{D}$ iff its [[Limits of Real Vector Functions|limit]] for $\mathbf{x} \to \mathbf{a}$ is $f(\mathbf{a})$
>
>$$
>\lim_{\mathbf{x} \to \mathbf{a}} f(\mathbf{x}) = f(\mathbf{a})
>$$
>
>or $\mathbf{a}$ is an [[Isolated Points|isolated point]] of $D$.
>
>We say that $f$ is **continuous on** $\mathcal{D}$ if it is continuous at every $\mathbf{a} \in \mathcal{D}$.
>
>>[!DEFINITION] Definition: Piecewise Continuity
>>
>>Let $f: D \subseteq \mathbb{R}^m \to \mathbb{R}^n$ be a [[Functions of the Real Numbers|real vector function]].
>>
>>We say that $f$ is **piecewise continuous** if $D$ can be expressed as the [[Operations with Collections|union]] of a finite [[Collections|collection]] of [[Disjoint Sets]] $D = D_1 \cup \cdots \cup D_p$ such that the [[Functions|restrictions]] $f\big|_{D_1},\ldots, f\big|_{D_p}$ are [[Continuity of Real Vector Functions|continuous]].
>>
>

## Characterizations

>[!THEOREM] Theorem: Continuity via Component Functions
>
>A [[Functions of the Real Numbers|real vector function]] $f: \mathcal{D} \subseteq \mathbb{R}^m \to \mathbb{R}^n$ is [[Continuity of Real Vector Functions|continuous]] at $\mathbf{x}_0 \in \mathcal{D}$ if and only if its [[Functions of the Real Numbers|component functions]] $f_1, \dotsc, f_n$ are [[Continuity of Real Vector Functions|continuous]] at $\mathbf{x}_0$.
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Continuity via Limits of Scalar Fields
>
>A [[Functions of the Real Numbers|real vector function]] $f: \mathcal{D} \subseteq \mathbb{R}^m \to \mathbb{R}^n$ is [[Continuity of Real Vector Functions|continuous]] at $\mathbf{a} \in \mathcal{D}$ if and only if $\mathbf{a} \in \mathcal{D}$ is an [[Isolated Points|isolated point]] of $\mathcal{D}$ or the following [[Limits of Real Scalar Fields|limit]] is zero.
>
>$$
>\lim_{\mathbf{x} \to \mathbf{a}} ||f(\mathbf{x}) - f(\mathbf{a})|| = 0
>$$
>
>>[!PROOF]-
>>
>>We need to prove two things:
>>
>>- (I) If $f$ is [[Continuity of Real Vector Functions|continuous]] at $\mathbf{a} \in \mathcal{D}$, then $\lim_{\mathbf{x} \to \mathbf{a}} ||f(\mathbf{x}) - f(\mathbf{a})|| = 0$.
>>- (II) If $\lim_{\mathbf{x} \to \mathbf{a}} ||f(\mathbf{x}) - f(\mathbf{a})|| = 0$, then $f$ is [[Continuity of Real Vector Functions|continuous]] at $\mathbf{a}$.
>>
>>**Proof of (I):**
>>
>>To prove that
>>
>>$$
>>\lim_{\mathbf{x} \to \mathbf{a}} ||f(\mathbf{x}) - f(\mathbf{a})|| = 0,
>>$$
>>
>>we need to show that for each $\varepsilon \gt 0$, there exists some $\delta \gt 0$ such that if $\mathbf{x} \in \mathcal{D}$ and $0 \lt ||\mathbf{x} - \mathbf{a}|| \lt \delta$, then $| \, ||f(\mathbf{x}) - f(\mathbf{a})|| - 0 \,|\lt \varepsilon$, i.e. $||f(\mathbf{x}) - f(\mathbf{a})||\lt \varepsilon$.
>>
>>Now, since $f$ is [[Continuity of Real Vector Functions|continuous]], we have
>>
>>$$
>>\lim_{\mathbf{x} \to \mathbf{a}} f(\mathbf{x}) = f(\mathbf{a})
>>$$
>>
>>In other words, for each [[The Topology of Euclidean Space|open ball]] $B_{\varepsilon}(f(\mathbf{a}))$ around $\mathbf{a}$, there exists some [[The Topology of Euclidean Space|open ball]] $B_{\delta}(\mathbf{a})$ around $\mathbf{a}$ such that for all $\mathbf{x} \in \mathcal{D}$ different from $\mathbf{a}$, if $\mathbf{x} \in B_{\delta}(\mathbf{a})$, then $f(\mathbf{x}) \in B_{\varepsilon}(f(\mathbf{a}))$. By recalling the [[index|definition of an open ball]], we can restate the previous sentence as the following - for each $\varepsilon \gt 0$, there exists some $\delta \gt 0$ such that for all $\mathbf{x} \in \mathcal{D}$, if $0 \lt || \mathbf{x} - \mathbf{a} || \lt \delta$, then $|| f(\mathbf{x}) - f(\mathbf{a}) || \lt \varepsilon$, which is precisely what we set out to prove.
>>
>>**Proof of (II):**
>>
>>To prove that $f$ is [[Continuity of Real Vector Functions|continuous]] at $\mathbf{a}$, we need to prove that
>>
>>$$
>>\lim_{ \mathbf{x} \to \mathbf{a}} f(\mathbf{x}) = f(\mathbf{a})
>>$$
>>
>>Restating this using the [[Limits of Real Vector Functions|definition of a limit]], we need to prove that for each [[The Topology of Euclidean Space|open ball]] $B_{\varepsilon}(f(\mathbf{a}))$ around $f(\mathbf{a})$, there exists some [[The Topology of Euclidean Space|open ball]] $B_{\delta}(\mathbf{a})$ around $\mathbf{a}$ such that for all $\mathbf{x} \in \mathcal{D}$ different from $\mathbf{x}$, if $\mathbf{x} \in B_{\delta}(\mathbf{a})$, then $f(\mathbf{x}) \in B_{\varepsilon}(f(\mathbf{a}))$. Further paraphrasing this using the [[index|definition of an open ball]], we need to prove that for each $\varepsilon \gt 0$, there exists some $\delta \gt 0$ such that for all $\mathbf{x} \in \mathcal{D}$, if $0 \lt || \mathbf{x} - \mathbf{a} || \lt \delta$, then $|| f(\mathbf{x}) - f(\mathbf{a}) || \lt \varepsilon$.
>>
>>We are given that
>>
>>$$
>>\lim_{\mathbf{x} \to \mathbf{a}} ||f(\mathbf{x}) - f(\mathbf{a})|| = 0
>>$$
>>
>>Using the [[Limits of Real Scalar Fields|definition of the limit for scalar fields]], we know that for each $\varepsilon \gt 0$, there exists some $\delta \gt 0$ such that for all $\mathbf{x} \in \mathcal{D}$, if $|| \mathbf{x} - \mathbf{a} ||$, then $|\, ||f(\mathbf{x}) - f(\mathbf{a})|| - 0 \,| \lt \varepsilon$. Since $|\, || f(\mathbf{x}) - f(\mathbf{a})|| - 0 \, | = || f(\mathbf{x}) - f(\mathbf{a}) ||$, this just means that for each $\varepsilon \gt 0$, there exists some $\delta \gt 0$ such that for all $\mathbf{x} \in \mathcal{D}$, if $|| \mathbf{x} - \mathbf{a} ||$, then $|| f(\mathbf{x}) - f(\mathbf{a}) || \lt \varepsilon$, which is what we wanted to prove.
>>

## Properties

>[!THEOREM] Theorem: Properties of Continuous Real Vector Functions
>
>If $f,g: \mathcal{D} \subseteq \mathbb{R}^m \to \mathbb{R}^n$ are [[Continuity of Real Vector Functions|continuous]] at $\mathbf{x}_0 \in \mathcal{D}$, then so are $f+g$ and $\lambda f$ for all $\lambda \in \mathbb{R}$.
>
> >[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Continuity of Composition
>
>If $g: \mathcal{D} \subseteq \mathbb{R}^m \to \mathbb{R}^n$ and $f: g(\mathcal{D}) \to \mathbb{R}^p$ are [[Continuity of Real Vector Functions|continuous]], then so is their [[Composition]] $f \circ g$.
>
>>[!PROOF]-
>>
>>TODO
>>
>