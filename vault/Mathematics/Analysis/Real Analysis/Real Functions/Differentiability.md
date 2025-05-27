---
title: Differentiability of Real Functions
tags:
  - differentiability
  - real-functions
  - real-analysis
  - analysis
  - mathematics
---

# Differentiability of Real Functions

>[!DEFINITION] Definition: Derivative of a Real Function
>
>Let $f: \mathcal{D} \subseteq \mathbb{R} \to \mathbb{R}$ be a [[Functions of the Real Numbers|real function]].
>
>The **derivative of** $f$ **at** $x_0 \in \mathcal{D}$ is the [[Limits of Real Functions|limit]]
>
>$$
>\lim_{\Delta x \to 0} \frac{f(x_0 + \Delta x) - f(x_0)}{\Delta x},
>$$
>
>if it exists.
>
>>[!NOTATION]
>>
>>$$
>>f'(x_0) \qquad \frac{\mathrm{d}f}{\mathrm{d}x} (x_0) \qquad \frac{\mathrm{d}}{\mathrm{d}x}f(x_0)
>>$$
>>
>
>>[!NOTE] Note: Derivative Function
>>
>>When we say just "the derivative of $f$", we mean the [[Functions of the Real Numbers#Real Functions|function]] which maps every $x \in D$ to $f'(x)$.
>>
>
>>[!DEFINITION] Definition: Higher-Order Derivatives
>>
>>The $k$**-th order derivative** of $f$ is the derivative of the $(k-1)$-th order derivative of $f$:
>> - The $0$**-th order derivative of** $f$ is just $f$ itself;
>> - The **first order derivative of** $f$ is just the aforementioned derivative $f'$;
>> - The **second order derivative of** $f$ is the derivative of $f'$, etc.
>>
>>>[!NOTATION]
>>>
>>>$$
>>>f' \qquad f'' \qquad f''' \qquad f^{\mathrm{IV}} \qquad f^{\mathrm{V}} \qquad \cdots \qquad f^{(n)}
>>>$$
>>>
>>>$$
>>>\frac{\mathrm{d}f}{\mathrm{d}x} \qquad \frac{\mathrm{d}^2 f}{\mathrm{d}x^2} \qquad \frac{\mathrm{d}^3 f}{\mathrm{d}x^3} \qquad \frac{\mathrm{d}^4 f}{\mathrm{d}x^4} \qquad  \frac{\mathrm{d}^5 f}{\mathrm{d}x^5} \qquad \cdots \qquad \frac{\mathrm{d}^n f}{\mathrm{d}x^n}
>>>$$
>>>
>>
>

>[!DEFINITION] Definition: Differentiability
>
>Let $f: \mathcal{D} \subseteq \mathbb{R} \to \mathbb{R}$ be a [[Functions of the Real Numbers|real function]].
>
>We say that a [[Functions of the Real Numbers#Real Functions|real function]] $f$ is **differentiable at** some $x \in \mathcal{D}$ if the derivative of $f$ at $x$, i.e. $f'(x)$, exists.
>
>We say that $f$ is $k$**-times (continuously) differentiable on** $S \subseteq \mathcal{D}$ if its $k$-th order derivative exists (and is [[Continuity|continuous]]).
>

>[!DEFINITION] Definition: Critical Point
>
>We call $x_0 \in \mathcal{D}$ a **critical point** of $f: \mathcal{D} \subseteq \mathbb{R} \to \mathbb{R}$ if $f$ is not [[Differentiability|differentiable]] at $x_0$ or its [[Differentiability|derivative]] at $x_0$ is zero.
>

## Properties

>[!THEOREM]- Theorem: Differentiability $\implies$ Continuity
>
>If $f: D \subseteq \mathbb{R} \in \mathbb{R}$ is [[Differentiability|differentiable]] at $x_0 \in D$, then $f$ is also [[Continuity|continuous]] at $x_0$.
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM]- Mean Value Theorem for Derivatives
>
>If $f: D \to \mathbb{R}$ is [[Continuity|continuous]] on the [[Intervals|closed interval]] $D = [a;b] \subset \mathbb{R}$ and [[Differentiability|differentiable]] on the [[Intervals|open interval]] $(a;b)$, then there exists at least one $x_0 \in (a;b)$ such that
>
>$$
>f'(x_0) = \frac{f(b) - f(a)}{b - a}
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>
>>[!INTUITION]- Intuition: Geometric Meaning
>>
>>The theorem says that there is at least one point $(x_0; f(x_0))$ on the graph of $f$, where the tangent line to $f$ is parallel to the secant line through the points $(a; f(a))$ and $(b; f(b))$.
>>
>>TODO
>>
>

>[!THEOREM]- Theorem: Darboux's Theorem
>
>Let $f: D \to \mathbb{R}$ be a [[Differentiability|differentiable]] [[Functions of the Real Numbers|real function]] on a [[Intervals|closed interval]] $D = [a;b] \subset \mathbb{R}$.
>
>For each $\lambda \in \mathbb{R}$ such that $f'(a) \lt \lambda \lt f'(b)$ or $f'(a) \gt \lambda \gt f'(b)$, there exists some $c \in (a;b)$ such that
>
>$$
>f'(c) = \lambda
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

# Differentiation Rules

>[!THEOREM]- Theorem: Arithmetic Differentiation Rules
>
>If $f,g: D \subseteq \mathbb{R} \to \mathbb{R}$ are [[Differentiability|differentiable]] at $x \in D$, then the following hold:
>
>- Linearity: $[\alpha\, f(x) + \beta\, g(x)]' = \alpha\, f'(x) + \beta\, g'(x)$ for all $\alpha, \beta \in \mathbb{R}$
>- Product Rule: $[f(x)g(x)]' = f'(x)g(x) + f(x)g'(x)$
>- Quotient Rule: $\left[\frac{f(x)}{g(x)}\right]' = \frac{f'(x)g(x)-f(x)g'(x)}{g(x)^2}$ provided that $g(x) \ne 0$
>- General Power Rule: $\left[f(x)^{g(x)}\right]' = f(x)^{g(x)}\left[f'(x)\frac{g(x)}{f(x)} + g'(x)\ln(f(x))\right]$
>
>>[!PROOF]-
>>
>>**Proof of linearity:**
>>
>>$$
>>\begin{align*}[\lambda\, f(x) + \mu\, g(x)]' &= \operatorname*{lim}_{\Delta x\rightarrow0}\frac{\lambda f(x_{0}+\Delta x)+\mu g(x_{0}+\Delta x) - \lambda f(x_{0})-\mu g(x_{0})}{\Delta x}\\ &= \lim_{\Delta x\to 0}\frac{\lambda[f(x_{0}+\Delta x)-f(x_{0})] + \mu[g(x_{0}+\Delta x)-g(x_{0})]}{\Delta x} \\ &= \lim_{\Delta x\to 0}\lambda\frac{f(x_0+\Delta x)-f(x_0)}{\Delta x} + \lim_{\Delta x\to 0}\mu\frac{g(x_0+\Delta x)-g(x_0)}{\Delta x} \\ &= \lambda\lim_{\Delta x\to 0}\frac{f(x_0+\Delta x)-f(x_0)}{\Delta x} + \mu\lim_{\Delta x\to 0}\frac{g(x_0+\Delta x)-g(x_0)}{\Delta x} \\ &= \lambda f'(x_0) + \mu g'(x_0)\end{align*}
>>$$
>>
>

>[!THEOREM]- Theorem: The Chain Rule
>
>If $g: D \subseteq \mathbb{R} \to \mathbb{R}$ is [[Differentiability|differentiable]] at $x \in D$ and $f: g(D) \to \mathbb{R}$ is [[Differentiability|differentiable]] at $g(x)$, then
>
>$$
>[f(g(x))]' = f'(g(x)) \cdot g'(x)
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM]- Theorem: Derivative of the Inverse Function
>
>Let $f: D \subseteq \mathbb{R} \to \mathbb{R}$ be [[Injections, Surjections and Bijections|invertible]].
>
>If $f$ is [[Differentiability|differentiable]] at $f^{-1}(y), y \in f(D)$ and $f'(f^{-1}(y)) \ne 0$, then
>
>$$
>[f^{-1}(y)]' = \frac{1}{f'(f^{-1}(y))}
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

## Common Derivatives


>[!THEOREM]- Theorem: Power Rule
>
>$$
>(x^\alpha)' = \alpha x^{\alpha - 1} \qquad \forall \alpha \in \mathbb{R}
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM]- Theorem: Derivative of Exponential Functions
>
>$$
>(\mathrm{e}^x)' = \mathrm{e}^x
>$$
>
>$$
>(a^x)' = a^x \ln a
>$$
>
>>[!PROOF]-
>>
>>$$
>>\begin{align*}(e^x)' &= \lim_{\Delta x \to 0}\frac{e^{x+\Delta x}-e^x}{\Delta x} = \lim_{\Delta x \to 0}\frac{e^x(e^{\Delta x}-1)}{\Delta x} = e^x\lim_{\Delta x \to 0}\frac{e^{\Delta x}-1}{\Delta x} \\ &= e^x \lim_{\Delta x\to 0}\frac{\displaystyle \lim_{n\to \infty} \left(1+\frac{\Delta x}{n}\right)^n - 1}{\Delta x} = e^x \lim_{\Delta x\to 0} \operatorname*{lim}_{n\rightarrow\infty}\frac{(1+\frac{\Delta x}{n})^{n}-1}{\Delta x} \\ &= e^x \lim_{\Delta x\to 0} \operatorname*{lim}_{n\rightarrow\infty} \frac{\displaystyle 1+n\frac{\Delta x}{n} + \begin{pmatrix}n \\ 2\end{pmatrix}\left(\frac{\Delta x}{n}\right)^{2}+\cdots+\begin{pmatrix}n \\ n-1\end{pmatrix}\left(\frac{\Delta x}{n}\right)^{n-1} + \left(\frac{\Delta x}{n}\right)^n - 1}{\Delta x} \\ &= e^x \lim_{\Delta x\to 0} \operatorname*{lim}_{n\rightarrow\infty} \left(\displaystyle 1 + \begin{pmatrix}n \\ 2\end{pmatrix} \frac{\Delta x}{n^2}+\cdots + \begin{pmatrix} n \\ n-1 \end{pmatrix}\frac{\Delta x^{n-2}}{n^{n-1}} + \frac{\Delta x^{n-1}}{n^n}\right) \\ &= e^x \lim_{n\to \infty}\lim_{\Delta x\to 0} \left(\displaystyle 1 + \underset{\to 0}{\underbrace{\begin{pmatrix}n \\ 2\end{pmatrix} \frac{\Delta x}{n^2}+\cdots + \begin{pmatrix} n \\ n-1 \end{pmatrix}\frac{\Delta x^{n-2}}{n^{n-1}} + \frac{\Delta x^{n-1}}{n^n}}}\right) \\ &= e^x \lim_{n\to\infty} 1 = e^x\end{align*}
>>$$
>>
>>$$
>>\begin{align*}(a^x)' = ((e^{\ln a})^x)' = (e^{x \ln a})' = e^{x\ln a}\ln a = (e^{\ln a})^x \ln a = a^x \ln a\end{align*}
>>$$
>>
>

>[!THEOREM]- Theorem: Derivative of Logarithmic Functions
>
>$$
>(\ln x)' = \frac{1}{x}
>$$
>
>$$
>(\log_a x)' = \frac{1}{x \ln a}
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>