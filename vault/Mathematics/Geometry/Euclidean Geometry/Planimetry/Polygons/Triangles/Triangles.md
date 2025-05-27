---
title: Triangles
tags:
  - triangles
  - planimetry
  - euclidean-geometry
  - geometry
  - mathematics
  - polygons
---

# Triangles

>[!DEFINITION] Definition: Triangle
>
>A **triangle** is a [[Polygons|polygon]] with three [[Polygons|vertices]] and three [[Polygons|sides]].
>
>![[res/Triangles.svg]]
>

## Properties

>[!THEOREM]- Theorem: Sum of Interior Angles
>
>The sum of the [[Polygons#Interior Angles|interior angles]] $\alpha, \beta, \gamma$ of a [[Triangles|triangle]] is always $180 \degree$.
>
>$$
>\alpha + \beta + \gamma = 180 \degree
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM]- Theorem: The Triangle Inequality
>
>If a [[Triangles|triangle]] has side lengths $a, b,c$, then
>
>$$
>\begin{align*} a + b \gt c \\ b + c \gt a \\ a + c \gt b \end{align*}
>$$
>
>Conversely, if $a, b, c$ are positive [[The Real Numbers|real numbers]] for which all of the above inequalities hold, then there exists a [[Triangles|triangle]] with side lengths $a, b, c$.
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM]- Theorem: Cyclicity of Triangles
>
>Every [[Triangles|triangle]] is a [[Cyclic Polygon|cyclic]].
>
>>[!PROOF]-
>>
>>TODO
>>
>
>>[!DEFINITION] Definition: Circumcircle
>>
>>The **circumcircle** of a [[Triangles|triangle]] is the [[Circle]] on which all of its the vertices lie.
>>
>

>[!THEOREM]- Theorem: Law of Sines
>
>The ratios of each side in a [[Triangles|triangle]] to the [[Real Sine Function|sine]] of its opposite angle are all equal to the [[Circle|diameter]] of the [[Triangles#Properties|circumcircle]].
>
>$$
>\frac{a}{\sin \alpha} = \frac{b}{\sin \beta} = \frac{c}{\sin \gamma} = 2R
>$$
>
>![[res/Law of Sines.svg]]
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM]- Theorem: Law of Cosines
>
>The side lengths $a,b,c$ of a [[Triangles|triangle]] and the [[Real Cosine Function|cosines]] of the corresponding opposite angles $\alpha$, $\beta$, $\gamma$ are related as follows:
>
>$$
>\begin{align*}
>a^2 &= b^2 + c^2 - 2bc \cos \alpha \\
>b^2 &= a^2 + c^2 - 2ac \cos \beta \\
>c^2 &= a^2 + b^2 - 2ab \cos \gamma
>\end{align*}
>$$
>
>![[res/Law of Cosines.svg|Law of Cosines]]
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM]- Theorem: Menelaus's Theorem
>
>Let $\triangle ABC$ be a [[Triangles|triangle]] and let $A'$, $B'$ and $C'$ be points respectively on the [[Straight Line|lines]] defined by the sides $BC$, $AC$ and $AB$.
>
>The points $A'$, $B'$ and $C'$ lie on one [[Straight Line]] if and only if exactly one or three of them lie outside of the triangle's sides and
>
>$$
>\frac{AC'}{BC'} \cdot \frac{BA'}{CA'} \cdot \frac{CB'}{AB'} = 1
>$$
>
>- If exactly one of the points lies outside of the triangle's sides, then this line is outside the triangle.
>- If exactly three of these points lie outside the triangle's sides, then this line passes through the triangle.
>
>![[res/Menelaus's Theorem.svg]] 
>
>>[!PROOF]-
>>
>>TODO
>>
>

# Similarity

## Characterizations

>[!THEOREM]- Theorem: Angle-Angle-Angle (AAA)
>
>Two [[Triangles]] are [[Geometric Shapes#Similarity|similar]] if and only if their three angles are respectively equal.
>
>$$
>\triangle ABC \sim \triangle A'B'C' \iff \begin{cases} \angle A = \angle A' \\ \angle B = \angle B' \\ \angle C = \angle C \end{cases}
>$$
>
>![[res/Similar Triangles - AAA.svg]]
>
>>[!PROOF]-
>>
>>TODO
>>
>
>>[!TIP]
>>
>>In practice, one only needs two angles and not three, since the third can always be determined using the [[Triangles#Properties|sum of angles theorem]].
>>
>

>[!THEOREM]- Theorem: Side-Side-Side (SSS)
>
>Two [[Triangles]] are [[Geometric Shapes#Similarity|similar]] if and only if each side in one can be paired with another such that the ratios of these pairs are all equal.
>
>$$
>\triangle ABC \sim \triangle A'B'C' \iff \frac{AB}{A'B'} = \frac{BC}{B'C'} = \frac{AC}{A'C'}
>$$
>
>![[res/Similar Triangles - SSS.svg]]
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM]- Theorem: Side-Angle-Side (SAS)
>
>Two [[Triangles]] are [[Geometric Shapes#Similarity|similar]] if and only if two sides of one triangle can be paired with two sides of the other such that the ratios of the pairs are equal and the angles between these sides are equal.
>
>$$
>\triangle ABC \sim \triangle A'B'C' \iff \begin{cases} \frac{AB}{A'B'} = \frac{AC}{A'C'} \\ \angle A = \angle A' \end{cases}
>$$
>
>![[res/Similar Triangles - SAS.svg]]
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM]- Theorem: Side-Side-Angle (SSA)
>
>Two [[Triangles]] are [[Geometric Shapes#Similarity|similar]] if and only if two sides of one triangle can be paired with two sides of the other such that the ratios of the pairs are equal and the angles opposite to the longer of these sides are equal.
>
>$$
>\triangle ABC \sim \triangle A'B'C' \iff \begin{cases} \frac{AB}{A'B'} = \frac{BC}{B'C'} \\ AB \gt BC \\ A'B' \gt B'C' \\ \angle C = \angle C' \end{cases}
>$$
>
>![[res/Similar Triangles - SSA.svg]]
>
>>[!PROOF]-
>>
>>TODO
>>
>

# Congruence

>[!THEOREM]- Theorem: Side-Angle-Side (SAS)
>
>Two [[Triangles]] $T_1$ and $T_2$ are [[Geometric Shapes|congruent]] if and only if two sides of $T_1$ and the [[Line Segments|angle]] between them are respectively equal to two sides of $T_2$ and the angle between them.
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM]- Theorem: Angle-Side-Angle
>
>Two [[Triangles]] $T_1$ and $T_2$ are [[Geometric Shapes|congruent]] if and only if two [[Polygons|interior angles]] of $T_1$ and the side joining them are respectively equal to two [[Polygons|interior angles]] of $T_2$ and the side joining them.
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM]- Theorem: Side-Side-Side (SSS)
>
>Two [[Triangles]] $T_1$ and $T_2$ are [[Geometric Shapes|congruent]] if and only if the three sides of $T_1$ are respectively equal to the three sides of $T_2$.
>
>>[!PROOF]-
>>
>>TODO
>>
>

# Surface Area

>[!THEOREM]- Theorem: Heron's Formula (Area using Sides)
>
>The [[Polygons|area]] $A$ of a [[Triangles|triangle]] with [[Polygons|sides]] $a,b,c$ and [[Polygons|semiperimeter]] $p$ is given by
>
>$$A = \sqrt{p(p-a)(p-b)(p-c)}$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM]- Theorem: Area using Altitudes
>
>The [[Polygons|area]] $S$ of a [[Triangles|triangle]] with [[Polygons|sides]] $a,b,c$ and corresponding [[Altitudes]] $h_a,h_b,h_c$ is given by
>
>$$S = \frac{a \cdot h_a}{2} = \frac{b \cdot h_b}{2} = \frac{c \cdot h_c}{2}$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM]- Theorem: Area using Medians
>
>The [[Polygons|area]] $S$ of a [[Triangles|triangle]] with [[Medians]] $m_a, m_b, m_c$ is given by
>
>$$S = \frac{4}{3}\sqrt{\sigma(\sigma - m_a) (\sigma - m_b) (\sigma - m_c)},$$
>
>where  $\sigma = \frac{m_a + m_b + m_c}{2}$.
>
>>[!PROOF]-
>>
>>TODO
>>
>