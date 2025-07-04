# Chosen Plaintext Attack (CPA)

A *chosen plaintext attack (CPA)* models the scenario where an adversary can choose arbitrary plaintexts $m_1, m_2, ..., m_q$ and obtain their corresponding ciphertexts $c_1, c_2, ..., c_q$ that are all generated by encrypting the messages with the *same* secret key $k$. The adversary's goal is to then decrypt a ciphertext $c$ that was obtained by encrypting an unknown message $m$, also with the secret key $k$. 

>[!EXAMPLE]-
>
>In World War 2, the British would place mines at specific locations and when the Germans found them, they would encrypt their locations and send them to their superiors. The intercepted encrypted messages would later be used at Bletchley Park to break the encryption scheme of the Germans.
>

This scenario gives the adversary (partial) control over the messages and ciphertexts it has access to and one can imagine this as the attacker being able to influence to some extent the messages that are exchanged by the two authentic parties Alice and Bob.

>[!NOTE]
>
>It is imperative to remember that in the CPA model, all messages are encrypted using the same key.
>

# CPA-Security

So what does it mean for an encryption scheme to be secure under the chosen plaintext thread model?

>[!DEFINITION] Definition: CPA-Security
>
>The efficient adversary $\textit{Eve}$ is given oracle access to the encryption function $\textit{Enc}_k$ for some random secret key $k$ and queries it with $q$ messages $m_1, m_2, ..., m_q$ to obtain their respective ciphertexts $c_1, c_2, ..., c_q$. The cipher $(\textit{Enc}, \textit{Dec})$ is *CPA-secure* if for any two messages $\mu_0, \mu_1$ and ciphertext $c$ belonging to either $\mu_0$ or $\mu_1$, the adversary $\textit{Eve}$ still cannot guess with probability non-negligibly greater than $\frac{1}{2}$ whether $c$ is the encryption of $\mu_0$ or $\mu_1$, i.e.
>
>$$
>\Pr_{k \leftarrow \mathcal{K}, b \leftarrow \{0,1\}}[\textit{Eve}(\textit{Enc}_k(\mu_b)) = \mu_b] \le \frac{1}{2} + \textit{negl}(n)
>$$
>
>>[!INTUITION]-
>>
>>As previously mentioned, the adversary has oracle access to $\textit{Enc}_k$ and can thus obtain plaintext-ciphertext pairs $(m_1, c_1), (m_2,c_2), ..., (m_q, c_q)$. They then attempt to guess whether a given ciphertext $c$ belongs to a message $\mu_0$ or $\mu_1$ (the adversary of course also knows $\mu_0$ and $\mu_1$). The word "any" in the definition entails that Eve is even free to choose $\mu_0$ and $\mu_1$ herself. The cipher is considered CPA-secure if even with all this information, the adversary cannot guess with success marginally better than $\frac{1}{2}$ if the ciphertext corresponds to $\mu_0$ or $\mu_1$.
>>
>

At first glance, there appears to be something wrong with this definition. The adversary Eve is free to choose both $m_1, ..., m_q$ as well as $\mu_0$ and $\mu_1$. Therefore, it seems that this definition can be trivially broken by Eve simply by choosing $\mu_0$ to be the same as one of the previously queried messages $m_i$. When Eve is presented with a ciphertext $c$ at the end, she can just check if $c$ is the ciphertext she obtained when querying $m_i$ - since $\mu_0 = m_i$, she will know with 100% certainty whether the ciphertext $c$ is the encryption of $\mu_0$ or $\mu_1$. This leads to the following consequence for all CPA-secure ciphers.

>[!THEOREM]
>
>There is no CPA-secure cipher with a deterministic encryption function $\textit{Enc}$.
>

If $\textit{Enc}$ is probabilistic, i.e. it uses internal randomness, then the same message $m$ will produce different ciphertexts each time it is encrypted which kills the aforementioned breaking technique stone-dead. It might seem weird that the same message can produce different ciphertexts at first, but this is actually fairly easy to implement. The internal randomness used in each encryption can be encoded in the ciphertext is such a way that it can be recovered later if one knows the secret key $k$.

This property of CPA-security means that it is a *stronger* notion than [[Ciphertext-Only Attack (COA|semantic security]]/Semantic%20Security.md) - every CPA-secure cipher is also semantically secure, but the opposite is not necessarily true. In fact, CPA-security is nowadays the bare minimum definition which is expected to be satisfied by a cipher in order to be considered usable, since it provides security in the case of key reuse.

## Theoretical Implementation

As with many things in cryptography, [[Pseudorandom Function Generators (PRFGs|pseudorandom function generators (PRFGs)]].md) come to the rescue when trying to implement a CPA-secure cipher. 

>[!NOTE]
>
>This is just a proof-of-concept and the following cipher is *not* used in practice.
>

Suppose we have a pseudorandom function generator $\textit{PRFG}(\textit{seed}: \textbf{str}[n], \textit{input}: \textbf{str}[n]) \to \textbf{str}[l]$. The encryption function $\textit{Enc}$ is first going to generate a random string $r \leftarrow_R \{0,1\}^n$ of length $n$. It will then seed the PRFG with the key $k$ (which also has length $n$) and it will pass $r$ to it. The output of the PRFG will be XOR-ed with the message. Finally, $\textit{Enc}$ will prepend $r$ to this XOR-ed value:

$$\textit{Enc}_k(m) = r||(\textit{PRFG}(k, r) \oplus m)$$

```rust
fn Enc(key: str[n], message: str[l]) -> str[n + l] 
{
	let r = random_binary_string(length: n);
	return r + (xor(PRFG(key, r), message));
}
```

The decryption function $\textit{Dec}$ takes the ciphertext $c$ of length $n+l$ and parses it as two strings - a string $r \coloneqq c[0..n]$ of length $n$ and a string $z \coloneqq c[n..]$ of length $l$. It then seeds the PRFG with the key $k$ and passes it the string $r$. The output of the PRFG is then XOR-ed with $z$ to obtain the original message.

$$\textit{Dec}_k(c) = \textit{RPFG}(k, r) \oplus z$$

```rust
fn Dec((key: str[n], ciphertext: str[n + l])) -> str[l] 
{
	let r = ciphertext[0..n];
	let z = ciphertext[n..];
	return xor(PRFG(key, r), z);
}
```

Indeed, this is a [[index|valid encryption scheme]] - every ciphertext can only be mapped to one plaintext.

>[!PROOF]- Proof of Validity
>
>Given a key $k$, the encryption of a message $m$ is
>
>$$
>\textit{Enc}_k(m) = r||(\textit{PRFG}(k, r) \oplus m)
>$$
>
>Let's see the decryption of this output for the same key $k$:
>
>$$
>\textit{Dec}_k(r||(\textit{PRFG}(k, r) \oplus m)) = \textit{PRFG}(k, r) \oplus (\textit{PRFG}(k, r) \oplus m) = m
>$$
>
>Therefore, the validity condition is satisfied.
>

Moreover, this construction has a probabilistic encryption function and also turns out to be CPA-secure.

>[!PROOF]- Proof of CPA-Security
>
>Suppose we follow the CPA model and the adversary Eve obtains the ciphertexts $c_1, c_2, ..., c_q$ of the messages $m_1, m_2, ..., m_q$. For the $i$-th encryption a random string $r_i$ of length $n$ is generated and each message is also encrypted with the same key $k$ (as per the definition of CPA-security).
>
>Each of these strings is generated randomly, so the probability that the last string $r_q$ is the same as one of the previous random strings is $\frac{q}{2^n}$, which is negligible. 
>
>Suppose, towards contradiction that Eve could break the CPA-security of the cipher with probability $\frac{1}{2} + \xi$ for some non-negligible $\xi$. If instead of a PRFG the encryption used a truly random function $R$, then the probability that Eve could distinguish between $\mu_0$ and $\mu_1$ would be strictly $\frac{1}{2}$ because she would simply lack any additional information. However, the encryption *does* use a PRFG and if Eve can distinguish between an encryption of $\mu_0$ and an encryption of $\mu_1$ with probability non-negligibly greater than $\frac{1}{2}$, then that means that she can distinguish between the output of a PRFG and that of a truly random function with non-neglgible advantage over $\frac{1}{2}$, which is a contradiction.
>
