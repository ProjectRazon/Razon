# Introduction

The **Hypertext Transfer Protocol (HTTP)** is the modern Internet's courier. It is responsible for the delivery of vast amounts and different types of data online such as web pages, images, video, audio and more. 

# Architecture Overview

HTTP is based on a client-server architecture. A **client** is anyone who requests a **resource** from a web **server**.

>[!EXAMPLE]
>
>An example is you (the client) watching a cat video (the resource) on YouTube (the server).
>

The communication between the client and the server is actuated by the so-called **transactions**. Each transaction consists of a [[index|request]], sent by the client to the server, and a [[index|response]], sent back by the server to the client. Generally, a request describes what action the client wants the server to perform and the response contains information about the outcome of the action. 

>[!EXAMPLE]
>
>The client could request a specific web page from the web server, or they could try to upload a file to it. The server would then respond with information about whether or not the action was successful and any accompanying data.
>

>[!DEFINITION]
>
>Requests and responses are collectively known as **messages**.
>
