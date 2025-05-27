---
title: Rings
tags:
  - ring-theory
  - abstract-algebra
  - algebra
  - mathematics
---

# Rings

>[!DEFINITION] Definition: Ring
>
>A **ring** $(R, +, \cdot)$ is an [[Algebraic Structure]] whose [[Algebraic Structure|domain]] $R$ is equipped with an **addition** $+: R\times R \to R$ and a **multiplication** $\cdot: R\times R \to R$ [[Binary Operation|operations]] which satisfy the following properties.
>
>1. $R$ is an [[Abelian Group]] under addition, i.e.:
>	- $a + b = b + a$ for all $a,b \in R$
>	- $(a + b) + c = a + (b + c)$ for all $a,b,c \in R$;
>	- There exists an **additive identity** $0_R \in R$ such that $a + 0_R = 0_R + a = 0_R$ for all $a \in R$;
>	- For each $a \in R$ there exists $-a$ such that $a + (-a) = 0_R$.
>
>2. $R$ is a [[Monoid]] under multiplication, i.e.:
>	- $(a\cdot b) \cdot c = a \cdot (b \cdot c)$ for all $a,b,c \in R$;
>	- There exists a **multplicative identity** $1_R \in R$ such that $a\cdot 1_R = 1_R \cdot a = a$ for all $a \in R$.
>3. Multiplication is distributive with respect to addition, i.e.
>	- $a \cdot (b + c) = a \cdot b + a \cdot c$ for all $a,b,c \in R$
>	- $(a+b) \cdot c = a\cdot c + b \cdot c$ for all $a,b,c \in R$
>
>>[!NOTE]
>>
>>The additive identity is often called "zero" and the multiplicative identity is often called "one".
>
>>[!NOTATION]-
>>
>>When it is clear from context which ring we are talking about, we can write simply $0$ and $1$ for the additive and multiplicative identities, respectively.
>>
>>Multiplication is often denoted as $ab$ or $a\times b$ instead of $a\cdot b$.
>>
>>Multiplying an element by itself $n$ times is denoted as
>>
>>$$
>>a^n = \underset{n \text{ times}}{\underbrace{a \times \cdots \times a}}
>>$$
>>
>>We also define $a^0 = 1_R$ for every $a \in R, a \ne 0$.
>>
>


## Properties

>[!THEOREM]- Theorem: Uniqueness of the Additive Identity
>
>The additive identity $0_R$ of a [[Ring]] $R$ is unique.
>
>>[!PROOF]-
>>
>>Suppose there were two additive identities $0_R$ and $0_R'$.
>>
>>Since $0_R'$ is an additive identity, we have
>>
>>$$
>>0_R + 0_R' = 0_R
>>$$
>>
>>Similarly, since $0_R$ is an additive identity, we have
>>
>>$$
>>0_R' + 0_R = 0_R'
>>$$
>>
>>The commutativity of addition tells us that
>>
>>$$
>>0_R + 0_R' = 0_R' + 0_R
>>$$
>>
>>and so $0_R = 0_R'$.
>>
>

>[!THEOREM]- Theorem: Uniqueness of the Multiplicative Identity
>
>The multiplicative identity $1_R$ of a [[Ring]] $R$ is unique.
>
>>[!PROOF]-
>>
>>Suppose there were two multiplicative identities $1_R$ and $1_R'$.
>>
>>Since $1_R'$ is a multiplicative identity, we have
>>
>>$$
>>1_R \cdot 1_R' = 1_R' \cdot 1_R = 1_R
>>$$
>>
>>Similarly, since $1_R$ is a multiplicative identity, we have
>>
>>$$
>>1_R' \cdot 1_R = 1_R \cdot 1_R' = 1_R'
>>$$
>>
>>From these two equations we conclude that $1_R = 1_R'$.
>>

>[!THEOREM]- Theorem: Uniqueness of Additive Inverses
>
>The additive inverse $-a$ of each element $a$ in a [[Ring]] is unique.
>
>>[!PROOF]-
>>
>>Let $a$ be a ring element and suppose it has two additive inverses $-a$ and $-a'$.
>>
>>Since $-a$ is an additive inverse, we have
>>
>>$$
>>a + (-a) = 0
>>$$
>>
>>Since $-a'$ is an additive inverse, we have
>>
>>$$
>>a + (-a') = 0
>>$$
>>
>>From the two equations we get
>>
>>$$
>>a + (-a) = a + (-a')
>>$$
>>
>>Let's add $-a$ to both sides.
>>
>>$$
>>a + (-a) + (-a) = a + (-a') + (-a)
>>$$
>>
>>Using associativity on the left side and commutativity on the right side we get
>>
>>$$
>>0 + (-a) = a + (-a) + (-a')
>>$$
>>
>>We again apply associativity, this time to the right side.
>>
>>$$
>>0 + (-a) = 0 + (-a')
>>$$
>>
>>By the property of the additive identity we get
>>
>>$$
>>-a = -a'
>>$$
>>
>

>[!THEOREM] Theorem: Multiplication with the Additive Identity
>
>Multiplying any element $a$ of a [[index|ring]] by its additive identity results in the additive identity.
>
>$$
>a \cdot 0 = 0 \cdot a = 0
>$$
>
>>[!PROOF]-
>>
>>The property of the additive identity tells us that $0 = 0 + 0$ and so
>>
>>$$
>>a \cdot 0 = a \cdot (0 + 0)
>>$$
>>
>>The distributivity of multiplication gives us
>>
>>$$
>>a \cdot (0 + 0) = a \cdot 0 + a \cdot 0
>>$$
>>
>>$$
>>a \cdot 0 = a \cdot 0 + a \cdot 0
>>$$
>>
>>By the existence of additive inverses we obtain
>>
>>$$
>>(1) \qquad a \cdot 0 + (- (a \cdot 0)) = (a \cdot 0 + a \cdot 0) + (- (a \cdot 0))
>>$$
>>
>>Associativity entails
>>
>>$$
>>(2) \qquad (a \cdot 0 + a \cdot 0) + (- (a \cdot 0)) = a \cdot 0 + (a \cdot 0 + (- (a \cdot 0)))
>>$$
>>
>>Combining $(1)$ and $(2)$ we get
>>
>>$$
>>a \cdot 0 + (- (a \cdot 0)) = a \cdot 0 + (a \cdot 0 + (- (a \cdot 0)))
>>$$
>>
>>The property of the additive identity also tells us that
>>
>>$$
>>a \cdot 0 + (- (a \cdot 0)) = 0
>>$$
>>
>>Therefore,
>>
>>$$
>>a \cdot 0 + (- (a \cdot 0)) = a \cdot 0 + (a \cdot 0 + (- (a \cdot 0)))
>>$$
>>
>>$$
>>0 = a \cdot 0 + 0 = a \cdot 0
>>$$
>>
>>The proof for $0 \cdot a$ is analogous.
>>
>

>[!THEOREM] Theorem: Multiplication with the Additive Inverse of the Multiplicative Identity
>
>Multiplying any element $a$ of a [[index|ring]] by the additive inverse of the multiplicative identity results in the additive inverse of $a$.
>
>$$
>(-1)\cdot a = a \cdot (-1) = -a
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>