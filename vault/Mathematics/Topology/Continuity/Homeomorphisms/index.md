---
title: Homeomorphisms
tags:
  - homeomorphisms
  - continuity
  - topology
  - mathematics
---

# Homeomorphisms

>[!DEFINITION] Definition: Homeomorphism
>
>Let $(X, \tau_X)$ and $(Y,\tau_Y)$ be [[Topological Spaces]].
>
>A **homeomorphism** between $X$ and $Y$ is a [[index#^continuity|continuous]] [[Injections, Surjections and Bijections|bijection]] $f: X \to Y$ with a continuous [[Injections, Surjections and Bijections|inverse]] $f^{-1}: Y \to X$.

## Criteria for Homeomorphisms

>[!THEOREM]- Theorem: Equivalent Definition
>
>A [[Injections, Surjections and Bijections|bijection]] $f: X \to Y$ between two [[Topological Spaces]] $(X, \tau_X)$ and $(Y, \tau_Y)$ is a [[Homeomorphism]] if and only if the [[Functions|image]] of each [[Topological Spaces|open subset]] of $(X, \tau_X)$ is [[Topological Spaces|open]] in $(Y, \tau_Y)$ and the [[Functions|inverse image]] of each [[Topological Spaces|open subset]] in $(Y, \tau_Y)$ is [[Topological Spaces|open]] in $(X, \tau_X)$.
>
>>[!PROOF]-
>>
>>We have to prove two things:
>>- (I) If $f: X \to Y$ is a [[Homeomorphism]], then the [[Functions|image]] $f(U)$ of each [[Topological Spaces|open subset]] $U$ of $(X, \tau_X)$ is [[Topological Spaces|open]] in $(Y, \tau_Y)$.
>>- (II) If $f: X \to Y$ is a [[Injections, Surjections and Bijections|bijection]] and the [[Functions|image]] $f(U)$ of each [[Topological Spaces|open subset]] $U$ of $(X, \tau_X)$ is [[Topological Spaces|open]] in $(Y, \tau_Y)$, then $f$ is a [[Homeomorphism]].
>>
>>**Proof of (I):**
>>
>>**Proof of (II):**
>>
>>TODO
>>
>

>[!THEOREM]- Theorem: Homeomorphism via Open Maps
>
>A [[Injections, Surjections and Bijections|bijection]] $f: X \to Y$ between two [[Topological Spaces]] $(X, \tau_X)$ and $(Y, \tau_Y)$ is a [[Homeomorphism]] if and only if it is an [[Open Map]].
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM]- Theorem: Homeomorphism via Closed Maps
>
>A [[Injections, Surjections and Bijections|bijection]] $f: X \to Y$ between two [[Topological Spaces]] $(X, \tau_X)$ and $(Y, \tau_Y)$ is a [[Homeomorphism]] if and only if it is a [[Closed Map]].
>
>>[!PROOF]-
>>
>>TODO
>>
>

## Properties

>[!THEOREM]- Theorem: Composition of Homeomorphisms
>
>Let $(X, \tau_X)$, $(Y, \tau_Y)$ and $(Z, \tau_Z)$ be [[Topological Spaces]].
>
>If $f: X \to Y$ and $g: Y \to Z$ are [[index|homeomorphisms]], then their [[Composition]] $g \circ f: X \to Z$ is also a [[index|homeomorphism]].
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM]- Theorem: Homeomorphism $\implies$ Local Homeomorphism
>
>Every [[index|homeomorphism]] is also a [[Local Homeomorphisms|local homeomorphism]].
>
>>[!PROOF]-
>>
>>TODO
>>
>