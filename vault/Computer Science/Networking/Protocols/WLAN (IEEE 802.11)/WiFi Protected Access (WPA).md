# Introduction

WPA, WPA2, and WPA3 are consecutive versions of the most-widely used WiFi security standard today. All versions support two authentication modes:

- **Personal Mode** - this mode uses a pre-shared key (PSK) for authentication and is commonly referred to as WPA-PSK. This is typically utilised in home and small office networks. The PSK is derived from the WiFi network's password and its SSID, but is actually never sent over the air for security reasons. Instead, it is used for the derivation of other encryption keys.
- **Enterprise Mode** - this mode uses [[Authentication and Association#the-extensible-authentication-protocol-eap|802.1X authentication]] and supports all EAP methods. As the name implies, this authentication mode is typically used in larger enterprise networks.

WPA was developed after WEP was found to be vulnerable. Its encryption and MIC were provided by [[Encryption and Integrity|TKIP]].

It was superseded by WPA2 in 2004 which utilises [[Encryption and Integrity|CCMP]] for encryption and MIC.

WPA3 is the successor to WPA2 introduced in 2018 and uses [[Encryption and Integrity|GCMP]]. Furthermore, it now mandates *Protected Management Frames (PMF)* to protect 802.11 [[index|management frames]] from eavesdropping and forging. Moreover, the 4-way handshake in Personal Mode is protected by *Simultaneous Authentication of Equals (SAE)* and forward secrecy is used to prevent save-now-decrypt-later attacks of frames.