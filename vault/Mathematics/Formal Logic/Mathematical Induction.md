---
title: Mathematical Induction
tags:
    - formal-logic
    - mathematics
---

# Mathematical Induction

**Mathematical induction** is a proof technique which allows us to prove that a certain statement $P$ holds for every [[TODO|integer]] in some [[Subsets|subset]] of $\mathbb{Z}$. It is most commonly used to prove statements about the [[TODO|natural numbers]], although it can be a powerful tool for much more.

## Proof by Induction

A proof by induction looks very much like a domino. Essentially, it boils down to two things:
- *Base case* - we find some integer $k$ for which the statement $P$ is true;
- *Inductive step* - we prove that for every integer $n$, if the statement $P$ is true for $n$, then $P$ is also true for $n+1$. The assumption that $P$ holds for $n$ is often called the **induction hypothesis**.

We can imagine the proof as an infinite chain of dominoes. The inductive step is like proving that if we can push any domino, it will fall in just the right way so as to push the domino to its right. Then, the base case is just the proof that there is indeed at least one piece of domino we can actually push - once we push this piece, all the pieces to its right will fall thanks to the inductive step.

>[!TIP] Tip: The Principle of Mathematical Induction
>
>The principle of mathematical induction can be summarized as follows:
>
>>If there exists some $k \in \mathbb{Z}$ for which $P(k)$ is true and if $P(n)$ implies $P(n + 1)$ for all $n \ge k$, then $P(n)$ is true for all $n \ge k$.
>

Essentially, if we manage to prove the inductive step and find a base case, then we would have proven that $P$ holds for all integers greater than or equal to $k$.

>[!EXAMPLE]- Example: Proof of the Sum of the First $n$ Natural Numbers
>
>We want to prove that the sum of the first $n$ natural numbers $1 + 2 + \cdots + n$ is equal to $\frac{n(n+1)}{2}$:
>
>$$
>1 + 2 + \cdots + n = \frac{n(n+1)}{2}
>$$
>
>**Proof:**
>
>Base case: We begin with the base case. Let's see if the formula holds for $n = 2$:
>
>$$
>1 + 2 = 3 = \frac{2 \cdot 3}{2}.
>$$
>
>Okay, we have found a base case. This means that we have found a piece of domino which we have enough force to push. Now, we need to show that all dominoes are placed at just the right distance so that if we push one piece, then all pieces to its right will fall, i.e. we need to prove our inductive step.
>
>Inductive step: We assume that the sum of the first $k \ge 2$ (greater than or equal to $2$ because we have already shown this is true for $2$ as $2$ was our base case) natural numbers $1 + 2 + \cdots + k$ is $\frac{k(k+1)}{2}$, i.e.
>
>$$
>1 + 2 + \cdots + k = \frac{k(k+1)}{2},
>$$
>
>and want to show that the sum of the first $k + 1$ natural numbers $1 + 2 + \cdots + k + (k + 1)$ is $\frac{(k+1)[(k+1) + 1]}{2}$, i.e.
>
>$$
>1 + 2 + \cdots + k + (k + 1) = \frac{(k+1)[(k+1) + 1]}{2} = \frac{(k+1)(k+2)}{2}.
>$$
>
>Alright, observe that $1 + 2 + \cdots + k + (k + 1)$ contains $1 + 2 + \cdots + k$ which is the sum of the first $k$ natural numbers. According to our assumption, $1 + 2 + \cdots + k = \frac{k(k+1)}{2}$. Therefore, we can rewrite $1 + 2 + \cdots + k + (k + 1)$ as
>
>$$
>1 + 2 + \cdots + k + (k + 1) = \frac{k(k+1)}{2} + (k+1) = \frac{k(k+1) + 2 (k+1)}{2} = \frac{(k+1)(k+2)}{2},
>$$
>
>which is exactly what we wanted to prove in the inductive step.
>
>Now we are done. The inductive step shows us that if the we can prove the formula for some specific $k$, then the formula will also be true for $k+1$. However, the proof never actually refers to a specific $k$, so if the formula is true for $k+1$, then it will also be true for $k+2$ and so on. In the base case, however, we found a specific $k$ for which the formula is indeed true, namely $k = 2$. Since the formula holds for $2$, the inductive step tells us it also holds for $3$. Since it holds for $3$, the inductive step tells it holds for $4$ and so on. Therefore, we have proven the formula for all $k \ge 2$.
>