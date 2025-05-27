---
title: Probability Spaces
tags:
    - probability-theory
    - mathematics
---

# Probability

At its core, the probability of an [[Experiments|event]] is just a [[The Real Numbers|real number]] between $0$ and $1$, inclusively, which measures the likelihood of that event occurring.

>[!DEFINITION] Definition: Probability Space
>
>A **probability space** $(\Omega, P)$ is a [[Experiments|sample space]] $\Omega$ equipped with a [[Functions of the Real Numbers|real-valued]] **probability function** $P: \mathcal{P}(\Omega) \to [0;1]$ defined on the [[Power Set]] of $\Omega$ with the following properties:
>- $P(\varnothing) = 0$ and $P(\Omega) = 1$;
>- For every [[Countable Sets|countable]] [[Collections|collection]] $\mathcal{E} = \{E_1, E_2, \dotsc \}$ of [[Experiments|mutually exclusive]] [[Experiments|events]], we have
>
>$$
>P\left(\bigcup \mathcal{E} \right) = \sum_{E \in \mathcal{E}} P(E)
>$$
>
>>[!NOTATION]
>>
>>Some people may denote the probability space as $(\Omega, \mathcal{P}(\Omega), P)$.
>>
>
>>[!DEFINITION] Definition: (Absolute) Probability
>>
>>Given an [[Experiments|event]] $E \in \mathcal{P}(\Omega)$, we call $P(E)$ the **(absolute) probability** of $E$.
>>
>

## Properties

>[!THEOREM]- Theorem: Probability of Unions
>
>If $A$ and $B$ are arbitrary [[Experiments|events]] in a [[Probability Spaces|probability space]], then
>
>$$
>P(A \cup B) = P(A) + P(B) - P(A \cap B)
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>


# Conditional Probability

>[!DEFINITION] Definition: Conditional Probability
>
>Let $A$ and $B$ be two [[Experiments|events]] in a [[Probability Spaces|probability space]].
>
>The **probability of** $A$ **given** $B$ is defined as
>
>$$
>P(A\mid B) \overset{\text{def}}{=} \frac{P(A \cap B)}{P(B)}
>$$
>
>>[!NOTE] Note: Prior and Posterior Probabilities
>>
>>In the context of conditional probabilities, the number $P(A)$ is often called the **prior probability** and $P(A\mid B)$ the **posterior probability** of $A$.
>>
>

Conditional probability is a measure of the likelihood that $A$ will occur if we know that $B$ has occurred. 

>[!DEFINITION] Definition: Independent Events
>
>Let $A$ and $B$ be two [[Experiments|events]] in a [[Probability Spaces|probability space]].
>
>We say that $A$ is **independent** of $B$ if the [[Probability Spaces|conditional probability]] of $A$ given $B$ is the same as the [[Probability Spaces|absolute probability]] of $A$.
>
>$$
>P(A \mid B) = P(A)
>$$
>
>>[!THEOREM] Theorem: Mutual Independence
>>
>>If $A$ is [[Probability Spaces|independent]] of $B$, then $B$ is also [[Probability Spaces|independent]] of $A$.
>>
>>>[!PROOF]-
>>>
>>>This follows directly from [[Probability Spaces#Properties|Bayes' rule]]
>>>
>>
>

## Properties

>[!THEOREM]- Theorem: Bayes' Rule
>
>If $A$ and $B$ are two [[Experiments|events]] in a [[Probability Spaces|probability space]], then their [[Probability Spaces#Conditional Probability|conditional probabilities]] are related as follows:
>
>$$
>P(A \mid B) = \frac{P(A)}{P(B)} P(B \mid A)
>$$
>
>>[!NOTE]
>>
>>Bayes' rules essentially allows us to switch the events around.
>>
>
>>[!PROOF]-
>>
>>By definition,
>>
>>$$
>>P(A \mid B) = \frac{P(A \cap B)}{P(B)}
>>$$
>>
>>and so
>> 
>>$$
>>P(A \cap B) = P(A \mid B) P(B).
>>$$
>>
>>Similarly,
>>
>>$$
>>P(B \mid A) = \frac{P(B \cap A)}{P(A)} = \frac{P(A \cap B)}{P(A)}
>>$$
>>
>>and so
>>
>>$$
>>P(A \cap B) = P(B \mid A) P(A).
>>$$
>>
>>By combining the two equations, we obtain the result from the theorem. 
>>
>>$$
>>P(A \mid B) P(B) = P(B \mid A) P(A)
>>$$
>>
>>$$
>>P(A \mid B) = \frac{P(B \mid A) P(A)}{P(B)}
>>$$
>>
>

>[!THEOREM]- Theorem: Law of Total Probability
>
>Let $(\Omega, P)$ be a [[Probability Spaces|probability space]], let $\{B_1, \dotsc, B_n\}$ be a [[Collections|collection]] of [[Experiments|events]] and let $A$ be some other [[Experiments|event]].
>
>If $\{B_1, \dotsc, B_n\}$ are [[Experiments|mutually exclusive]] and their [[Operations with Collections|union]] is $\Omega$, then the [[Probability Spaces|probability]] of $A$ is the sum of its [[Probability Spaces|conditional probability]] given each $B_i$ multiplied by the [[Probability Spaces|probability]] of $B_i$:
>
>$$
>P(A) = \sum_{i = 1}^n P(A \mid B_i) P(B_i)
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>