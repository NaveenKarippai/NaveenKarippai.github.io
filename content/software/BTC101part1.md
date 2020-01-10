Title: Bitcoin 101: Terminology - part 1
Tags: bitcoin, blockchain
Date: 2020-01-10 18:20
HeaderImage: https://i.imgur.com/U0jHPgG.png
HeaderImageCaption: src: pixabay.com
author: Naveen Karippai
Category: Software
Summary: Understanding some common keywords in Bitcoin

### ELI5 Bitcoin

Bitcoin is the first successful implementation of a decentralized digital currency that works without a central bank and can be sent from a user to another user. BTC is the abbreviation for Bitcoin currency similar to USD for the US Dollar. Essentially, you own a Bank in your own pocket when you use Bitcoin. Bitcoin exists only in a digital form unlike the hybrid (physical + digital) form of traditional currencies like USD, EURO.

The Bitcoin network is powered by bitcoin nodes spread across the Earth making it a decentralized currency. Anyone in any part of the Earth could host a Bitcoin node. The Bitcoin transactions are immutable i.e., Bitcoin sent to a user cannot be reverted after a certain number of confirmation blocks. The key advantages of using Bitcoin are its low transaction fees and relatively faster transaction time. There are numerous forks of Bitcoin known as Altcoins. The original Bitcoin software was written by Satoshi Nakamoto and released under the MIT license.


### Terminology 101

1. BTC/Satoshi

    BTC is the abbreviation used to represent Bitcoin similar to USD for the US Dollar. Satoshi is the smallest unit of bitcoin. 1 Satoshi = 10^(-8) Bitcoin. In simple terms, it is similar to what a Cent is for EURO except that the conversion scale is different. As of 2020, Satoshi is used to denote bitcoin transaction fees. The abbreviation for Satoshi is sat, or s.


2. Double-Spending

    To describe the double-spending issue in layman's terms, you cannot create a unique entity in the digital world. For example, if you visit the Van Gogh museum in Amsterdam, you shall see the wonderful paintings by the great artist in its physical form. There may be many replicas in the market but the original ones can be easily identified and are always tagged highly valuable or expensive. This ability to distinguish from a replica does not exist in the digital world. If you have a picture in digital form (imagine the picture was created in digital form), multiple copies of it can be easily made and there is nothing as a unique entity anymore. The original digital picture does not hold a unique value anymore.


3. Bitcoin Improvement Proposal (BIP)

    BIP is a document that is used to introduce features or modifications to Bitcoin. It is supposed to provide concise technical information and rationale behind the proposed feature. You may checkout the bips [here](https://github.com/bitcoin/bips).


4. Altcoins

    Altcoins are derivatives of Bitcoin. The majority of them are forks of Bitcoin with no major changes while some of them implement a different consensus algorithm and many more features on top of the Bitcoin software. For example, Bitcoin uses Proof of Work consensus algorithm while some Altcoins like QTUM use Proof of Stake algorithm. Altcoins also popularised smart contracts and DApps (decentralized applications) that run on the blockchain. Some of the popular Altcoins are Basic Attention Token (BAT) used by Brave web browser and Ethereum blockchain. 


5. Blockchain

    The Bitcoin [whitepaper](https://bitcoin.org/bitcoin.pdf) does not mention the term Blockchain in it. The closest it gets is defining Bitcoin as a chain of blocks that are linked using cryptography. If you are familiar with any Distributed Version Control System like Git, you may find Blockchain to be quite similar. In essence, Blockchain refers to the technology layer of Bitcoin.

    ![Blockchain](https://i.imgur.com/SymUuRx.png)
    {.adjust-width}

    Blockchain. src: Matthäus Wander, CC BY-SA 3.0
    {.caption}


6. Softfork/Hardfork

    A softfork occurs when non-upgraded nodes do not follow a rule followed by upgraded nodes. Nodes are machines that host and validates the bitcoin network. A softfork is backward compatible since old nodes can validate newer blocks.

    A Hardfork is not backward compatible. It requires an upgrade of software by all nodes and if not, there will be a chain split. It will be a permanent divergence and old nodes cannot validate transactions by newer consensus rules.