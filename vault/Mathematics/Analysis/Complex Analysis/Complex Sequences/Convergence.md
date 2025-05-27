---
title: Convergence of Complex Sequences
tags:
    - convergence
    - complex-sequences
    - complex-analysis
    - mathematics
---

# Convergence and Limits

>[!DEFINITION] Definition: Convergence of Complex Sequences
>
>Let $\{a_n\}$ be a [[Complex Sequences|complex sequence]].
>
>We say that $\{a_n\}$ **converges** to $L \in \mathbb{C}$ iff for each $\varepsilon \gt 0$, there exists some integer $N$ such that
>
>$$
>|a_n - L| \lt \varepsilon \qquad \forall n \ge N
>$$
>
>The number $L$, if it exists, is called the **limit** of $\{a_n\}$ as $n$ approaches infinity.
>
>>[!NOTATION]-
>>
>>The most common notation is
>>
>>$$
>>\lim_{n \to \infty} a_n = L
>>$$
>>
>>In text, one also writes "$a_n \to L$ as $n \to \infty$" or just "$a_n \to L$". Sometimes, one might also encounter $a_n \underset{n \to \infty}{\longrightarrow} L$ and $a_n \overset{n \to \infty}{\longrightarrow} L$.
>>
>
>>[!THEOREM] Theorem: Uniqueness of the Limit
>>
>>The [[Convergence|limit]] of a [[Complex Sequences|complex sequence]], if it exists, is unique - if $\{a_n\}$ [[Convergence|converges]] to both $L$ and $M$, then $L = M$.
>>
>>>[!PROOF]-
>>>
>>>Pick some arbitrary $\varepsilon \gt 0$.
>>>
>>>Since $\{a_n\} \to L$, by definition, there exists some integer $N_L$ such that
>>>
>>>$$
>>>|a_n - L| \lt \varepsilon \qquad \forall n \ge N_L.
>>>$$
>>>
>>>Similarly, since $\{a_n\} \to M$, there exists some integer $N_M$ such that
>>>
>>>$$
>>>|a_n - M| \lt \varepsilon \qquad \forall n \ge N_M.
>>>$$
>>>
>>>Now, let $N = \max\{N_L, N_M\}$. For all $n \ge N$, both of the aforementioned inequalities hold. Therefore, for all $n \ge N$, we have
>>>
>>>$$
>>>|L - M| = |L - a_n + a_n - M| \le |L - a_n| + |a_n - M| \lt \varepsilon + \varepsilon = 2\varepsilon.
>>>$$
>>>
>>>Therefore,
>>>
>>>$$
>>>\frac{1}{2}|L - M| \lt \varepsilon
>>>$$
>>>
>>>So far, the argument does not actually depend on the particular choice of $\varepsilon$ and is thus true for every $\varepsilon \gt 0$. This means that $\frac{1}{2}|L - M|$ is smaller that every positive real number. This is only possible if $\frac{1}{2}|L - M|$ is zero which is in turn only possible if $|L - M| = 0$. Therefore, $L = M$.
>>>
>>
>

>[!DEFINITION] Definition: Divergence of Complex Sequences
>
>If a [[Complex Sequences|complex sequence]]  does not [[Convergence|converge]] to any $L \in \mathbb{C}$, then we say that it **diverges**.
>

## Convergence Criteria

>[!THEOREM] Theorem: Component-Wise Convergence
>
>A [[Complex Sequences|complex sequence]] $\{a_n\}$ [[Convergence|converges]] to $L \in \mathbb{C}$ if and only if the [[Real Sequence|sequences]] of its real and imaginary part [[Convergence of Real Sequences|converge]] to the real and imaginary part of $L$, respectively.
>
>$$
>\lim_{n \to \infty} a_n = L \iff \lim_{n \to \infty} \operatorname{Re}(a_n) = \operatorname{Re}(L) \qquad \text{and} \qquad \lim_{n \to \infty} \operatorname{Im}(a_n) = \operatorname{Im}(L)
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Cauchy Sequences
>
>A [[Complex Sequences|complex sequence]] $\{a_n\}$ is [[Convergence|convergent]] if and only if, for each $\varepsilon \gt 0$, there exists some integer $N$ such that
>
>$$
>\lim_{n \to \infty} |a_n - a_m| = 0 \qquad \forall n,m \ge N 
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>
>>[!NOTE]
>>
>>Sequences for which the above holds, i.e. convergent sequences, are also known as **Cauchy sequences**.
>>
>

# Limit Properties

>[!THEOREM] Theorem: Boundedness of Convergent Sequences
>
>Every [[Convergence|convergent]] [[Complex Sequences|complex sequence]] is [[Boundedness|bounded]].
>
>>[!PROOF]-
>>
>>Suppose that $\{a_n\}$ [[Convergence|converges]] to some $L \in \mathbb{C}$. Then, by definition, for each $\varepsilon \gt 0$, there exists some integer $N$ such that
>>
>>$$
>>|a_n - L| \lt \varepsilon \qquad \forall n \ge N.
>>$$
>>
>>Choose $\varepsilon = 1$. The actual choice is irrelevant, it will just result in a different bound. Then,
>>
>>$$
>>|a_n - L| \lt 1 \qquad \forall n \ge N.
>>$$
>>
>>Let's look at the absolute value of $a_n$:
>>
>>$$
>>|a_n| = |a_n - L + L|
>>$$
>>
>>Using the triangle inequality, we get
>>
>>$$
>>|a_n| = |a_n - L + L| \le |a_n - L| + |L|.
>>$$
>>
>>For all $n \ge N$,
>>
>>$$
>>|a_n - L| + |L| \lt 1 + |L|
>>$$
>>
>>and so $|a_n| \lt 1 + |L|$ for all $n \ge N$. This means that the modulus of all sequence terms from the $N$-th one onwards is less than $1 + |L|$. Amongst the first $N-1$ terms of the sequence, choose the one whose modulus $M$ is greatest. The moduli of the first $N-1$ terms are thus all less than or equal to $M$. Essentially, we have
>>
>>- $|a_n| \le M$ for every $n \lt N$;
>>- $|a_n| \lt 1 + |L|$ for every $n \ge N$.
>>
>>Let $B = \max\{M, 1 + |L|\}$. Therefore, $|a_n| \le B$ for every integer $n$ and so $a_n$ is [[Boundedness|bounded]].
>>
>

>[!THEOREM] Theorem: Convergence to Zero
>
>A [[Complex Sequences|complex sequence]] $\{a_n\}$ [[Convergence|converges]] to zero if and only if $\{|a_n|\}$ converges to zero.
>
>$$
>\lim_{n \to \infty} a_n = 0 \iff \lim_{n \to \infty} |a_n| = 0
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM]
>
>Let $\{a_n\}$ and $\{b_n\}$ be [[Complex Sequences]].
>
>If $\{a_n\}$ [[Convergence|converges]] to zero and there exists some integer $N$ such that $|b_n| \le |a_n|$ for all $n \ge N$, then $\{b_n\}$ also [[Convergence|converges]] to zero.
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Limit Arithmetic
>
>If $\{a_n\}$ and $\{b_n\}$ are both [[Convergence|convergent]] [[Complex Sequences]], then
>
>$$
>\begin{align*}
>
>&\lim_{n \to \infty} (\alpha a_n + \beta b_n) = \alpha \lim_{n \to \infty} a_n + \beta \lim_{n \to \infty} b_n \qquad \forall \alpha, \beta \in \mathbb{C} \\
>
>\\
>
>&\lim_{n \to \infty} (a_n \cdot b_n) = \lim_{n \to \infty} a_n \cdot \lim_{n \to \infty} b_n \\
>
>\\
>
>&\lim_{n \to \infty} \frac{a_n}{b_n} = \frac{\displaystyle \lim_{n \to \infty} a_n}{\displaystyle \lim_{n \to \infty} b_n}, \qquad \lim_{n \to \infty} b_n \ne 0 \\
>
>\\
>
>&\lim_{n \to \infty} \overline{a_n} = \overline{\lim_{n \to \infty} a_n} \\
>
>\\
>
>&\lim_{n \to \infty} |a_n| = \left|\lim_{n \to \infty} a_n\right|
>
>\end{align*}
>$$
>
>>[!PROOF]-
>>
>>Let $A = \displaystyle \lim_{n \to \infty} a_n$ and $B = \displaystyle \lim_{n \to \infty} b_n$.
>>
>>**Proof of (1):**
>>
>>We have to prove that for each $\varepsilon \gt 0$, there exists some integer $N$ such that
>>
>>$$
>>|\alpha a_n + \beta b_n - (\alpha A + \beta B)| \lt \varepsilon \qquad \forall n \ge N.
>>$$
>>
>>The case of $\alpha = \beta = 0$ is trivial, since then $|\alpha a_n + \beta b_n - (\alpha A + \beta B)|$ is always zero and is thus smaller than all $\varepsilon \gt 0$. As for the existence of $N$ - not only does such an integer $N$ exist, but there are actually infinitely many such integers, since the inequality holds irrespective of $N$.
>>
>>If $\alpha$ and $\beta$ are not zero, choose some arbitrary $\varepsilon' \gt 0$. Since $a_n \to A$ and $b_n \to B$, there exist integers $N_A$ and $N_B$ such that
>>
>>$$
>>\begin{align*}
>>
>>|a_n - A| \lt \varepsilon' \qquad \forall n \ge N_A \\
>>
>>|b_n - B| \lt \varepsilon' \qquad \forall n \ge N_B
>>
>>\end{align*}
>>$$
>>
>>Let $N = \max \{N_A, N_B\}$. Then both inequalities hold for every $n \ge N$. Now, we look at
>>
>>$$
>>|\alpha a_n + \beta b_n - (\alpha A + \beta B)| = |\alpha (a_n - A) + \beta (b_n - B)|.
>>$$
>>
>>By the triangle inequality, we obtain
>>
>>$$
>>|\alpha (a_n - A) + \beta (b_n - B)| \le |\alpha (a_n - A)| + |\beta (b_n - B)| = |\alpha| |a_n - A| + |\beta| |b_n - B|.
>>$$
>>
>>For every $n \ge N$, we know that $|a_n - A| \lt \varepsilon'$ and $|b_n - B| \lt \varepsilon'$ and so we get
>>
>>$$
>>|\alpha| |a_n - A| + |\beta| |b_n - B| \lt |\alpha| \varepsilon' + |\beta| \varepsilon'.
>>$$
>>
>>Since $|\alpha (a_n - A) + \beta (b_n - B)| \le |\alpha| |a_n - A| + |\beta| |b_n - B|$ and $|\alpha a_n + \beta b_n - (\alpha A + \beta B)| = |\alpha (a_n - A) + \beta (b_n - B)|$, we get
>>
>>$$
>>|\alpha a_n + \beta b_n - (\alpha A + \beta B)| \lt |\alpha| \varepsilon' + |\beta| \varepsilon' \qquad \forall n \ge N
>>$$
>>
>>So far, the argument does not depend on the choice of $\varepsilon'$ which means that it must be true for all $\varepsilon' \gt 0$. Thus, we have proven that for each $\varepsilon = |\alpha| \varepsilon' + |\beta| \varepsilon'$, there exists some integer, namely $N$, such that
>>
>>$$
>>|\alpha a_n + \beta b_n - (\alpha A + \beta B)| \lt \varepsilon \qquad \forall n \ge N,
>>$$
>>
>>which is what we set out to prove.
>>
>>**Proof of (2):**
>>
>>We have to prove that for each $\varepsilon \gt 0$, there exists some integer $N$ such that
>>
>>$$
>>|a_n \cdot b_n - A \cdot B| \lt \varepsilon \qquad \forall n \ge N.
>>$$
>>
>>Choose some arbitrary $\varepsilon' \gt 0$. Since $a_n \to A$ and $b_n \to B$, there exist integers $N_A$ and $N_B$ such that
>>
>>$$
>>\begin{align*}
>>
>>&|a_n - A| \lt \varepsilon' \qquad \forall n \ge N_A \\
>>
>>&|b_n - B| \lt \varepsilon' \qquad \forall n \ge N_B.
>>
>>\end{align*}
>>$$
>>
>>Let $N = \max \{N_A, N_B\}$. Then both inequalities hold for all $n \ge N$. We transform the expression $|a_n \cdot b_n - A \cdot B|$ a bit:
>>
>>$$
>>|a_n \cdot b_n - A \cdot B| = |a_n \cdot b_n - A \cdot b_n + A \cdot b_n - A \cdot B|.
>>$$
>>
>>Using the triangle inequality, we obtain
>>
>>$$
>>|a_n \cdot b_n - A \cdot b_n + A \cdot b_n - A \cdot B| \le |a_n \cdot b_n - A \cdot b_n| + |A \cdot b_n - A \cdot B|,
>>$$
>>
>>which is equivalent to
>>
>>$$
>>|a_n \cdot b_n - A \cdot B| \le |b_n| \cdot |a_n - A| + |A| \cdot |b_n - B|.
>>$$
>>
>>For all $n \ge N$,
>>
>>$$
>>|b_n| \cdot |a_n - A| + |A| \cdot |b_n - B| \lt |b_n| \cdot \varepsilon' + |A| \cdot \varepsilon',
>>$$
>>
>>which in turn means that, for all $n \ge N$,
>>
>>$$
>>|a_n \cdot b_n - A \cdot B| \lt |b_n| \cdot \varepsilon' + |A| \cdot \varepsilon'
>>$$
>>
>>Recall that every convergent sequence is bounded. This means that there exists some $B \gt 0$ and some integer $\mathcal{N}$ such that $|b_n| \le B$ for all $n \ge \mathcal{N}$. Therefore,
>>
>>$$
>>|a_n \cdot b_n - A \cdot B| \lt B \cdot \varepsilon' + |A| \cdot \varepsilon' \qquad \forall n \ge \mathcal{N}.
>>$$
>>
>>Set $\varepsilon = B \cdot \varepsilon' + |A| \cdot \varepsilon'$. Therefore,
>>
>>$$
>>|a_n \cdot b_n - A \cdot B| \lt \varepsilon \qquad \forall n \ge \mathcal{N}.
>>$$
>>
>>It is obvious that $\varepsilon$ can be any positive real number. Moreover, since the argument so far does not depend on any particular choice of $\varepsilon$, we know the argument holds for all $\varepsilon \gt 0$. We have thus proven that for each $\varepsilon \gt 0$, there exists some integer, namely $\mathcal{N}$, such that
>>
>>$$
>>|a_n \cdot b_n - A \cdot B| \lt \varepsilon \qquad \forall n \ge \mathcal{N},
>>$$
>>
>>which is what we set out to show.
>>
>>**Proof of (3):**
>>
>>TODO
>>
>>**Proof of (4):**
>>
>>TODO
>>
>>**Proof of (5):**
>>
>>TODO
>>
>