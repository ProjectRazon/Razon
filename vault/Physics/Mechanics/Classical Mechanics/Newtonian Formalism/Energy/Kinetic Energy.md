>[!DEFINITION] Definition: Kinetic Energy
>
>The **kinetic energy** of a physical object is the [[Work]] needed to bring the object from rest to its current state of motion.
>
>>[!NOTATION]-
>>
>>$$
>>E_{\text{kin}} \qquad E_{\text{k}} \qquad K
>>$$
>>
>

>[!THEOREM] Theorem: Non-Relativistic Kinetic Energy of a Point Mass
>
>The [[Kinetic Energy]] of a [[Point Mass]] $m$ moving with [[Velocity|speed]] $v$ is given by the formula
>
>$$
>E_{\text{kin}} = \frac{1}{2}mv^2
>$$
>
>provided that $v$ is a lot smaller than the [[Speed of Light in a Vacuum|speed of light]].
>
>>[!PROOF]-
>>
>>At time $t_1$, the [[Force|resultant force]] $\boldsymbol{F}$ begins to accelerates the [[Point Mass]] from 0 m/s and at time $t_2$ the [[Velocity|speed]] reaches $v$ m/s, i.e. $||\boldsymbol{v}(t_1)|| = 0$ and $||\boldsymbol{v}(t_2)||=v$. During this time $\boldsymbol{F}$ does [[Work]]
>>
>>$$
>>W = \int_{t_1}^{t_2} \boldsymbol{F}\cdot \boldsymbol{v}\mathop{\mathrm{d}t}
>>$$
>>
>>According to [[Newton's Laws of Translational Motion|Newton's second laws of motion]], $\boldsymbol{F}=m\boldsymbol{a}$.
>>
>>$$
>>W = \int_{t_1}^{t_2} m\boldsymbol{a}\cdot \boldsymbol{v}\mathop{\mathrm{d}t} = m \int_{t_1}^{t_2} \boldsymbol{a}\cdot \boldsymbol{v}\mathop{\mathrm{d}t}
>>$$
>>
>>And since [[Acceleration]] is the temporal derivative of [[Velocity]], we have 
>>
>>$$
>>\frac{\mathrm{d}\boldsymbol{v}}{\mathrm{d}t} = \boldsymbol{a}
>>$$
>>
>>$$
>>\boldsymbol{a}\mathop{\mathrm{d}t} = \mathop{\mathrm{d}\boldsymbol{v}}
>>$$
>>
>>$$
>>\begin{align*}W = m \int_{t_1}^{t_2} \boldsymbol{a}\cdot \boldsymbol{v}\mathop{\mathrm{d}t} &= m \int_{t_1}^{t_2} (\boldsymbol{a}\mathop{\mathrm{d}t}) \cdot \boldsymbol{v} \\ &= m \int_{t_1}^{t_2} \boldsymbol{v} \cdot \mathop{\mathrm{d}\boldsymbol{v}}\end{align*}
>>$$
>>
>>Let's see what the temporal derivative of $\boldsymbol{v}\cdot\boldsymbol{v}$ is. Using the product rule, we obtain
>>
>>$$
>>\frac{\mathrm{d}}{\mathrm{d}t}(\boldsymbol{v}\cdot\boldsymbol{v}) = \frac{\mathrm{d}\boldsymbol{v}}{\mathrm{d}t} \cdot \boldsymbol{v} + \boldsymbol{v}\cdot \frac{\mathrm{d}\boldsymbol{v}}{\mathrm{d}t} = 2\left( \boldsymbol{v}\cdot\frac{\mathrm{d}\boldsymbol{v}}{\mathrm{d}t}\right)
>>$$
>>
>>$$
>>\boldsymbol{v}\cdot\mathop{\mathrm{d}\boldsymbol{v}} = \frac{1}{2}\mathop{\mathrm{d}(\boldsymbol{v}\cdot\boldsymbol{v})}
>>$$
>>
>>We just substitute this into the above formula for the [[Work]] $W$.
>>
>>$$
>>W = m\int_{t_1}^{t_2} \boldsymbol{v} \cdot \mathop{\mathrm{d}\boldsymbol{v}} = m\int_{t_1}^{t_2} \frac{1}{2}\mathop{\mathrm{d}(\boldsymbol{v}\cdot\boldsymbol{v})} = \frac{1}{2}m \int_{t_1}^{t_2} \mathop{\mathrm{d}(\boldsymbol{v}\cdot\boldsymbol{v})}
>>$$
>>
>>Solve the integral:
>>
>>$$
>>W = \frac{1}{2}m \int_{t_1}^{t_2} \mathop{\mathrm{d}}(\boldsymbol{v}\cdot\boldsymbol{v}) = \frac{1}{2}m[\boldsymbol{v}(t_2)\cdot\boldsymbol{v}(t_2)-\boldsymbol{v}(t_1)\cdot\boldsymbol{v}(t_1)]
>>$$
>>
>>Using the properties of the dot product, we obtain
>>
>>$$
>>\boldsymbol{v}(t_2)\cdot\boldsymbol{v}(t_2) = ||\boldsymbol{v}(t_2)||^2 = v^2
>>$$
>>
>>$$
>>\boldsymbol{v}(t_1)\cdot\boldsymbol{v}(t_1) = ||\boldsymbol{v}(t_1)||^2 = 0^2
>>$$
>>
>>Thus
>>
>>$$
>>W = \frac{1}{2}m(v^2-0^2) = \frac{1}{2}mv^2
>>$$
>>
>