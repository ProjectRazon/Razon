---
title: Relations
tags:
  - set-theory
  - mathematics
---

# Relations

>[!DEFINITION] Definition: Relation
>
>A **relation** $R \subseteq A \times B$ between two [[Sets]] $A$ and $B$ is any [[Sets|subset]] of the [[Set Operations#cartesian product|Cartesian product]] $A\times B$.
>
>>[!NOTATION]-
>>
>>For any $a \in A$ and any $b \in B$, if $(a;b) \in R$, then we write
>>
>>$$
>>a\,\, R\,\, b
>>$$
>>
>
>>[!INTUITION]-
>>
>>The statement $a \,\, R\,\, b$ translates to "there is a relationship between $a$ and $b$ which is expressed by $R$".
>>
>
>>[!EXAMPLE]-
>>
>>Let $R \subseteq \mathbb{N} \times \mathbb{N}$ be the relation
>>
>>$$
>>R = \{(a;b)\mid a,b \in \mathbb{N} \text{ and } b \text{ is a divisor of a} \}
>>$$
>>
>>For any $x,y \in \mathbb{N}$, the statement $x\,\, R\,\, y$ means that $(x,y) \in R$ which in this case translates to "$y$ is a divisor of $b$".
>>
>

# Types of Relations

## Reflexive and Irreflexive Relations

>[!DEFINITION] Definition: Reflexive Relation
>
>A [[Relations|relation]] $R \subseteq A \times A$ is **reflexive** iff
>
>$$
>x\,\, R\,\, x
>$$
>
>is true for all $x\in A$.
>

>[!DEFINITION] Definition: Irreflexive Relation
>
>A [[Relations|relation]] $R \subseteq A \times A$ is **irreflexive** if there is no $x \in A$ such that
>
>$$
>x\,\, R\,\, x
>$$
>
>>[!NOTE]
>>
>>Irreflexive relations are also called **anti-reflexive** or **aliorelative**.
>>
>

## Unique Relations

>[!DEFINITION] Definition: Right-Unique Relation
>
>A [[Relations|relation]] $R\subseteq A\times B$ is **right-unique**, if for all $a \in A$ and all $b_1, b_2 \in B$
>
>$$
>((a\,\, R\,\, b_1)\land(a\,\, R\,\, b_1)) \implies b_1 = b_2
>$$
>

## Symmetric and Asymmetric Relations

>[!DEFINITION] Definition: Symmetric Relation
>
>A [[Relations|relation]] $R \subseteq A \times A$ is **symmetric** if
>
>$$
>x\,\, R\,\, y \implies y\,\, R\,\, x
>$$
>
>for all $x,y \in A$.
>
>^symmetric-relation
>

>[!DEFINITION] Definition: Asymmetric Relation
>
>A [[Relations|relation]] $R \subseteq A \times A$ is **asymmetric** if
>
>$$
>((x\,\, R\,\, y) \land (y\,\, R \,\, x)) \implies x=y
>$$
>
>for all $x,y, \in A$
>
>^asymmetric-relation
>

## Transitive Relations

>[!DEFINITION] Definition: Transitivity
>
>A [[Relations|relation]] $R \subseteq A \times A$ is **transitive** iff
>
>$$
>((x\,\, R\,\, y) \land (y\,\, R \,\, z)) \implies x\,\, R \,\, z
>$$
>
>for all $x,y,z \in A$.
>

## Equivalence Relations

>[!DEFINITION] Definition: Equivalence Relation
>
>An **equivalence relation** on the [[Sets|set]] $A$ is any [[Relations|relation]] $R \subseteq A \times A$ which is [[Relations|reflexive]], [[Relations|transitive]] and [[Relations|symmetric]].
>
>>[!NOTATION]-
>>
>>Equivalence relations are usually denoted with $\sim$ instead of $R$.
>>
>
>>[!INTUITION]-
>>
>>The statement $x\sim y$ means that $x$ is equal to $y$ in the sense of $\sim$.
>>
>

>[!DEFINITION] Definition: Equivalence Class
>
>Let $A$ be a [[Sets|set]] with an [[Equivalence Relation]] $\sim$.
>
>The **equivalence class** of an element $a \in A$ formed by $\sim$ is the [[Sets|set]] of all $x \in A$ which are equivalent to $a$.
>
>
>$$
>\{x\in A\mid a\sim x\}
>$$
>
>>[!NOTATION]-
>>
>>$$
>>[a]_\sim
>>$$
>>
>