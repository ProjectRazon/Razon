---
title: Asymptotes of Real Functions
tags:
  - asymptotes
  - real-functions
  - real-analysis
  - analysis
  - mathematics
---

# Asymptotes

>[!DEFINITION] Definition: Vertical Asymptote
>
>Let $f: D \subseteq \mathbb{R} \to \mathbb{R}$ be a [[Functions of the Real Numbers|real function]].
>
>We say that $f$ has a **vertical asymptote** at $x = c \in \mathbb{R}$ if it has at least one [[Limits of Real Functions|infinite one-sided limit]] at $c$, i.e. at least one of the following holds:
>
>- $\displaystyle \lim_{x \to c^-} f(x) = -\infty$
>- $\displaystyle \lim_{x \to c^+} f(x) = -\infty$
>- $\displaystyle \lim_{x \to c^-} f(x) = \infty$ 
>- $\displaystyle \lim_{x \to c^+} f(x) = \infty$
>
>>[!INTUITION]-
>>
>>Intuitively, this definition means that the value of $f(x)$ gets closer and closer to $- \infty$ or $+ \infty$ as $x$ approaches $c$ either from the left or from the right.
>>
>

>[!DEFINITION] Definition: Horizontal Asymptote
>
>Let $f: D \subseteq \mathbb{R} \to \mathbb{R}$ be a [[Functions of the Real Numbers|real function]].
>
>We say that $f$ has a **horizontal asymptote** $y = a \in \mathbb{R}$ if the [[Limits of Real Functions|limit]] of $f$ as $x$ approaches positive or negative infinity is $a$, i.e. if at least one of the following holds:
>
>- $\displaystyle \lim_{x \to -\infty} f(x) = a$
>- $\displaystyle \lim_{x \to \infty} f(x) = a$
>
>>[!INTUITION]-
>>
>>Intuitively, this definition means that the value of $f(x)$ gets closer and closer to $a$ as $x$ approaches either positive or negative infinity.
>>
>

>[!DEFINITION] Definition: Oblique Asymptote
>
>Let $f: D \subseteq \mathbb{R} \to \mathbb{R}$ be a [[Functions of the Real Numbers|real function]].
>
>The line $y = ax + b$ is an **oblique** or **slanted asymptote** of $f$ if at least one of the following is true:
>- $\displaystyle \lim_{x \to -\infty} [f(x) - (ax + b)] = 0$
>- $\displaystyle \lim_{x \to \infty} [f(x) - (ax + b)] = 0$
>
>>[!INTUITION]-
>>
>>Intuitively, this definition means $f(x)$ gets closer and closer to the line $y = ax + b$ as $x$ approaches either positive or negative infinity.
>>
>

## Properties

>[!THEOREM] Theorem: Oblique Asymptotes
>
>Let $f$ be a [[Functions of the Real Numbers|real function]].
>
>The [[Straight Line]] $y = ax + b$ is an [[Asymptotes|asymptote]] of $f$ if and only if the [[Limits of Real Functions|limits]] $\lim_{x \to \pm \infty} \frac{f(x)}{x}$ and $\lim_{x \to \pm \infty} (f(x) - ax)$ exist and
>
>$$
>\begin{align*}
>a &= \lim_{x \to \pm \infty} \frac{f(x)}{x} \\
>
>\\
>
>b &= \lim_{x \to \pm \infty} (f(x) - ax)
>\end{align*}
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>