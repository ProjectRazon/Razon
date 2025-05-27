---
title: Antiderivatives
tags:
  - antiderivatives
  - real-functions
  - real-analysis
  - analysis
  - mathematics
---

# Antiderivatives

>[!DEFINITION] Definition: Antiderivative
>
>An **antiderivative** of the [[Functions of the Real Numbers|real function]] $f: D \subseteq \mathbb{R} \to \mathbb{R}$ is any [[Differentiability|differentiable]] [[Functions of the Real Numbers|function]] $F: D \subseteq \mathbb{R} \to \mathbb{R}$ whose [[Differentiability|derivative]] is $f$.
>
>$$
>F'(x) = f(x)
>$$
>
>>[!THEOREM] Theorem: Family of Antiderivatives
>>
>>Let $F$ be an [[Antiderivatives|antiderivative]] of $f$.
>>
>>Any other [[Differentiability|differentiable]] [[Functions of the Real Numbers|function]] $\mathcal{F}: D \subseteq \mathbb{R} \to \mathbb{R}$ is also an [[Antiderivatives|antiderivative]] of $f$ if and only if there is some constant $C \in \mathbb{R}$ such that
>>
>>$$\mathcal{F}(x) = F(x) + C \qquad \forall x \in D$$
>>
>>>[!PROOF]-
>>>
>>>TODO
>>>
>>
>

## Indefinite Integrals

>[!DEFINITION] Definition: Indefinite Integral
>
>The **indefinite integral** of a [[Functions of the Real Numbers|real function]] $f$ is the [[Sets|set]] of all [[Antiderivatives]] of $f$.
>
>$$
>\int f(x) \mathop{\mathrm{d}x} \overset{\text{def}}{=} \{F \mid F' = f\}
>$$
>
>>[!NOTATION]-
>>
>>The notation $\int f(x) \mathop{\mathrm{d}x}$ is often used to denote a particular [[Antiderivatives|antiderivative]] of $f$ or simply the process of [[Integration]], as well.
>>
>>Since [[Antiderivatives]] are unique up to a constant, if we know a particular [[Antiderivatives|antiderivative]] $F$ of $f$, we write 
>>
>>$$
>>\int f(x) \mathop{\mathrm{d}x} = F(x) + C
>>$$
>>
>>for the indefinite integral.
>>
>

>[!THEOREM]
>
>If $f$ and $g$ are [[Continuity|continuous]] on a closed interval $[a;b]$, then for all $\alpha, \beta \in \mathbb{R}$
>
>$$\int \alpha \, f(x) + \beta \, g(x) \mathop{\mathrm{d}x} = \alpha \int f(x) \mathop{\mathrm{d}x} + \beta \int g(x) \mathop{\mathrm{d}x}$$
>
>>[!PROOF]-
>>
>>Let $F(x)$ be an [[Antiderivatives|antiderivative]] $f(x)$ and $G(x)$ be an [[Antiderivatives|antiderivative]] of $g(x)$.
>> 
>>Let's examine the [[Differentiability|derivative]] of the right-hand side.
>> 
>>$$
>>\frac{\mathrm{d}}{\mathrm{d}x}\left(\lambda \int f(x) \mathop{\mathrm{d}x} + \mu \int g(x) \mathop{\mathrm{d}x}\right)
>>$$
>> 
>>Since [[Differentiability|differentiation]] is linear, we have
>> 
>>$$
>>\begin{align*}\frac{\mathrm{d}}{\mathrm{d}x}\left(\lambda \int f(x) \mathop{\mathrm{d}x} + \mu \int g(x) \mathop{\mathrm{d}x}\right) &= \lambda\frac{\mathrm{d}}{\mathrm{d}x}\int f(x) \mathop{\mathrm{d}x} + \mu \frac{\mathrm{d}}{\mathrm{d}x}\int g(x) \mathop{\mathrm{d}x} \\ &= \lambda\frac{\mathrm{d}}{\mathrm{d}x} F(x) + \mu\frac{\mathrm{d}}{\mathrm{d}x}G(x) \\ &= \lambda f(x) + \mu g(x)\end{align*}
>>$$
>> 
>>This means that $\lambda F(x) + \mu G(x)$ is an [[Antiderivatives|antiderivative]] of $\lambda \, f(x) + \mu \, g(x)$. All other [[Antiderivatives]] of $\lambda \, f(x) + \mu \, g(x)$ can be expressed as $\lambda F(x) + \mu G(x) + C$ for some $C\in \mathbb{R}$.
>>
>

>[!THEOREM] Theorem: Integration by Parts
>
>If $u$ and $v$ are [[Differentiability|continuously differentiable]], then
>
>$$\int u(x) v'(x) \mathop{\mathrm{d}x} = u(x)v(x) + \int u'(x)v(x) \mathop{\mathrm{d}x}$$
>
>>[!PROOF]-
>>
>>TODO

>[!THEOREM] Theorem: Integration by Substitution
>
>$$
>\int f(\underset{u}{\underbrace{g(x)}})\underset{\mathop{\mathrm{d}u}}{\underbrace{g'(x) \mathop{\mathrm{d}x}}} = \int f(u) \mathop{\mathrm{d}u}
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM]
>
>$$
>\int \frac{f'(x)}{f(x)} \mathop{\mathrm{d}x} = \ln (f(x)) + C, \qquad f(x) \gt  0
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Antiderivatives of Polynomial Functions
>
>$$
>\int x^\alpha \mathop{\mathrm{d}x} = \frac{1}{\alpha + 1} x^{\alpha + 1} + C \qquad \forall \alpha \ne -1 \in \mathbb{R}
>$$
>
>$$
>\int (ax + b)^\gamma \mathop{\mathrm{d}x} = \frac{(ax+b)^{\gamma+1}}{a(\gamma +1)} + C
>$$
>
>>[!PROOF]-
>>
>>TODO
>

>[!THEOREM] Theorem: Antiderivatives of Rational Functions
>
>$$\int \frac{c}{ax+b} \mathop{\mathrm{d}x} = \frac{c}{a} \ln |ax+b| + C$$
>
>For all $n \in \mathbb{N}$ and $a \in \mathbb{R}$:
>
>$$\int \frac{\mathop{\mathrm{d}x}}{(x-a)^n} = \begin{cases}\displaystyle \ln |x-a| + C, \text{ if } n = 1 \\\displaystyle -\frac{1}{(n-1)(x-a)^{n-1}} + C, \text{ if } n\ge 2 \end{cases}$$
>
>For all $a,b \in \mathbb{R}$ and all polynomials $x^2 + px + q$ with $p^2 -4q \lt 0$:
>
>$$\int\frac{\mathop{\mathrm{d}x}}{x^2+px+q} = \frac{2}{\sqrt{4q-p^2}}\arctan \frac{2x+p}{\sqrt{4q-p^2}} + C$$
> 
>$$\int\frac{ax+b}{x^2+px+q}\mathop{\mathrm{d}x} = \frac{a}{2}\ln (x^2+px+q)- \left(b-\frac{ap}{2}\right)\int\frac{\mathop{\mathrm{d}x}}{x^2+px+q}$$
>
>For all $n\ge 2 \in \mathbb{N}$ and all polynomials $x^2+px+q$ with $p^2-4q\lt 0$:
>
>$$\int\frac{\mathop{\mathrm{d}x}}{(x^2+px+q)^n} = \frac{2x+p}{(n-1)(4q-p^2)(x^2+px+q)^{n-1}}+\frac{2(2n-3)}{(n-1)(4q-p^2)}\int\frac{\mathop{\mathrm{d}x}}{(x^2+px+q)^{n-1}}$$
> 
>$$\int\frac{ax+b}{(x^2+px+q)^n}\mathop{\mathrm{d}x} = -\frac{a}{2(n-1)(x^2+px+q)^{n-1}}+\left(b-\frac{ap}{2}\right)\int\frac{\mathop{\mathrm{d}x}}{(x^2+px+q)^{n-1}}$$
>
>>[!PROOF]-
>>
>>TODO
>

>[!THEOREM] Theorem: Antiderivatives of Exponential Functions
>
>$$\int e^{\alpha x} \mathop{\mathrm{d}x} = \frac{1}{\alpha}e^{\alpha x} + C$$
>
>$$\int f'(x) e^{f(x)} \mathop{\mathrm{d}x} = e^{f(x)} + C$$
>
>$$\int a^x \mathop{\mathrm{d}x} = \frac{a^x}{\ln a} + C$$
>
>$$\int e^x (f(x) + f'(x)) \mathop{\mathrm{d}x} = e^x f(x) + C$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Antiderivatives of Logarithmic Functions
>
>$$\int \ln x \mathop{\mathrm{d}x} = x (\ln x - 1) + C$$
>
>$$\int \log_a x \mathop{\mathrm{d}x} = \frac{x}{\ln a} (\ln x - 1) + C$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Antiderivatives of Trigonometric Functions
>
>$$
>\int \sin x \mathop{\mathrm{d}x} = -\cos x + C
>$$
>
>$$
>\int \cos x \mathop{\mathrm{d}x} = \sin x + C
>$$
>
>$$
>\int \tan x \mathop{\mathrm{d}x} = - \ln |\cos x| + C
>$$
>
>$$
>\int \cot x \mathop{\mathrm{d}x} = \ln |\sin x| + C
>$$
>
>$$
>\int \arctan x \mathop{\mathrm{d}x} = x \arctan x - \frac{1}{2}\ln (x^2 + 1) + C
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>