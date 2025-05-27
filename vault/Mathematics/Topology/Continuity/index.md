---
title: Continuity
tags:
  - continuity
  - topology
  - mathematics
---

# Continuity

>[!DEFINITION] Definition: Continuity at a Point
>
>Let $(X,\tau_X)$ and $(Y,\tau_Y)$ be [[Topological Spaces]].
>
>A [[Functions|function]] $f: X \to Y$ is **continuous at** $x \in X$ iff for each [[Topological Spaces|neighbourhood]] $V$ of $f(x)$ there exists a neighbourhood $U$ of $x$ such that $f(U) \subset V$.
>

>[!DEFINITION] Definition: Continuity
>
>Let $(X,\tau_X)$ and $(Y,\tau_Y)$ be [[Topological Spaces]].
>
>A [[Functions|function]] $f: X \to Y$ is **continuous on** $X$ or simply **continuous** iff it is [[Continuity|continuous]] at each $x \in X$.

## Continuity Criteria

>[!THEOREM]- Theorem: Continuity via Openness
>
>Let $(X,\tau_X)$ and $(Y,\tau_Y)$ be [[Topological Spaces]].
>
>A [[Functions|function]] $f: X \to Y$ is [[index|continuous]] if and only if the [[Functions|inverse image]] of each [[Topological Spaces|open subset]] of $Y$ is an open subset of $X$.
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM]- Theorem: Continuity via Closedness
>
>Let $(X,\tau_X)$ and $(Y,\tau_Y)$ be [[Topological Spaces]].
>
>A [[Functions|function]] $f: X \to Y$ is [[index|continuous]] if and only if the [[Functions|inverse image]] of each [[Topological Spaces|closed subset]] of $Y$ is a [[Topological Spaces|closed subset]] of $X$.
>
>>[!PROOF]-
>>
>>TODO
>>
>>

>[!THEOREM]- Theorem: Local Criterion
>
>Let $(X,\tau_X)$ and $(Y,\tau_Y)$ be [[Topological Spaces]].
>
>A [[Functions|function]] $f: X \to Y$ is [[index|continuous]] if and only if each point $x \in X$ has a [[Topological Spaces|neighbourhood]] $N$ such that the [[Functions|restriction]] $f\big|_N$ is [[index|continuous]].
>
>>[!PROOF]-
>>
>>TODO
>>
>

## Properties

>[!THEOREM]- Extreme Value Theorem
>
>Let $(X, \tau_X)$ and $(Y,\tau_Y)$ be [[Topological Spaces]].
>
>If $(X,\tau_X)$ is [[index|compact]], then its [[Functions|image]] $f(X)$ under every [[index|continuous function]] $f: X \to Y$ is also [[index|compact]].
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM]- Theorem: Continuity of Composition
>
>Let $(X, \tau_X)$, $(Y, \tau_Y)$ and $(Z, \tau_Z)$ be [[Topological Spaces]].
>
>If $f: X \to Y$ and $g: Y \to Z$ are [[index|continuous]], then so is their [[Composition]] $g \circ f: X \to Z$.
>
>>[!PROOF]-
>>
>>We need to prove only that if $U$ is [[Topological Spaces|open]] in $(Z, \tau_Z)$, then its [[Functions|inverse image]]  $(g\circ f)^{-1}(U)$ is [[Topological Spaces|open]] in $(X, \tau_X)$.
>>
>>
>>
>>Let $U$ be [[Topological Spaces|open]] in $(Z, \tau_Z)$. We know that $(g\circ f)^{-1}(U) = f^{-1}(g^{-1}(U))$. Since $g$ is [[index#^continuity]] and $U$ is [[Topological Spaces|open]] in $(Z, \tau_Z)$, the aforementioned theorem tells us that $g^{-1}(U)$ is [[Topological Spaces|open]] in $(Y, \tau_Y)$. Analogously, since $f$ is [[index#^continuity]] and $g^{-1}(U)$ is [[Topological Spaces|open]] in $(Y, \tau_Y)$, the theorem tells us that $f^{-1}(g^{-1}(U))$ is [[index#^continuity]] in $(X,\tau_X)$.
>>
>

>[!THEOREM]- Theorem: Continuity of Restrictions
>
>Let $(X, \tau_X)$ and $(Y, \tau_Y)$ be [[Topological Spaces]].
>
>If $f: X \to Y$ is [[index|continuous]] and $S$ is an [[Topological Spaces|open subset]] of $X$, then the [[Functions|restriction]] $f\big|_S$ is also [[index|continuous]].
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Intermediate Value Theorem
>
>Let $(X, \tau_X)$ and $(Y, \tau_Y)$ be [[Topological Spaces]].
>
>If $(X, \tau_X)$ is [[index|connected]], then so its [[Functions|image]] $f(X)$ under any [[index|continuous function]] $f: X \to Y$.
>
>>[!PROOF]-
>>
>>TODO
>>
>