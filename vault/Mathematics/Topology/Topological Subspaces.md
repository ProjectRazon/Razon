---
title: Topological Subspaces
tags:
  - topology
  - mathematics
---

# Topological Subspaces

>[!THEOREM] Theorem: Topological Subspace
>
>Let $(X, \tau_X)$ be a [[Topological Spaces|topological space]].
>
>For every [[Sets|non-empty]] [[Sets|subset]] $S$ of $X$, the [[Collections|collection]]
>
>$$
>\tau_S \overset{\text{def}}{=} \{O \cap S \mid O \in \tau_X\}
>$$
>
>is a [[Topological Spaces|topology]] on $S$.
>
>>[!PROOF]-
>>
>>We need to prove three things:
>>- (I) $S \in \tau_S$ and $\varnothing \in \tau_S$.
>>- (II) $\tau_S$ is closed under arbitrary unions.
>>- (III) $\tau_S$ is closed under finite intersections.
>>
>>**Proof of (I):**
>>
>>This follows from the fact that $\varnothing = S \cap \varnothing$ and $S = S \cap X$.
>>
>>**Proof of (II):**
>>
>>Let $\mathcal{U}$ be an arbitrary [[Sets|subset]] of $\tau_S$. By definition, for each $U \in \mathcal{U}$ there exists some $O_U \in \tau_X$ such that $U = O_U \cap S$.  Then
>>
>>$$
>>\bigcup \mathcal{U} = \bigcup_{U \in \mathcal{U}} (O_U \cap S) = \left(\bigcup_{U \in \mathcal{U}} O_U\right) \cap S
>>$$
>>
>>Since $\bigcup_{U \in \mathcal{U}} O_U$ is a [[Operations with Collections|union]] of [[Topological Spaces|open sets]], it is itself [[Topological Spaces|open]], i.e. $\bigcup_{U \in \mathcal{U}} O_U \in \tau_X$. Therefore $\left(\bigcup_{U \in \mathcal{U}} O_U\right) \cap S$ is in $\tau_S$.
>>
>>**Proof of (III):**
>>
>>Consider the [[Operations with Collections|intersection]] $U_1 \cap \cdots \cap U_n$ where $U_1,\cdots, U_n \in \tau_S$. By definition, for each $U_k$ there exists some $O_k \in \tau_X$ such that $U_k = O_k \cap S$. This means that
>>
>>$$
>>U_1 \cap \cdots \cap U_n = (O_1 \cap S) \cap \cdots \cap (O_n \cap S) = (O_1 \cap \cdots \cap O_n) \cap S
>>$$
>>
>>Since $(O_1 \cap \cdots \cap O_n)$ is an [[Operations with Collections|intersection]] of finitely many [[Topological Spaces|open sets]], it is itself [[Topological Spaces|open]]. Therefore, $U_1 \cap \cdots \cap U_n \in \tau_S$.
>>
>
>>[!DEFINITION] Definition: Topological Subspace
>>
>>The [[Topological Spaces|topological space]] $(S, \tau_S)$ is known as a **subspace** of $(X,\tau_X)$.
>>
>

## Properties

>[!THEOREM] Theorem: Openness in Topological Subspaces
>
>Let $(S, \tau_S)$ be a [[Topological Subspaces|subspace]] of a [[Topological Spaces|topological space]] $(X, \tau_X)$ and let $U$ be a [[Sets|subset]] of $S$.
>
>If $U$ is [[Topological Spaces|open]] in $(S, \tau_S)$ and $S$ is [[Topological Spaces|open]] $(X, \tau_X)$, then $U$ is also [[Topological Spaces|open]] in $(X, \tau_X)$.
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Closedness in Topological Subspaces (I)
>
>Let $(S, \tau_S)$ be a [[Topological Subspaces|subspace]] of a [[Topological Spaces|topological space]] $(X, \tau_X)$.
>
>A [[Sets|set]] $A$ is [[Topological Spaces|closed]] in $(S, \tau_S)$ if and only if it is the [[Set Operations|intersection]] of a [[Topological Spaces|closed set]] of $(X, \tau_X)$ with $S$.
>
>>[!PROOF]-
>>
>>We need to prove two things:
>>- (I) If $A$ is a [[Topological Spaces|closed set]] of $(S, \tau_S)$, then there exists a [[Topological Spaces|closed set]] $C$ of $(X, \tau_X)$ such that $A = C \cap S$.
>>- (II) If there exists a [[Topological Spaces|closed set]] $C$ of $(X, \tau_X)$ such that $A = C \cap S$, then $A$ is [[Topological Spaces|closed]] in $(S, \tau_S)$.
>>
>>**Proof of (I):**
>>
>>Suppose that $A$ is [[Topological Spaces|closed]] in $(S, \tau_S)$. Then its [[Complement]] $S \setminus A$ is [[Topological Spaces|open]] in $(S, \tau_S)$ and, by definition, there exists an [[Topological Spaces|open set]] $O_A$ of $(X, \tau_X)$ such that $S \setminus A = O_A \cap S$. Furthermore, $X \setminus O_A$ is [[Topological Spaces|closed]] in $(X, \tau_X)$, since $O_A$ is [[Topological Spaces|open]] in $(X, \tau_X)$.
>>
>>**Proof of (II):**
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Closedness in Topological Subspaces (II)
>
>Let $(S, \tau_S)$ be a [[Topological Subspaces|subspace]] of a [[Topological Spaces|topological space]] $(X, \tau_X)$ and let $C$ be a [[Sets|subset]] of $S$.
>
>If $C$ is [[Topological Spaces|closed]] in $(S, \tau_S)$ and $S$ is [[Topological Spaces|closed]] $(X, \tau_X)$, then $C$ is also [[Topological Spaces|closed]] in $(X, \tau_X)$.
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Base for Topological Subspaces
>
>Let $(S, \tau_S)$ be a [[Topological Subspaces|subspace]] of a [[Topological Spaces|topological space]] $(X, \tau_X)$.
>
>If $\mathcal{B}$ is a [[index|base]] for $(X, \tau_X)$, then the [[Collections|collection]]
>
>$$
>\mathcal{B}_S \overset{\text{def}}{=} \{ B \cap S \mid B \in \mathcal{B}\}
>$$
>
>is a [[index|base]] for $(S, \tau_S)$.
>
>>[!PROOF]-
>>
>>TODO
>>
>

### Compactness of Subspaces

>[!THEOREM] Theorem: Compactness of Subspaces
>
>A [[Topological Subspaces|subspace]] $(S, \tau_S)$ of a [[Topological Spaces|topological space]] $(X, \tau_X)$ is [[index|compact]] if and only if every [[index#covers|cover]] of $S$ by [[Topological Spaces|open subsets]] in $(X, \tau_X)$ contains a finite [[Collections|subcollection]] which is also a [[index#covers|cover]] of $(S, \tau_S)$.
>
>>[!PROOF]-
>>
>>We need to prove two things:
>>- (I) If $(S, \tau_S)$ is [[index|compact]], then every [[index|cover]] of $S$ by [[Topological Spaces|open subsets]] in $(X, \tau_X)$ contains a finite [[Collections|subcollection]] which is also a [[index|cover]] of $(S, \tau_S)$.
>>- (II) If every [[index|cover]] of $S$ by [[Topological Spaces|open subsets]] in $(X, \tau_X)$ contains a finite [[Collections|subcollection]] which is also a [[index#covers|cover]] of $(S, \tau_S)$, then $(S, \tau_S)$ is [[index|compact]].
>>
>>**Proof of (I):**
>>
>>Suppose that $(S, \tau_S)$ is [[index|compact]] and let $\mathcal{C}$ be a [[index#covers|cover]] of $S$ consisting of [[Topological Spaces|open subset]] of $(X, \tau_X)$.
>>
>

>[!THEOREM] Theorem
>
>Let $(S, \tau_S)$ be a [[Topological Subspaces|subspace]] of a [[Topological Spaces|topological space]] $(X, \tau_X)$.
>
>If $(X, \tau_X)$ is [[index|compact]] and $S$ is [[Topological Spaces|closed]] in $(X, \tau_X)$, then $(S, \tau_S)$ is also [[index|compact]].
>
>>[!PROOF]-
>>
>>TODO
>>
>