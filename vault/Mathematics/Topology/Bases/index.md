---
title: Bases for a Topological Space
tags:
  - topology
  - mathematics
---

# Base

>[!DEFINITION] Definitiom: Base for a Topological Space
>
>Let $(X, \tau)$ be a [[Topological Spaces|topological space]].
>
>A **base** for $(X,\tau)$ is a [[Collections|collection]] $\mathcal{B}$ of [[Topological Spaces|open subsets]] of $X$ such that every open set can be represented as a [[Operations with Collections|union]] of a [[Sets|subset]] of $\mathcal{B}$.
>
>>[!WARNING]
>>
>>This representation is not necessarily unique.
>>

## Base Criteria

>[!THEOREM]- Theorem
>
>Let $(X, \tau)$ be a [[Topological Spaces|topological space]].
>
>A [[Collections|collection]] $\mathcal{B}$ of [[Topological Spaces|open sets]] is a [[index|base]] for $(X, \tau)$ if and only if for each [[Topological Spaces|open set]] $U$ and each $u \in U$, there exists some $B \in \mathcal{B}$ such that $B \subseteq U$ and $u \in B$.
>
>>[!PROOF]-
>>
>>We need to prove two things:
>>- (I) If $\mathcal{B}$ is a [[index|base]] for $(X, \tau)$, then for each [[Topological Spaces|open set]] $U$ and each $u \in U$, there exists some $B \in \mathcal{B}$ such that $B \subseteq U$ and $u \in B$.
>>- (II) If for each [[Topological Spaces|open set]] $U$ and each $u \in U$, there exists some $B \in \mathcal{B}$ such that $B \subseteq U$ and $u \in B$, then $\mathcal{B}$ is a  [[index|base]] for $(X, \tau)$.
>>
>>**Part I:**
>>
>>Suppose $\mathcal{B}$ is a [[Base for a Topological Space|base]] for $(X, \tau)$. Let $U$ be [[Topological Spaces|open]] and let $u \in U$. Since $\mathcal{B}$ is a [[Base for a Topological Space|base]], $U$ can be represented as a [[Operations with Collections|union]] of some [[Sets|subset]] $\mathcal{B}_U \subseteq \mathcal{B}$, i.e. $U = \bigcup \mathcal{B}_U$. This implies that every $B \in \mathcal{B}_U$ is a [[Sets|subset]] of $U$. Moreover, since $u \in U$, there must exist at least one $B \in \mathcal{B}_U$ which contains $u$.
>>
>>**Part II:**
>>
>>Suppose that for each [[Topological Spaces|open set]] $U \in \tau$ and each $u \in U$, there exists a $B(u) \in \mathcal{B}$ such that $B(u) \subseteq U$ and $u \in B(u)$. Since $B(u) \subseteq U$ for each $u \in U$, it holds that $\bigcup_{u \in U} B(u) \subseteq U$. Since this [[Operations with Collections|union]] contains every $u \in U$, it follows that $\bigcup_{u \in U} B(u) = U$. Therefore, $U$ is a [[Operations with Collections|union]] of a [[Sets|subset]] of $\mathcal{B}$, Q.E.D.
>>
>

## Topology Generation

>[!THEOREM] Theorem: Topology Generation
>
>Let $(X, \tau)$ be a [[Topological Spaces|topological space]] and let $\mathcal{B}$ be a [[index|base]] for $(X, \tau)$.
>
>A [[Sets|subset]] $U \subseteq X$ is [[Topological Spaces|open]] if and only if for each $u \in U$ there exists some $B \in \mathcal{B}$ such that $B \subseteq U$ and $u \in B$.
>
>>[!PROOF]-
>>
>>We need to prove two things separately:
>>- (I) If $U$ is [[Topological Spaces|open]], then for each $u \in U$ there exists some $B_u \in \mathcal{B}$ such that $B_u \subseteq U$ and $u \in B_u$.
>>- (II) If for each $u \in U$ there exists some $B \in \mathcal{B}$ such that $B \subseteq U$ and $u \in B$, then $U$ is [[Topological Spaces|open]].
>>
>>**Proof of (I):**
>>
>>Suppose $U$ is [[Topological Spaces|open]]. The fact that for each $u \in U$ there exists some $B_u \in \mathcal{B}$ such that $B_u \subseteq U$ and $u \in B_u$ follows immediately from the [[index|base criterion]].
>>
>>**Proof of (II):**
>>
>>Suppose that for each $u \in U$ there exists some $B \in \mathcal{B}$ such that $B \subseteq U$ and $u \in B$. Since $u$ is contained in $B_u$ and $B_u \subseteq U$, we know that $U = \bigcup_{u \in U} B_u$, i.e. $U$ is a [[Set Operations|union]] of [[Topological Spaces|open subsets]] and is thus [[Topological Spaces|open]].
>>
>
>>[!INTUITION]
>>
>>This theorems allows us to determine the [[Topological Spaces|topology]] $\tau$ given only a [[index|base]] for it.
>>
>
>^topology-generation
>
