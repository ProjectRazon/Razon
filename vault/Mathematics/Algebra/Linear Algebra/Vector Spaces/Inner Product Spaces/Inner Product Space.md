>[!DEFINITION] Definition: Complex Inner Product Space
>
>A **complex inner product space** is a [[Complex Vector Space]] $(V,F,+,\cdot)$ equipped with an **inner product** [[Functions|operation]] $\langle \cdot, \cdot \rangle: V\times V \to \mathbb{C}$ which has the following properties:
>
>1. Conjugate symmetry
>
>$$
>\langle\mathbf{u},\mathbf{v}\rangle = \overline{\langle\mathbf{v},\mathbf{u}\rangle} \qquad \forall \mathbf{u},\mathbf{v} \in V
>$$
>
>2. Sesquilinearity
>	- Distributivity I: $\langle\mathbf{u} + \mathbf{v}, \mathbf{w}\rangle = \langle\mathbf{u}, \mathbf{w}\rangle + \langle\mathbf{v}, \mathbf{w}\rangle \qquad \forall \mathbf{u},\mathbf{v},\mathbf{w} \in V$
>	- Distributivity II: $\langle\mathbf{u},\mathbf{v} + \mathbf{w}\rangle = \langle\mathbf{u},\mathbf{v}\rangle + \langle\mathbf{u},\mathbf{w}\rangle \qquad \forall \mathbf{u},\mathbf{v},\mathbf{w} \in V$
>	- Semi-linearity in the first argument: $\langle\lambda\mathbf{u},\mathbf{v}\rangle = \bar{\lambda}\langle\mathbf{u},\mathbf{v}\rangle \qquad \forall \mathbf{u},\mathbf{v} \in V, \forall \lambda \in \mathbb{C}$
>	- Linearity in the second argument: $\langle\mathbf{u},\lambda\mathbf{v}\rangle = \lambda\langle\mathbf{u},\mathbf{v}\rangle \qquad \forall \mathbf{u},\mathbf{v} \in V, \forall \lambda \in \mathbb{C}$
>
>3. Positive-definiteness
>
>$$
>\langle\mathbf{v},\mathbf{v}\rangle \ge 0 \text{ with } \langle\mathbf{v},\mathbf{v}\rangle = 0 \iff \mathbf{v} = \mathbf{0} \qquad \forall \mathbf{v} \in V
>$$
>

>[!DEFINITION] Definition: Real Inner Product Space
>
>A **real inner product space** is a [[Real Vector Space]] $(V,F,+,\cdot)$ equipped with an **inner product** [[Functions|operation]] $\langle \cdot, \cdot \rangle: V\times V \to \mathbb{R}$ which has the following properties:
>
>1. Symmetry
>
>$$
>\langle\mathbf{u},\mathbf{v}\rangle = \langle\mathbf{v},\mathbf{u}\rangle \qquad \forall \mathbf{u},\mathbf{v} \in V
>$$
>
>2. Sesquilinearity
>	- Distributivity I: $\langle\mathbf{u} + \mathbf{v}, \mathbf{w}\rangle = \langle\mathbf{u}, \mathbf{w}\rangle + \langle\mathbf{v}, \mathbf{w}\rangle \qquad \forall \mathbf{u},\mathbf{v},\mathbf{w} \in V$
>	- Distributivity II: $\langle\mathbf{u},\mathbf{v} + \mathbf{w}\rangle = \langle\mathbf{u},\mathbf{v}\rangle + \langle\mathbf{u},\mathbf{w}\rangle \qquad \forall \mathbf{u},\mathbf{v},\mathbf{w} \in V$
>	- Linearity in the first argument: $\langle\lambda\mathbf{u},\mathbf{v}\rangle = \lambda \langle\mathbf{u},\mathbf{v}\rangle \qquad \forall \mathbf{u},\mathbf{v} \in V, \forall \lambda \in \mathbb{C}$
>	- Linearity in the second argument: $\langle\mathbf{u},\lambda\mathbf{v}\rangle = \lambda\langle\mathbf{u},\mathbf{v}\rangle \qquad \forall \mathbf{u},\mathbf{v} \in V, \forall \lambda \in \mathbb{C}$
>
>3. Positive-definiteness
>
>$$
>\langle\mathbf{v},\mathbf{v}\rangle \ge 0 \text{ with } \langle\mathbf{v},\mathbf{v}\rangle = 0 \iff \mathbf{v} = \mathbf{0} \qquad \forall \mathbf{v} \in V
>$$
>

>[!NOTATION]
>
>We write $(V,F,+,\cdot)$ when it does not matter if the inner product space is real or complex. 
>