---
title: Experiments
tags:
  - probability-theory
  - mathematics
---

# Experiments

>[!DEFINITION] Definition: Experiment
>
>An **experiment** in [[index|probability theory]] is a process with the following properties:
>- The process can occur multiple times;
>- All possible outcomes are known and unambiguously defined;
>- It is always one and only one of the outcomes which happens.
>

>[!DEFINITION] Definition: Sample Space
>
>The **sample space** of an [[Experiments#Experiments|experiment]] is the [[Sets|set]] of all possible outcomes of said experiment.
>
>>[!NOTATION]
>>
>>Sample spaces are often denoted by $\Omega$.
>>
>
>>[!EXAMPLE]- Example: Flipping a Coin
>>
>>Flipping a coin is a very simple experiment whose sample space $S$ contains only two possible outcomes - the coin falls heads-up or the coin falls tails-up. Hence, $S$ is just
>>
>>$$
>>S = \{\mathrm{heads}, \mathrm{tails}\}
>>$$
>>
>
>>[!EXAMPLE]- Example: Rolling a Die
>>
>>Another common experiment is the roll of a single six-sided die. There are six possible outcomes - the number on the die is 1, 2, 3, 4, 5 or 6. Hence, the sample space is
>>
>>$$
>>S = \{1, 2, 3, 4, 5, 6\}
>>$$
>>
>
>>[!EXAMPLE]- Example: Flipping Two Coins
>>
>>
>>
>

## Events

>[!DEFINITION] Definition: Event
>
>An **event** is any [[Sets|subset]] of the [[index#experiments|sample space]] of an [[index#experiments|experiment]].
>

Defined in this way, mathematical events allow us to closely model real-world conditions. However, we need a way to translate between the mathematical formalism of events and their physical reality. Hence, we say that an event has **occurred** if the outcome of the experiment is an element of the event.

>[!TIP] Tip: Union of Events
>
>The [[Operations with Collections|union]] of a [[Collections|collection]] of [[index#experiments|events]] is the event which occurs if and only if at least one of the events in the collection occurs.
>

>[!TIP] Tip: Intersection of Events
>
>The [[Operations with Collections|intersection]] of a [[Collections|collection]] of [[index#experiments|events]] is the event which occurs if and only if all of the events in the collection occur.
>

>[!TIP] Tip: Complement of an Event
>
>The [[Complement]] of an event $E$ is the event which occurs if and only if $E$ does *not* occur.
>

>[!DEFINITION] Definition: Mutual Exclusiveness
>
>A [[Collections|collection]] of [[Experiments#experiments|events]] are **mutually exclusive** if and only if every [[Set Operations|intersection]] between two of the [[Experiments#experiments|events]] is [[Sets|empty]].
>