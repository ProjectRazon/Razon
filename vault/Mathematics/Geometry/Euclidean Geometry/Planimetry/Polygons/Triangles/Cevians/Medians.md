---
title: Medians
tags:
  - triangles
  - polygons
  - planimetry
  - euclidean-geometry
  - geometry
  - mathematics
---

# Medians

>[!DEFINITION] Definition: Median
>
>A **median** in a [[Triangles|triangle]] is a [[Cevians|cevian]] which connects a [[Polygons|vertex]] of the triangle to the [[Line Segments|midpoint]] of the opposite [[Polygons|side]].
>
>![[res/Median.jpg|Median]]
>
>>[!NOTATION]-
>>
>>The median towards the side $s$ is usually denoted as $m_s$.
>>
>

## Properties

>[!THEOREM] Theorem: Concurrency of a Triangle's Medians
>
>The [[Medians]] of a [[Triangles|triangle]] are all [[Concurrent Lines|concurrent]] and intersect at its [[Centroid]].
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Median Lengths from Side Lengths (Apollonius's Theorem)
>
>If a [[Triangles|triangle]] has [[Polygons|sides]] $a,b,c$, then their respective [[Medians]] are given by
>
>$$\begin{align*} m_a &= \frac{1}{2}\sqrt{2b^2+2c^2-a^2} \\ m_b &= \frac{1}{2}\sqrt{2a^2+2c^2-b^2} \\ m_c &= \frac{1}{2}\sqrt{2a^2+2b^2-c^2}\end{align*}$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Side Lengths from Median Lengths
>
>If a [[Triangles|triangle]] has [[Medians]] $m_a,m_b,m_c$, then their respective [[Polygons|sides]] are given by
>
>$$\begin{align*} a &= \frac{2}{3}\sqrt{2m_b^2 + 2m_c^2 -m_a^2} \\ b &= \frac{2}{3}\sqrt{2m_a^2 + 2m_c^2 -m_b^2} \\ c &= \frac{2}{3}\sqrt{2m_a^2 + 2m_b^2 - m_c^2} \end{align*}$$
>
>>[!PROOF]-
>>
>>TODO
>>
>
>>[!NOTE]
>>
>>This means that a triangle is completely determined by its medians.
>>
>