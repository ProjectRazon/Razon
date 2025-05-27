---
title: Operations with Complex Numbers
tags:
  - operations
  - complex-numbers
  - abstract-algebra
  - algebra
  - mathematics
---

# Complex Conjugation

>[!DEFINITION] Definition: Complex Conjugate
>
>The **complex conjugate** of a [[index#complex numbers|complex number]] $z = a +\mathrm{i}b$ is the number
>
>$$
>\bar z \overset{\text{def}}{=} a - \mathrm{i}b
>$$
>

>[!THEOREM] Theorem: Distributivity of Complex Conjugation
>
>The [[Operations|complex conjugation]] of is distributive over [[Operations|addition]] and [[Operations|multiplication]]:
>
>$$
>\overline{z_1 + z_2} = \bar{z}_1 + \bar{z}_2
>$$
>
>$$
>\overline{z_1 \cdot z_2} = \bar{z}_1 \cdot \bar{z}_2
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

# Arithmetic with Complex Numbers

>[!DEFINITION] Definition: Addition and Subtraction of Complex Numbers
>
>The **addition** and **subtraction** of two [[index|complex numbers]] $z_1 = a + \mathrm{i}b$ and $z_2 = c +\mathrm{i}d$ are defined as
>
>$$
>z_1 \pm z_2 \overset{\text{def}}{=} (a\pm c) + \mathrm{i}(b \pm d)
>$$

>[!DEFINITION] Definition: Multiplication of Complex Numbers
>
>The **multiplication** of two [[index|complex numbers]] $z_1 = a + \mathrm{i}b$ and $z_2 = c +\mathrm{i}d$ is defined as
>
>$$
>z_1 \cdot z_2 \overset{\text{def}}{=} (ac - bd) + \mathrm{i}(ad + bc)
>$$
>
>>[!THEOREM] Theorem: Multiplication in Polar Form
>>
>>If $z_1$ and $z_2$ have the [[index#the forms of a complex number|polar forms]] $z_1 = r_1(\cos \varphi_1 +\mathrm{i}\sin\varphi_1)$ and $z_2 = r_2(\cos \varphi_2 +\mathrm{i}\sin\varphi_2)$, then
>>
>>$$
>>z_1\cdot z_2 = r_1r_2(\cos (\varphi_1+\varphi_2) +\mathrm{i}\sin(\varphi_1+\varphi_2))
>>$$
>>
>>>[!PROOF]-
>>>
>>>TODO
>>>
>>
>
>>[!THEOREM] Theorem: Multiplication in Exponential Form
>>
>>If $z_1$ and $z_2$ have the [[index#the forms of a complex number|exponential forms]] $z_1 = r_1\mathrm{e}^{\mathrm{i}\varphi_1}$ and $z_2 = r_2\mathrm{e}^{\mathrm{i}\varphi_2}$, then
>>
>>$$
>>z_1 \cdot z_2 = r_1r_2\mathrm{e}^{\mathrm{i}(\varphi_1+\varphi_2)}
>>$$
>>
>>>[!PROOF]-
>>>
>>>TODO
>>>
>>
>>

>[!DEFINITION] Definition: Division of Complex Numbers
>
>The **division** of two [[index|complex numbers]] $z_1 = a + \mathrm{i}b$ and $z_2 = c +\mathrm{i}d$ is
>
>$$
>\frac{z_1}{z_2} \overset{\text{def}}{=} \frac{z_1\cdot \bar{z}_2}{|z_2|^2}
>$$
>

>[!THEOREM] Theorem: The Field of the Complex Numbers
>
>The [[Sets|set]] of all [[index|complex numbers]] $\mathbb{C}$ forms a [[index|field]] together with the [[Operations|addition and multiplication]] defined on it.
>
>>[!PROOF]-
>>
>>TODO
>>
>