>[!THEOREM] Theorem: Linearity of Differentiation
>
>The [[Differentiability of Parametric Curves|differentiation]] operation for [[Parametric Curve|curve parameterisations]] is linear - for all [[Parametric Curve|curve parameterisations]]  $\mathbf{u},\mathbf{v}:I\subseteq \mathbb{R}\to\mathbb{R}^n$ and all $\mu,\lambda \in \mathbb{R}$:
>
>$$\frac{\mathrm{d}}{\mathrm{d}t}[\lambda\,\mathbf{u}(t) + \mu\,\mathbf{v}(t)] = \lambda\,\mathbf{u}'(t) + \mu\,\mathbf{v}'(t)$$
>
>
>>[!PROOF]-
>>
>>TODO
>>

>[!THEOREM] Theorem: Chain Rule
>For every [[Differentiability|differentiable real function]] $f:I\subseteq\mathbb{R}\to\mathbb{R}$ and every [[Differentiability of Parametric Curves|differentiable curve parameterisation]] $\mathbf{r}:f(I)\to\mathbb{R}^n$:
>
>$$\frac{\mathrm{d}}{\mathrm{d}t}\mathbf{r}(f(t)) = f'(t)\,\mathbf{r}'(f(t))$$
>
>>[!PROOF]-
>>
>>TODO
>>
>
>^chainrule

>[!THEOREM] Theorem: Product Rules
>
>- *Basic Product Rule*: For every [[Differentiability of Parametric Curves|differentiable curve parameterisation]] $\mathbf{r}:I\to\mathbb{R}^n$ and every [[Differentiability|differentiable real function]] $f:I\subseteq\mathbb{R}\to\mathbb{R}$
>
>$$\frac{\mathrm{d}}{\mathrm{d}t}[f(t)\mathbf{r}(t)] = f'(t)\mathbf{r}(t) + \mathbf{r}'(t)f(t)$$
>
>- *Dot Product Rule*: For the [[Real Dot Product|dot product]] of all [[Differentiability of Parametric Curves|differentiable curve parameterisations]] $\mathbf{u},\mathbf{v}:I\subseteq \mathbb{R}\to\mathbb{R}^n$
>
>$$\frac{\mathrm{d}}{\mathrm{d}t}[\mathbf{u}(t)\cdot\mathbf{v}(t)] = \mathbf{u}'(t)\cdot \mathbf{v}(t) + \mathbf{u}(t)\cdot\mathbf{v}'(t)$$
>
>- *Cross Product Rule*: For the [[Real Cross Product|cross product]] of all [[Differentiability of Parametric Curves|differentiable curve parameterisations]] $\mathbf{u},\mathbf{v}:I\subseteq \mathbb{R}\to\mathbb{R}^3$
>
>$$\frac{\mathrm{d}}{\mathrm{d}t}[\mathbf{u}(t)\times \mathbf{v}(t)] = \mathbf{u}'(t)\times\mathbf{v}(t) + \mathbf{u}(t)\times\mathbf{v}'(t)$$
>
>>[!PROOF]-
>>
>>TODO
>>
>