# Constraints

In practice, it is rare that we simply need to find the [[Local Extrema|local]] and [[Extrema|global extrema]] of a [[Real Scalar Field]]. Usually, we are interested in finding extrema under certain conditions. 

>[!EXAMPLE]-
>
>Imagine you are tasked with the construction of a box with a lid which should be able to fit exactly $1$ cubic metre of stuff. You want to minimise the cost and thus the amount of paperboard used for the box. In other words, you want to find what dimensions of the box which require the least material. The amount of material is given by
>
>$$
>p(x, y, z) = \underset{\text{front and back}}{2xy} + \underset{\text{sides}}{2yz} + \underset{\text{bottom and lid}}{2xz}
>$$
>
>You can check that, by itself, this function has neither local nor global extrema. However, we also have another condition - the box should have a volume of $1$ cubic metre. This gives us a constraint for the dimensions $x, y, z$:
>
>$$
>xyz = 1
>$$
>
>This allows us to the express one variable using the other three and obtain an expression for $p$ which has only 2 variables.
>
>$$
>z = \frac{1}{xy}
>$$
>
>$$
>p(x, y) = 2xy + 2y\times \frac{1}{xy} + 2x \times \frac{1}{xy} = 2xy + \frac{2}{x} + \frac{2}{y} 
>$$
>
>This function *does* have a local minimum, which occurs at $x = 1$ and $y = 1$. Using $z = \frac{1}{xy}$, we find that $z = 1$. Thus, a cube is the box shape which requires the least amount of material to fit $1$ cubic metre of stuff.
>

>[!DEFINITION] Definition: Equality Constraint
>
>Let $f: \mathcal{D} \subseteq \mathbb{R}^n \to \mathbb{R}$ be a [[Real Scalar Field]].
>
>An **equality constraint** is an [[Equation]] of the form
>
>$$
>g(\mathbf{x}) = c
>$$
>
>for some [[Real Scalar Field|function]] $g: \mathcal{D} \to \mathbb{R}$ and some constant $c \in \mathbb{R}$.
>
>>[!INTUITION]-
>>
>>Constraints restrict the part of the domain of $f$ in which we are interested. Although $f$ itself might not admit extrema on its entire domain, when restricted to only those values for which the constraint is fulfilled, this might change might. In other words, $f$ might not have extrema, but its [[Functions|restriction]] $f\big|_{S}$ on $S = \{\mathbf{x} \mid g(\mathbf{x}) = c\}$ might.
>>
>
>>^equality-constraint
>
