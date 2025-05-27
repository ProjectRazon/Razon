>[!DEFINITION] Definition: Motion with Constant Acceleration
>
>In **motion with constant** or **uniform acceleration** the [[Acceleration]] remains constant in time.
>
>$$
>\boldsymbol{a} = \text{const}
>$$
>

>[!THEOREM] Satz: Laws of Motion with Constant Acceleration
>
>A [[Point Mass|point pass]] is initially ($t = 0$) [[Position|located]] at $\boldsymbol{r}_0$ and begins to move with initial [[Velocity]] $\boldsymbol{v}_0$ and constant [[Acceleration]] $\boldsymbol{a}$.
>
>The [[Position]] $\boldsymbol{r}$ and [[Velocity]] $\boldsymbol{v}$ of the [[Point Mass]] at any subsequent moment $t$ are given by:
>
>$$
>\boldsymbol{v}(t) = \boldsymbol{v}_0+\boldsymbol{a}t
>$$
>
>$$
>\boldsymbol{r}(t) = \boldsymbol{r}_0+\boldsymbol{v}_0 t + \frac{1}{2}\boldsymbol{a}t^2
>$$
>
>>[!PROOF]- Proof
>>
>>Since [[Acceleration]] is the derivative of [[Velocity]], we need to solve the following initial value problem in order to determine a formula for $\boldsymbol{v}(t)$:
>>
>>$$
>>\frac{\mathrm{d}\boldsymbol{v}}{\mathrm{d}t} = \boldsymbol{a} \qquad \boldsymbol{v}(0) = \boldsymbol{v}
>>$$
>>
>>Integrate both sides with respect to $t$.
>>
>>$$
>>\int \frac{\mathrm{d}\boldsymbol{v}}{\mathrm{d}t} \mathop{\mathrm{d}t} = \int \boldsymbol{a} \mathop{\mathrm{d}t}
>>$$
>>
>>$$
>>\boldsymbol{v}(t) = \boldsymbol{a}t + \boldsymbol{c}
>>$$
>>
>>We must now determine $\boldsymbol{c}$ so that $v(t)$ satisfies the initial condition $\boldsymbol{v}(0) = \boldsymbol{v}_0$.
>>
>>$$
>>\boldsymbol{v}(0) = \boldsymbol{a}\cdot 0 + \boldsymbol{c} = \boldsymbol{v}_0 \implies \boldsymbol{c} = \boldsymbol{v}_0
>>$$
>>
>>We just proved the formula for the [[Velocity]].
>>
>>$$
>>\boldsymbol{v}(t) = \boldsymbol{v}_0+\boldsymbol{a}t
>>$$
>>
>>To find the formula for the [[Position]], we need to solve another initial value problem.
>>
>>$$
>>\frac{\mathrm{d}\boldsymbol{r}}{\mathrm{d}t} = \boldsymbol{v}(t) \qquad \boldsymbol{r}(0) = \boldsymbol{r}_0
>>$$
>>
>>$$
>>\frac{\mathrm{d}\boldsymbol{r}}{\mathrm{d}t} = \boldsymbol{v}_0+\boldsymbol{a}t
>>$$
>>
>>Integrate both sides with respect to $t$.
>>
>>$$
>>\int \frac{\mathrm{d}\boldsymbol{r}}{\mathrm{d}t} \mathop{\mathrm{d}t} = \int \boldsymbol{v}_0+\boldsymbol{a}t \mathop{\mathrm{d}t}
>>$$
>>
>>$$
>>\boldsymbol{r}(t) = \frac{1}{2}\boldsymbol{a}t^2 + \boldsymbol{v}_0 t + \boldsymbol{c}
>>$$
>>
>>We must now find the constant $\boldsymbol{c}$ so that it satisfies the initial condition $\boldsymbol{r}(0) = \boldsymbol{r}$.
>>
>>$$
>>\boldsymbol{r}(0) = \frac{1}{2}\boldsymbol{a}\cdot 0^2 + \boldsymbol{v}_0\cdot 0 + \boldsymbol{c} = \boldsymbol{r}_0 \implies \boldsymbol{c} = \boldsymbol{r}_0
>>$$
>>
>>Thus
>>
>>$$
>>\boldsymbol{r}(t) = \boldsymbol{r}_0+\boldsymbol{v}_0 t + \frac{1}{2}\boldsymbol{a}t^2
>>$$
>>
>