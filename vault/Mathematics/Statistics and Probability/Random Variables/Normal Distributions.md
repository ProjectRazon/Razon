
# The Standard Normal Distribution

>[!DEFINITION] Definition: Standard Normal Distribution
>
>We say that a [[Random Variables#Continuous Random Variables|continuous random variable]] $X$ has the **standard normal distribution** if its [[Random Variables#Probability Density Functions|probability density function]] $f$ can be written in terms of the [[The Real Exponential Function|real exponential function]] as follows:
>
>$$
>f(x) = \frac{1}{\sqrt{2\pi}} \mathrm{e}^{-x^2/2}
>$$
>
>>[!NOTATION]
>>
>>$$
>>X \sim \mathcal{N}(0,1) \qquad X \in \mathcal{N}(0,1)
>>$$
>>
>>In this case, it is also typical to denote the [[Random Variables#Probability Density Functions|probability density function]] of $X$ by $\varphi$ and its [[Random Variables#Cumulative Distribution Function|cumulative distribution function]] by $\Phi$.
>>
>

## Properties

>[!THEOREM]- Theorem: Expectation of the Standard Normal Distribution
>
>The [[Expectation]] of a [[Random Variables#Continuous Random Variables|continuous random variable]] which has the [[Normal Distributions#The Standard Normal Distribution|standard normal distribution]] is zero.
>
>$$
>X \sim \mathcal{N}(0,1) \implies \mathbb{E}[X] = 0
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM]- Theorem: Variance of the Standard Normal Distribution
>
>The [[Variance and Standard Deviation#Variance|variance]] of a [[Random Variables#Continuous Random Variables|continuous random variable]] which has the [[Normal Distributions#The Standard Normal Distribution|standard normal distribution]] is one.
>
>$$
>X \sim \mathcal{N}(0,1) \implies \operatorname{Var}(X) = 1
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

# General Normal Distributions

>[!DEFINITION] Definition: Normal Distribution
>
>We say that a [[Random Variables#Continuous Random Variables|continuous random variable]] $X$ has a **normal distribution** if there exist $\mu \in \mathbb{R}$, $\sigma \gt 0$ and a [[Random Variables#Continuous Random Variables|continuous random variable]] $Z$ which has the [[Normal Distributions#Standard Normal Distribution|standard normal distribution]] such that
>
>$$
>X = \mu + \sigma Z.
>$$
>
>>[!NOTATION]
>>
>>$$
>>X \sim N(\mu, \sigma^2) \qquad X \in N(\mu, \sigma^2)
>>$$
>>
>
>>[!DEFINITION] Definition: Standardization
>>
>>We call $Z$ the **standardization** of $X$.
>>
>

## Properties

>[!THEOREM]- Theorem: Cumulative Distribution Functions of Normal Distributions
>
>The [[Random Variables#Cumulative Distribution Function|cumulative distribution function]] $F$ of a [[Random Variables#Continuous Random Variables|continuous random variable]] $X$ which has the [[Normal Distributions#General Normal Distributions|normal distribution]] $\mathcal{N}(\mu, \sigma^2)$ is
>
>$$
>F(x) = \Phi\left(\frac{x - \mu}{\sigma}\right),
>$$
>
>where $\Phi$ is the [[Random Variables#Cumulative Distribution Function|cumulative distribution function]] of $X$'s [[Normal Distributions#General Normal Distributions|standardization]].
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM]- Theorem: Probability Density of Normal Distributions
>
>The [[Random Variables#Probability Density Functions|probability density function]] $f$ of a [[Random Variables#Continuous Random Variables|continuous random variable]] $X$ which has the [[Normal Distributions#General Normal Distributions|normal distribution]] $\mathcal{N}(\mu, \sigma^2)$ is
>
>$$
>f(x) = \frac{1}{\sigma \sqrt{2\pi}} \mathrm{e}^{-\frac{1}{2}\left(\frac{x-\mu}{\sigma}\right)^2} = \frac{1}{\sigma}\varphi\left(\frac{x - \mu}{\sigma}\right),
>$$
>
>where $\mathrm{e}^{-\frac{1}{2}\left(\frac{x-\mu}{\sigma}\right)^2}$ is the [[The Real Exponential Function|real exponential function]] and $\varphi$ is the [[Random Variables#Probability Density Functions|probability density function]] of $X$'s [[Normal Distributions#General Normal Distributions|standardization]].
>
>
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM]- Theorem: Expectation of Normal Distributions
>
>The [[Expectation]] of a [[Random Variables#Continuous Random Variables|continuous random variable]] $X$ which has the [[Normal Distributions#General Normal Distributions|normal distribution]] $\mathcal{N}(\mu, \sigma^2)$ is $\mu$.
>
>$$
>X \sim \mathcal{N}(\mu, \sigma^2) \implies \mathbb{E}(X) = \mu
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM]- Theorem: Variance of Normal Distributions
>
>The [[Variance and Standard Deviation|variance]] of a [[Random Variables#Continuous Random Variables|continuous random variable]] $X$ which has the [[Normal Distributions#General Normal Distributions|normal distribution]] $\mathcal{N}(\mu, \sigma^2)$ is $\sigma^2$.
>
>$$
>X \sim \mathcal{N}(\mu, \sigma^2) \implies \operatorname{Var}(X) = \sigma^2
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM]- Theorem: The 68–95–99.7 Rule
>
>If a [[Random Variables#Continuous Random Variables|continuous random variable]] $X$ has the [[Normal Distributions#General Normal Distributions|normal distribution]] $\mathcal{N}(\mu, \sigma^2)$, then
>
>$$
>\begin{align*}
>P(|X - \mu| \lt 1\sigma) \approx 68.27 \% \\
>P(|X - \mu| \lt 2\sigma) \approx 95.45 \% \\
>P(|X - \mu| \lt 3\sigma) \approx 99.73 \%
>\end{align*}
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>