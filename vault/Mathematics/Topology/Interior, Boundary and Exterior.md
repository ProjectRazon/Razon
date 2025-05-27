---
title: Boundary
tags:
  - topology
  - mathematics
---

Every [[Subsets|subset]] of $S$ of a [[Topological Spaces|topological space]] $(X, \tau)$ divides it into three different regions such that $X$ is always equal to the [[Operations with Collections|union]] of those regions.

# Interior

>[!DEFINITION] Definition: Interior of a Set
>
>Let $(X, \tau)$ be a [[Topological Spaces|topological space]] and let $S$ be a [[Subsets|subset]] of $X$.
>
>A point $p \in X$ is an **interior point** of $S$ if and only if it has a [[Topological Spaces#Neighborhoods|neighbourhood]] $N(p)$ contained in $S$. The **interior** of $S$ is the [[Sets|set]] of all of its [[Interior, Boundary and Exterior|interior points]].
>
>$$
>\{p \in X \mid \exists N(p) : N(p) \subseteq S \}
>$$
>
>>[!NOTATION]
>>
>>$$
>>\mathring S \qquad S^\circ \qquad \operatorname{int} S \qquad \operatorname{int}_X S
>>$$
>>
>

## Characterizations

>[!THEOREM]- Theorem: Interior via Open Sets
>
>Let $(X, \tau)$ be a [[Topological Spaces|topological space]].
>
>The [[Interior, Boundary and Exterior#Interior|interior]] of a [[Subsets|subset]] $S \subseteq X$ is the [[Operations with Collections|union]] of all [[Topological Spaces#Open Sets|open sets]] contained in $S$.
>
>$$
>\operatorname{int} S = \bigcup\{I \subseteq S \mid I \in \tau \}
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

## Properties

>[!THEOREM]- Theorem: Interior is a Subset
>
>Let $(X, \tau)$ be a [[Topological Spaces|topological space]].
>
>The [[Interior, Boundary and Exterior#Interior|interior]] $\operatorname{Int} S$ of each [[Subsets|subset]] $S \subseteq X$ is a [[Subsets|subset]] of $S$.
>
>$$
>\operatorname{Int} S \subseteq S
>$$
>
>>[!PROOF]-
>>
>>Suppose that $\operatorname{int} S$ is not a [[Subsets|subset]] of $S$. Then there must exist some $s \in \operatorname{int} S$ such that $s \notin S$. Since $s \in \operatorname{int} S$, there must exist some [[Topological Spaces#Open Sets|open set]] $O$ such that $s \in O$ and $O \subseteq S$. However, $s \notin S$ implies that $O$ is not a [[Subsets|subset]] of $S$, which is a contradiction.
>>
>

# Boundary

>[!DEFINITION] Definition: Boundary
>
>Let $(X, \tau)$ be a [[Topological Spaces|topological space]] and let $S$ be a [[Sets|subset]] of $X$.
>
>The **boundary** of $S$ is the [[Sets|set]] of all points $x \in X$ such that every [[Topological Spaces|neighbourhood]] of $x$ contains at least one point of $S$ and at least one point of its [[Complement]] $X \setminus S$.
>
>>[!NOTATION]-
>>
>>$$
>>\partial S \qquad \partial_X S \qquad \operatorname{Bd}_X S
>>$$
>>
>

>[!DEFINITION] Definition: Boundary Point
>
>Let $(X, \tau)$ be a [[Topological Spaces|topological space]] and let $S$ be a [[Sets|subset]] of $X$.
>
>A point $p \in X$ is a **boundary point** of $S$ iff it belongs to the [[Boundary]] of $S$.
>
>$$
>p \in \partial S
>$$
>

# Exterior

>[!DEFINITION] Definition: Exterior of a Set
>
>Let $(X, \tau_X)$ be a [[Topological Spaces|topological space]] and let $S$ be a [[Sets|subset]] of $X$.
>
>The **exterior** of $S$ is the [[Complement]] of its [[Closure]] in $X$.
>
>$$
>X \setminus \overline{S}
>$$
>
>>[!NOTATION]-
>>
>>$$
>>\operatorname{ext} S \qquad \operatorname{Ext} S
>>$$
>>
>
>^exterior
>

>[!DEFINITION] Definition: Exterior Point
>
>Let $(X, \tau_X)$ be a [[Topological Spaces|topological space]] and let $S$ be a [[Sets|subset]] of $X$.
>
>A point $p \in X$ is an **exterior point** of $S$ iff it belongs to the [[Exterior]] of $S$.
>

## Properties

>[!THEOREM] Theorem: Exterior is Closed
>
>Let $(X, \tau)$ be a [[Topological Spaces|topological space]].
>
>The [[Interior, Boundary and Exterior|exterior]] $\operatorname{Ext} S$ of each [[Sets|subset]] $S \subseteq X$ is [[Topological Spaces|closed]].
>
>>[!PROOF]-
>>
>>The [[Exterior]] of $S$ is the [[Complement]] of its [[Closure]] and since the [[Closure]] is a [[Topological Spaces|closed set]], the [[Exterior]] is [[Topological Spaces|open]].
>>
>