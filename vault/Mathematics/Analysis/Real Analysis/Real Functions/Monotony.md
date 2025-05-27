---
title: Monotony of Real Functions
tags:
  - monotony
  - real-functions
  - real-analysis
  - analysis
  - mathematics
---

# Monotony

>[!DEFINITION] Definition: Increasing Function
>
>A [[Functions of the Real Numbers|real function]] $f: D \subseteq \mathbb{R} \to \mathbb{R}$ is **increasing** if, for all $x_1, x_2 \in D$,
>
>$$
>x_1 \lt x_2 \implies f(x_1) \le f(x_2).
>$$
>
>>[!DEFINITION] Definition: Strictly Increasing Function
>>
>>A [[Functions of the Real Numbers|real function]] $f: D \subseteq \mathbb{R} \to \mathbb{R}$ is **strictly increasing** if, for all $x_1, x_2 \in D$,
>>
>>$$
>>x_1 \lt x_2 \implies f(x_1) \lt f(x_2).
>>$$
>>
>

>[!DEFINITION] Definition: Decreasing Function
>
>A [[Functions of the Real Numbers|real function]] $f: D \subseteq \mathbb{R} \to \mathbb{R}$ is **decreasing** if, for all $x_1, x_2 \in D$,
>
>$$
>x_1 \lt x_2 \implies f(x_1) \ge f(x_2).
>$$
>
>>[!DEFINITION] Definition: Strictly Decreasing Function
>>
>>A [[Functions of the Real Numbers|real function]] $f: D \subseteq \mathbb{R} \to \mathbb{R}$ is **strictly decreasing** if, for all $x_1, x_2 \in D$,
>>
>>$$
>>x_1 \lt x_2 \implies f(x_1) \gt f(x_2).
>>$$
>>
>

>[!DEFINITION] Definition: Monotonic Function
>
>A [[Functions of the Real Numbers|real function]] is **monotonic** if it is (strictly) increasing or (strictly) decreasing.
>

## Criteria

>[!THEOREM] Theorem: Monotony of Real Functions
>
>Let $f: D \to \mathbb{R}$ be a [[Functions of the Real Numbers|real function]] which is [[Continuity|continuous]] on a [[Intervals|closed interval]] $D = [a;b] \subset \mathbb{R}$ [[Differentiability|differentiable]] on the [[Intervals|open interval]] $(a;b)$:
>- $f$ is [[Monotony|increasing]] if and only if $f'(x) \ge 0$ for all $x \in (a;b)$;
>- $f$ is [[Monotony|strictly increasing]] if and only if $f'(x) \gt 0$ for all $x \in (a;b)$;
>- $f$ is [[Monotony|decreasing]] if and only if $f'(x) \le 0$ for all $x \in (a;b)$;
>- $f$ is [[Monotony|strictly decreasing]] if and only if $f'(x) \lt 0$ for all $x \in (a;b)$.
>
>>[!PROOF]-
>>
>>TODO
>>
>

## Properties

>[!THEOREM]- Theorem: Bijectivity of Real Monotonous Functions
>
>Let $f: I \subseteq \mathbb{R} \to \mathbb{R}$ be a [[Functions of the Real Numbers|real function]].
>
>If $f$ is [[Continuity|continuous]] and [[Monotony|strictly monotonous]], then $f$ is a [[Injections, Surjections and Bijections|bijective]] between $I$ and its [[Functions|image]] $f(I)$.
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM]- Theorem: Inverses of Strictly Monotonous Real Functions
>
>Let $f: I \subseteq \mathbb{R} \to \mathbb{R}$ be a [[Functions of the Real Numbers|real function]].
>
>If $f$ is [[index|continuous]] and [[Monotony|strictly increasing]] (strictly decreasing), then its [[Injections, Surjections and Bijections|inverse]] $f^{-1}: f(I) \to I$ is continuous and strictly increasing (strictly decreasing).
>
>>[!PROOF]-
>>
>>Suppose that $f$ is strictly increasing. To prove that $f^{-1}$ is strictly decreasing, observe two $x_1,x_2 \in I$ with $x_1 \lt x_2$. Since $f$ is strictly increasing, we have $f(x_1) \lt f(x_2)$. Let $y_1 = f(x_1)$ and $y_2 = f(x_2)$, i.e. $y_1 \lt y_2$. Therefore, $f^{-1}(y_1) = x_1$ and $f^{-1}(y_2) = x_2$ and so $f^{-1}(y_1) \lt f^{-1}(y_2)$ for $y_1 \lt y_2$ which means that $f^{-1}$ is strictly increasing. The proof is analogous for when $f$ is strictly decreasing.
>>
>>
>>
>

>[!THEOREM]- Theorem: Integrability of Monotone Functions
>
>Every [[Monotony|monotone]] [[Functions of the Real Numbers|real function]] on a closed interval is also [[Definite Integrals|Riemann-integrable]] on it.
>
>>[!PROOF]-
>>
>>TODO
>>
>