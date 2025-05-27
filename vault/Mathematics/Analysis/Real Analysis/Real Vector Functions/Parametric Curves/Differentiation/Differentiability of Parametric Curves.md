>[!THEOREM] Theorem: Differentiability of Parametric Curves
>
>Let $\gamma: I \subseteq \mathbb{R} \to \mathbb{R}^n$ be a [[Parametric Curve]] and let $t$ be an [[Accumulation Point]] of $I$.
>
>Then $\gamma$ is [[Differentiability of Real Vector Functions|differentiable]] at $t_0 \in I$ if and only if the following [[Limits of Parametric Curves|limit]] exists
>
>$$
>\lim_{t \to t_0} \frac{\gamma(t) - \gamma(t_0)}{t - t_0}
>$$
>
>>[!PROOF]-
>>
>>We need to prove two things:
>>
>>- (I) If $\displaystyle \lim_{t \to t_0} \frac{\gamma(t) - \gamma(t_0)}{t - t_0}$ exists, then there is a [[Linear Transformation]] $T: I \to \mathbb{R}^n$ such that 
>>
>>$$
>>\lim_{t \to t_0} \frac{||\gamma(t) - \gamma(t_0) - T(t - t_0)||}{|t- t_0|} = 0
>>$$
>>
>>- (II) If there is a [[Linear Transformation]] $T: I \to \mathbb{R}^n$ such that $\displaystyle \lim_{t \to t_0} \frac{||\gamma(t) - \gamma(t_0) - T(t - t_0)||}{||t- t_0||} = 0$, then $\displaystyle \lim_{t \to t_0} \frac{\gamma(t) - \gamma(t_0)}{t - t_0}$ exists.
>>
>>**Proof of (I):**
>>
>>Let $\mathbf{L} = \lim_{t \to t_0} \frac{\gamma(t) - \gamma(t_0)}{t - t_0}$. Define $T: I \to \mathbb{R}^n$ as
>>
>>$$
>>T(x) = x\mathbf{L}
>>$$
>>
>>We can easily check that $T$ is a [[Linear Transformation]]:
>>
>>$$
>>T(\alpha x + \beta y) = (\alpha x + \beta y)\mathbf{L} = \alpha x \mathbf{L} + \beta y \mathbf{L} = \alpha T(x) + \beta T(y)
>>$$
>>
>>Then
>>
>>$$
>>\begin{align*}
>>
>>\lim_{t \to t_0} \frac{||\gamma(t) - \gamma(t_0) - T(t - t_0)||}{||t- t_0||} &= \lim_{t \to t_0} \frac{||\gamma(t) - \gamma(t_0) - (t - t_0)\mathbf{L}||}{|t- t_0|} \\
>>
>>&= \lim_{t \to t_0} \frac{ |t-t_0| \cdot \left|\left|\frac{\gamma(t) - \gamma(t_0)}{t-t_0} - \mathbf{L}\right|\right|}{|t- t_0|} \\
>>
>>&= \lim_{t \to t_0} \left|\left|\frac{\gamma(t) - \gamma(t_0)}{t-t_0} - \mathbf{L}\right|\right| \\
>>
>>&= \left|\left| \lim_{t \to t_0} \left( \frac{\gamma(t) - \gamma(t_0)}{t - t_0} - \mathbf{L}\right) \right|\right| \\
>>
>>&= \left|\left|\lim_{t \to t_0} \left( \frac{\gamma(t) - \gamma(t_0)}{t - t_0} - \frac{\gamma(t) - \gamma(t_0)}{t-t_0}\right)\right|\right| \\
>>
>>&= ||\mathbf{0}|| = 0
>>
>>\end{align*}
>>$$
>>
>>
>>**Proof of (II):**
>>
>>Let $\mathbf{T}$ be the [[Matrix Representations of Linear Transformations|matrix representation]] of $T$ with respect to the [[Standard Basis of the Real Vector Space|standard bases]] of $\mathbb{R}$ and $\mathbb{R}^n$. Then,
>>
>>$$
>>\lim_{t \to t_0} \frac{||\gamma(t) - \gamma(t_0) - \mathbf{T}\begin{bmatrix}t-t_0\end{bmatrix}||}{|t- t_0|} = \lim_{t \to t_0} \frac{||\gamma(t) - \gamma(t_0) - (t-t_0)\mathbf{T}||}{|t- t_0|} = 0
>>$$
>>
>>Factor out $t-t_0$ from the numerator and move it outside the magnitude.
>>
>>$$
>>\begin{align*}
>>
>>\lim_{t \to t_0} \frac{||\gamma(t) - \gamma(t_0) - (t-t_0)\mathbf{T}||}{|t- t_0|} &= \lim_{t - t_0} \frac{|t-t_0|\cdot \left|\left| \frac{\gamma(t) - \gamma(t_0)}{t - t_0} - \mathbf{T} \right|\right|}{|t-t_0|} \\ 
>>
>>&= \lim_{t \to t_0} \left|\left| \frac{\gamma(t) - \gamma(t_0)}{t - t_0} - \mathbf{T} \right|\right| \\ 
>>
>>&= \left|\left| \lim_{t \to t_0} \left( \frac{\gamma(t) - \gamma(t_0)}{t - t_0} - \mathbf{T} \right) \right|\right| = 0
>>
>>\end{align*}
>>$$
>>
>>Therefore,
>>
>>$$
>>\begin{align*}
>>
>>&\lim_{t \to t_0} \left(\frac{\gamma(t) - \gamma(t_0)}{t - t_0} - \mathbf{T}\right) = \mathbf{0} \\
>>
>>&\lim_{t \to t_0} \left(\frac{\gamma(t) - \gamma(t_0)}{t - t_0}\right) - \mathbf{T} = \mathbf{0} \\
>>
>>&\lim_{t \to t_0} \frac{\gamma(t) - \gamma(t_0)}{t - t_0} = \mathbf{T}
>>
>>\end{align*}
>>$$
>>
>
>>[!DEFINITION] Definition: Derivative of a Parametric Curve
>>
>>The **derivative** of $\gamma$ at $t_0$ is the [[Limits of Parametric Curves|limit]]
>>
>>$$
>>\lim_{t \to t_0} \frac{\gamma(t) - \gamma(t_0)}{t - t_0},
>>$$
>>
>>provided that it exists.
>>
>>If there is no specific $t_0 \in I$ mentioned, then "derivative" refers to the [[Parametric Curve|function]] which to each $t^\ast$ assigns the aforementioned limit (if said limit exists).
>>
>>>[!NOTATION]
>>>
>>>$$
>>>\frac{\mathrm{d}\gamma}{\mathrm{d}t}(t_0) \qquad \left.\frac{\mathrm{d}\gamma}{\mathrm{d}t}\right|_{t_0} \qquad \frac{\mathrm{d}}{\mathrm{d}t}\gamma (t_0) \qquad \gamma'(t_0) \qquad \dot{\gamma}(t_0)
>>>$$
>>>
>>
>>>[!NOTE]- Note: Derivative Terminology
>>>
>>>Referring to this limit as the "derivative" is technically a misnomer, since the [[Differentiability of Real Vector Functions|derivative of a vector function]] is a [[Linear Transformation]] and the aforementioned limit is only a [[Matrix Representations of Linear Transformations|matrix representation]] of said transformation. However, in the case of parametric curves, using the matrix representation of the derivative is very common. This is why, in this context, the term "derivative" is usually used for the matrix representation of the transformation instead of the transformation itself.
>>>
>>
>

>[!TIP] Tip: (Continuous) Differentiability of Curve Parameterisations
>
>A [[Parametric Curve|curve parameterisation]] $\gamma$ is $k$**-times (continuously) differentiable** if its $k$-th order [[Differentiability of Parametric Curves|derivative]] exists (and is [[Continuity of Real Vector Functions|continuous]]).
>
>^continuous-differentiability
>

>[!TIP] Tip: Piecewise (Continuous) Differentiability of Curve Parameterisations
>
>A [[Parametric Curve|curve parameterisation]] $\gamma: I \subseteq \mathbb{R} \to \mathbb{R}^n$ is $k$**-times piecewise (continuously) differentiable** if $I$ can be expressed as a [[Disjoint Sets|disjoint]] [[Set Operations|union]] $I = I_1 \cup \cdots \cup I_n$ such that the [[Functions|restrictions]] $\gamma \big|_{I_1}, \cdots, \gamma \big|_{I_n}$ are $k$-times [[Differentiability of Parametric Curves|continuously differentiable]].
>
>^piecewise-continuous-differentiablity
>

>[!TIP] Tip: Smoothness of Curve Parameterisations
>
>A [[Parametric Curve|curve parameterisation]] is **smooth** if it is $k$-times [[Differentiability of Parametric Curves|continuously differentiable]] for all $k \in \mathbb{N}$.
>
>^smoothness
>

>[!TIP] Tip: Piecewise Smoothness of Curve Parameterisations
>
>A [[Parametric Curve|curve parameterisation]] $\gamma: I \subseteq \mathbb{R} \to \mathbb{R}^n$ is **piecewise smooth** if $I$ can be expressed as a [[Operations with Collections|union]] of a finite [[Collections|collection]] of [[Intervals]] $I = I_1 \cup \cdots \cup I_p$ such that the [[Functions|restrictions]] $\gamma \big|_{I_1}, \ldots, \gamma \big|_{I_n}$ are [[Differentiability of Parametric Curves|smooth]].
>
>^piecewise-smoothness
>