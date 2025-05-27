>[!TIP] Tip: Partial Derivatives in Cartesian Coordinates
>
>Let $f: \mathcal{D} \to \mathbb{R}$ be a [[Real Scalar Field]] on an [[The Topology of Euclidean Space|open subset]] $\mathcal{D} \subseteq \mathbb{R}^n$.
>
>The [[Partial Derivatives of Real Scalar Fields|partial derivative]] of $f$ at $\mathbf{a}$ with respect to the $i$-th [[Cartesian Coordinate System|Cartesian coordinate]] $x^i$ coincides with the [[Directional Derivatives of Real Scalar Fields|directional derivative]] of $f$ there along the $i$-th [[Standard Basis of the Real Vector Space|standard basis vector]] $\mathbf{e}_i$:
>
>$$
>\frac{\partial f}{\partial x^i}(\mathbf{a}) = \lim_{h\to 0} \frac{f(\mathbf{a} + h \cdot \mathbf{e}_i) - f(\mathbf{a})}{h}
>$$
>
>>[!NOTATION]-
>>
>>Cartesian coordinates in partial derivatives can be denoted using either subscripts and superscripts, i.e.
>>
>>$$
>>\frac{\partial}{\partial x^i} (\mathbf{a}) \qquad  \frac{\partial f}{\partial x^i} f(\mathbf{a}) \qquad \left. \frac{\partial f}{\partial x^i}\right|_{\mathbf{a}} \qquad f_{x^i}(\mathbf{a})
>>$$
>>
>>$$
>>\frac{\partial}{\partial x_i} (\mathbf{a}) \qquad  \frac{\partial f}{\partial x_i} f(\mathbf{a}) \qquad \left. \frac{\partial f}{\partial x_i}\right|_{\mathbf{a}} \qquad f_{x_i}(\mathbf{a})
>>$$
>>
>>are equivalent. Writing the coordinates using subscripts is cleaner when partial derivatives of higher orders are involved.
>>
>