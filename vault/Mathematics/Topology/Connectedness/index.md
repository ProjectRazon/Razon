---
title: Connectedness
tags:
  - connectedness
  - topology
  - mathematics
---

# Connectedness

>[!DEFINITION] Definition: Connectedness of a Topological Space
>
>A [[Topological Spaces|topological space]] is **connected** iff it cannot be represented as the [[Set Operations|union]] of two [[Disjoint Sets|disjoint]], [[Sets|nonempty]] [[Topological Spaces|open sets]].
>

>[!DEFINITION] Definition: Connectedness of a Subset
>
>Let $(X, \tau_X)$ be a [[Topological Spaces|topological space]].
>
>A [[Sets|subset]] $S \subseteq X$ is **connected** iff it is [[index|connected]] as a [[Topological Subspaces|subspace]].
>

>[!DEFINITION] Definition: Disconnectedness
>
>A [[Topological Spaces|topological space]] is **disconnected** iff it is not [[index|connected]].
>

## Connectedness Criteria

>[!THEOREM]-
>
>A [[Topological Spaces|topological space]] $(X, \tau)$ is [[index|connected]] if and only if its only [[Topological Spaces|clopen subsets]] are $\varnothing$ and $X$.
>
>>[!PROOF]-
>>
>>We need to prove two things:
>>- (I) If $(X, \tau)$ is [[index|connected]], then its only [[Topological Spaces|clopen subsets]] are $\varnothing$ and $X$.
>>- (II) If the only [[Topological Spaces|clopen subsets]] of $(X, \tau)$ are $\varnothing$ and $X$, then $(X, \tau)$ is [[index|connected]].
>>
>>**Proof of (I):**
>>
>>We prove this by contradiction.
>>
>>Suppose that $(X, \tau)$ is [[index|connected]] and let $U \subset X$ be [[Topological Spaces|clopen]]. If $U$ is [[Sets|nonempty]], then so is $X \setminus U$. Since $U$ is [[Topological Spaces|clopen]], so is its [[Complement]] $X \setminus U$.  More importantly, this implies that both $U$ and $X \setminus U$ are [[Topological Spaces|open]]. However, since $X = U \cup X\setminus U$, this means that $X$ can be represented as the [[Set Operations|union]] of two [[Disjoint Sets|disjoint]], [[Sets|nonempty]] [[Topological Spaces|open sets]] and is thus not [[index|disconnected]], which is a contradiction.
>>
>>**Proof of (II):**
>>
>>We prove this by contradiction.
>>
>>Suppose that the only [[Topological Spaces|clopen subsets]] of $(X, \tau)$ are $\varnothing$ and $X$. Assume that $(X, \tau)$ is [[index|disconnected]], i.e. there exists two [[Disjoint Sets|disjoint]], [[Sets|nonempty]] [[Topological Spaces|open sets]] $U$ and $V$ such that $X = U \cup V$.
>>
>>
>

>[!THEOREM]
>
>Let $(X, \tau)$ be a [[Topological Spaces|topological space]] and let $S$ be a [[Sets|subset]] of $X$.
>
>If $S$ can be expressed as the [[Operations with Collections|union]] of a [[Collections|collection]] $\mathcal{C}$ of [[index#^connected-subset]] [[Sets|subsets]] whose [[Operations with Collections|intersection]] is [[Sets|nonempty]],  then $S$ is also [[index#^connected-subset]].
>
>>[!PROOF]-
>>
>>TODO
>>
>