# Introduction

The most naive mode of operation is called *Electronic Cookboook (ECB)* mode. It divides the message into blocks $\mu_1, \mu_2, ..., \mu_q$ with length $l_b$, according to whatever block cipher is used, and then separately encrypts each block with the block cipher's encryption algorithm and the same key $k$. The final ciphertext is produced by concatenating the ciphertexts of each block.

![[res/ECB Encryption.svg]]

Decryption is just the opposite - it divides the ciphertext into blocks $\sigma_1, \sigma_2, ..., \sigma_q$ and decrypts each one separately. The original message is recovered by concatenating the decryptions of every ciphertext block.

![[res/ECB Decryption.svg]]

# Security of ECB Mode

The ECB Mode is very simple so it comes as no surprise that it is not very secure. 

>[!WARNING]
>
>The ECB mode should *never* be used.
>

In particular, it is *not* [[Chosen Plaintext Attack (CPA|CPA-secure]].md), since it is entirely deterministic. Moreover, it is not even [[Ciphertext-Only Attack (COA|semantically secure]]/Semantic%20Security.md) because if a block is repeated in the plaintext, then the corresponding ciphertext block will also be repeated in the ciphertext which reveals a lot of information about the underlying message. 
