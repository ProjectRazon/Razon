# The Shift Cipher

One of the oldest known ciphers is known as Caesar's cipher. Julius Caesar encrypted his messages by shifting every letter of the alphabet three spaces forward and looping back when the end of the alphabet is reached. Consequently, `A` would be mapped to `D` and `Z` would be mapped to `C`.

An immediate problem with this cipher is the lack of a key - the shift amount is always the same. A natural extension of the cipher would then be to let the shift amount vary, turning it into a key whose possible values are the numbers between 0 and 25. Therefore, the key space is  $K \equiv \{ 0, ..., 25 \}$.

An encryption algorithm $Enc_k$ would take a plaintext $m$, shift its letters forwards by $k$ positions and spit out a ciphertext $c$. In contrast, a decryption algorithm $Dec_k$ would take the ciphertext $c$ and shift its letters *backwards* by $k$ places to retrieve the original plaintext. If we map the alphabet to the set ${0,...,25}$ ($a = 0, b = 1$, etc.), a more mathematical description is obtained. Encryption of any message $m = m_1 \cdot\cdot\cdot m_l$ ($m_i \in {0,...,25}$) using the key $k$ is given by
 
 $$
 \operatorname{Enc}_k (m_1 \cdot\cdot\cdot m_l) = c_1 \cdot\cdot\cdot c_l, \hspace{1cm} where \hspace{1mm} c_i = [(m_i + k) \mod 26]
 $$

The notation $[a \mod N]$ is the remainder of $a$ upon division by $N$ where $0\leq[a \mod N] < N$ and $\cdot\cdot\cdot$ denotes concatenation and not multiplication. Decryption of a cyphertext $c = c_1 \cdot\cdot\cdot c_l$ using a key $k$ would then be given by 

 $$
 \operatorname{Dec}_k (c_1 \cdot\cdot\cdot c_l) = m_1 \cdot\cdot\cdot m_l, \hspace{1cm} where \hspace{1mm} m_i = [(c_i - k) \mod 26]
 $$

It is only natural to now ask, is this cipher secure? And the simple answer is no. There are only 26 possible keys and so the key-space is not sufficiently big. You can even go through all 26 possible keys with a given ciphertext by hand and check which resulting plaintext makes sense. Most likely, there will be only one and so you would have recovered the original message.

Another method to crack this cipher is by using frequency analysis. Since the shift cipher is a one-to-one mapping on a letter-by-letter basis, the frequency distribution of letters is preserved. For example, the most common letter in English is the letter "e". If we analyse the ciphertext and discover that the most common letter there is "g", then we know that most likely the letter "g" is the letter "e" encrypted with the given key. From this we can calculate the key to be 2 (however, the plaintext, and therefore the ciphertext, may actually deviate from this distribution, so it is not with 100% certainty that the key is 2). We can also perform the same procedure with the rest of the letters in the ciphertext and retrieve the original plaintext. This process can also be automated with some math.

![[res/TODO]]

Let's once again map the alphabet with the integers 0 through 25 and also this time let $p_i$ ($0 \leq p_i \leq 1$) denote the frequency of the $i$th letter. Using the above table, we can calculate that

$$
\sum_{i=0}^{25} p_i^2 \approx 0.065
$$

Now, let $q_i$ denote the frequency of the $i$th letter in the ciphertext - this is just equal to the number of occurrences of the $i$th letter divided by the length of the ciphertext. If the key is $k$, then $p_i$ should be approximately equal to $q_{i+k}$, since the $i$th letter gets mapped to the $(i+k)$th letter (technically, these should be $i+k \mod 26$, but that's too cumbersome to write here). Therefore, if we compute

$$
I_j \overset{\mathrm{def}}{=} \sum_{i=0}^{25} p_i \cdot q_{i+j}
$$

for every value of $j \in \{0,...,25\}$, then $I_k$ should be approximately equal to 0.065, where $k$ is the actual key. For all $j \neq k$, $I_j$ would be different from 0.065. This ultimately leads to a way to recover the original key that is fairly easy to automate.

# The Vigenère Cipher

This cipher is a more advanced version of the shift cipher. It is a *poly-alphabetic* shift cipher. Unlike the previous ciphers, it does not define a fixed mapping on a letter-by-letter basis. Instead, it maps blocks of letters whose size depends on the key length. For example, `ab` could be mapped to `xy`, `ac` to `zt`, and `aa` to `bc`. Moreover, identical blocks will be mapped to different blocks depending on their relative position in the plaintext. `ab` could once be mapped to `xy`, but then when `ab` appears again, it may be mapped to `ci`.

In the Vigenère cipher the key is no longer a single number, but rather a string of letters, where each letter is again mapped to the integers $\{0,...,25\}$. The key is then repeatedly overlaid with the plaintext and each letter in the plaintext is shifted by the amount denoted by the key letter it has been matched with.

```
Plaintext:  the golden sun shone brightly, bathing the beach in its warm sunlight
Key:        cok ecokec oke cokec okecokec, okecoke cok ecoke co kec okec okecokec
Ciphertext: vvo kqznip ger uvyrg pbmivdpa, pkxjwxk vvo fgoml kb sxu kkvo gernwqlv
```

Given a known key length, also called a period, $t$, a ciphertext $c = c_1 \cdot\cdot\cdot c_l$ can be divided into parts, each with length $t$. Therefore, ciphertext characters with the same relative position in each of these groups with length $t$ would have all been encrypted using the same shift amount. In the above example, for the groups `theg` and `olde`, `t` and `o` would have both been encrypted with `c`, `h` and `l` with `o` and so on. Such characters are said to comprise a *stream*. Stated in a more mathematical way, for all $j \in \{1,...,t\}$, the ciphertext characters $c_j,c_{j+t},c_{j+2t},...$ have all been encrypted by shifting the corresponding plaintext character by $k_j$ positions, where $k_j$ is the $j$th character in the key $k$. It is now possible to use frequency analysis on each stream and check what shift amount yields the correct probability distribution.

If the period $t$ is not known, it may be possible to determine it by using Kasiski's method. Initially, you must identify repeated patterns of length 2-3 characters. Kasiski observed that the distance between these repeated patterns (given that they are not coincidental) is a multiple of the period $t$. In the above example, the distance between the two `vvo`s is 32 which is 8 times the period 4. 

There is also a more automatable (if this is even a word) approach. Recall that, given a period $t$, the ciphertext characters in the first stream 
$$c_1,c_{1+t},c_{1+2t},...$$
are the upshot of encrypting the corresponding plaintext characters with the same shift amount. Therefore, the frequencies of the characters in the stream will be close to the character frequencies in the English language in some shifted order. 

If we let $q_i$ denote the observed frequency of the $i$th letter in the stream ($q_i = \frac{\text{number of occurrences of the ith letter of the alphabet}}{\text{length of the stream}}$), we would expect that $q_{i+j \mod 26} \approx p_i$, where $j$ is the shift amount and $p_i$ is the frequency of the $i$th letter of the alphabet in a standard English text. Therefore, the sequence $q_0,q_1,...q_{25}$ is simply the sequence $p_0,p_1,...,p_{25}$ shifted by $j$.

Referring back to previous analysis, we get that 

$$
\sum_{i=0}^{25}q_i^2=\sum_{i=0}^{25}p_i^2 \approx 0.065
$$

We can easily find the period $t$. For every $\tau =1,2,...$ and the stream $c_1,c_{1+\tau},c_{1+2\tau},...$ we can define

$$
S_{\tau} \overset{\mathrm{def}}{=} \sum_{i=0}^{25}q_i^2
$$

When $\tau=t$, it is expected that $S_{\tau} \approx 0.065$. In the rest of the cases, we would expect that the character distribution in the stream is fairly uniform (recall that the Vigenère cipher smooths out character distributions) and so 

$$
S_{\tau} = \sum_{i=0}^{25} \left(\frac{1}{26}\right)^2 \approx 0.038
$$

Ergo, the smallest value $\tau$, for which $S_{\tau} \approx 0.065$, is likely the period $t$. This can be further validated by performing the same procedure on the subsequent streams in the ciphertext such as $c_2,c_{2+\tau},c_{2+2\tau},...$ and so on.