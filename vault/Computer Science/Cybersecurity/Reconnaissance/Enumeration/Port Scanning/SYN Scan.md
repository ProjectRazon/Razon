# SYN Scan

This is the type of scan which nmap defaults to when run with elevated privileges and is also also referred to as a "stealth scan". Nmap sends a `SYN` packet to the target, initiating a TCP connection. The target responds with `SYN ACK`, telling Nmap that the port is accessible. Finally, Nmap terminates the connection before it's finished by issuing an `RST` packet.

![[res/tcp-syn-scan.png]]

![[res/tcp-syn-scan-wireshark.png]]

This type of scan can also be specified using the `-sS` option.

>[!NOTE]
>
>Despite its moniker, a SYN scan is no longer considered "stealthy" and is quite easily detected nowadays.
>
