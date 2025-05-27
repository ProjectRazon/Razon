---
title: Complex Numbers
tags:
  - complex-numbers
  - field-theory
  - abstract-algebra
  - algebra
  - mathematics
---

# The Imaginary Unit

>[!DEFINITION] Definition: The Imaginary Unit
>
>The **imaginary unit** $\mathrm{i}$ is a number with the property
>
>$$
>\mathrm{i}^2 = -1
>$$
>

## Imaginary Numbers

>[!DEFINITION] Definition: Imaginary Number
>
>An **imaginary number** has the form $\mathrm{i}b$, where $\mathrm{i}$ is the [[index#the imaginary unit|imaginary unit]] and $b \in \mathbb{R}$ is a [[The Real Numbers|real number]].
>

# Complex Numbers

>[!DEFINITION] Definition: Complex Number
>
>A **complex number** has the form $a + \mathrm{i}b$, where $\mathrm{i}$ is the [[index|imaginary unit]] and $a,b \in \mathbb{R}$ are [[The Real Numbers|real numbers]].
>
>>[!NOTATION]-
>>
>>Complex numbers are usually denoted by $z$.
>>
>>The [[Sets|set]] of all complex numbers is denoted by $\mathbb{C}$.
>>
>
>>[!DEFINITION] Definition: Real Part
>>
>>The **real part** of a complex number $z = a + \mathrm{i}b$ is $a$.
>>
>>>[!NOTATION]-
>>>
>>>$$
>>>\operatorname{Re}(z) \qquad \Re(z) 
>>>$$
>>>
>>
>
>>[!DEFINITION] Definition: Imaginary Part
>>
>>The **imaginary part** of a complex number $z = a + \mathrm{i}b$ is $b$.
>>
>>>[!NOTATION]-
>>>
>>>$$
>>>\operatorname{Im}(z) \qquad \Im(z)
>>>$$
>>>
>>
>

## The Complex Plane

[[index|Complex numbers]] can be plotted on a plane where the horizontal axis contains the [[The Real Numbers|real numbers]] and the vertical axis contains the [[index#imaginary numbers|imaginary numbers]].

![[res/The Complex Plane.svg]]

### Modulus

>[!DEFINITION] Definition: Modulus (Absolute Value) of a Complex Number
>
>The **modulus** (or **absolute value**) of a [[index|complex number]] $z \in \mathbb{C}$ is defined as the square root of the sum of the squares of its real and imaginary parts
>
>$$
>\sqrt{\operatorname{Re}^2(z) + \operatorname{Im}^2(z)}
>$$
>
>>[!NOTATION]
>>
>>$$
>>|z|
>>$$
>>
>

>[!THEOREM] Theorem: Triangle Inequality for Complex Numbers
>
>For the [[index#modulus|moduli]] of all [[index|complex numbers]] $z_1$ and $z_2$
>
>$$
>|z_1 + z_2| \le |z_1| + |z_2|
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

### Argument

>[!DEFINITION] Definition: Argument of a Complex Number
>
>The **argument** $\arg (z)$ of a [[index|complex number]] $z = a + \mathrm{i}b$ is the angle between $z$ and the real axis in the [[index#the complex plane|the complex plane]].
>
>>[!NOTATION]
>>
>>$$
>>\arg (z)
>>$$
>
>>[!NOTE]
>>
>>By convention, the argument lies in the range $(-\pi; \pi]$. Positive angles are assigned to numbers of the real axis and negative angles are assigned to numbers below it.
>>
>

## The Forms of a Complex Number

>[!DEFINITION] Definition: Cartesian Form of Complex Numbers
>
>The **cartesian form** of a [[index#complex numbers|complex number]] $z$ is just its usual form $z = a+\mathrm{i}b$.
>

>[!DEFINITION] Definition: Polar Form of a Complex Number
>
>The **polar form** of a [[index#complex numbers|complex number]] $z$ is
> 
>$$
>z = r(\cos \varphi + \mathrm{i}\sin \varphi),
>$$
>
>where $r$ is the [[index|magnitude]] of $z$ and $\varphi$ is its [[index|argument]].
>

>[!DEFINITION] Definition: Exponential Form of a Complex Number
>
>The **exponential form** of a [[index#complex numbers|complex number]] $z$ is $r\mathrm{e}^{\mathrm{i}\varphi}$, where $r$ is the [[index|magnitude]] of $z$ and $\varphi$ is its [[index|argument]].
>

### Form Conversions

>[!THEOREM] Theorem: Cartesian $\to$ Polar
>
>Let $z = a +\mathrm{i}b$ be a [[index|complex number]] in [[index#the forms of a complex number|cartesian form]].
>
>The [[index#the forms of a complex number|polar form]] of $z$ is $r(\cos \varphi +\mathrm{i}\sin \varphi)$, where
>
>$$
>\begin{align*} r &= \sqrt{a^2+b^2} \\ \varphi &= \begin{cases}\displaystyle\hphantom{-}\arccos \left(\frac{a}{r}\right) \qquad b \ge 0 \\ \displaystyle -\arccos \left(\frac{a}{r}\right) \qquad b \lt 0\end{cases}\end{align*}
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Polar $\to$ Cartesian
>
>Let $z = r(\cos \varphi + \mathrm{i}\sin \varphi)$ be a [[index|complex number]] in [[index#the forms of a complex number|polar form]].
>
>The [[index#the forms of a complex number|cartesian form]] of $z$ is $a +\mathrm{i}b$, where
>
>$$
>\begin{align*}a &= r \cos (\varphi) \\ b &= r\sin(\varphi)\end{align*}
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>