---
title: Limits of Complex Functions
tags:
    - limits
    - complex-functions
    - complex-analysis
    - analysis
    - mathematics
---

# Limits

>[!DEFINITION] Definition: Limit of a Complex Function
>
>Let $f: \mathcal{D} \subseteq \mathbb{C} \to \mathbb{C}$ be a [[index|complex function]] and let $c \in \mathbb{C}$ be an [[Accumulation Point]] of $\mathcal{D}$.
>
>We say that $L$ is the **limit** of $f$ as $z$ approaches $c$ iff for each $\varepsilon \gt 0$ there exists some $\delta \gt 0$ such that, for all $z \in \mathcal{D}$,
>
>$$
>0 \lt |z - c| \lt \delta \implies |f(z) - L| \lt \varepsilon.
>$$
>
>>[!NOTATION]
>>
>>Most commonly, the limit is denoted by
>>
>>$$
>>\lim_{z \to c} f(z) = L \qquad 
>>$$
>>
>>In text, one also writes "$f(z) \to L$ as $z \to c$". Sometimes, one might also encounter $f(z) \underset{z \to c}{\longrightarrow} L$ and $f(z) \overset{z \to c}{\longrightarrow} L$.
>>
>
>>[!NOTE] Note: Existence of a Limit
>>
>>We say that the limit of $f$ as $z$ approaches $c$ *exists* if and only if there is some $L \in \mathbb{C}$ such that $\lim_{z \to c} f(z) = L$.
>>
>

>[!THEOREM] Theorem: Uniqueness of the Limit
>
>Let $f: \mathcal{D} \subseteq \mathbb{C} \to \mathbb{C}$ be a [[index|complex function]] and let $c \in \mathbb{C}$ be an [[Accumulation Point]] of $\mathcal{D}$.
>
>If the [[Limits|limit]] of $f$ exists for $z \to c$, then it is unique, i.e. if $\lim_{z \to c} f(z) = L \in \mathbb{C}$ and $\lim_{z \to c} f(z) = M \in \mathbb{C}$, then $L = M$.
>
>>[!PROOF]-
>>
>>TODO
>>
>

## Characterizations

>[!THEOREM]-
>
>Let $f: \mathcal{D} \subseteq \mathbb{C} \to \mathbb{C}$ be a [[index|complex function]] and let $c \in \mathbb{C}$ be an [[Accumulation Point]] of $\mathcal{D}$.
>
>A number $L \in \mathbb{C}$ is the [[Limits|limit]] of $f$ for $z \to c$ if and only if
>
>$$
>\lim_{z \to c} |f(z) - L| = 0
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM]- Theorem: Component-wise Limits
>
>Let $f: \mathcal{D} \subseteq \mathbb{C} \to \mathbb{C}$ be a [[index|complex function]], let $c \in \mathbb{C}$ be an [[Accumulation Point]] of $\mathcal{D}$.
>
>A number $L \in \mathbb{C}$ is the [[Limits|limit]] of $f$ for $z \to c$ if and only if the [[Limits]] of its [[Complex-Valued Functions|real]] and [[Complex-Valued Functions|imaginary]] parts for $z \to c$ are, respectively, $\operatorname{Re} (L)$ and $\operatorname{Im} (L)$.
>
>$$
>\lim_{z \to c} f(z) = L \iff \lim_{z \to c} \operatorname{Re} f (z) = \operatorname{Re} (L) \qquad \text{and} \qquad \lim_{z \to c}\operatorname{Im} f (z) = \operatorname{Im} (L)
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

## Properties

>[!THEOREM]- Theorem: Operations with Limits
>
>Let $f, g: \mathcal{D} \subseteq \mathbb{C} \to \mathbb{C}$ be [[Complex Functions]] and let $c \in \mathbb{C}$ be an [[Accumulation Point]] of $\mathcal{D}$.
>
>If the [[Limits]] $\displaystyle \lim_{z \to c} f(z)$ and $\displaystyle \lim_{z \to c} g(z)$ exist, then
>
>$$
>>\lim_{z\to c} \left( \alpha f(z) + \beta g(z) \right) = \alpha \lim_{z \to c} f(z) + \beta \lim_{z \to c} g(z) \qquad \forall \alpha, \beta \in \mathbb{C}
>$$
>
>Moreover, if there also exists some [[Topology of the Complex Plane|open ball]] around $c$ on which $f$ and $g$ are [[Boundedness|bounded]], then
>
>$$
>\begin{align*}
>
>&\lim_{z \to c} \left(f(z) g(z)\right) = \left(\lim_{z \to c} f(z)\right) \cdot \left(\lim_{z \to c} g(z)\right) \\
>
>\\
>
>&\lim_{z \to c} \frac{f(z)}{g(z)} = \frac{\displaystyle \lim_{z \to c} f(z)}{\displaystyle \lim_{z \to c} g(z)}, \qquad \text{ provided that } \lim_{z \to c} g(z) \ne 0
>
>\end{align*}
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM]- Squeeze Theorem
>
>Let $f,g: \mathcal{D} \subseteq \mathbb{C} \to \mathbb{C}$ be [[Complex Functions]] and let $c \in \mathbb{C}$ be an [[Accumulation Point]] of $f$.
>
>If there exists some [[Topology of the Complex Plane|deleted neighborhood]] $N \subseteq \mathcal{D}$ of $c$ such that $|g(z)| \le |f(z)|$ for all $z \in N$ and $\lim_{z \to c} f(z) = 0$, then $\lim_{z \to c} g(z) = 0$.
>
>If there exists [[Topology of the Complex Plane|deleted neighborhood]] $N \subseteq \mathcal{D}$ of $c$ on which $g$ is [[Boundedness|bounded]] and $\lim_{z \to c} f(z) = 0$, then $\lim_{z \to c} (f(z) \cdot g(z)) = 0$.
>
>
>>[!PROOF]-
>>
>>TODO
>>
>

# Limits at Infinity

>[!NOTATION] Notation: Limits at Infinity
>
>Let $f: \mathcal{D} \subseteq \mathbb{C} \to \mathbb{C}$ be a [[index|complex function]] such that $\mathcal{D}$ is the [[Complement]] of some [[Topology of the Complex Plane|open ball]] around $0$.
>
>We write
>
>$$
>\lim_{z \to \infty} f(z) = L,
>$$
>
>where $L$ is some complex number, if for each $\varepsilon \gt 0$ there exists some $R \gt 0$ such that
>
>$$
>|z| \gt R \implies |f(z) - L| \lt \varepsilon \qquad \forall z \in \mathcal{D}.
>$$
>

## Characterizations

>[!THEOREM]-
>
>Let $f: \mathcal{D} \subseteq \mathbb{C} \to \mathbb{C}$ be a [[index|complex function]] such that $\mathcal{D}$ is the [[Complement]] of some [[Topology of the Complex Plane|open ball]] around $0$.
>
>The [[Limits#Limits at Infinity|limit]] of $f$ for $z \to \infty$ is $L \in \mathbb{C}$ if and only if the [[Limits#Limits at Infinity|limit]] of $|f(z) - L|$ for $|z| \to \infty$ is zero.
>
>$$
>\lim_{z \to \infty} f(z) = L \iff \lim_{|z| \to \infty} |f(z) - L| = 0
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

# Converting Limits

>[!THEOREM]- Theorem: Limit $\leftrightarrow$ Limit at Infinity
>
>Let $f: \mathcal{D} \subseteq \mathbb{C} \to \mathbb{C}$ be a [[index|complex function]] such that $\mathcal{D}$ is the [[Complement]] of some [[Topology of the Complex Plane|open ball]] around $0$.
>
>The [[Limits#Limits at Infinity|limit]] of $f$ for $z \to \infty$ is equal to $L \in \mathbb{C}$ if and only if the [[Limits#Limits|limit]] of $f\left(\frac{1}{z}\right)$ for $z \to 0$ is $L$.
>
>$$
>\lim_{z \to \infty} f(z) = L \iff \lim_{z \to 0} f \left( \frac{1}{z} \right) = L
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>