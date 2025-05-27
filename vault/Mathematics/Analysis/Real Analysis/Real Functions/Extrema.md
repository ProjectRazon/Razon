---
title: Extrema
tags:
  - extreme-values
  - real-functions
  - real-analysis
  - analysis
  - mathematics
---

# Local Extrema


>[!DEFINITION] Definition: Local Minimum
>
>Let $f: D \subseteq \mathbb{R} \to \mathbb{R}$ be a [[Functions of the Real Numbers|real function]].
> 
>We say that $f$ **has a local minimum at** $a \in \mathbb{D}$ if there is some $\varepsilon \gt 0$ such that
>
>$$
>f(a) \le f(x) \qquad \forall x \in (a - \varepsilon; a + \varepsilon)
>$$
>
>This **local minimum** is $f(a)$.

>[!DEFINITION] Definition: Local Maximum
>
>Let $f: D \subseteq \mathbb{R} \to \mathbb{R}$ be a [[Functions of the Real Numbers|real function]].
> 
>We say that $f$ **has a local maximum at** $a \in \mathbb{D}$ if there is some $\varepsilon \gt 0$ such that
>
>$$
>f(a) \ge f(x) \qquad \forall x \in (a - \varepsilon; a + \varepsilon)
>$$
>
>This **local maximum** is $f(a)$.
>

>[!DEFINITION] Definition: Local Extremum
>
>The local minima and maxima of a function are known as its **local extrema**.
>
>TODO: Add Diagram
>

# Global Extrema


>[!DEFINITION] Definition: Global Minimum
>
>Let $f: D \to \mathbb{R}$ be a [[Functions of the Real Numbers|real function]].
>
>We say that $f$ **has a global minimum at** $a \in D$ if
>
>$$
>f(a) \le f(x) \qquad \forall x \in D
>$$
>
>This **global minimum** is $f(a)$.
>
>>[!NOTE]
>>
>>There cannot be more than one value for the global minimum, but there may be multiple places in the domain of the function where said minimum occurs.
>>
>

>[!DEFINITION] Definition: Global Maximum
>
>Let $f: D \to \mathbb{R}$ be a [[Functions of the Real Numbers|real function]].
>
>We say that $f$ **has a global maximum at** $a \in D$ if
>
>$$
>f(a) \ge f(x) \qquad \forall x \in D
>$$
>
>This **global maximum** is $f(a)$.
>
>>[!NOTE]
>>
>>There cannot be more than one value for the global maximum, but there may be multiple places in the domain of the function where said maximum occurs.
>>
>

>[!DEFINITION] Definition: Global Extremum
>
>The global minimum and maximum of a function are known as its **global extrema**.
>

# Finding Extrema

>[!THEOREM] Theorem: Critical Points and Local Extrema
>
>Let $f: D \subseteq \mathbb{R} \to \mathbb{R}$ be a [[Functions of the Real Numbers|real function]].
>
>All [[Extrema|local extrema]] of $f$ occur at [[Differentiability|critical points]] of $f$.
>
>>[!PROOF]-
>>
>>TODO
>
>>[!THEOREM] Theorem: Criteria of the First Derivative
>>
>>If $f$ is [[Continuity|continuous]] and [[Differentiability|differentiable]] at a [[Differentiability|critical point]] $x_0$, then:
>>- $f$ has a [[Extrema|local minimum]] at $x_0$ if there is some $\varepsilon \gt 0$ such that
>>
>>$$
>>f'(x) \lt 0 \qquad \forall x \in (x_0 - \varepsilon; x_0) \qquad \text{ and } \qquad f'(x) \gt 0 \qquad \forall x \in (x_0; x_0 + \varepsilon)
>>$$
>>
>>- $f$ has a [[Extrema|local maximum]] at $x_0$ if there is some $\varepsilon \gt 0$ such that
>>
>>$$
>>f'(x) \gt 0 \quad \forall x \in (x_0-\varepsilon; x_0)\qquad \text{ and } \qquad f'(x) \lt 0 \quad \forall x\in (x_0; x_0+\varepsilon)
>>$$
>>
>>>[!PROOF]-
>>>
>>>TODO
>>
>
>>[!THEOREM] Theorem: Criteria of the Second Derivative
>>
>>If $f$ is [[Continuity|continuous]] and [[Differentiability|twice differentiable]] at a [[Differentiability|critical point]] $x_0$, then:
>>
>>- $f$ has a [[Extrema|local minimum]] at $x_0$ if its [[Differentiability|second derivative]] at $x_0$ is positive, i.e. $f''(x_0) \gt 0$;
>>- $f$ has a [[Extrema|local maximum]] at $x_0$ if its [[Differentiability|second derivative]] at $x_0$ is negative, i.e. $f''(x_0) \lt 0$.
>>
>>>[!WARNING]
>>>
>>>If $f''(x_0) = 0$ or $f$ is not [[Differentiability|twice differentiable]] at $x_0$, then $f$ may or may not have a [[Extrema|local extremum]] at $x_0$, but we cannot use the second derivative to verify this.
>>>
>>
>>>[!PROOF]-
>>>
>>>TODO
>>>
>>
>

>[!ALGORITHM] Algorithm: Finding the Extrema of a Function
>
>Requirements: $f: D \subseteq \mathbb{R} \to \mathbb{R}$ is [[Continuity|continuous]].
>
>1. Determine the [[Differentiability|critical points]] $x_1, x_2, \cdots, x_n \in D$ of $f$ by solving $f'(x) = 0$ and also seeing where $f$ is not [[Differentiability|differentiable]].
>2. Use the above criteria to check at which [[Differentiability|critical points]] $f$ has [[Extrema|local extrema]].
>3. Evaluate $f$ at the places of its [[Extrema|local extrema]] to obtain the values of the [[Extrema|local minima]] and [[Extrema|local maxima]].
>4. Evaluate $f$ at the following locations:
>	- If $D = [a;b]$ where $a,b \in \mathbb{R}$, evaluate $f(a)$ and $f(b)$;
>	-  If $D = [a;b)$ where $a \in \mathbb{R}$ and $b \in \mathbb{R} \cup \{\infty\}$, evaluate $f(a)$ and $\lim_{x\to b} f(x)$;
>	- If $D = (a;b]$ where $a \in \mathbb{R} \cup \{-\infty \}$ and $b \in \mathbb{R}$, evaluate $\lim_{x\to a} f(x)$ and $f(b)$;
>	- If $D = (a;b)$ where $a \in \mathbb{R} \cup \{-\infty \}$ and $b \in \mathbb{R} \cup \{\infty\}$, evaluate $\lim_{x\to a} f(x)$ and $\lim_{x\to b} f(x)$;
>	- If $D = D_1 \cup \cdots \cup D_n$ is a [[Set Operations|union]] of [[Disjoint Sets|disjoint]] intervals $D_1, \cdots, D_n$, then perform Step 4 separately for each interval.
>5. Compare the [[Extrema|local extrema]] of $f$ with the values from Step 4:
>	- If there is a greatest value, then it is the [[Extrema|global maximum]] of $f$;
>	- If there is a smallest value, then it is the [[Extrema|global minimum]] of $f$;