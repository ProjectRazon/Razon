---
title: Topological Spaces
tags:
  - topology
  - mathematics
---

# Topologies and Topological Spaces

>[!DEFINITION] Definition: Topology
>
>A **topology** on a [[Sets|non-empty]] [[Sets|set]] $X$ is a [[Collections|collection]] $\tau$ of [[Sets|subsets]] of $X$ which has the following properties:
>
>- The [[Sets|empty set]] $\varnothing$ and $X$ are in $\tau$.
>- The [[Operations with Collections|union]] of any subset of $\tau$ is in $\tau$.
>- The [[Set Operations|intersection]] of any two elements of $\tau$ is in $\tau$.
>
>>[!INTUITION]-
>>
>>A topology $\tau$ on a [[Sets|set]] $X$ can be interpreted as a definition of "closeness" between elements of $X$ without using any notion of distance. Moreover, a topology provides a way for us to define what is "inside" a set, what is "outside" a set and what separates the inside of a set from its outside.
>> 
>
>>[!EXAMPLE]-
>>
>>Consider the sets $X = \{1,2,3,4,5,6\}$ and $\tau = \{\varnothing, X, \{1\}, \{3,4\}, \{1,3,4\}, \{2,3,4,5,6\}\}$. The set $\tau$ is a topology on $X$, since it satisfies the requirements in the definition.
>>
>

>[!DEFINITION] Definition: Topological Space
>
>A **topological space** $(S,\tau)$ is a [[Sets|non-empty]] [[Sets|set]] $S$ equipped with a [[Topological Spaces|topology]] $\tau$ on it.
>
>>[!NOTE] Note: Points
>>
>>It is common to refer to the elements $s \in S$ of a topological space as **points**.
>>
>


# Open Sets

>[!DEFINITION] Definition: Open Subset
>
>Let $(X, \tau)$ be a [[Topological Spaces|topological space]].
>
>A [[Sets|subset]] of $X$ is **open** iff it is an element of $\tau$.
>

## Openness Criteria

>[!THEOREM]-
>
>Let $(X, \tau)$ be a [[Topological Spaces|topological space]].
>
>A [[Sets|subset]] $U \subseteq X$ is [[Open Sets|open]] if and only if each $x \in U$ has [[Topological Spaces|neighbourhood]]d) $N(x)$ such that $N(x) \subseteq U$.
>
>>[!PROOF]-
>>
>>If $U$ is [[Open Sets|open]], then $U$ is, by definition, [[Topological Spaces|neighbourhood]]d) of every $x \in U$.
>>
>>If there exists [[Topological Spaces|neighbourhood]]d) $N(x)$ of each $x$ such that $N(x) \subseteq U$, then inside each neighbourhood $N(x)$ there exists, by definition, an open set $O(x) \subseteq N(x)$ which contains $x$. Since $N(x) \subseteq U$, we have $O(x) \subseteq N(x) \subseteq U$. This means that we can construct $U$ as the [[Operations with Collections|union]] of these open sets $O(x)$.
>>
>>$$
>>U = \bigcup_{x \in U} O(x)
>>$$
>>
>>Since this is a union of open sets, i.e. it is a union of a subset of the [[Topological Spaces|topology]] $\tau$, we have that $U \in \tau$. 
>>
>

>[!THEOREM]- Theorem
>
>Let $(X, \tau)$ be a [[Topological Spaces|topological space]].
>
>A [[Sets|subset]] $U \subseteq X$ is [[Open Sets|open]] if and only if for each $x \in U$ there exists an open set $V$ such that $V \subseteq U$ and $x \in V$.
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM]- Theorem
>
>Let $(X, \tau)$ be a [[Topological Spaces|topological space]].
>
>A [[Sets|subset]] $S \subseteq X$ is [[Open Sets|open]] if and only if it is equal to its own [[Interior, Boundary and Exterior|interior]].
>
>$$
>S = \operatorname{int} S
>$$
>
>>[!PROOF]-
>>
>>We need to prove two things:
>>- (I) If $S$ is [[Open Sets|open]], then $S = \operatorname{int} S$.
>>- (II) If $S = \operatorname{int} S$, then $S$ is [[Open Sets|open]].
>>
>>**Proof of (I):**
>>
>>Suppose $S$ is [[Open Sets|open]]. Recall the definition of the [[Interior, Boundary and Exterior|interior]] $\operatorname{int} S$:
>>
>>$$
>>\operatorname{int} S \overset{\text{def}}{=} \bigcup \{O \subseteq S \mid O \text{ is open}\}
>>$$
>>
>>Since $S\subseteq S$ and $S$ is [[Open Sets|open]], we know that $S \in \{O \subseteq S \mid O \text{ is open}\}$ and thus $S \subseteq \operatorname{int} S$. However, the [[Interior, Boundary and Exterior|interior]] is a [[Sets|subset]] of $S$. Since $S \subseteq \operatorname{int} S$ and $\operatorname{int} S \subseteq S$, we know deduce that $S = \operatorname{int} S$.
>>
>>**Proof of (II):**
>>
>>Suppose that $S = \operatorname{int} S$. Since the [[Interior, Boundary and Exterior|interior]] $\operatorname{int} S$ is a [[Operations with Collections|union]] of [[Open Sets]], it is itself [[Open Sets|open]]. Therefore, $S$ is [[Open Sets|open]].
>>
>

## Properties of Open Sets

>[!THEOREM]- Theorem: Union of Open Sets
>
>Let $(S, \tau)$ be a [[Topological Spaces|topological space]].
>
>The [[Operations with Collections|union]] of any [[Collections|collection]] of [[Open Sets|open subsets]] is also open.
>
>>[!PROOF]-
>>
>>This follows directly from the definition of a [[Topological Spaces|topology]].
>>
>

>[!THEOREM]- Theorem: Intersection of Open Sets
>
>Let $(S, \tau)$ be a [[Topological Spaces|topological space]].
>
>The [[Operations with Collections|intersection]] of any finite [[Collections|collection]] of [[Open Sets]] is also open.
>
>>[!PROOF]-
>>
>>We consider $n \ge 2$ arbitrary [[Open Sets|open subsets]] $U_1,\cdots, U_n$.
>>
>>For $n = 2$, the definition of the [[Topological Spaces|topology]] $\tau$ tells us that $U_1 \cap U_2 \in \tau$.
>>
>>Now suppose $U' = U_1 \cap \cdots \cap U_{n-1} \in \tau$. We have
>>
>>$$
>>\begin{align*}U_1 \cap \cdots \cap U_n &= (U_1 \cap \cdots \cap U_{n-1}) \cap U_n \\ U_1 \cap \cdots \cap U_n &= U' \cap U_n\end{align*}
>>$$
>>
>>Since $U_1 \cap \cdots \cap U_n$ is the intersection of two elements of $\tau$, it must itself be an element of $\tau$, Q.E.D.
>>
>
>^intersection-of-open-sets
>

# Closed Sets

>[!DEFINITION] Definition: Closed Set
>
>Let $(S, \tau)$ be a [[Topological Spaces|topological space]].
>
>A [[Sets|subset]] $U$ of $S$ is **closed** if its [[Complement]] $S \setminus U$ is an [[Topological Spaces|open set]].
>
>>[!THEOREM]
>>
>>Let $(S, \tau)$ be a [[Topological Spaces|topological space]].
>>
>>A [[Sets|subset]] $C \subseteq S$ is [[Closed Sets|closed]] if and only if for each $x$ in its [[Complement]] $S \setminus C$ there exists [[Topological Spaces|neighbourhood]]d) $N$ of $x$ such that $N \subseteq S \setminus C$.
>>
>>>[!PROOF]-
>>>
>>>TODO
>>>
>>
>

## Closedness Criteria

>[!THEOREM]-
>
>Let $(X, \tau)$ be a [[Topological Spaces|topological space]].
>
>A [[Subsets|subset]] $S \subseteq X$ is [[Topological Spaces|closed]] if and only if it is equal to its own [[Closure]].
>
>>[!PROOF]-
>>
>>We have to prove two things:
>>- (I) If $S$ is [[Closed Sets|closed]], then $S = \overline{S}$.
>>- (II) If $S = \overline{S}$, then $S$ is [[Topological Spaces|closed]].
>>
>>**Proof of (I):**
>>
>>TODO
>>
>>**Proof of (II):**
>>
>>TODO
>>
>

>[!THEOREM]- Theorem: Limit Points of Closed Subsets
>
>Let $(X, \tau)$ be a [[Topological Spaces|topological space]].
>
>A [[Subsets|subset]] $S \subseteq X$ is [[Closed Sets|closed]] if and only if it contains all of its [[Accumulation Point|limit points]].
>
>>[!PROOF]-
>>
>>We need to prove two things separately:
>>- (I) If $S$ is [[Closed Sets|closed]], then every [[Accumulation Point|limit point]] of $S$ lies in $S$.
>>- (II) If $S$ contains all of its [[Accumulation Point|limit points]], then it is [[Closed Sets|closed]].
>>
>>**Proof of (I):**
>>
>>We prove this by contradiction. Suppose that $S$ is [[Closed Sets|closed]] and there exists a [[Accumulation Point|limit point]] $p$ of $S$ which lies outside of $S$, i.e. $p \in X \setminus S$. We know that $X \setminus S$ is [[Topological Spaces|open]] because it is the [[Complement]] of a [[Closed Sets|closed set]]. However, since $p$ is a [[Accumulation Point|limit point]] of $S$, every [[Topological Spaces|open set]] which contains $p$ must also contain an element of $S$. This implies that $X \setminus S$ contains an element of $S$ which is a contradiction.
>>
>>**Proof of (II):**
>>
>>Suppose that $S$ contains all of its [[Accumulation Point|limit points]]. This means that there are no points $p \in X\setminus S$ such that every [[Topological Spaces|open set]] $U$ which contains $p$ also contains another element of $S$. Alternatively, this means that each $p \in X \setminus S$ is contained in some [[Topological Spaces|open set]] $U_p$ such that $U_p \cap S = \varnothing$, i.e. $U_p \subseteq X \setminus S$. Therefore, the [[Operations with Collections|union]] $\bigcup_{p \in X \setminus S} U_p$ is a [[Sets|subset]] of $X \setminus S$ and, since it contains every $p \in X \setminus S$, it means that $\bigcup_{p \in X \setminus S} U_p = X \setminus$. Since $X \setminus S$ is a [[Operations with Collections|union]] of [[Topological Spaces|open sets]], it is itself [[Topological Spaces|open]] and so $S$ is [[Closed Sets|closed]].
>>
>

## Properties

>[!THEOREM] Theorem: Intersection of Closed Sets
>
>Let $(S, \tau)$ be a [[Topological Spaces|topological space]].
>
>The [[Operations with Collections|intersection]] of any [[Collections|collection]] of [[Topological Spaces|closed subsets]] is also closed.
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Union of Closed Sets
>
>Let $(S, \tau)$ be a [[Topological Spaces|topological space]].
>
>The [[Operations with Collections|union]] of any finite [[Collections|collection]] of [[Topological Spaces|closed subsets]] is also closed.
>
>>[!PROOF]-
>>
>>Let $S_1,\cdots,S_n$ be closed sets. We need to show that $\bigcup \{S_1,\cdots, S_n\} = S_1 \cup \cdots \cup S_n$ is closed. According to the definition of a closed set, this means we must show that $S \setminus (S_1 \cup \cdots \cup S_n)$ is [[Topological Spaces|open]].
>>
>>By the [[Set Operations|distributive law]]
>>
>>$$
>>S \setminus (S_1 \cup \cdots \cup S_n) = (S\setminus S_1) \cap \cdots \cap (S \setminus S_n)
>>$$
>>
>>The sets $S_1,\cdots,S_n$ are closed and by definition their [[Complement|complements]] $S\setminus S_1,\cdots, S \setminus S_n$ are open. The right-hand side is thus an intersection of open sets and is, therefore, open itself. This means that the complement $S \setminus S_1 \cup \cdots \cup S_n$ is open and so $S_1 \cup \cdots \cup S_n$ is closed.
>>
>

# Clopen Sets

It is important to note that "openness" and "closedness" are neither mutually exclusive nor complete - [[Subsets]] in a [[Topological Spaces]] can be both [[Topological Spaces#Open Sets.md|open]] and [[Topological Spaces#Closed Sets.md|closed]] or they can also be neither.

>[!DEFINITION] Definition: Clopen Set
>
>Let $(X, \tau)$ be a [[Topological Spaces|topological space]].
>
>A [[Sets|subset]] of $X$ is a **clopen** iff it is both [[Topological Spaces|open]] and [[Topological Spaces|closed]].
>

# Neighborhoods

>[!DEFINITION] Definition: Neighborhood of a Point
>
>Let $(X,\tau)$ be a [[Topological Spaces|topological space]] and let $x \in X$.
>
>A [[Sets|subset]] $N \subseteq X$ is a **neighbourhood** of $x$ iff there exists an [[Topological Spaces|open set]] $U$ such that $U \subseteq N$ and $x \in U$.
>
>>[!NOTATION]-
>>
>>$$
>>N(x) \qquad N_x
>>$$
>>
>
>^neighbourhood-of-a-point
>

>[!DEFINITION] Definition: Neighbourhood of a Set
>
>Let $(X,\tau)$ be a [[Topological Spaces|topological space]] and let $S$ be a [[Sets|subset]] of $X$.
>
>A [[Sets|subset]] $N \subseteq X$ is a **neighbourhood** of $S$ iff there exists an [[Topological Spaces|open set]] $U$ such that
>
>$$
>S \subseteq U \subseteq N
>$$
>
>>[!NOTATION]-
>>
>>$$
>>N_S \qquad N(S)
>>$$
>>
>