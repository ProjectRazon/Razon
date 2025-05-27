---
title: Operations with Collections
tags:
  - set-theory
  - mathematics
---

# Union

>[!DEFINITION] Definition: Union of a Collection
>
>The **union** of a [[Collections|collection]] $\mathcal{C}$ is the [[Sets|set]] of all elements which belong to at least one of the sets in $\mathcal{C}$.
>
>$$
>\{x \mid \exists E\in \mathcal{C}  : x\in E \}
>$$
>
>>[!NOTATION]-
>>
>>Usually, the union of a collection is denoted by
>>
>>$$
>>\bigcup \mathcal{C}
>>$$
>>
>>However, an alternative notation is more useful when we need to consider specific elements of $\mathcal{C}$. In this case, indexing notation using an [[Indexing|index set]] $I$ for $\mathcal{C}$ is used.
>>
>>$$
>>\bigcup_{i \in I} \mathcal{C}_i
>>$$
>>
>

# Intersection

>[!DEFINITION] Definition: Intersection of a Collection
>
>The **intersection** of a [[Collections|collection]] $\mathcal{C}$ is the [[Sets|set]] of elements which belong to all sets of $\mathcal{C}$.
>
>$$
>\{x \mid \forall E \in \mathcal{C}:  x \in \mathcal{C}\}
>$$
>
>>[!NOTATION]-
>>
>>Usually, the intersection of a collection is denoted by
>>
>>$$
>>\bigcap \mathcal{C}
>>$$
>>
>>However, an alternative notation is more useful when we need to consider specific elements of $\mathcal{C}$. In this case, indexing notation using an [[Indexing|index set]] $I$ for $\mathcal{C}$ is used.
>>
>>$$
>>\bigcap_{i \in I} \mathcal{C}_i
>>$$
>>
>