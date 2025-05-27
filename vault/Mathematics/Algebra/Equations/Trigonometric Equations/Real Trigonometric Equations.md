---
title: Real Trigonometric Equations
tags:
  - trigonometry
  - equations
  - algebra
  - mathematics
---

# Real Trigonometric Equations

>[!DEFINITION] Definition: Trigonometric Equation
>
>A **trigonometric equation** is an [[Equation]] which contains variables in the arguments of [[Real Trigonometric Functions]].
>

## Elementary Trigonometric Equations

>[!ALGORITHM]- Algorithm: Solving Equations of the Form $\sin x = c$
>
>$$
>\sin x = c
>$$
> 
>Solutions:
>- If $|c| \gt 1$, then $x \in \varnothing$.
>- If $c \in [-1;1]$, then
>
>$$
>\begin{align*}x &= \arcsin c + 2k \pi \\ x &= -\arcsin c + (2k+1)\pi \end{align*} \qquad k \in \mathbb{Z}
>$$
>

>[!ALGORITHM]- Algorithm: Solving Equations of the Form $\cos x = c$
>
>$$
>\cos x = c
>$$
>
>Solutions:
>- If $|c| \gt 1$, then $x \in \varnothing$.
>- If $c \in [-1;1]$, then
>
>$$
>x =\pm \arccos c +  2k\pi \qquad k \in \mathbb{Z}
>$$
>

>[!ALGORITHM]- Algorithm: Solving Equations of the Form $\tan x = c$
>
>$$
>\tan x = c
>$$
>
>Requirements:
>- $x \ne \frac{\pi}{2} + k\pi \qquad k \in \mathbb{Z}$
>
>Solution:
>
>$$
>x = \arctan c + k\pi \qquad k \in \mathbb{Z}
>$$ 
>

>[!ALGORITHM]- Algorithm: Solving Equations of the Form $\cot x = c$
>
>$$
>\cot x = c
>$$
>
>Requirements:
>- $x \ne k\pi \qquad k \in \mathbb{Z}$
>
>Solution:
>
>$$
>x = \mathop{\operatorname{arccot}} + k\pi \qquad k \in \mathbb{Z}
>$$ 
>

## Composed Trigonometric Equations

>[!ALGORITHM]- Algorithm: Solving Equations of the Form $\sin f(x) = \sin g(x)$
>
>We are given a [[Real Trigonometric Equations|trigonometric equation]] of the form
>
>$$
>\sin f(x) = \sin g(x)
>$$
>
>Solution:
>
>$$
>\begin{align*}f(x) &= g(x) + 2k\pi \\ f(x) &= -g(x) + (2k+1)\pi \end{align*} \qquad k \in \mathbb{Z}
>$$
>
>

>[!ALGORITHM]- Algorithm: Solving Equations of the Form $\cos f(x) = \cos g(x)$
>
>We are given a [[Real Trigonometric Equations|trigonometric equation]] of the form
>
>$$
>\cos f(x) = \cos g(x)
>$$
>
>Solution:
>
>$$
>f(x) = \pm g(x) + 2k\pi \qquad k \in \mathbb{Z}
>$$
>

>[!ALGORITHM]- Algorithm: Solving Equations of the Form $\tan f(x) = \tan g(x)$
>
>We are given a [[Real Trigonometric Equations|trigonometric equation]] of the form
>
>$$
>\tan f(x) = \tan g(x)
>$$
>
>Requirements:
>- $f(x),g(x) \ne \frac{\pi}{2} + k\pi \qquad k \in \mathbb{Z}$
>
>Solution:
>
>$$
>f(x) = g(x) + k\pi \qquad k \in \mathbb{Z}
>$$
>

>[!ALGORITHM]- Algorithm: Solving Equations of the Form $\cot f(x) = \cot g(x)$
>
>We are given a [[Real Trigonometric Equations|trigonometric equation]] of the form
>
>$$
>\cot f(x) = \cot g(x)
>$$
>
>Requirements:
>- $f(x), g(x) \ne k\pi \qquad k \in \mathbb{Z}$
>
>
>Solution:
>
>$$
>f(x) = g(x) + k\pi \qquad k \in \mathbb{Z}
>$$
>

## Homogeneous Trigonometric Equations

>[!DEFINITION] Definition: Homogeneous Trigonometric Equation
>
>A **homogeneous trigonometric equation** is a [[Real Trigonometric Equations|trigonometric equation]] of the form
>
>$$
>a_0 \sin^n x + a_1 \sin^{n-1} x \cos x + \cdots + a_{n-1}\sin x \cos^{n-1} x + a_n \cos^n x = 0,
>$$
>
>where $a_k \in \mathbb{R}$.
>

>[!ALGORITHM]- Algorithm: Solving Homogeneous Trigonometric Equations (Tangent Substitution)
>
>We are given the following [[Homogeneous Trigonometric Equations]].
>
>$$
>a_0 \sin^n x + a_1 \sin^{n-1} x \cos x + \cdots + a_{n-1}\sin x \cos^{n-1} x + a_n \cos^n x = 0
>$$
>
>1. Check whether $\cos^n (x) = 0$, i.e. $x = \pm\frac{\pi}{2} + 2k\pi$ for $k \in \mathbb{Z}$, is a solution.
>2. Divide by $\cos^n (x)$.
>
>$$
>a_0 \frac{\sin^n x}{\cos^n x} + a_1 \frac{\sin^{n-1} x}{\cos^{n-1} x} + \cdots + a_{n-1} \frac{\sin x}{\cos x} + a_n = 0
>$$
>
>$$
>a_0 \tan^n x + a_1 \tan^{n-1} x + \cdots + a_{n-1} \tan x + a_n = 0
>$$
>
>3. Substitute $t = \tan x$ and solve the [[Polynomial Equations|polynomial equation]]
> 
>$$
>a_0 t^n + a_1 t^{n-1} + \cdots + a_{n-1} t + a_n = 0
>$$
>
>4. For each solution $t^\ast$ to the equation in Step 3, solve the [[Real Trigonometric Equations|elementary trigonometric equation]] $\tan x = t^\ast$.
>
>>[!EXAMPLE]-
>>
>>TODO
>>
>

>[!ALGORITHM]- Algorithm: Solving Homogeneous Trigonometric Equations (Cotangent Substitution)
>
>We are given the following [[Homogeneous Trigonometric Equations|homogeneous trigonometric equation]].
>
>$$
>a_0 \sin^n x + a_1 \sin^{n-1} x \cos x + \cdots + a_{n-1}\sin x \cos^{n-1} x + a_n \cos^n x = 0
>$$
>
>1. Check whether $\sin^n (x) = 0$, i.e. $x = k\pi$ for $k \in \mathbb{Z}$, is a solution.
>2. Divide by $\sin^n (x)$.
>
>$$
>a_0 + a_1 \frac{\cos x}{\sin x} + \cdots + a_{n-1} \frac{\cos^{n-1} x}{\sin^{n-1} x} + a_n \frac{\cos^n x}{\sin^n x} = 0
>$$
>
>$$
>a_0 + a_1 \cot x + \cdots + a_{n-1} \cot^{n-1} x + a_n\cot^n x = 0
>$$
>
>3. Substitute $t = \cot x$ and solve the [[Polynomial Equations|polynomial equation]]
> 
>$$
>a_0 + a_1 t + \cdots + a_{n-1} t^{n-1} + a_n t^n = 0
>$$
>
>4. For each solution $t^\ast$ to the equation in Step 3, solve the [[Real Trigonometric Equations|elementary trigonometric equation]] $\cot x = t^\ast$.
>
>>[!EXAMPLE]-
>>
>>TODO
>>
>

## Other Trigonometric Equations

>[!ALGORITHM]- Algorithm: Solving Trigonometric Equations of the Form $a \sin x + b \cos x = c$
>
>We are given a [[Real Trigonometric Equations|trigonometric equation]] of the following form.
>
>$$
>a \sin x + b \cos x = c
>$$
>
>1. Divide both sides by $\sqrt{a^2 + b^2}$.
>
>$$
>\frac{a}{\sqrt{a^2 + b^2}}\sin x + \frac{b}{\sqrt{a^2 + b^2}}\cos x = \frac{c}{\sqrt{a^2+b^2}}
>$$
>
>2. Substitute $\cos \varphi = \frac{a}{\sqrt{a^2 + b^2}}$ and $\sin \varphi = \frac{b}{\sqrt{a^2 + b^2}}$
>
>$$
>\cos \varphi \sin x + \sin \varphi \cos x = \frac{c}{\sqrt{a^2+b^2}}
>$$
>
>- The reason we can do this is that $\left(\frac{a}{\sqrt{a^2 + b^2}}\right)^2 +\left(\frac{b}{\sqrt{a^2 + b^2}}\right)^2 = 1$.
>
>3. Use an identity to simplify the left-hand side.
>
>$$
>\sin (x + \varphi) = \frac{c}{\sqrt{a^2+b^2}}
>$$
>
>- Requirements: $\frac{c}{\sqrt{a^2+b^2}} \in [-1;1]$
>
>4. Solve the [[Real Trigonometric Equations|elementary trigonometric equation]].
>
>$$
>\begin{align*}x + \varphi &= \arcsin\frac{c}{\sqrt{a^2+b^2}} + 2k\pi \\ x + \varphi &= -\arcsin\frac{c}{\sqrt{a^2+b^2}} + (2k+1)\pi \end{align*}
>$$
>
>5. Rearrange to isolate $x$.
>
>$$
>\begin{align*}x &= \arcsin\frac{c}{\sqrt{a^2+b^2}} -\varphi + 2k\pi \\ x &= -\arcsin\frac{c}{\sqrt{a^2+b^2}} -\varphi + (2k+1)\pi \end{align*}
>$$
>
>6.Substitute back for $\varphi$ to obtain the final set of solutions.
>
>- If you substitute back $\varphi = \arccos \frac{a}{\sqrt{a^2 + b^2}}$, you obtain
>
>$$
>\begin{align*}x &= \arcsin\frac{c}{\sqrt{a^2+b^2}} - \arccos \frac{a}{\sqrt{a^2 + b^2}} + 2k\pi \\ x &= -\arcsin\frac{c}{\sqrt{a^2+b^2}} - \arccos \frac{a}{\sqrt{a^2 + b^2}} + (2k+1)\pi \end{align*}
>$$
>
>- If you susbtitute back $\varphi = \arcsin \frac{b}{\sqrt{a^2 + b^2}}$, you obtain
>
>$$
>\begin{align*}x &= \arcsin\frac{c}{\sqrt{a^2+b^2}} - \arcsin \frac{b}{\sqrt{a^2 + b^2}} + 2k\pi \\ x &= -\arcsin\frac{c}{\sqrt{a^2+b^2}} - \arcsin \frac{b}{\sqrt{a^2 + b^2}} + (2k+1)\pi \end{align*}
>$$
>
>>[!EXAMPLE]-
>>
>>TODO
>>
>