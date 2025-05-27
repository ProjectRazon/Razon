---
title: Propositional Logic
tags:
    - two-valued-logic
    - formal-logic
    - mathematics
---

>[!DEFINITION] Definition: The Formal Language of Propositional Logic
>
>The **formal language of propositional logic** is the [[Formal Languages|formal language]] $\mathcal{L}_\text{PL}$ whose [[Countable Sets|countable]] [[Formal Languages|alphabet]] $\mathcal{A}_\text{PL}$ and [[Formal Languages|syntax]] $\mathcal{S}_\text{PL}$ are defined as follows.
>
>The alphabet $\mathcal{A}_\text{PL}$ contains:
>- the *parentheses* symbols "$($" and "$)$";
>- the *sentential connective* symbols "$\neg$", "$\land$", "$\lor$", "$\rightarrow$", "$\leftrightarrow$";
>- *atomic formula* symbols $A_1,A_2,\ldots$
>
>The syntax $\mathcal{S}_\text{PL}$ is comprised of the following rules:
>- Every atomic formula is a [[Formal Languages|well-formed formula]].
>- If $P$ is a wff, then $(P)$ is also a wff.
>- Any [[Propositional Connectives|negation]] of a wff is also a wff.
>- Any [[Propositional Connectives|conjunction]] of two wffs ia also a wff.
>- Any [[Propositional Connectives|disjunction]] of two wffs is also a wff.
>- Any [[Propositional Connectives|conditional]] of two wffs is also a wff.
>- Any [[Propositional Connectives|biconditional]] of two wffs is also a wff.
>- All other [[Formal Languages|expressions]] are *not* wffs.
>
>>[!INTUITION]-
>>
>>Each well-formed formula $P$ can be thought of as a translation of an English [[Proposition]] into the language $\mathcal{L}_\text{PL}$. Atomic formulas then represent the most basic and fundamental propositions we have chosen to examine.
>>
>
>>[!NOTE]
>>
>>The language $\mathcal{L}_\text{PL}$ is also known as the **zeroth order language**.
>>
>