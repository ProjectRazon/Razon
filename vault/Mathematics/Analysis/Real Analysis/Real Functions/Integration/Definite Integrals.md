---
title: Improper Integrals
tags:
  - integration
  - real-functions
  - real-analysis
  - analysis
  - mathematics
---

# Riemann-Sums

>[!DEFINITION] Definition: Riemann Sum
>
>Let $f: \mathcal{D} \subseteq \mathbb{R} \to \mathbb{R}$ be a [[Functions of the Real Numbers|real function]], let $I = [a;b] \subseteq \mathcal{D}$ be a closed interval and let $x_0 \lt x_1 \lt \cdots \lt x_n \in I$.
>
>A **Riemann sum** of $f$ over $I$ is any sum of the form
>
>$$
>\sum_{i = 1}^n f(x_i^\ast) \Delta x_i,
>$$
>
>where $\Delta x_i = (x_i - x_{i-1})$ and $x_i^\ast \in [x_{i-1};x_i]$.
>
>>[!NOTE] Note: Choice of $x_i^\ast$
>>
>>Different choices for $x_i^\ast$ yield different Riemann sums.
>
>>[!DEFINITION]- Definition: Left Riemann Sum
>>
>>A **left Riemann sum** has $x_i^\ast = x_{i-1}$ for all $i$.
>>
>
>>[!DEFINITION]- Definition: Right Riemann Sum
>>
>>A **right Riemann sum** has $x_i^\ast = x_{i}$ for all $i$.
>>
>
>>[!DEFINITION]- Definition: Left Riemann Sum
>>
>>A **middle Riemann sum** has $\displaystyle x_i^\ast = \frac{x_{i-1} + x_i}{2}$ for all $i$.
>>
>

# Definite Integrals

>[!DEFINITION] Definition: Riemann-Integrability
>
>A [[Functions of the Real Numbers|real function]] $f: \mathcal{D} \subseteq \mathbb{R} \to \mathbb{R}$ is **Riemann-integrable** on the interval $I = [a;b] \subseteq \mathcal{D}$ iff all of its [[Definite Integrals|Riemann sums]] on $I$ have the same [[Limits of Real Functions|limit]] as $\Delta x_i$ approaches $0$.
>
>$$
>\lim_{\Delta x_i\to 0}\sum_{i=1}^n f(x_i^\ast)\Delta x_i = S \in \mathbb{R}
>$$
>
>>[!DEFINITION] Definition: Definite Integral
>>
>>If the aforementioned [[Limits of Real Functions|limit]] exists, then we call it the **definite integral** of $f$ over $I$.
>>
>>>[!NOTATION]-
>>>
>>>The most common notation for the definite integral is
>>>
>>>$$
>>>\int_a^b f(x) \mathop{\mathrm{d}x}
>>>$$
>>>
>>>The upside of this notation is that it clearly shows where the integrand, i.e. the thing being integrated, begins and where it ends. This is not very useful when we are referring to $f$ by its name, but it helps to remove ambiguity when we substitute $f$ with an expression such as $\displaystyle \int_a^b x^3 + \ln x \mathop{\mathrm{d}x}$.
>>>
>>>Its main downside is that it forces us to assign a symbol to the function's argument which is redundant and can even be confusing in some contexts where we refer to $f$ by its name. In particular, it is irrelevant whether we write $\displaystyle \int_a^b f(x) \mathop{\mathrm{d}x}$ or $\displaystyle \int_a^b f(y) \mathop{\mathrm{d}y}$ or $\displaystyle \int_a^b f(\omega) \mathop{\mathrm{d}\omega}$, hence we can shorten the notation to just
>>>
>>>$$
>>>\qquad \int_a^b f
>>>$$
>>>
>>>The main downside of this notation is that it implies that the order of $a$ and $b$ matters, which is not the case - what matters is the actual [[Sets|set]] which $[a;b]$ represents. To emphasise this, we can use the following notations:
>>>
>>>$$
>>>\int_{[a;b]} f \qquad \int_D f
>>>$$
>>>
>>>In the latter case, we can also add $\mathrm{d}D$ to clarify where the integrand begins and ends, such as
>>>
>>>$$
>>>\int_D f \mathop{\mathrm{d}D}
>>>$$
>>>
>>>All of these notations are useful in specific contexts and less so in others.
>>>
>>
>>>[!NOTATION]- Notation: Definite Integrals with Special Bounds
>>>
>>>A common convention is to define the notations
>>>
>>>$$
>>>\int_b^a f = -\int_a^b f
>>>$$
>>>
>>>and
>>>
>>>$$
>>>\int_c^c f = 0
>>>$$
>>>
>>>for each $c \in [a;b]$. This is merely notation which makes the formulation of many theorems easier and more natural.
>>>
>>
>>>[!NOTE]- Note: Definite Integrals over Non-Interval Domains
>>>
>>>If $I$ is not an interval but can be represented as the [[Operations with Collections#Union|union]] of finitely many closed intervals $I_1 \cup \cdots \cup I_n$ such that each interval overlaps with at most two other intervals and only at the endpoints, then we define the definite integral of $f$ over $I$ as the sum of $f$'s definite integrals over $I_1, \dotsc, I_n$:
>>>
>>>$$
>>>\int_I f = \int_{I_1} f \mathop{\mathrm{d}I_1} + \cdots + \int_{I_n} f \mathop{\mathrm{d}I_n} 
>>>$$
>>>
>>
>

## Properties

>[!THEOREM]- Theorem: Linearity of the Definite Integral
>
>The [[Definite Integrals|definite integral]] is linear - if $f$ and $g$ are [[Functions of the Real Numbers|real functions]] which are [[Definite Integrals|Riemann-integrable]] on $I$, then for all $\alpha,\beta \in \mathbb{R}$
>
>$$
>\int_I \alpha \, f(x) + \beta\, g(x) \mathop{\mathrm{d}x} = \alpha \int_I f(x) \mathop{\mathrm{d}x} + \beta \int_I g(x) \mathop{\mathrm{d}x}
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM]- Theorem: Integration by Parts
>
>Let $f$ and $g$ are [[Functions of the Real Numbers|real functions]] which are defined on the closed interval $[a;b]$ and are [[Definite Integrals|continuously differentiable]] on the open interval $(a;b)$, then they are [[Definite Integrals|Riemann-integrable]] on $[a;b]$ with
>
>$$
>\int_a^b f(x) g'(x) \mathop{\mathrm{d}x} = f(b)g(b) - f(a)g(a) - \int_a^b f'(x)g(x) \mathop{\mathrm{d}x}
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM]- Theorem: Substitution
>
>Let $g: [a;b] \to \mathbb{R}$ and $f: [c;d] \to \mathbb{R}$ be [[Functions of the Real Numbers|real functions]] such that the [[Functions|image]] of $g$ is a [[Sets|subset]] of $[c;d]$, i.e. $g([a;b]) \subseteq [c;d]$.
>
>If $f$ is [[Continuity|continuous]] and $g$ is [[Differentiability|continuously differentiable]], then the following [[Definite Integrals|definite Integral]] can be solved via substitution.
>
>$$
>\int_a^b f(g(x))g'(x) \mathop{\mathrm{d}x} = \int_{g(a)}^{g(b)} f(u) \mathop{\mathrm{d}u}
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM]- Mean Value Theorem for Definite Integrals
>
>Let $f,g: D \to \mathbb{R}$ be [[Functions of the Real Numbers|real functions]] on a [[Intervals|closed interval]] $D = [a;b] \subset \mathbb{R}$.
>
>If $f$ and $g$ are [[Continuity|continuous]] and $g(x) \gt 0$ for all $x\in D$, then there exists some $\xi \in (a;b)$ such that
>
>$$
>\int_a^b f(x)g(x) \mathop{\mathrm{d}x} = f(\xi)\int_a^b g(x) \mathop{\mathrm{d}x}
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>
>>[!TIP]- Tip: $g(x) = 1$
>>
>>In the case of $g(x) = 1$ for all $x$, the mean value theorem simplifies to
>>
>>$$
>>\int_a^b f(x) \mathop{\mathrm{d}x} = f(\xi)(b - a)
>>$$
>>

>[!THEOREM]- Theorem: Integrability of the Absolute Value
>
>Let $f$ be a [[Functions of the Real Numbers|real function]].
>
>If $f$ is [[Definite Integrals|Riemann-integrable]] on $l$, then so is its absolute value $|f|$ and
>
>$$
>\left|\int_I f(x) \mathop{\mathrm{d}x} \right| \le \int_I |f(x)| \mathop{\mathrm{d}x}
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

# Improper Integrals

>[!NOTATION] Notation: Improper Integrals
>
>An **improper integral** is a [[Definite Integrals|definite integral]] for a [[Functions of the Real Numbers|real function]] $f: D \subseteq \mathbb{R} \to \mathbb{R}$ on an open or a semi-open interval $D$:
>- If $D = [[Limits of Real Functions|a;b)$ where $a, b \in \mathbb{R}$, the improper integral is defined through the [left-sided limit]]
>
>$$\int_a^b f(x) \mathop{\mathrm{d}x} \overset{\text{def}}{=} \lim_{\beta \to b^-} \int_a^\beta f(x) \mathop{\mathrm{d}x}$$
>
>- If $D = (a;b]$ where $a, b \in \mathbb{R}$, the improper integral is defined through the [[Limits of Real Functions|right-sided limit]]
>
>$$\int_a^b f(x) \mathop{\mathrm{d}x} \overset{\text{def}}{=} \lim_{\alpha \to a^+} \int_\alpha^b f(x) \mathop{\mathrm{d}x}$$
>
>- If $D = [[Limits of Real Functions|a;\infty)$ where $a \in \mathbb{R}$, the improper integral is defined through the [limit]]
>
>$$\int_a^\infty f(x) \mathop{\mathrm{d}x} \overset{\text{def}}{=} \lim_{\beta \to \infty} \int_a^\beta f(x) \mathop{\mathrm{d}x}$$
>
>- If $D = (-\infty;b]$ where $b \in \mathbb{R}$, the improper integral is defined through the [[Limits of Real Functions|limit]]
>
>$$\int_{-\infty}^b f(x) \mathop{\mathrm{d}x} \overset{\text{def}}{=} \lim_{\alpha \to -\infty} \int_\alpha^b f(x) \mathop{\mathrm{d}x}$$
>
>- If $D = (-\infty;\infty)$, then for any choice of $c \in \mathbb{R}$ the improper integral is defined as
>
>$$\int_{-\infty}^\infty f(x)\mathop{\mathrm{d}x} \overset{\text{def}}{=} \int_{-\infty}^c f(x)\mathop{\mathrm{d}x} +\int_c^\infty f(x)\mathop{\mathrm{d}x}$$
>
>If the respective limit exists, then the improper integral is said to **converge** or simply **exist**. Otherwise, it **diverges** or does **not exist**.
>

## Convergence Criteria

>[!THEOREM]-
>
>Let $f,g: [[Definite Integrals|a;\infty) \to \mathbb{R}$ be [Riemann-integrable]] on every closed interval $[a;b]$ where $a \le b$.
>
>If $|f(x)| \le g(x)$ for all $x \in [[Definite Integrals#Improper Integrals|a;\infty)$ and the [integral]] $\int_a^\infty g(x) \mathop{\mathrm{d}x}$ converges, then $\int_a^\infty f(x) \mathop{\mathrm{d}x}$ also converges.
>
>>[!PROOF]-
>>
>>TODO


>[!THEOREM]-
>
>Let $f,g: (-\infty;b] \to \mathbb{R}$ be [[Definite Integrals|Riemann-integrable]] on every closed interval $[a;b]$ where $a \le b$.
>
>If $|f(x)| \le g(x)$ $x \in [[Definite Integrals#Improper Integrals|a;\infty)$ the [integral]] $\int_{-\infty}^b g(x) \mathop{\mathrm{d}x}$ converges, then $\int_{-\infty}^b f(x) \mathop{\mathrm{d}x}$ also converges.
>
>>[!PROOF]-
>>
>>TODO
>

# Bibliography