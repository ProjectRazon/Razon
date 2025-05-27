---
title: Topology of the Complex Plane
tags:
    - complex-analysis
    - topology
    - mathematics
---

# Topology of the Complex Plane

>[!THEOREM] Theorem: Topology of the Complex Plane
>
>The function $d: \mathbb{C} \times \mathbb{C} \to \mathbb{R}$ defined as
>
>$$
>d(z_1, z_2) = |z_2 - z_1|
>$$
>
>is a [[index|metric]] on the [[index|complex numbers]].
>
>>[!PROOF]-
>>
>>TODO
>>
>
>>[!NOTE]
>>
>>As a metric, $d$ induces a [[index#The Metric Topology|topology]] on $\mathbb{C}$ and, unless otherwise specified, all topology-related terminology relates to this induced topology.
>>
>

## Neighborhoods

>[!DEFINITION] Definition: $r$-Neighborhood
>
>Let $r \gt 0$ and $z \in \mathbb{R}$.
>
>The $r$-**neighborhood** of $z$ is the [[index|open ball]] $B_r(z)$, i.e. 
>
>$$
>B_r(z) = \{x \in \mathbb{C} \mid |x - z| \lt r\}
>$$
>

>[!DEFINITION] Definition: Deleted $r$-Neighborhood
>
>Let $r \gt 0$ and $z \in \mathbb{R}$.
>
>The **deleted** $r$**-neighborhood** of $z$ is its $r$-[[Topology of the Complex Plane|neighborhood]] without $z$ itself:
>
>$$
>B_r(z) \setminus \{z\} = \{x \in \mathbb{C} \mid 0 \lt |x - z| \lt r \}
>$$
>

### Properties

>[!THEOREM] Theorem: Boundary and Interior of Neighborhoods
>
>Let $r \gt 0$ and $z \in \mathbb{C}$.
>
>The [[Interior, Boundary and Exterior|boundary]] of the $r$-[[Topology of the Complex Plane#Neighborhoods|neighborhood]] and the deleted $r$-[[Topology of the Complex Plane#Neighborhoods|neighborhood]] of $z$ is the disk
>
>$$
>\{ x \in \mathbb{C} \mid |x - z| = r \}
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>