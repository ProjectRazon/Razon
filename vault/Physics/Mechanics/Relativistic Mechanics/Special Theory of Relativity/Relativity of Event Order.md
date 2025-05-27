>[!THEOREM] Theorem: Relativity of Event Order
>
>Suppose $S$ and $S'$ are two inertial frames of reference and that $S'$ is moving with constant [[Velocity]] $\boldsymbol{u}$ relative to $S$.
>
>Two events will be perceived in the same order in $S$ as they are perceived in $S'$ if and only if the locations $(x_1',y_1',z_1')$ and $(x_2',y_2',z_2')$ and the times $t_1'$ and $t_2'$ at which they happen in $S'$ obey
>
>$$
>\operatorname{sign} \{ c^2(t_2' - t_1') + u_x (x_1'-x_2') + u_y (y_1' - y_2') + u_z (z_1' - z_2') \} = \operatorname{sign} \{t_2' - t_1'\}
>$$
>
>>[!NOTE]
>>
>>This means that it is possible for an event which happens *after* another event in $S'$ to be perceived as happening *before* it in $S$ and vice versa.
>>
>
>>[!PROOF]-
>>
>>If $t_1$ and $t_2$ are the times at which the events happen in $S$, then the [[Lorentz Boost|Lorentz transformation]] gives us
>>
>>$$
>>t_1 = \frac{\gamma}{c} \left(ct_1' - \frac{u_x}{c} x_1' - \frac{u_y}{c} y_1' - \frac{u_z}{c} z_1' \right)
>>$$
>>
>>$$
>>t_2 = \frac{\gamma}{c} \left(ct_2' - \frac{u_x}{c} x_2' - \frac{u_y}{c} y_2' - \frac{u_z}{c} z_2' \right)
>>$$
>>
>>If $t_2' \gt t_1'$, then we want $t_2 \gt t_1$ and so
>>
>>$$
>>\frac{\gamma}{c} \left(ct_2' - \frac{u_x}{c} x_2' - \frac{u_y}{c} y_2' - \frac{u_z}{c} z_2' \right) - \frac{\gamma}{c} \left(ct_1' - \frac{u_x}{c} x_1' - \frac{u_y}{c} y_1' - \frac{u_z}{c} z_1' \right) \gt 0
>>$$
>>
>>$$
>>c^2(t_2 - t_1) + u_x (x_1'-x_2') + u_y (y_1' - y_2') + u_z (z_1' - z_2') \gt 0
>>$$
>>
>>Alternatively, if $t_2' \lt t_1'$, then we want $t_2 \lt t_1$ and so 
>>
>>$$
>>c^2(t_2 - t_1) + u_x (x_1'-x_2') + u_y (y_1' - y_2') + u_z (z_1' - z_2') \lt 0
>>$$
>>
>>This can be summarised as
>>
>>$$
>>\operatorname{sign} \{ c^2(t_2' - t_1') + u_x (x_1'-x_2') + u_y (y_1' - y_2') + u_z (z_1' - z_2') \} = \operatorname{sign} \{t_2' - t_1'\}
>>$$
>>
>

>[!THEOREM] Theorem: Relativity of Simultaneity
>
>Suppose $S$ and $S'$ are two inertial frames of reference and that $S'$ is moving with constant [[Velocity]] $\boldsymbol{u}$ relative to $S$.
>
>Two events which happen at locations $(x_1',y_1',z_1')$ and $(x_2',y_2',z_2')$ and at times $t_1'$ and $t_2'$ in $S'$, will be perceived as simultaneous in $S$ if and only if
>
>$$
>u_x (x_2' - x_1') + u_y (y_2' - y_1') + u_z (z_2' - z_1') = c^2 (t_2' - t_1'),
>$$
>
>where $c$ is the [[Speed of Light in a Vacuum|speed of light]] in a vacuum.
>
>>[!NOTE]
>>
>>This means that two events which are perceived as simultaneous in one inertial frame of reference need not be perceived as simultaneous in another and two events which are *not* simultaneous in one inertial frame of reference *may* be simultaneous in another: 
>>
>>- Two events which happen at the same time $t'$ in $S'$ will also be perceived as simultaneous in $S$ if and only if their locations $(x_1', y_1', z_1')$ and $(x_2', y_2', z_2')$ in $S'$ obey
>>
>>$$
>>u_x (x_2' - x_1') + u_y(y_2' - y_1') + u_z (z_2' - z_1') = 0
>>$$
>>
>>- Even if two events are not simultaneous in $S'$, they will be perceived as simultaneous in $S$ if they obey the first equation but not the second.
>>
>
>>[!PROOF]-
>>
>>If $t_1$ and $t_2$ are the times at which the events happen in $S$, then the [[Lorentz Boost|Lorentz transformation]] gives us
>>
>>$$
>>t_1 = \frac{\gamma}{c} \left(ct_1' - \frac{u_x}{c} x_1' - \frac{u_y}{c} y_1' - \frac{u_z}{c} z_1' \right)
>>$$
>>
>>$$
>>t_2 = \frac{\gamma}{c} \left(ct_2' - \frac{u_x}{c} x_2' - \frac{u_y}{c} y_2' - \frac{u_z}{c} z_2' \right)
>>$$
>>
>>For the events to be perceived as simultaneous in $S$, we want $t_1$ to be equal to $t_2$ and so
>>
>>$$
>>\frac{\gamma}{c} \left(ct_1'-\frac{u_x}{c} x_1' - \frac{u_y}{c} y_1' - \frac{u_z}{c} z_1' \right) = \frac{\gamma}{c} \left(ct_2' - \frac{u_x}{c} x_2' - \frac{u_y}{c} y_2' - \frac{u_z}{c} z_2' \right)
>>$$
>>
>>$$
>>ct_1'-\frac{u_x}{c} x_1' - \frac{u_y}{c} y_1' - \frac{u_z}{c} z_1' = ct_2'-\frac{u_x}{c} x_2' - \frac{u_y}{c} y_2' - \frac{u_z}{c} z_2'
>>$$
>>
>>$$
>>\frac{u_x}{c} x_2' + \frac{u_y}{c} y_2' + \frac{u_z}{c} z_2' -\frac{u_x}{c} x_1' - \frac{u_y}{c} y_1' - \frac{u_z}{c} z_1' = c(t_2 - t_1)
>>$$
>>
>>$$
>>\frac{u_x}{c} (x_2' - x_1') + \frac{u_y}{c} (y_2' - y_1') + \frac{u_z}{c} (z_2' - z_1') =  c(t_2 - t_1)
>>$$
>>
>>$$
>>u_x (x_2' - x_1') + u_y(y_2' - y_1') + u_z (z_2' - z_1') = c^2(t_2 - t_1)
>>$$
>>
>