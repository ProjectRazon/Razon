---
title: Infinite Limits of Complex Functions
tags:
    - limits
    - complex-functions
    - complex-analysis
    - analysis
    - mathematics
---

# Infinite Limits

>[!NOTATION] Notation: Infinite Limits
>
>Let $f: \mathcal{N} \subseteq \mathbb{C} \to \mathbb{C}$ be a [[index|complex function]] defined on some [[Topology of the Complex Plane#Neighborhoods|deleted neighborhood]] of $c \in \mathbb{C}$.
>
>We write
>
>$$
>\lim_{z \to c} f(z) = \infty
>$$
>
>if, for each $M \gt 0$, there exists some $\delta \gt 0$ such that
>
>$$
>0 \lt |z - c| \lt \delta \implies |f(z)| \gt M \qquad \forall z \in \mathcal{N}.
>$$
>

## Characterizations

>[!THEOREM]- Theorem: Infinite Limit via Modulus
>
>Let $f: \mathcal{N} \subseteq \mathbb{C} \to \mathbb{C}$ be a [[index|complex function]] defined on some [[Topology of the Complex Plane#Neighborhoods|deleted neighborhood]] of $c \in \mathbb{C}$.
>
>The [[Infinite Limits|limit]] of $f$ for $z \to c$ is $\infty$ if and only if the [[Infinite Limits|limit]] of $|f|$ for $z \to c$ is $\infty$.
>
>$$
>\lim_{z \to c} f(z) = \infty \iff \lim_{z \to c} |f(z)| = \infty
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

# Infinite Limits at Infinity

>[!NOTATION] Notation: Limits at Infinity
>
>Let $f: \mathcal{D} \subseteq \mathbb{C} \to \mathbb{C}$ be a [[index|complex function]] such that $\mathcal{D}$ is the [[Complement]] of some [[Topology of the Complex Plane|open ball]] around $0$.
>
>We write
>
>$$
>\lim_{z \to \infty} f(z) = \infty
>$$
>
>if for each $M \gt 0$ there exists some $R \gt 0$ such that
>
>$$
>|z| \gt R \implies |f(z)| \gt M \qquad \forall z \in \mathcal{D}.
>$$ 
>

>[!WARNING]
>
>Even though we use limit notation for infinite limits and infinite limits at infinity, we never say that these limits *exist*, since they are not complex numbers.
>

## Characterizations

>[!THEOREM]- Theorem: Infinite Limit via Absolute Value
>
>Let $f: \mathcal{D} \subseteq \mathbb{C} \to \mathbb{C}$ be a [[index|complex function]] such that $\mathcal{D}$ is the [[Complement]] of some [[Topology of the Complex Plane|open ball]] around $0$.
>
>The [[Infinite Limits|limit]] of $f$ for $z \to \infty$ is $\infty$ if and only if the  [[Infinite Limits|limit]] of $|f|$ for $|z| \to \infty$ is $\infty$.
>
>$$
>\lim_{z \to \infty} f(z) = \infty \iff \lim_{|z| \to \infty } |f(z)| = \infty
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

# Converting Limits

>[!THEOREM]- Theorem: Infinite Limit $\leftrightarrow$ Infinite Limit at Infinity
>
>Let $f: \mathcal{D} \subseteq \mathbb{C} \to \mathbb{C}$ be a [[index|complex function]] such that $\mathcal{D}$ is the [[Complement]] of some [[Topology of the Complex Plane|open ball]] around $0$.
>
>The [[Infinite Limits#Infinite Limits At Infinity|limit]] of $f$ for $z \to \infty$ is $\infty$ if and only if the [[Infinite Limits#Infinite Limits|limit]] of $f\left( \frac{1}{z} \right)$ for $z \to 0$ is $\infty$.
>
>$$
>\lim_{z \to \infty} f(z) = \infty \iff \lim_{z \to 0} f\left( \frac{1}{z} \right) = \infty
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

# Bibliography

1. N. H. Asmar, L. Grafakos, "Analytic Functions," in *Complex Analysis with Applications*, Columbia, USA: Springer, 2018