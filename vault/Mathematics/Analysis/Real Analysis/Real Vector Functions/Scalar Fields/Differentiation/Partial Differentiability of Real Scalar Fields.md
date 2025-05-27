>[!DEFINITION] Definition: (Continuous) Partial Differentiability of Real Scalar Fields
>
>A [[Real Scalar Field]] $f: \mathcal{D} \subseteq \mathbb{R}^n \to \mathbb{R}$ and let $\phi$ be a [[index|coordinate system]] for $\mathbb{R}^n$.
>
>We say that $f$ is $k$**-times (continuously) partially differentiable at** some $\mathbf{a} \in \mathcal{D}$ iff all of its $k$-th order [[Partial Derivatives of Real Scalar Fields|partial derivatives]] with respect to all coordinates of $\phi$ exist at $\mathbf{a}$ (and are [[Continuity of Real Scalar Fields|continuous]] there).
>
>If the above is true for every $\mathbf{x} \in \mathcal{D}$, then we say that $f$ is $k$**-times (continuously) partially differentiable on** $\mathcal{D}$. We can also omit "on $\mathcal{D}$".
>
>>[!NOTE]
>>
>>If there is no specific coordinate system mentioned, then we mean that $f$ is $k$-times (continuously) partially differentiable with respect to [[Cartesian Coordinate System|Cartesian coordinates]].
>>
>

>[!WARNING]- Warning: Partial Differentiability's Dependence on Coordinate Systems
>
>If $f$ is partially differentiable in *one* coordinate system, then that does not necessarily mean that it is partially differentiable in *every* coordinate system.
>
>Consider the function $f: \mathbb{R}^2 \to \mathbb{R}$ defined in [[Cartesian Coordinate System|Cartesian coordinates]] as
>
>$$
>f(x,y) \overset{\text{def}}{=}
>
>\begin{cases} 
>x^2 + y^2 \hphantom{000} \text{ if } y \ne 0 \\
>
>0 \hphantom{00000000} \text{ if } y = 0
>
>\end{cases}
>$$
>
>Let's see what $f$'s [[Partial Derivatives of Real Scalar Fields|partial derivatives]] with respect to $x$ and $y$ are.
>
>**Partial derivative with respect to** $x$:
>
>For $y \ne 0$, 
>
>$$
>\frac{\partial }{\partial x} f(x, y) = \frac{\partial f}{\partial x} x^2 + y^2 = 2x
>$$
>
>For $y = 0$, we have $f(x, 0) = 0$ and thus
>
>$$
>\frac{\partial }{\partial x} f(x, y) = \lim_{h \to 0} \frac{f(x + h, 0) - f(x, 0)}{h} = \lim_{h \to 0} \frac{0 - 0}{h} = 0
>$$
>
>So, the partial derivative of $f$ with respect to $x$ exists at every point.
>
>**Partial derivative with respect to** $y$:
>
>For $y \neq 0$,
>
>$$
>\frac{\partial }{\partial y} f(x,y) = \frac{\partial}{\partial y}(x^2 + y^2) = 2y.
>$$
>
>For $y = 0$, again we have $f(x, 0) = 0$ and so
>
>$$
>\frac{\partial }{\partial y}  f(x,y) = \lim_{h \to 0} \frac{f(x, 0 + h) - f(x, 0)}{h} = \lim_{h \to 0} \frac{(x^2 + h^2) - 0}{h} = \lim_{h \to 0} \frac{x^2 + h^2}{h}
>$$
>
>However, this [[Limits of Real Functions|limit]] does not exists, since it depends on whether $h$ approaches $0$ from the left or the right. 
>
>Therefore, $f$ is *not* partially differentiable with respect to $y$ on the points $(x, 0)$.
>
>Now, let's take a look at another coordinate system $u, v$. The transformations between $(u,v)$ and $(x, y)$ are given below.
>
>$$
>\begin{align*}
>
>&u = x + y \qquad v = x - y \\
>
>&x = \frac{u + v}{2} \hphantom{000} y = \frac{u - v}{2}
>
>\end{align*}
>$$
>
>When $u = v$, i.e. when $y = 0$, the function $f$ is also $0$.
>
>When $u \ne v$, the function $f$ expressed in the coordinate system $(u,v)$ is
>
>$$
>\begin{align*}
>
>f(u,v) &= \left( \frac{u + v}{2} \right)^2 + \left( \frac{u - v}{2} \right)^2 \\
>
>&= \frac{u^2 + 2uv + v^2}{4} + \frac{u^2 - 2uv + v^2}{4} \\
>
>&= \frac{2u^2 + 2v^2}{4} \\
> 
>&= \frac{u^2 + v^2}{2}
>
>\end{align*}
>$$
>
>Therefore,
>
>$$
>f(u, v) = 
>
>\begin{cases}
>
>\frac{u^2 + v^2}{2} \hphantom{000} u \ne v \\
>
>0 \hphantom{\frac{u^2 + v^2}{2}00} u = v
>
>\end{cases}
>$$
>
>Let's examine the partial derivatives of $f$ with respect to $u$ and $v$.
>
>**Partial derivative with respect to** $u$:
>
>For $u \ne v$,
>
>$$
>\frac{\partial}{\partial u} f(u,v) = \frac{\partial}{\partial u} \frac{u^2 + v^2}{2} = \frac{1}{2} \times 2u = u
>$$
>
>For $u = v$, we have $f(u,v) = 0$
>
>$$
>\frac{\partial}{\partial u} f(u,v) = \lim_{h \to 0} \frac{f(u + h, v) - f(u,v)}{h} = \lim_{h \to 0} \frac{\frac{(u+h)^2 + v^2}{2} - 0}{h} = \lim_{h \to 0} \frac{(u+h)^2 + v^2}{2h} = 0
>$$
>
>Therefore, the partial derivative of $f$ with respect to $u$ exists at every point.
>
>**Partial derivative with respect to** $v$:
>
>For $u \ne v$,
>
>$$
>\frac{\partial}{\partial v} f(u,v) = \frac{\partial}{\partial v} \frac{u^2 + v^2}{2} = \frac{1}{2} \times 2v = v
>$$
>
>For $u = v$, we have $f(u,v) = 0$
>
>$$
>\frac{\partial}{\partial v} f(u,v) = \lim_{h \to 0} \frac{f(u, v + h) - f(u,v)}{h} = \lim_{h \to 0} \frac{\frac{u^2 + (v + h)^2}{2} - 0}{h} = \lim_{h \to 0} \frac{u^2 + (v + h)^2}{2h} = 0
>$$
>
>Therefore, the partial derivative of $f$ with respect to $v$ exists at every point.
>
>This means that $f$ is partially differentiable at every point with respect to the coordinate system $(u,v)$, but it is not partially differentiable with respect to $(x,y)$.
>