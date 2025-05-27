>[!DEFINITION] Definition: Potential Energy
>
>A **potential energy function** $U$ of a [[Conservative Force]] $\boldsymbol{F}$ is a scalar field such that
>
>$$\boldsymbol{F} = -\nabla U$$
>
>There are infinitely many such functions but we are free to choose where $U = 0$ and thus fix a particular one, so long as we are consistent with our choice. Once $U$ is fixed, we call $U(\boldsymbol{r})$ the **potential energy** of a [[Point Mass]] at the [[Position]] $\boldsymbol{r}$ due to $\boldsymbol{F}$.
>
>>[!NOTATION]
>>
>>$$E_{\text{p}} \qquad E_{\text{pot}} \qquad U$$
>>
>

>[!THEOREM] Theorem: Work of a Conservative Force
>
>The [[Work]] done by a [[Conservative Force]] $\boldsymbol{F}$ acting on a [[Physical System]] is equal to the negative change in its [[Potential Energy]].
>
>$$
>W = -\Delta U
>$$
>
>>[!NOTE]
>>
>>The exact choice of the potential energy function is irrelevant.
>
>>[!PROOF]-
>>
>>$$W = \int_{t_1}^{t_2} \boldsymbol{F} \cdot \boldsymbol{v} \mathop{\mathrm{d}t} = -U(\boldsymbol{r}(t_2)) - (-U(\boldsymbol{r}(t_1))) = -U(\boldsymbol{r}(t_2)) + U(\boldsymbol{r}(t_1)) = -\Delta U$$
>>
>