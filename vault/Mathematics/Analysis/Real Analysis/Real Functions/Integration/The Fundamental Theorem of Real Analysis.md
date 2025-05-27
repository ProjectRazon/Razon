>[!THEOREM] The Fundamental Theorem of Real Analysis (Part I)
>
>Let $f: D \to \mathbb{R}$ be a [[Functions of the Real Numbers|real function]] on a [[Intervals|closed interval]] $D = [a;b]$.
>
>If $f$ is [[Definite Integrals|Riemann-integrable]], then $F: D \to \mathbb{R}$ defined by the [[Definite Integrals|definite integral]]
>
>$$
>F(x) \overset{\text{def}}{=} \int_a^x f
>$$
>
>is [[Continuity|continuous]]. Furthermore, if $f$ is [[Continuity|continuous]] at some $c \in D$, then $F$ is an [[Antiderivatives|antiderivative]] of $f$ at $c$, i.e. $F'(c) = f(c)$.
>
>>[!PROOF]-
>>
>>According to the definition of the [[Parity|derivative]] we need to prove
>>
>>$$
>>\lim_{\Delta x\to 0}\frac{F(x+\Delta x) - F(x)}{\Delta x} = f(x)
>>$$
>>
>> 
>>For all $c, x_0,\Delta x \in [a;b]$, where $x_0+\Delta x \in [a;b]$, it holds that
>>
>>$$
>>\begin{align*}F(x_0+\Delta x) - F(x_0) &= \int_c^{x_0+\Delta x} f(t)\mathop{\mathrm{d}t} - \int_c^{x_0} f(t)\mathop{\mathrm{d}t} \\ &= \int_c^{x_0+\Delta x} f(t)\mathop{\mathrm{d}t} + \int_{x_0}^c f(t)\mathop{\mathrm{d}t} \\ &= \int_{x_0}^c f(t)\mathop{\mathrm{d}t} + \int_c^{x_0+\Delta x} f(t)\mathop{\mathrm{d}t} \\ &= \int_{x_0}^{x_0+\Delta x}f(t) \mathop{\mathrm{d}t}\end{align*}
>>$$
>> 
>>The [[Definite Integrals|mean value theorem for definite integrals]] says that there is at least one $\xi \in[x_0;x_0+\Delta x]$ such that
>>
>>$$
>>\int_{x_0}^{x_0+\Delta x}f(t) \mathop{\mathrm{d}t} = f(\xi)(x_0 + \Delta x - x_0) = f(\xi)\cdot\Delta x
>>$$
>>
>>$$
>>\frac{F(x_0+\Delta x) - F(x_0)}{\Delta x} = f(\xi)
>>$$
>>
>>We now take the [[Limits of Real Functions|limit]] as $\Delta x \to 0$.
>>
>>$$
>>\lim_{\Delta x \to 0}\frac{F(x_0+\Delta x) - F(x_0)}{\Delta x} = \lim_{\Delta x \to 0}f(\xi)
>>$$
>>
>>The left-hand side is just the [[Differentiability|derivative]] of $F$ at $x_0$. Since $\xi$ is between $x_0$ and $x_0 + \Delta x$, it must approach $x_0$ for $\Delta x \to 0$. This means that
>>
>>$$
>>\lim_{\Delta x\to 0}f(\xi) = f(x_0)
>>$$
>>
>>and so we have
>>
>>$$
>>\lim_{\Delta x \to 0}\frac{F(x_0+\Delta x) - F(x_0)}{\Delta x} = f(x_0)
>>$$
>>
>>We have thus proven
>>
>>$$
>>F'(x_0) = f(x_0)
>>$$
>>
>

>[!THEOREM] The Fundamental Theorem of Real Analysis (Part II)
>
>If $f: [a;b] \to \mathbb{R}$ , then any [[Antiderivatives|antiderivative]] $F:[a;b] \to \mathbb{R}$ of $f$ can be used to calculate its [[Definite Integrals|definite integral]] as follows:
>
>$$
>\int_a^b f(x) \mathop{\mathrm{d}x} = F(b) - F(a)
>$$
>
>>[!NOTATION]-
>>
>>The expression $F(b) - F(a)$ is usually shortened to just $F(x)\big|_a^b$.
>
>>[!PROOF]-
>>
>>TODO
>>
>