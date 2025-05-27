# Introduction

The ARP protocol can also be used to find the IP address of a device when only knowing its MAC address. 

>[!NOTE] Note: RARP
>
>When ARP is utilised to find an IP address, it is called RARP for "reverse ARP".
>

This is a common situation in the so-called "bootstrapping", or starting from zero. In such cases a device X may not know its own IP address, but know its MAC address, since it is embedded in the hardware. But who knows X's IP address if not X itself?

The answer is a RARP server. The RARP server listens for RARP broadcasts and responds to them with the appropriate IP address.

# Reverse Address Resolution
The process for reverse address resolution avails itself of the same ARP protocol and the terminology remains the same, except that the source and the destination may now be the exact same device.

1. *The source device generates a RARP request message:* This is done by using the value 3 for the [[ARP Message Format|Opcode]] of the request. It populates the [[ARP Message Format|Sender Hardware Address]] and [[ARP Message Format|Target Hardware Address]] with its own MAC address, but leaves the [[ARP Message Format|Sender Protocol Address]] and [[ARP Message Format|Target Protocol Address]], since they are unknown.
2. *The source device broadcasts the RARP request on the network:* All devices which are not a RARP server simply ignore the broadcast.
3. *RARP server receives the RARP request and generates a RARP response:* Any device set up as a RARP server will process the broadcasted request and generate an appropriate response. The Opcode for a RARP response is the value 4. The RARP server sets the Sender Hardware Address and Sender Protocol Address to its own MAC and IP address, respectively, and populates the Target Hardware Address with the MAC address which it obtained from the request. Ultimately, it looks up this MAC address in a table in order to determine the corresponding IP address which it then places in the Target Protocol Address field.
4. *RARP server sends the RARP response back to the source:* Note that there is no need to broadcast the response.
5. *The source device receives the RARP response:* The source device may receive multiple responses if multiple RARP servers are configured. In this case, it usually uses the first response, whilst ignoring the rest. The source determines its own IP address from the Target Protocol Address in the response.

![[res/Reverse Address Resolution.svg]]