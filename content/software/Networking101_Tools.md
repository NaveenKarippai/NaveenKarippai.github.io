Title: Networking 101: Analysis Tools
Tags: networking, debug
Date: 2020-01-11 17:27
HeaderImage: https://i.imgur.com/NDzQYpa.jpg
HeaderImageCaption: src: pixabay.com
author: Naveen Karippai
Category: Software
Summary: Tools used for troubleshooting computer networks

## Home Network

A typical home network has many clients (laptops, desktop, tablets, mobile phones, smart things) connected to it. All of these clients connect to a Home Router either via a Wireless (WLAN) or a Wired connection depending on the availability of hardware ports on clients and the ease of usage. A modern home router has a built-in Switch and also features an integrated Modem. The basic difference between a Router and Switch is that Router filters data packets based on IP address while a Switch filters packets based on its MAC address. So, if you need to communicate with a network outside your home network, you need a Router. A modem modulates/demodulates signals depending on the carrier medium.


![Networking 101](https://i.imgur.com/0yCPMJq.png)
{.adjust-width}

Data packets movement from home network to the internet. Created with draw.io
{.caption}

Let's look at the high-level overview of the journey of data packets from its source to the destination. You open the Chrome web browser on your desktop and open yellowelephant.xyz website. Network Interface Card on your desktop sends the data packets to Router via WLAN. The router realizes that the IP address of destination is outside your home network by using subnet mask and destination IP address. The integrated modem in your router device sends the data as a signal to your Internet Service Provider (ISP). There is more happening before transmitting data packets to ISP such as Network Address Translation (NAT) but this is not relevant in this context. Your ISP uses the Border Gateway Protocol (BGP) to transmit data packets to a network of other routers and subsequently to the ISP of destination address. The destination ISP then forwards the packets to the destination router and server.

The gist behind this micro article is to show the most commonly used tools for troubleshooting networking issues. Let's look at the tools by scenarios where it could be useful.


## netstat

[netstat](https://en.wikipedia.org/wiki/Netstat) stands for Network statistics. It analyses the active Network Interface card for network connections and can also show the routing table. 

> $ netstat

*Scenario*: You have started a local web server for a DIY weekend project and later the same day, you are not sure if the webserver was killed or not. You could do a netstat on your machine where you started the webserver and filter for the port number (standard port = 80). You may be thinking why not open a web browser and go to http://localhost:80 but the point is to give you an eli5 example. You can also find other ghost processes or spy network connections with netstat utility.


## wireshark/tcpdump

[wireshark](https://en.wikipedia.org/wiki/Wireshark) is a packet analyzer and it allows you to analyze the payload and headers of data packets using Wireshark. The analyzed data packets can be at different levels of the OSI Networking model or TCP/IP model.

> $ wireshark

*Scenario*: Imagine you have an FTP server (unencrypted connection) at home network and you are not able to login with your FTP client. The best approach would be to analyze packets received on the FTP server. You should be able to view the headers and transmitted payload. This may help to narrow down the failure. 

tcmpdump is an alternative tool to Wireshark (cross-platform) and offers similar functionality in the UNIX-like world. The good thing about wireshark is that GUI does some log formatting and makes it easy to analyze logs for a human.


## ping

[ping](https://en.wikipedia.org/wiki/Ping_(networking_utility)) is a network admin tool that is used to test the reachability of a host on an IP network.

> $ ping -c 5 www.example.com

ping utility transmits ICMP packets and not TCP/UDP. 

*Scenario*: Your web browser shows that no websites are accessible. It could be an issue with the DNS server that you have assigned to your host. To test if your network is up and connected to the outside world, run the following on your terminal

> $ ping 8.8.8.8

8.8.8.8 is google's DNS server and if you are receiving back packets, the issue is with the DNS server you are using. I would assign an alternative fallback DNS to avoid this failure in the future.


## traceroute

[traceroute](https://en.wikipedia.org/wiki/Traceroute) is a packet route analyzer. It tells you the path traveled by the packet across the internet to your destination host.

> $ traceroute yellowelephant.xyz

The above command will tell you the route traveled by data packets to reach the website.

*Scenario*: Imagine the network cable between your router and ISP is exposed on the streets and there was an accident last day that resulted in the breakage of this cable. You come home and realize that you are not able to connect to the internet. You don't know where the problem is. traceroute utility could come to rescue in this situation. You can observe that packets are transmitted from your client device to the router (Gateway server) but the next-hop fails. So, you can narrow down where the point of failure is and report it to your ISP or relevant authority.