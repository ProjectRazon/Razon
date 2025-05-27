---
title: Trigonometric Identities
tags:
  - real-analysis
  - analysis
  - mathematics
---

# Fundamental Trigonometric Properties

>[!THEOREM] Theorem: Trigonometric Functions of Standard Angles
>
>Here are some common values for [[Real Sine Function|sine]], [[Real Cosine Function|cosine]], [[Real Tangent Function|tangent]] and [[Real Cotangent Function|cotangent]]:
>
>||$0$|$\frac{\pi}{6}$|$\frac{\pi}{4}$|$\frac{\pi}{3}$|$\frac{\pi}{2}$|$\frac{2\pi}{3}$|$\frac{5\pi}{6}$|$\pi$|
>|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
>|$\sin \theta$|$0$|$\frac{1}{2}$|$\frac{\sqrt{2}}{2}$|$\frac{\sqrt{3}}{2}$|$1$|$\frac{\sqrt{3}}{2}$|$\frac{1}{2}$|$0$|
>|$\cos \theta$|$1$|$\frac{\sqrt{3}}{2}$|$\frac{\sqrt{2}}{2}$|$\frac{1}{2}$|$0$|$-\frac{1}{2}$|$-\frac{\sqrt{3}}{2}$|$-1$|
>|$\tan \theta$|$0$|$\frac{\sqrt{3}}{3}$|$1$|$\sqrt{3}$||$-\sqrt{3}$|$-\frac{\sqrt{3}}{3}$|$0$|
>|$\cot \theta$||$\sqrt{3}$|$1$|$\frac{\sqrt{3}}{3}$|$0$|$-\frac{\sqrt{3}}{3}$|$-\sqrt{3}$||
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Fundamental Trigonometric Identities
>
>[[Real Sine Function|Sine]], [[Real Cosine Function|cosine]], [[Real Tangent Function|tangent]] and [[Real Cotangent Function|cotangent]] obey the following identities:
>
>$$
>\sin^2 \theta + \cos^2 \theta = 1
>$$
>
>$$
>\tan \theta \cot \theta = 1
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Universal Trigonometric Substitution
>
>The [[Real Sine Function|sine]], [[Real Cosine Function|cosine]], [[Real Tangent Function|tangent]] and [[Real Cotangent Function|cotangent]] of $\theta$ can all be expressed in terms of $\tan \frac{\theta}{2}$:
>
>$$
>\sin \theta = \frac{2\tan \frac{\theta}{2}}{1+\tan^2 \frac{\theta}{2}}
>$$
>
>$$
>\cos \theta = \frac{1 - \tan^2 \frac{\theta}{2}}{1 + \tan^2 \frac{\theta}{2}}
>$$
>
>$$
>\tan \theta = \frac{2\tan \frac{\theta}{2}}{1-\tan^2\frac{\theta}{2}}
>$$
>
>$$
>\cot \theta = \frac{1-\tan^2\frac{\theta}{2}}{2\tan \frac{\theta}{2}}
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

# Angle Sums

>[!THEOREM] Theorem: Trigonometric Identities for Angle Sums
>
>[[Real Sine Function|Sine]], [[Real Cosine Function|cosine]], [[Real Tangent Function|tangent]] and [[Real Cotangent Function|cotangent]] have the following properties:
>
>$$
>\begin{align*}\sin(\theta \pm \varphi) &= \sin\theta\cos\varphi \pm \cos\theta \sin \varphi \\ \\ \cos (\theta \pm \varphi) &= \cos \theta \cos \varphi \mp \sin \theta \varphi \\ \\ \tan (\theta \pm \varphi) &= \frac{\tan \theta \pm \tan \varphi}{1 \mp \tan \theta \tan \varphi} \\ \\ \cot(\theta \pm \varphi) &= \frac{\cot \theta \cot \varphi \mp 1}{\cot \varphi \pm \cot \theta}\end{align*}
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

# Angle Products

>[!THEOREM] Theorem: Chebyshev's Formulas
>
>The [[Real Sine Function|sine]], [[Real Cosine Function|cosine]] and [[Real Tangent Function|tangent]] obey Chebyshev's formulas for every $r \in \mathbb{R}$:
>
>$$
>\begin{align*}\sin(r\varphi) &= 2\cos \varphi \sin ((r-1)\varphi) - \sin ((r-2)\varphi) \\ \\ \cos (r \varphi) &= 2\cos \varphi \cos ((r-1)\varphi) - \cos((r-2)\varphi) \\ \\ \tan(r\varphi) &= \frac{\tan((r-1)\varphi) + \tan \varphi}{1 - \tan \varphi\tan ((r-1)\varphi)} \end{align*}
>$$
>
>>[!PROOF]-
>>
>>TODO
>
>

>[!THEOREM] Theorem: Double-Angle Formulas
>
>The [[Real Sine Function|sine]], [[Real Cosine Function|cosine]], [[Real Tangent Function|tangent]] and [[Real Cotangent Function|cotangent]] of $2\theta$ can be expressed as
>
>
>$$\begin{align*} \sin(2\theta) &= 2\sin \theta \cos \theta \\ \\ \cos(2\theta) &= 2\cos^2\theta + 1 = \cos^2 \theta - \sin^2 \theta = 1-2\sin^2 \theta \\ \\ \tan (2\theta) &= \frac{2\tan \theta}{1-\tan^2 \theta} \end{align*}$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Half-Angle Formulae
>
>The [[Real Sine Function|sine]], [[Real Cosine Function|cosine]], [[Real Tangent Function|tangent]] and [[Real Cotangent Function|cotangent]] obey the following properties:
>
>$$
>\begin{align*}\sin \frac{\theta}{2} &= \operatorname{sgn}\left(\sin \frac{\theta}{2}\right) \sqrt{\frac{1-\cos\theta}{2}} \\ \\ \cos \frac{\theta}{2} &= \operatorname{sgn}\left(\cos \frac{\theta}{2}\right) \sqrt{\frac{1+\cos\theta}{2}} \\ \\ \tan\frac{\theta}{2} &= \frac{\sin \theta}{1+\cos \theta} = \frac{1 - \cos \theta}{\sin \theta} = \operatorname{sgn}(\sin \theta) \sqrt{\frac{1-\cos \theta}{1+\cos \theta}} \\ \\ \cot \frac{\theta}{2} &= \frac{1+\cos \theta}{\sin \theta} = \frac{\sin \theta}{1 - \cos \theta} = \pm \sqrt{\frac{1+\cos \theta}{1-\cos \theta}} \end{align*}
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

# Argument Offsets

>[!THEOREM] Theorem: Trigonometric Identities for Argument Offsets
>
>The [[Real Sine Function|sine]], [[Real Cosine Function|cosine]], [[Real Tangent Function|tangent]] and [[Real Cotangent Function|cotangent]] have the following properties:
>
>||$\frac{\pi}{2}+\theta$|$\frac{\pi}{2}-\theta$|$\pi+\theta$|$\pi-\theta$|$\frac{3\pi}{2} + \theta$|$\frac{3\pi}{2} - \theta$|
>|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
>|$\sin$|$\cos \theta$|$\cos \theta$|$-\sin \theta$|$\sin \theta$|$-\cos \theta$|$-\cos \theta$|
>|$\cos$|$-\sin \theta$|$\sin \theta$|$-\cos \theta$|$-\cos \theta$|$\sin \theta$|$-\sin \theta$|
>|$\tan$|$-\cot \theta$|$\cot \theta$|$\tan \theta$|$-\tan \theta$|$-\cot \theta$|$\cot \theta$|
>|$\cot$|$-\tan \theta$|$\tan \theta$|$\cot \theta$|$-\cot \theta$|$-\tan \theta$|$\tan \theta$|
>
>>[!PROOF]-
>>
>>TODO
>>
>

# Function Sums

>[!THEOREM] Theorem: Trigonometric Identities for Function Sums
>
>[[Real Sine Function|Sine]], [[Real Cosine Function|cosine]], [[Real Tangent Function|tangent]] and [[Real Cotangent Function|cotangent]] have the following properties:
>
>$$
>\begin{align*}\sin \theta \pm \sin \varphi &= 2\sin \frac{\theta \pm \varphi}{2} \cos \frac{\theta \mp \varphi}{2} \\ \\ \cos \theta + \cos \varphi &= 2 \cos \frac{\theta + \varphi}{2} \cos \frac{\theta - \varphi}{2} \\ \\ \cos \theta - \cos \varphi &= -2 \sin \frac{\theta + \varphi}{2} \sin \frac{\theta - \varphi}{2} \\ \\ \tan \theta \pm \tan \varphi &= \frac{\sin(\theta \pm \varphi)}{\cos \theta \cos \varphi} \\ \\ \cot \theta \pm \cot \varphi &= \frac{\sin(\varphi \pm \theta)}{\sin \theta \sin \varphi}\end{align*}
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

# Function Products

>[!THEOREM] Theorem: Trigonometric Identities for Function Products
>
>[[Real Sine Function|Sine]], [[Real Cosine Function|cosine]], [[Real Tangent Function|tangent]] and [[Real Cotangent Function|cotangent]] have the following properties:
>
>$$
>\begin{align*}\cos \theta \cos \varphi &= \frac{1}{2}(\cos(\theta - \varphi) + \cos(\theta + \varphi)) \\ \\ \sin \theta \sin \varphi &= \frac{1}{2}(\cos(\theta - \varphi) - \cos(\theta + \varphi)) \\ \\ \sin \theta \cos \varphi &= \frac{1}{2}(\sin(\theta + \varphi) + \sin(\theta - \varphi)) \\ \\ \cos \theta \sin \varphi &= \frac{1}{2}(\sin(\theta + \varphi) - \sin(\theta - \varphi)) \\ \\ \tan \theta \tan \varphi &= \frac{\cos(\theta - \varphi) - \cos (\theta + \varphi)}{\cos(\theta - \varphi) + \cos (\theta + \varphi)} \\ \\ \tan \theta \cot \varphi &= \frac{\sin(\theta + \varphi) + \sin(\theta - \varphi)}{\sin(\theta + \varphi) - \sin(\theta - \varphi)}\end{align*}
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

# Compositions

>[!THEOREM] Theorem: Functions of Arcfunctions
>
>The [[Composition|compositions]] of [[Real Trigonometric Functions|real inverse trigonometric functions]] inside [[Real Trigonometric Functions]] have the following properties:
>
>$$
>\begin{align*}
>
>&\cos(\arctan (x)) = \frac{1}{\sqrt{1 + x^2}} \\
>
>&\cos(\arcsin(x)) = \frac{1}{\sqrt{1 - x^2}} \\
>
>&\cos\left(\arctan \left( \frac{1}{x} \right) \right) = \frac{|x|}{\sqrt{1 + x^2}}
>
>\end{align*}
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>