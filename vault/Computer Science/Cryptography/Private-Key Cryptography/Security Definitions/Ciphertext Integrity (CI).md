# Ciphertext Integrity (CI)

Ciphertext integrity is a notion which closely resembles [[Message Authentication Codes (MACs|message authentication codes (MACs)]]/index.md) and is the cipher analogue of [[Message Authentication Codes (MACs|CMA-security]]/index.md#admonition-definition-cma-security-for-message-authentication-codes) for them.

>[!DEFINITION] Definition: Ciphertext Integrity (CI)
>
>The adversary Eve is given oracle access $\textit{Enc}_k$ and can query it with $q$ messages $m_1, m_2, ..., m_q$ in order to obtain their ciphertexts $c_1, c_2, ..., c_q$. Her goal is to produce a new valid ciphertext $c \notin \{c_1, c_2, ..., c_q\}$, i.e. a ciphertext such that $\textit{Dec}_k(c) \ne \textbf{error}$.
>
>A cipher $(\textit{Enc}_k, \textit{Dec}_k)$ provides *ciphertext integrity (CI)*, if for all keys $k \in \mathcal{K}$, the probability that Mallory achieves her goal is negligible, i.e.
>
>$$
>\Pr_{k \leftarrow_R \mathcal{K}}[\textit{Dec}_k(\textit{Eve}()) \ne \textbf{error}] \le \textit{negl(n)}
>$$
>
>>[!INTUITION]-
>>
>>Similarly to MACs, Eve has access to a bunch of messages and their ciphertexts and she strives to produce a new valid ciphertext which does not cause the decryption function to error. A cipher has CI if she cannot succeed with significant probability.
>>
>