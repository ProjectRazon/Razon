---
title: Formal Languages
tags:
  - formal-logic
  - mathematics
---

# Symbols and Alphabets

>[!DEFINITION] Definition: Alphabet
>
>An **alphabet** is a [[Sets|set]] whose elements we call **symbols**.
>

## Expressions

>[!DEFINITION] Definition: Expression
>
>Let $\mathcal{A}$ be an [[Formal Languages#symbols and alphabets|alphabet]].
>
>An **expression** over $\mathcal{A}$ is a [[Tuples|tuple]] of [[Formal Languages#symbols and alphabets|symbols]] from $\mathcal{A}$.
>
>>[!NOTE] Note: Strings
>>
>>Expressions are also called **strings**.
>>
>
>>[!NOTATION]-
>>
>>Expressions are usually written by listing their symbols directly, instead of placing them between parentheses in a comma-separated list, as is usually the case with tuples. For example, the expression $(a, 2, s, s, 1,w)$ is written as $a2ss1w$.
>>
>>The [[Sets|set]] of all expressions which can be formed using the alphabet $\mathcal{A}$ is denoted by $\mathcal{A}^\ast$.
>>

>[!DEFINITION] Definition: Concatenation
>
>Let $\alpha$ and $\beta$ be two [[Formal Languages#expressions|expressions]] formed from the same [[Formal Languages#symbols and alphabets|alphabet]].
>
>The **concatenation** of $\beta$ to $\alpha$ is the expression obtained by listing the symbols of $\alpha$ first and then the symbols of $\beta$.
>
>>[!NOTATION]-
>>
>>$$
>>\alpha \beta
>>$$
>>
>

# Syntax

>[!DEFINITION] Definition: Well-Formed Formula
>
>Let $\mathcal{L} = (\mathcal{A}, \mathcal{S})$ be a [[Formal Languages#formal languages|formal language]].
>
>A **well-formed formula** in $\mathcal{L}$ is an [[Formal Languages#expressions|expression]] in the [[Formal Languages#symbols and alphabets|alphabet]] $\mathcal{A}$ which is considered valid under the [[Formal Languages#syntax|syntax]] $\mathcal{S}$.
>
>>[!NOTE]
>>
>>The term "well-formed formula" is often abbreviated to "wff".
>>
>
>>[!INTUITION]-
>>
>>Well-formed formulas can be thought of as expressions which are meaningful in the context of a given language. For example, the sentence "Yesterday, Harry went to the bar" is meaningful and can be considered a wff in English. In constrast, the sentence "Fall on the in chair sock" does not carry any meaning and is, therefore, *not* a wff in English.
>>
>

>[!DEFINITION] Definition: Syntax
>
>Let $\mathcal{A}$ be an [[Formal Languages#symbols and alphabets|alphabet]].
>
>A **syntax** is a [[Sets|set]] of rules that specify which [[Formal Languages#expressions|expressions]] in $\mathcal{A}$ are considered [[Formal Languages#syntax|well-formed formulas]] and how to generate new wffs from existing ones.
>

# Formal Languages

>[!DEFINITION] Definition: Formal Language
>
>A **formal language** is an [[Ordered Pairs|ordered pair]] $(\mathcal{A}, \mathcal{S})$ consisting of an [[Formal Languages#symbols and alphabets|alphabet]] $\mathcal{A}$ and a [[Formal Languages#syntax|syntax]] $\mathcal{S}$.
>
>>[!NOTATION]-
>>
>>Formal languages are often denoted by $\mathcal{L}$ with or without subscripts.
>>
>