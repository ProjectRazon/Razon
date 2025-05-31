---
title: Sound and Waveforms
tags:
    - music-production
---

# Introduction

>[!DEFINITION] Definition: Sound
>
>**Sound** is what our brains experience when our ears detect variations in the pressure of the air surrounding us.
>

As air pressure changes, it causes some parts of the inside of the ears to move. These movements are then turned into electric signals which propagate through the neurons inside the brain and are ultimately interpreted as sound.

How do we know that it is the changes which matter and not the pressure itself? Well, If this were not the case, then listening to a song at home would sound completely different from listening to the same song on a mountain peak, since the overall pressure of the air at the top of the mountain is less than the overall pressure of the air in your living room. However, we do not experience any significant difference in practice, indicating that our ears are primarily designed to detect pressure changes and not absolute pressure.

# Waveforms

>[!DEFINITION] Definition: Waveform
>
>The **waveform** of a sound is a graph which illustrates how air pressure varies in time as the sound is playing.
>

![[res/Waveform.png]]

Although possible, it is practically very difficult to provide a graph of how air pressure *itself* varies in time, since doing so requires a lot of knowledge about the internals of the microphone with which the sound was recorded as well some as some external equipment. Besides, what matters for our sound perception are the relative changes in pressure and not its absolute values, so there is no point in displaying pressure itself anyway.

This is why waveforms show a quantity called **amplitude**, instead. The details of what amplitude actually *is* are largely irrelevant to music production and are related to how digital and analog audio signals are recorded. However, amplitude has one crucial property - it is directly proportional to changes in air pressure. This means that the shape of the amplitude's graph is the same as the shape of the graph of the air pressure. Ultimately, amplitude is just a representation of the changes in air pressure.

By convention, an amplitude of $0.0$ is assigned to "ambient pressure", i.e. the pressure under which 

As such, the choice of what pressure corresponds to an amplitude of $-1.0$ and what pressure corresponds to an amplitude of $1.0$ is completely arbitrary. The only important thing is that lower pressure values are assigned lower amplitudes and higher pressure values are assigned higher amplitudes to make visualization more intuitive. Additionally, amplitudes must be assigned in such a way so as to never go above $1.0$ and below $-1.0$.

Another common convention is to assign an amplitude of $-1.0$ to the lowest value to which air pressure drops while the sound is playing and an amplitude of $1.0$ to the highest value to which air pressure rises while the sound is playing. An amplitude of $0.0$ is then assigned to the arithmetic mean of the minimum and the maximum, exactly halfway in-between the two values. This is a very common thing to do when visualizing sounds recorded in isolation. Nevertheless, there are also many cases in which this is not done.

The crucial thing to remember is that the actual pressure values behind the amplitudes are irrelevant, only the changes in the amplitude matter. Therefore, the way we perceive a sound is uniquely determined by the shape of its waveform.

>[!NOTE] Note: Realistic Waveforms
>
>In practice, the waveforms of actual, physical sounds have a much more complex shapes than the simplified illustration above and look more like this:
>
>![[res/Real Waveform.png]]
>
>However, if you zoom in close enough, you will see that it is ultimately the same thing as before.
>
>![[res/Zoomed Real Waveform.png]]
>

## Synthetic Waveforms




