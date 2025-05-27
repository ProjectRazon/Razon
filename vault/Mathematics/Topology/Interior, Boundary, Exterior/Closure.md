---
title: Closure
tags:
  - topology
  - mathematics
---

# Closure

>[!THEOREM] Theorem: Closure
>
>Let $(X, \tau)$ be a [[Topological Spaces|topological space]] let $A$ be a [[Sets|subset]] of $X$.
>
>The [[Set Operations|union]] of the [[Interior, Boundary and Exterior|interior]] $\operatorname{int} A$ of $A$ with the [[Interior, Boundary and Exterior|boundary]] $\partial A$ of $A$ is [[Topological Spaces|closed]].
>
>>[!PROOF]-
>>
>>TODO
>>
>
>>[!DEFINITION] Definition: Closure
>>
>>Let $(X, \tau)$ be a [[Topological Spaces|topological space]] and let $A$ be a [[Sets|subset]] of $X$.
>>
>>The **closure** of $A$ is the [[Set Operations|union]] of its [[Interior, Boundary and Exterior|interior]] and its [[Interior, Boundary and Exterior|boundary]].
>>
>>$$
>>\operatorname{int} A \cup \partial A
>>$$
>>
>>>[!NOTATION]-
>>>
>>>$$
>>>\overline{A}
>>>$$
>>>
>>
>

## Properties

>[!THEOREM]+ Theorem: Closure is a Superset
>
>Let $(X, \tau)$ be a [[Topological Spaces|topological space]].
>
>Every [[Sets|subset]] $S$ is a [[Sets|subset]] of its own [[Closure]].
>
>$$
>S \subseteq \overline{S}
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>
>^closure-is-a-superset
>

>[!THEOREM]+ Theorem: Closure of a Closure
>
>Let $(X, \tau)$ be a [[Topological Spaces|topological space]] and let $S$ be a [[Sets|subset]] of $X$.
>
>The [[Closure]] of the [[Closure]] of $S$ is still the [[Closure]] of $S$.
>
>$$
>\overline{\overline{S}} = \overline{S}
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM]+ Theorem: Closure of a Union
>
>Let $(X, \tau)$ be a [[Topological Spaces|topological space]] and let $A$ and $B$ be two arbitrary [[Sets|subsets]] of $X$.
>
>The [[Closure]] of the [[Set Operations|union]] of $A$ and $B$ is the [[Set Operations|union]] of the [[Closure|closures]] of $A$ and $B$.
>
>$$
>\overline{A \cup B} = \overline{A} \cup \overline{B}
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Closure of the Empty Set
>
>Let $(X, \tau_X)$ be a [[Topological Spaces|topological space]].
>
>The [[Closure]] of the [[Sets|empty set]] is itself.
>
>$$
>\overline{\varnothing} = \varnothing
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>
>^closure-of-the-empty-set
>