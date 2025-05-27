>[!DEFINITION] Definition: Vector Space
>
>A **vector space** $(V,F,+,\cdot)$ consists of a non-[[Sets|empty]] [[Sets|set]] $V$ and a [[index|field]] $F$ which are equipped with two [[Functions|operations]] - a **vector addition** $+: V \times V \to V$ and a **scalar multiplication** $\cdot: V \times F \to V$ - which have the following properties:
>
>- Commutativity: $\mathbf{u} + \mathbf{v} = \mathbf{v} + \mathbf{u} \qquad \forall \mathbf{u},\mathbf{v} \in V$
>- Associativity I: $\mathbf{u} + (\mathbf{v} + \mathbf{w}) = (\mathbf{u} + \mathbf{v}) + \mathbf{w} \qquad \forall \mathbf{u},\mathbf{v}, \mathbf{w} \in V$
>- Associativity II: $(\lambda\mu)\mathbf{u} = \lambda(\mu\mathbf{u}) \qquad \forall \lambda,\mu\in F, \forall \mathbf{u} \in V$
>- Distributivity I: $\lambda (\mathbf{u} + \mathbf{v}) = \lambda\mathbf{u}+\lambda\mathbf{v} \qquad \forall \mathbf{u},\mathbf{v} \in V, \forall \lambda \in F$
>- Distributivity II: $(\lambda + \mu)\mathbf{v} = \lambda\mathbf{v}+\mu\mathbf{v} \qquad \forall \lambda,\mu \in F, \forall \mathbf{v}\in V$
>- Existence of a zero vector: There is an element $\mathbf{0} \in V$ such that $\mathbf{v} + \mathbf{0} = \mathbf{v} \qquad \forall \mathbf{v} \in V$
>- Existence of the identity element: There is an element $1 \in F$ such that $1\cdot \mathbf{u} = \mathbf{u} \qquad \forall \mathbf{u}\in V$
>- Existence of vector inverses: For every $\mathbf{v} \in V$ there is a $-\mathbf{v} \in V$ such that $\mathbf{v} + (-\mathbf{v}) = \mathbf{0}$
>
>>[!NOTATION]- Notation: Vector Subtraction
>>
>>For any two vectors $\mathbf{u}$ and $\mathbf{v}$, where $-\mathbf{v}$ is the vector inverse of $\mathbf{v}$, we denote $\mathbf{u} + (-\mathbf{v})$ as simply $\mathbf{u} - \mathbf{v}$.
>>
>

>[!THEOREM] Theorem: Uniqueness of the Zero Vector
>
>Every [[Vector Space]] has exactly one zero vector.
>
>>[!PROOF]-
>>
>>Suppose that the vector space $(V,F,+,\cdots)$ had two zero vectors $\mathbf{0}, \mathbf{0}' \in V$, i.e. $\mathbf{v}+ \mathbf{0} = \mathbf{v}$ $\mathbf{v}+ \mathbf{0}'= \mathbf{v}$ for all $\mathbf{v} \in V$.
>>
>>It follows then that
>>
>>$$
>>\mathbf{0} + \mathbf{0}' = \mathbf{0}
>>$$
>>
>>$$
>>\mathbf{0}' + \mathbf{0} = \mathbf{0}'
>>$$
>>
>>But vector addition is commutative and so $\mathbf{0} + \mathbf{0}' = \mathbf{0}' + \mathbf{0}$ which means that $\mathbf{0} = \mathbf{0}'$.
>>
>

>[!THEOREM] Theorem: Uniqueness of Vector Inverses
>
>For every vector $\mathbf{v} \in V$ in a [[Vector Space]] $(V,F,+,\cdot)$ there is exactly one inverse vector $-\mathbf{v} \in V$ such that
>
>$$
>\mathbf{v} + (-\mathbf{v}) = \mathbf{0}
>$$
>
>>[!PROOF]-
>>
>>Suppose that there was another vector $\mathbf{v}' \in V$ such that
>>
>>$$
>>\mathbf{v} + \mathbf{v}' = \mathbf{0}
>>$$
>>
>>It then follows that
>>
>>$$
>>-\mathbf{v} + (\mathbf{v}+\mathbf{v}') = -\mathbf{v}+\mathbf{0}=-\mathbf{v}
>>$$
>>
>>and so
>>
>>$$
>>\mathbf{v}' = (-\mathbf{v}+\mathbf{v})+\mathbf{v}'=-\mathbf{v}+(\mathbf{v}+\mathbf{v}')=-\mathbf{v}+\mathbf{0}=-\mathbf{v}
>>$$
>>
>