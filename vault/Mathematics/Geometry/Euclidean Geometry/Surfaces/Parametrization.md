---
title: Parametrization
tags:
  - vector-analysis
  - real-analysis
  - analysis
  - euclidean-geometry
  - geometry
  - mathematics
---

# Parametrization

>[!DEFINITION] Definition: Surface Parametrization
>
>Let $\mathcal{S}$ be a [[Surfaces|surface]] in $\mathbb{R}^n$.
>
>A **parametrization** of $\mathcal{S}$ is a [[Continuity of Real Vector Functions|continuous]] [[Functions of the Real Numbers|function]] $\varphi: \mathcal{D} \subseteq \mathbb{R}^2 \to \mathbb{R}^n$ on a [[The Topology of Euclidean Space#Connectedness|connected set]] $\mathcal{D}$ which is [[Injections, Surjections and Bijections|injective]] on $\mathcal{D}$ except possibly at the [[Interior, Boundary and Exterior|boundary]] $\partial \mathcal{D}$ and whose [[Functions|image]] is $\mathcal{S}$.
>

## Equivalence of Parametrizations

>[!DEFINITION] Definition: Reparametrization
>
>Let $\psi: \mathcal{D}_{\psi} \subseteq \mathbb{R}^2 \to \mathbb{R}^n$ and $\phi: \mathcal{D}_{\phi} \subseteq \mathbb{R}^2 \to \mathbb{R}^n$ be [[Surfaces#Parametrizations|parametrizations]] of the same [[surfaces#Surfaces|surface]] $\mathcal{S} \subset \mathbb{R}^n$.
>
>A **reparametrization** between $\psi$ and $\phi$ is a [[Injections, Surjections and Bijections|bijective]] [[Functions of the Real Numbers|function]] $h_{\mathcal{D}_{\psi} \to \mathcal{D}_{\phi}}: \mathcal{D}_{\psi} \to \mathcal{D}_{\phi}$ with [[Injections, Surjections and Bijections|inverse]] $h_{\mathcal{D}_{\phi} \to \mathcal{D}_{\psi}}: \mathcal{D}_{\phi} \to \mathcal{D}_{\psi}$ such that
>
>$$
>\begin{align*}
>\psi(\mathbf{x}) = \phi(h_{\mathcal{D}_{\psi} \to \mathcal{D}_{\phi}}(\mathbf{x})) \qquad \forall \mathbf{x} \in \mathcal{D}_{\psi} \\
>\phi(\mathbf{x}) = \psi(h_{\mathcal{D}_{\phi} \to \mathcal{D}_{\psi}}(\mathbf{x})) \qquad \forall \mathbf{x} \in \mathcal{D}_{\phi}
>\end{align*}
>$$
>
>>[!NOTE]
>>
>>This is the most general definition for reparametrization. However, it is quite common to require that both $h_{I_{\psi} \to I_{\phi}}$ and $h_{I_{\phi} \to I_{\psi}}$ have additional properties such as [[Continuity]], [[Differentiability|continuous differentiability]] or [[Differentiability|smoothness]]. In this case, when we say that a reparametrization has some property, we mean that both $h_{I_{\psi} \to I_{\phi}}$ and $h_{I_{\phi} \to I_{\psi}}$ have this property.
>>
>

>[!DEFINITION] Definition: Equivalence of Parametrizations
>
>Two [[Surfaces#Parametrizations|parametrizations]] of a [[Surfaces#Parametrizations|surface]] $\mathcal{S}$ are **equivalent** if and only if there exists a [[Surfaces#Equivalence of Parametrizations|reparametrization]] between them.
>
>>[!NOTE] Note
>>
>>This is the most general definition of equivalence for parametrizations. However, sometimes we require that such a [[Surfaces#Equivalence of Parametrizations|reparametrization]] also has additional properties such as [[Continuity]], [[Differentiability|continuous differentiability]] or [[Differentiability|smoothness]]. In this case, we say that $\psi$ and $\phi$ are "equivalent up to a PROPERTY reparametrization" such as "equivalent up to a continuous reparametrization" or "equivalent up to a smooth reparametrization".
>>
>