---
title: Spherical Coordinate System
tags:
    - coordinate-systems
    - euclidean-geometry
    - geometry
    - mathematics
---

# Spherical Coordinates

Each vector (point) $P$ in the 3-dimensional [[The Topology of Euclidean Space|Euclidean space]] $\mathbb{R}^3$ can be uniquely identified using its magnitude $r$ (distance from the origin), the angle $\theta$ it makes with the $z$-axis and the angle $\phi$ its projection in the $xy$ plane makes with the $x$-axis.

![[res/Spherical Coordinates.drawio.svg]]

>[!DEFINITION] Definition: Radial Distance (Radius)
>
>The number $r$ is known as **radial distance** or **radius**.
>

>[!DEFINITION] Definition: Inclination (Polar Angle)
>
>The number $\theta$ is known as the **inclination** or **polar angle**.
>

>[!DEFINITION] Definition: Azimuth (Azimuthal Angle)
>
>The number $\phi$ is known as the **azimuth** or **azimuthal angle**.
>

## Conventions

The radial distance can be denoted either by $r$ or $\rho$. Some people also switch $\theta$ and $\phi$ around, using the former for the azimuthal angle and the latter for the polar angle. 

>[!NOTE]- Note: Elevation
>
>Instead of inclination, some people prefer to use **elevation**. This is the angle between the point and the $xy$-plane and is equal to $\frac{\pi}{2}$ minus the inclination.
>

If the range of values for the angles is not restricted, then every point has infinitely many different spherical coordinates because adding or subtracting an integer multiple of $2\pi$ to an angle does not change the point it corresponds to. However, in order to have a [[index|coordinate system]], coordinates must be unique. To guarantee this, the set of possible values for the angles needs to be restricted. Two of the most common conventions are $\theta \in [0;\pi]$, $\phi \in [0; 2\pi)$ and $\theta \in [0;\pi]$, $\phi \in (-\pi; \pi]$.