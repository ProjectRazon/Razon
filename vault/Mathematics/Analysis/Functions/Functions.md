---
title: Restriction
tags:
  - functions
  - analysis
  - mathematics
---

>[!DEFINITION] Definition: Function
>
>A **function** $f: \mathcal{D} \to C$ from a [[Sets|set]] $\mathcal{D}$ to a [[Sets|set]] $C$ is a [[Relations|right-unique]] [[Relations|relation]] $f \subseteq \mathcal{D} \times C$.
>
>![[res/Function.drawio.svg]]
>
>>[!DEFINITION] Definition: Domain
>>
>>We call $\mathcal{D}$ the **domain** of $f$.
>>
>
>>[!DEFINITION] Definition: Codomain
>>
>>We call $C$ the **codomain** of $f$.
>>
>
>>[!DEFINITION] Definition: Image
>>
>>The **image** of $f$ is the [[Sets|set]] of all $y \in C$ for which there is at least one $x \in \mathcal{D}$ such that $y = f(x)$.
>>
>>$$
>>\{f(x) \mid x \in D\}
>>$$
>>
>>![[res/Image.svg]]
>>
>>>[!NOTATION]-
>>>
>>>$$
>>>f(\mathcal{D}) \qquad f[\mathcal{D}]
>>>$$
>>>
>>
>>>[!INTUITION]-
>>>
>>>The image of a function is essentially the set of all values in $C$ which $f$ can produce.
>>>
>>
>
>>[!INTUITION]-
>>
>>A function $f$ is just a rule which to each $x \in \mathcal{D}$ assigns a single $f(x) \in C$.
>>
>

>[!DEFINITION] Definition: Inverse Image
>
>Let $f: X \to Y$ be a [[Functions|function]].
>
>The **inverse image** of a [[Subsets|subset]] $S \subseteq Y$ under $f$ is the subset of $X$ defined as
>
>$$
>\{x \in X \mid f(x) \in S \}
>$$
>
>>[!NOTATION]-
>>
>>$$
>>f^{-1} [S] \qquad f^{-1}(S) \qquad f^{-}(S)
>>$$
>>
>

>[!DEFINITION] Definition: Restriction
>
>Let $f: X \to Y$ be a [[Functions|function]].
>
>The **restriction** of $f$ on a [[Subsets|subset]] $S \subseteq X$ is the function $f\big|_S: S \to Y$ defined as
>
>$$
>f\big|_S (x) = f(x) \qquad \forall x \in S
>$$
>