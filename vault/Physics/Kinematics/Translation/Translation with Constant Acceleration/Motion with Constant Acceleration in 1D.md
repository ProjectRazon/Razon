>[!THEOREM] Theorem: Motion with Constant Acceleration in 1D
>
>In one-dimensional [[Motion with Constant Acceleration]] the [[Position]], [[Velocity]] and [[Acceleration]] vectors become scalars $r(t),v(t),a$.
>
>In addition to the general laws of [[Motion with Constant Acceleration]], in one dimension we also have:
>
>$$
>v_{\text{avg}}(t)=\frac{v(t)+v_0}{2}
>$$
>
>$$
>r(t) = r_0+t\cdot v_{\text{avg}}(t)
>$$
>
>$$
>v^2 = v_0^2 +2a(r-r_0)
>$$
>
>The last law makes it possible to compute the [[Velocity]] $v=v(t)$ of a [[Point Mass]] as a function of its [[Position]] $r=r(t)$.
>
>>[!PROOF]- Proof: First Law
>>
>>$$
>>v_{\text{avg}}(t) = \frac{r(t)-r(0)}{t-0}=\frac{r(t)-r_0}{t}=\frac{r_0+v_0t+\frac{1}{2}at^2-r_0}{t}=v_0+\frac{1}{2}at
>>$$
>>
>>We add $v_0$ to both sides of the following equation and then multiply by $2$.
>>
>>$$
>>v_{\text{avg}}(t) = v_0 + \frac{1}{2}at
>>$$
>>
>>$$
>>v_{\text{avg}}(t) + v_0 = 2v_0 + \frac{1}{2}at
>>$$
>>
>>$$
>>2v_{\text{avg}}(t) + 2v_0 = 4v_0 + at
>>$$
>>
>>$$
>>2v_{\text{avg}}(t) + 2v_0 = 3v_0 + (v_0 + at) = 3v_0 + v(t)
>>$$
>>
>>$$
>>2v_{\text{avg}}(t)= v_0+v(t)
>>$$
>>
>>$$
>>v_{\text{avg}}(t)=\frac{v(t)+v_0}{2}
>>$$
>>
>
>>[!PROOF]- Proof: Second Law
>>
>>$$
>>r(t) = r_0 + v_0 t + \frac{1}{2} at^2 = r_0 + t\left(v_0+\frac{1}{2}at\right)=r_0+t\cdot v_{\text{avg}}(t)
>>$$
>>
>>For an explanation for the last step, see the proof of the first law.
>>
>
>>[!PROOF]- Beweis: Third Law
>>
>>Rearrange the law for the [[Velocity]]:
>>
>>$$
>>t = \frac{v(t)-v_0}{a}
>>$$
>>
>>Susbtitute for $t$ in the law for [[Position]]:
>>
>>$$
>>r(t) = r_0+ v_0\frac{v(t)-v_0}{a} + \frac{1}{2}a\left(\frac{v(t)-v_0}{a}\right)^2
>>$$
>>
>>$$
>>2a r(t) = 2ar_0 + 2v_0(v(t)-v_0)+(v(t)-v_0)^2
>>$$
>>
>>$$
>>2a(r(t)-r_0)=2v_0v(t)-2v_0^2+ v(t)^2 - 2v_0v(t) + v_0^2
>>$$
>>
>>$$
>>2a(r(t)-r_0)=v(t)^2-v_0^2
>>$$
>>
>>$$
>>v(t)=2a(r(t)-r_0)+v_0^2
>>$$
>>
>