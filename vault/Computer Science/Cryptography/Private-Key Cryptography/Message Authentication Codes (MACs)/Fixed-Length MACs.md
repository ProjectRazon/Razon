# Fixed-Length MACs

This is the most basic type of MAC system and uses [[Pseudorandom Function Generators (PRFGs|Pseudorandom Function Generators (PRFGs)]].md). A fixed-length MAC uses keys and messages that are of the same length $n$ and also produce tags with length $n$. Indeed, they are very limited because they require long keys for long messages and produce equally long tags which is a problem because bandwidth is limited. Nevertheless, fixed-length MACs can be used to implement more sophisticated and useful systems.

The signing algorithm of a fixed-length MAC $\textit{Sign}(\textit{key}: \textbf{str}[n], \textit{message}: \textbf{str}[n]) \to \textbf{str}[n]$ can be any pseudorandom function generator $\textit{PRFG}(\textit{seed}: \textbf{str}[n], \textit{idb}: \textbf{str}[n]) \to \textbf{str}[n]$ where the secret key $k$ is used as the seed and the message $m$ is the input data block, i.e.

$$
\textit{Sign}(k, m) \coloneqq \textit{PRFG}(k, m)
$$

Since the signing algorithm is just a PRFG, this is a deterministic MAC system and so we can just use the trivial verification algorithm for $\textit{Verify}$, i.e.

```rust
fn Verify(key: str[n], message: str[n], tag: str[n]) -> bool {
	generated_tag = Sign(key, message);
	return generated_tag == tag;
}
```

Indeed, this construction turns out to be a secure MAC system so long as the PRFG used for signing is secure.

>[!PROOF]- Proof: Security of Fixed-Length MACs
>
>TODO
>

Despite being very limited themselves, fixed-length MACs can be used to construct much better MAC systems.

### Theoretical Abritrary-Length MACs

Fixed-length MACs can be used to construct MACs with arbitrary message length. In particular, suppose that we are given a fixed-length MAC system $(\textit{Sign}',\textit{Verify}')$ which uses keys, messages and tags all with length $n$. We can construct a MAC system $(\textit{Sign},\textit{Verify})$ which uses keys of length $n$ and messages of any length $l \lt 2^{n/4}$.

The $\textit{Sign}$ algorithm takes a $k \in \{0,1\}^n$ and a message $m \in \{0,1\}^l$. It then divides the message $m$ into $d$ blocks $m_1, m_2, ..., m_d$, each with length $n/4$. If necessary, the last block $m_d$ is padded with zeroes. Subsequently, a *message identifier* $r\leftarrow_R \{0,1\}^{n/4}$, which is just a string of length $n/4$, is randomly chosen. Each message is then signed separately. The tag $t_i$ of the $i$-th message $m_i$, where $i = 1,2,...,d$, is generated as by invoking $\textit{Sign}'$ on the concatenation of the message identifier $r$, the total message length $l$, the current block index $i$ and the block $m_i$ itself: $\tau_i = \textit{Sign}'(r||l||i||m_i)$, where the length $l$ and the index $i$ are both encoded as binary strings of length $n/4$, since $i,l \lt 2^{n/4}$. The final tag $\tau$ for the message $m$ is the concatenation of the message identifier $r$ and all the tags for the separate message blocks, i.e. $\tau = r||\tau_1||\tau_2||\cdots||\tau_d$.  The resulting tag has length $\frac{n}{4} + n\cdot d = \frac{n}{4} + n\cdot \frac{l}{n/4} = \frac{n}{4} + 4l$.

```rust
fn Sign(key: str[n], message: str[l < 2^(n/4)]) -> str[n/4 + 4l] {
	let blocks: Arr[str[n/4]] = message.split_with_length(n/4);
	let d = blocks.count();
	
	if blocks[d-1].length() != (n / 4) {
		pad_with_zeroes(blocks[d-1]);
	}
	
	let message_identifier = random_string(alphabet: [0,1], length: (n / 4)); // Generate a random binary string with length n/4 for the message identifier r
	
	let tags: Arr[str[n/4]];
	
	let final_tag = message_identifier;
	
	for (i, t) in tags.enumerate() { // Enumerate each tag t with its index i
		t = Sign'(message_identifier + l.to_bits(length: n/4) + i.as_bits(length: n/4) + blocks[i]); // Parse l and i as binary strings of length n/4
		final_tag += t;
	}
	
	return final_tag;
}
```

Unfortunately, we cannot use the canonical verification algorithm for this signing algorithm - $\textit{Sign}$ uses randomness to generate the message identifier and is thus non-deterministic. Luckily, we can still use $\textit{Verify}'$ to construct a verification algorithm. In particular, $\textit{Verify}$ takes the secret key $k \in \{0,1\}^n$, a message of length $0 \lt l \lt 2^{n/4}$ and a tag $\tau$. The tag $\tau$ is then parsed as a message identifier $r$ of length $n/4$ and $d'$ sub-tags of length $n$, i.e. $\tau = (r, \tau_1, ..., \tau_{d'})$. Similarly, the message $m$ is divided into $d$ blocks of length $n/4$ (if necessary, the last block is once again padded with 0s).

First, $\textit{Verify}$ checks if there are the same number of sub-tags as message blocks, since if there aren't, it is trivial that the tag is invalid. If this check passes, $\textit{Verify}$ uses $\textit{Verify}'$ to separately verify each message block with its corresponding sub-tag. Once again, the message identifier $r$, the total message length $l$ and the index $i$ of the current block are prepended to the contents of the block before invoking $\textit{Verify}'$.

```rust
fn Verify(key: str[n], message: str[l], tag: str) -> bool {
	let blocks: Arr[str[l]] = message.split_with_length(n/4);
	if blocks[blocks.count() - 1].length() != (n / 4) {
		pad_with_zeroes(blocks[d-1]);
	}
	
	let message_identifier = tag.remove(0, n/4); // Extract the message identifier from the tag
	let subtags = tag.split_with_length(n);
	if blocks.count() != subtags.count() {
		return false;
	}
	
	for(let i = 0;i < blocks.count(); ++i) {
		if subtags[i] != Verify'(message_identifier + l.to_bits(length: n/4) + i.as_bits(length: n/4) + blocks[i]) {
			return false; // If even a single tag does not match with its message block, the verification fails
		}
	}
	
	return true;
}
```

Proof of security: TODO

>[!NOTE]
>
>This MAC system is not used in practice because it can be rather slow and still imposes certain limitations on the messages. Nevertheless, it is a good theoretical example that arbitrary-length MACs are possible.
>
