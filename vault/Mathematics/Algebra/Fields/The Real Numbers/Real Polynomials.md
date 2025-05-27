---
title: Real Polynomials
tags:
  - real-polynomials
  - polynomials
  - real-numbers
  - abstract-algebra
  - algebra
  - mathematics
---

# Real Polynomials

>[!DEFINITION] Definition: Real Polynomial
>
>A **real polynomial** is a [[Polynomials|polynomial]] over the [[The Real Numbers|field of the real numbers]].
>

## Properties

>[!THEOREM]- The Binomial Theorem
>
>The expansion of the expression
>
>$$
>(x + y)^n,
>$$
>
>where $n \in \mathbb{N}$ is given by the [[Real Polynomials|polynomial]]
>
>$$
>(x + y)^n = C_n^0 x^n y^0 + C_n^1 x^{n-1}y^1 + C_n^2 x^{n - 2}y^{2} + \cdots + C_n^n x^0 y^n,
>$$
>
>where $C$ is the notation for the [[Combinations#Combinations without Repetition|total number of combinations without repetition]].
>
>>[!TIP]
>>
>>The expansion has $n+1$ terms. The $k$-th term ($k \in \{1, \dotsc, n + 1\}$) is $C_n^{k-1} x^{n-(k-1)} y^{k-1}$.
>>
>
>>[!PROOF]-
>>
>>TODO
>>
>

# Polynomial Division

>[!THEOREM] Theorem: Polynomial Division
>
>Let $A(x)$ and $B(x)$ be two [[Real Polynomials]] such that the [[Polynomials#Degree|degree]] of $A$ is greater than or equal to the degree of $B$.
>
>If $B(x)$ is [[Polynomials#Polynomials|nonzero]], then there exist unique polynomials $Q(x)$ and $R(x)$ such that
>
>$$
>A(x) = Q(x)B(x) + R(x),
>$$
>
>where 
>- $\deg(Q) = \deg(A) - \deg(B)$
>- $\deg(R) \lt \deg(B)$ or $R(x)$ is the zero polynomial.
>
>We call $A$ the **dividend**, $B$ the **divisor**, $Q$ the **quotient** and $R$ the **remainder**.
>
>>[!PROOF]-
>>
>>TODO
>>
>
>>[!DEFINITION] Definition: Divisibility
>>
>>If $R(x) = 0$, then we say that $A$ is **divisible** by $B$.
>>
>

## Properties

>[!THEOREM]- Polynomial Remainder Theorem (Little Bézout's Theorem)
>
>The [[Real Polynomials#Polynomial Division|remainder]] $R$ upon the [[Real Polynomials#Polynomial Division|division]] of a [[Real Polynomials|real polynomial]] $A(x)$ with a [[Real Polynomials|real polynomial]] $B(x) = x - p$ is the [[Polynomials#Evaluation|value]] of $A$ at $p$.
>
>$$
>R = A(p)
>$$
>
>>[!PROOF]-
>>
>>The polynomial division theorem tells us that
>>
>>$$
>>A(x) = (x-p)Q(x) + R(x)
>>$$
>>
>>Since the [[Polynomials|degree]] of $B(x)$ is $1$, the degree of $R$ must either be $1$, i.e. $R$ is a constant and contains no variables or $R$ must be [[Zero Polynomial|zero]]. We can therefore denote $R(x)$ as just $R$. For $x = p$ we obtain 
>>
>>$$
>>A(p) = (p-p)Q(p) + R = 0 + R = R
>>$$
>>
>

>[!ALGORITHM]- Algorithm: Horner's Method
>
>**Horner's method** is a way to easily [[Real Polynomials#Polynomial Division|divide]] a [[Real Polynomials|polynomial]] $A(x)$ by a [[Real Polynomials|polynomial]] $B(x)$ of [[Polynomials#Degree|degree]] one.
> 
>1. Write $B(x)$ as $B(x) = x - p$. Since $\deg(B) = 1$, the [[Real Polynomials#Polynomial Division|remainder]] $R$ is just a [[The Real Numbers|real number]] because $\deg (R) \lt \deg(B) \implies \deg (R) = 0$. This means that we have
>
>$$
>A(x) = (x-p)Q(x) + R
>$$
>
>2. To determine $Q(x)$ and $R$, construct the following table:
> 
>||$a_n$|$a_{n-1}$|$\cdots$|$a_1$|$a_0$|
>|:--:|:--:|:--:|:--:|:--:|:--:|
>|$p$|$q_{n-1} = a_n$|$q_{n-2} = pq_{n-1} + a_{n-1}$|$\cdots$|$q_0 = pq_1 + a_1$|$R = pq_0 + a_0$|
>
>- We calculate the table from left to right.
>- The first coefficient $q_{n-1}$ of $Q(x)$ is equal to the first coefficient of $A(x)$, i.e. $q_{n-1} = a_n$.
> - For all other coefficients of $Q(x)$ we have $q_i = pq_{i+1} + a_{i-1}$.
> - At the end of the calculation, the right-most cell will contain $R$.
>
>>[!EXAMPLE]-
>>
>>Let $A(x) = 2x^5+3x^3-11x^2+6$ and $B(x) = x-3$. Create the table.
>>
>>||$2$|$0$|$3$|$-11$|$0$|$6$|
>>|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
>>|$p = 3$|||||||
>>
>>Perform the algorithm step by step.
>> 
>>||$2$|$0$|$3$|$-11$|$0$|$6$|
>>|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
>>|$p = 3$|2||||||
>> 
>>||$2$|$0$|$3$|$-11$|$0$|$6$|
>>|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
>>|$p = 3$|2|6|||||
>>
>>||$2$|$0$|$3$|$-11$|$0$|$6$|
>>|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
>>
>

>[!ALGORITHM]- Algorithm: Change of Variables
>
>We are given a [[Real Polynomials|real polynomial]] $A(x)$ and want to transform it into another [[Real Polynomials|real polynomial]] $B(y)$ where $y = x - p$ for some $p \in \mathbb{R}$.
>
>1. [[Real Polynomials#Polynomial Division|Divide]] $A$ by $(x-p)$.
>
>$$
>A(x) = (x-p) Q_1(x) + R_0
>$$
>
>2. [[Real Polynomials#Polynomial Division|Divide]] $Q_1$ by $(x-p)$.
>
>$$
>Q_1(x) = (x-p) Q_2(x) + R_1
>$$
>
>3. Repeat step 2, dividing $Q_i$ by $(x-p)$ in order to obtain $Q_{i + 1}$ and $R_1$ until $Q_{i+1}$ is just a number.
>4. Finally,
>
>$$
>B(y) = R_0 + R_1y + R_2y^2 + R_3y^3 + \cdots
>$$
>
>>[!TIP]
>>
>>You can use [[Real Polynomials#Polynomial Division|Horner's method]] to speed up the process.
>>
>
>>[!EXAMPLE]-
>>
>>Let $A(x) = x^4 + 8x^3 + 24x^2 + 50x + 90$ and let $y = x + 2$. We can write $y$ as $y = x - p$, where $p = -2$.
>>
>>Apply [[Real Polynomials#Polynomial Division|Horner's method]]:
>>
>>||$1$|$8$|$24$|$50$|$90$|
>>|:--:|:--:|:--:|:--:|:--:|:--:|
>>|$-2$|$1$|$6$|$12$|$26$|$38 = R_0$|
>>|$-2$|$1$|$4$|$4$|$18 = R_1$||
>>|$-2$|$1$|$2$|$0 = R_2$|||
>>|$-2$|$1$|$0 = R_3$||||
>>|$-2$|$1 = R_4$|||||
>>
>>We have
>>
>>$$
>>\begin{align*}
>>B(y) &= R_0 + R_1 y + R_2 y^2 + R_3 y^3 + R_4 y^4 \\ 
>>&= 38 + 18y + y^4 \\
>>&= y^4 + 18y + 38 \\
>>&= (x+2)^4 + 18(x + 2) + 38
>>\end{align*}
>>$$
>>
>