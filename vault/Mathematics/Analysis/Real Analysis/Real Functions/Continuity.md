---
title: Continuity of Real Functions
tags:
  - continuity
  - real-functions
  - real-analysis
  - analysis
  - mathematics
---

# Continuity

>[!DEFINITION] Definition: Continuity of Real Functions
>
>A [[Functions of the Real Numbers|real function]] $f: \mathcal{D} \subseteq \mathbb{R} \to \mathbb{R}$ is **continuous at** $c \in \mathcal{D}$ if its [[Limits of Real Functions|limit]] for $x \to c$ exists and is equal to its value for $c$:
>
>$$
>\lim_{x \to c} f(x) = f(c)
>$$
>
>If $f$ is continuous at every $c \in S \subseteq \mathcal{D}$, then we say that $f$ is **continuous on** $S$. If $S = \mathcal{D}$, then we simply say that $f$ is **continuous**.
>

# Properties

>[!THEOREM]- Theorem: Operations with Continuous Functions
>
>If $f$ and $g$ are two [[Continuity|continuous functions]], then so are
>- $\alpha f + \beta g$ for all $\alpha,\beta \in \mathbb{R}$;
>- $f \cdot g$;
>- $f / g$;
>- $f \circ g$ provided that $g(D) \subseteq D$.
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM]- The Extreme Value Theorem
>
>If $f$ is [[Continuity|continuous]] on the closed interval $[a;b]$, then $f$ attains a minimum and a maximum value, i.e. there exist at least one $x_{\text{of min}} \in [a;b]$ and at least one $x_{\text{of max}} \in [a;b]$ such that
>
>$$
>f(x_{\text{of min}}) \le f(x) \le f(x_{\text{of max}}) \qquad \forall x \in [a;b]
>$$
>
>>[!INTUITION]
>>
>>This theorem says that if a function is continuous on a closed interval, then it has a minimum and a maximum value on it.
>>
>
>TODO: Add diagram
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM]- The Intermediate Value Theorem
>
>If $f$ is [[Continuity|continuous]] on a closed interval $[a;b]$, then for every $y$ between $f(a)$ and $f(b)$, i.e. $\min\{f(a), f(b)\} \le y \le \max\{f(a), f(b)\}$, there exists at least one $x \in [a;b]$ such that $f(x) = y$.
>
>>[!INTUITION]
>>
>>The theorem says that if a function is continuous on a closed interval, then it must generate all values between its minimum and maximum value on said interval.
>>
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM]- Bolzano's Theorem
>
>If $f$ is [[Continuity|continuous]] on a closed interval $[a;b]$ and $f(a) \lt 0$ and $f(b) \gt 0$ (or vice-versa), then there exists at least one $x \in (a;b)$ such that $f(x) = 0$.
>
>>[!PROOF]-
>>
>>This is just a special case of the intermediate value theorem.
>>
>

>[!THEOREM]- Theorem: Integrability of Continuous Functions
>
>If a [[Functions of the Real Numbers#Real Functions|real function]] is [[Continuity|continuous]], then it is also [[Definite Integrals|Riemann-integrable]].
>
>>[!PROOF]-
>>
>>TODO
>>
>

