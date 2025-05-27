---
title: Geometric Series
tags:
    - real-series
    - real-analysis
    - mathematics
---

# Geometric Series

>[!DEFINITION] Definition: Geometric Series
>
>A **geometric series** is a [[Real Series]] $\sum_{n = 1}^{\infty} a_n$ such that the [[Real Sequences|sequence]] $(a_n)_{n \in \mathbb{N}}$ can be specified as
>
>$$
>a_n = q^{n-1}a
>$$
>
>for some [[The Real Numbers|real numbers]] $a$ and $q$ with $q \ne 0$.
>

## Properties

>[!THEOREM]- Theorem: Product of Members of Geometric Series
>
>If $a_p$ and $a_m$ are members of a [[Geometric Series]], then for all $k \in \mathbb{N}$ with $k \lt m$, we have
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM]- Theorem: Partial Sums of Geometric Series
>
>The $n$-th [[Real Series#Partial Sums|partial sum]] $S_n$ of a [[Geometric Series]] $a_n$ with ratio $q$ is given by
>
>$$
>S_n = \frac{1 - q^n}{1 - q}a_1
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM]- Theorem: Convergence of Geometric Series
>
>A [[Geometric Series]] $(a_n)_{n \in \mathbb{N}}$ with ratio $q$ [[Convergence|converges absolutely]] if and only if $|q| \lt 1$ and [[Convergence|diverges otherwise]]. If $(a_n)_{n \in \mathbb{N}}$ [[Convergence|converges]], then
>
>$$
>\sum_{n = 1}^{\infty} a_n = \frac{a_1}{1 - q}
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>