---
title: Ellipse
tags:
    - planimetry
    - geometry
    - mathematics
---

# Ellipse

>[!DEFINITION] Definition: Ellipse
>
>Let $\lambda$ be a [[Planes|plane]] and let $F_1$ and $F_2$ be points from $\lambda$.
>
>The **ellipse** $E$ with **foci** $F_1$ and $F_2$ is the [[Sets|subset]] of $\lambda$ such that the sum of the distances between each point of $E$ and the points $F_1$ and $F_2$ is constant.
>
>$$
>E = \{ P \in \lambda \mid d(P; F_1) + d(P; F_2) = \text{const} \}
>$$
>
>The midpoint $O$ of the [[Line Segments|line segment]] $F_1F_2$ is known as $E$'s **center**.
>
>The **major axis** of $E$ is the [[Line Segments|line segment]] joining the two points of $E$ which are the farthest away from $O$.
>
>The **minor axis** of $E$ is the [[Line Segments|line segment]] connecting the two points of $E$ which are the closest to $O$.
>

>[!DEFINITION] Definition: Linear Eccentricity
>
>The **linear eccentricity** of an [[Ellipse]] is the distance from its center to its foci.
>
>>[!NOTATION]
>>
>>The linear eccentricity is usually denoted by $c$.
>>
>
>>[!THEOREM]- Theorem: Calculating Linear Eccentricity
>>
>>The [[Ellipse|linear eccentricity]] of an [[Ellipse]] can be calculated using the length $a$ of its semi-major axis and the length $b$ of its semi-minor axis:
>>
>>$$
>>c = \sqrt{a^2 - b^2}
>>$$
>>
>>>[!PROOF]-
>>>
>>>TODO
>>>
>>
>

## Properties

>[!THEOREM]- Theorem: Distance in Ellipses
>
>For each point $P$ of an [[Ellipse]] $E$, the sum of the distances from $P$ to the foci $F_1$ and $F_2$ is equal to the length of the major axis.
>
>$$
>d(P, F_1) + d(P, F_2) = 2a
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

## Standard Equation

>[!THEOREM] Theorem: Standard Equation of an Ellipse
>
>If $E$ is whose center has coordinates $(0,0)$, then the coordinates $(x,y)$ of each point of $E$ satisfy
>
>$$
>\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1,
>$$
>
>where $a$ is half the length of $E$'s [[Ellipse|major axis]] and $b$ is half the length of $E$'s [[Ellipse|minor axis]].
>
>>[!PROOF]-
>>
>>TODO
>>
>