Title: Virtual Private Network (VPN) 
Tags: networking, VPN
Date: 2020-01-19 13:47
HeaderImage: https://i.imgur.com/26WYkG5.jpg
HeaderImageCaption: src: pixabay.com
author: Naveen Karippai
Category: Software
Summary: What is a Virtual Private Network (VPN)?

### ELI5 Virtual Private Network (VPN)

A Virtual Private Network (VPN) extends a private network across a public network and enables users to send and receive data across a public network as if their devices are connected to the private network.

Let's try to understand this with a simple example. You live in California and have a Netflix subscription. Netflix offers different content to its users depending on the geographical location due to distribution rights in respective countries. So, you are on a business trip to Amsterdam and would like to watch the latest season of your favorite TV series on Netflix. You logon to Netflix to discover that due to a different location, you do not have access to your favorite TV series from Amsterdam, what a bummer! A VPN will save you in this situation. You could connect to your local network in California through a VPN tunnel connect to Netflix and get access to your favorite TV series. So, from Netflix's point of view, you appear to be located in California while your real location is Amsterdam.

![VPN Client-to-Site](https://i.imgur.com/3pFD7Uf.png)
{.adjust-width}

VPN Client-to-Site. Created with draw.io
{.caption}

You need to have a VPN Server or VPN Concentrator running on the local network you are trying to connect. To make a VPN tunnel, you need to use a VPN Client as an endpoint. As far as I know, you cannot randomly choose a VPN client but select the one that matches your VPN Server. The reason behind this is that there are different VPN types, Authentication protocols used on VPN. A VPN tunnel need not to be encrypted inherently.


### VPN Server

If you are running a Linux-based firmware like [dd-wrt](https://wiki.dd-wrt.com/wiki/index.php/Main_Page) or open-wrt on your access point or wireless router, you could install a VPN Server on your Router. There are also many third-party VPN services on the internet. The choice depends on your use case. 


### VPN data packets

The VPN Client encapsulates the data packets with a new set of VPN frames (last two frames on the right side of the packet). 

![VPN data packets](https://i.imgur.com/DYkOi6s.png)
{.adjust-width}

VPN data packets. Created with draw.io
{.caption}

Back to the above example with Netflix, the source private IP address on the data packet is the private IP address of your local network in Amsterdam. Source public IP address on the data packet is the public address from NAT (Network Address Translation) Router in Amsterdam. The destination public IP address points to the Home Router (VPN server). The process of encapsulating the data packets with VPN frames is known as tunneling. The VPN tunnel does not have to be encrypted inherently. The source public address on the data packet is used to receive data back from the VPN server.