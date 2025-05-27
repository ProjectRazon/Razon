---
title: Continuity in Metric Spaces
tags:
  - continuity
  - metric-spaces
  - topology
  - mathematics
---

>[!THEOREM] Theorem: Continuity at a Point
>
>Let $(X, d_X)$ and $(Y, d_Y)$ be [[index|metric spaces]].
>
>A [[Functions|function]] $f: X \to Y$ is [[index#^continuity-at-a-point]] at $x_0 \in X$ if and only if for each [[index|open ball]] $B_\varepsilon(f(x_0))$ around $f(x_0)$ there exists some [[index|open ball]] $B_\delta(x_0)$ around $x_0$ such that if $x$ is inside $B_\delta(x_0)$, then $f(x)$ is inside $B_\varepsilon(f(x_0))$.
>
>$$
>\forall \varepsilon \gt 0, \exists \delta \gt 0: x \in B_\delta(x_0) \implies f(x) \in B_\varepsilon(f(x_0))
>$$
>
>>[!PROOF]-
>>
>>
>>
>