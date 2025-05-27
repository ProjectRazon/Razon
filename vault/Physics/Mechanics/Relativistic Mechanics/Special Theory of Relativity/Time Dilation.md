>[!THEOREM] Theorem: Time Dilation
>
>Suppose $S$ and $S'$ are two inertial frames of reference and $S'$ is moving relative $S$ with constant [[Velocity]].
>
>If two events happen at the same location in $S'$ and a clock in $S'$ measures the time elapsed between them to be $\Delta t'$, then a clock in $S$ will measure the time between the events to be
>
>$$
>\Delta t = \gamma \Delta t'
>$$
>
>where $\gamma$ is the [[Lorentz Factor]] of the two inertial frames of reference.
>
>>[!NOTE]
>>
>>This means that the time elapsed between two events is *not* absolute - it depends on the frame of reference.
>>
>
>>[!PROOF]-
>>
>>To find the time elapsed $\Delta t$ between the two events in $S$, we need to know the times $t_1$ and $t_2$ at which they happen. These are given through the [[Lorentz Factor|Lorentz transformation]] and since both events happen at the same location $(x',y',z')$ in $S'$, we have
>>
>>$$
>>t_1 = \frac{\gamma}{c} \left(ct_1' - \frac{u_x}{c} x' - \frac{u_y}{c} y' - \frac{u_z}{c} z' \right)
>>$$
>>
>>$$
>>t_2 = \frac{\gamma}{c} \left(ct_2' - \frac{u_x}{c} x' - \frac{u_y}{c} y' - \frac{u_z}{c} z' \right)
>>$$
>>
>>We can now use these to calculate $\Delta t = |t_2 - t_1|$:
>>
>>$$
>>\begin{align*}\Delta t &= \left|\frac{\gamma}{c}\left(ct_2' - \frac{u_x}{c} x' - \frac{u_y}{c} y' - \frac{u_z}{c} z' \right) - \frac{\gamma}{c} \left(ct_1' - \frac{u_x}{c} x' - \frac{u_y}{c} y' - \frac{u_z}{c} z' \right)\right| \\ &= \left| \frac{\gamma}{c} \left(ct_2' - \frac{u_x}{c} x' - \frac{u_y}{c} y' - \frac{u_z}{c} z' - ct_1 + \frac{u_x}{c} x' + \frac{u_y}{c} y' + \frac{u_z}{c} z' \right) \right| \\ &= |\gamma(t_2' - t_1')| = \gamma|(t_2' - t_1')| = \gamma \Delta t'\end{align*}
>>$$
>>
>