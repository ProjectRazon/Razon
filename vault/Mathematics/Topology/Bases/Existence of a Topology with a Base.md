---
title: Existence of a Topology with a Base
tags:
  - topology
  - mathematics
---

>[!THEOREM] Theorem: Existence of a Topology with a Base
>
>Let $X$ be a [[Sets|non-empty]] [[Sets|set]] and let $\mathcal{B}$ be a [[Collections|collection]] of [[Sets|subsets]] of $X$.
>
>There exists a [[Topological Spaces|topology]] $\tau_\mathcal{B}$ on $X$ such that $\mathcal{B}$ is a [[index|base]] for the [[Topological Spaces|topological space]] $(X, \tau_\mathcal{B})$ if and only if
>- $X$ is the [[Operations with Collections|union]] of $\mathcal{B}$, i.e. $X = \bigcup \mathcal{B}$, and
>- for each $B_1, B_2 \in \mathcal{B}$, the [[Set Operations|intersection]] $B_1 \cap B_2$ is a union of a subset of $\mathcal{B}$.
>
>>[!PROOF]-
>>
>>We need to prove the following things separately:
>>- If there exists a [[Topological Spaces|topology]] $\tau_\mathcal{B}$ on $X$ such that $\mathcal{B}$ is a [[index|base]] for the [[Topological Spaces|topological space]] $(X, \tau_\mathcal{B})$, then $X = \bigcup \mathcal{B}$ and for each $B_1, B_2 \in \mathcal{B}$, the [[Set Operations|intersection]] $B_1 \cap B_2$ is a [[Operations with Collections|union]] of a subset of $\mathcal{B}$.
>>- If $\mathcal{B}$ is such that $X = \bigcup \mathcal{B}$ and for each $B_1, B_2 \in \mathcal{B}$, the [[Set Operations|intersection]] $B_1 \cap B_2$ is a union of a [[Sets|subset]] of $\mathcal{B}$, then there exists a [[Topological Spaces|topology]] $\tau_\mathcal{B}$ on $X$ such that $\mathcal{B}$ is a [[index|base]] for the [[Topological Spaces|topological space]] $(X, \tau_\mathcal{B})$.
>>
>>**Part 1**: 
>>
>>Suppose that there exists a [[Topological Spaces|topology]] $\tau_\mathcal{B}$ on $X$ such that $\mathcal{B}$ is a [[index|base]] for the [[Topological Spaces|topological space]] $(X, \tau_\mathcal{B})$.
>>
>>By the definition of a [[Topological Spaces|topology]], we have that $X$ is an [[Topological Spaces|open set]]. Since $\mathcal{B}$ is a [[index|base]] for $\tau_\mathcal{B}$, the [[Sets|set]] $X$ can be expressed as a [[Set Operations|union]] of a [[Sets|subset]] of $\mathcal{B}$. In particular, since $\mathcal{B}$ is comprised only of [[Sets|subsets]] of $X$, then $X = \bigcup \mathcal{B}$. Similarly, since $\mathcal{B}$ contains only [[Topological Spaces|open sets]] by definition, the [[Set Operations|intersection]] $B_1 \cap B_2$ is in $\tau_\mathcal{B}$, which completes the proof, since every [[Topological Spaces|open set]] can be expressed as a [[Operations with Collections|union]] of elements of $\mathcal{B}$ by definition.
>>
>>**Part 2:** 
>>
>>Suppose $\mathcal{B}$ is such that $X = \bigcup \mathcal{B}$ and for each $B_1, B_2 \in \mathcal{B}$, the [[Set Operations|intersection]] $B_1 \cap B_2$ is a union of a [[Sets|subset]] of $\mathcal{B}$. Define $\tau_\mathcal{B}$ as the [[Collections|collection]] of all [[Sets|subsets]] of $X$ which are [[Operations with Collections|unions]] of [[Sets|subsets]] of $\mathcal{B}$. 
>>
>>We need to show that $\tau_\mathcal{B}$ is a [[Topological Spaces|topology]] on $X$. To do this we need to show the following three things:
>>- $X \in \tau_\mathcal{B}$ and $\varnothing \in \tau_\mathcal{B}$;
>>- $\tau_\mathcal{B}$ is closed under arbitrary [[Operations with Collections|unions]];
>>- The [[Set Operations|intersection]] $U_1 \cap U_2$ of each $U_1, U_2 \in \tau_\mathcal{B}$ is in $\tau_\mathcal{B}$.
>>
>>The assumption that $X = \bigcup\mathcal{B}$ entails that $X \in \tau_\mathcal{B}$. The [[Sets|empty set]] is a [[Sets|subset]] of $\mathcal{B}$ and since $\varnothing = \bigcup \varnothing$, we have that $\varnothing \in \tau_\mathcal{B}$.
>>
>>Consider now an arbitrary [[Sets|subset]] $T$ of $\tau_\mathcal{B}$. Since each $U \in T$ is a [[Operations with Collections|union]] of a [[Sets|subset]] of $\mathcal{B}$, then $\bigcup T$ is also a [[Operations with Collections|union]] of a [[Sets|subset]] $\mathcal{B}$, meaning that $\bigcup T \in \tau_\mathcal{B}$.
>>
>>Finally, we consider two [[Sets]] $U_1, U_2 \in \tau_\mathcal{B}$. By definition of $\tau_\mathcal{B}$, there exists some [[Sets|subset]] $\{B_i\}_{i \in I} \subseteq \mathcal{B}$ such that $U_1 = \bigcup_{i \in I} B_i$. Similarly, $U_2 = \bigcup_{j \in J} B_j$. We thus have
>>
>>$$U_1 \cap U_2 = \left(\bigcup_{i \in I} B_i\right) \cap \left(\bigcup_{j \in J} B_j\right) = \bigcup_{i \in i, j \in J} (B_i \cap B_j)$$
>>
>>By assumption, for all $i \in I$ and $j \in J$, the [[Set Operations|intersection]] $(B_i \cap B_j)$ is a [[Set Operations|union]] of a [[Sets|subset]] of $\mathcal{B}$. Therefore, the [[Operations with Collections|union]] $\bigcup_{i \in i, j \in J} (B_i \cap B_j)$ is also a [[Operations with Collections|union]] of a [[Sets|subset]] of $\mathcal{B}$ and is thus in $\tau_\mathcal{B}$, Q.E.D.
>>
>