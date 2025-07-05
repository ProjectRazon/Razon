---
title: Text-Based Interfaces
tags:
    - linux
    - computer-science
---

# Introduction

The primary way of interacting with [[./index|Linux]] systems is via text. At a most abstract level what happens is quite simple: you input text, the computer processes it and outputs text back. However, this process actually goes through several different stages from beginning to end:

![[res/Text-Based Interface.svg]]

First, you type text on your keyboard. This text is taken by a [[Text-Based Interfaces#Terminals|terminal]] and is then forwarded to the underlying [[Text-Based Interfaces#Teletypewriters (TTYs) and Pseudo-Terminals (PTYs)|TTY / PTY]] without any modifications. The [[Text-Based Interfaces#Teletypewriters (TTYs) and Pseudo-Terminals (PTYs)|TTY / PTY]] receives the text from the terminal and may potentially modify it, if configured to do so. The result is forwarded to a [[Text-Based Interfaces#Shells|shell]]. The shell [[Text-Based Interfaces#Shells|shell]] looks at the text, interprets it and performs actions based on it. The most common thing for the [[Text-Based Interfaces#Shells|shell]] to do is to launch some program specified by your text, but most [[Text-Based Interfaces#Shells|shells]] have other capabilities as well. 

The same process happens in reverse with the program's output: the [[Text-Based Interfaces#Shells|shell]] receives text from the program and then forwards it to the [[Text-Based Interfaces#TTYs and PTYs|TTY / PTY]] which ultimately sends the text to the [[Text-Based Interfaces#Terminals|terminal]] to be displayed to you.

# Terminals

Historically, a **terminal** was a hardware device comprised of a keyboard and a screen that was connected to a computer (back in the days when computers were rather large). Terminals were used to send input to the computer and to display the output received from it. They were "dumb" in the sense that they could not actually perform any operations on their own. The sole purpose of a terminal was to take in what the user types on the keyboard, forward it to the computer and then display whatever the computer returned.

Nowadays, hardware terminals are pretty much extinct. Instead, we use software known as **terminal emulators**. There are many different terminal emulators such as [Konsole](https://konsole.kde.org/), [Alacritty](https://alacritty.org/), [xterm](https://invisible-island.net/xterm/xterm.html), etc. A terminal emulator does more or less the exact same thing as a terminal did - it takes user input, forwards it to the computer and display the computer's output. The main purpose of terminal emulators is to take your text input and forward it to the underlying [[Text-Based Interfaces#TTYs and PTYs|PTY]]. However, since a terminal emulators is a piece of software and is thus capable of much more than hardware terminals were, it usually has additional responsibilities such as actually creating the [[Text-Based Interfaces#TTYs and PTYs|PTY]] when the emulator is launched and handling window resizing.

>[!NOTE] Note: Terminal vs Terminal Emulator
>
>Since physical terminals are no longer a thing, people usually use the term "terminal" to refer to a terminal emulator.
>


# TTYs and PTYs

Historically, a teletypewriter (TTY) was a type of [[Text-Based Interfaces#Terminals|physical terminal]]. Nowadays, however, a **TTY** is a component of the kernel responsible for handling the communication between [[Text-Based Interfaces#Terminals|terminals]] and [[Text-Based Interfaces#Terminals|shells]]. 

# Shells

A **shell** is a program which 

is a text-based program for interacting with the [[./index|operating system]]. It allows you to enter commands which do something and then potentially return a result back to you, which the shell displays. 

A typical shell looks like the following:

![[res/Shell.png]]

The color