# Table of contents

<p>&nbsp;</p>

1. [Introduction](#Introduction)

    1.1. [Bitcoin structure](#Bitcoin-structure)

    1.2. [Proof of Work vs Proof of Stake](#Proof-of-Work-vs-Proof-of-Stake)

    1.3. [Basic Operations](#Basic-Operations)

    1.4 [Beyond Bitcoin](#Beyond-Bitcoin)



# Introduction

<p>&nbsp;</p>

**Some resources to start gaining knowledge of blockchaon**


- Bitcoin whitepaper - Bitcoin: A Peer-to-Peer Electronic Cash System [Link](https://bitcoin.org/bitcoin.pdf)


- Bitcoin's Academic Pedigree - The concept of cryptocurrencies is built from forgotten ideas in research literature [Link](https://www.pcmag.com/news/blockchain-the-invisible-technology-thats-changing-the-world)


- Blockchain: The Invisible Technology That's Changing the World [Link](https://www.pcmag.com/news/blockchain-the-invisible-technology-thats-changing-the-world)


- What is blockchain technology? What makes it so important? [Link](https://blockgeeks.com/guides/what-is-blockchain-technology/)

<p>&nbsp;</p>

## Bitcoin structure

<p>&nbsp;</p>

- Unspent Transaction Outputs (UTXO) - [Link](https://smithandcrown.com/glossary/unspent-transaction-outputs-utxo/)


<p>&nbsp;</p>

Bitcoin, and many protocols based on it, store data about transactions and user balances in the form of unspent transaction outputs, which are a list of “unspent” Bitcoin amounts that have been sent to a user, but have not yet been sent from him/her. The sum of these outputs is the user’s total balance. On the blockchain, they appear to be a collection of Bitcoin amounts on different addresses, and the role of a wallet is to identify which addresses the user has keys to. Individual Bitcoin are easy to track because they are signed from one person to another. A transaction is valid if one can prove ownership over the actual Bitcoin s/he is trying to send.

This is in contrast to Ethereum’s account model, which stores information about the entire balance associated with a user’s account. Other users send tokens to and from their own accounts. Individual ETH are more difficult to track because they are added and subtracted to user balances. A transaction is valid if one can prove ownership over the account and the account’s balance is high enough to support it.

The UTXO system is like a digital recreation of a cash economy. For example, Alice gives Bob 1 BTC , and the system now recognizes that there is 1 BTC signed to Bob that he has not yet given to anyone else. If Bob already had 1 BTC, then his balance on the blockchain would be 1 BTC + 1 BTC. Bob’s Bitcoin balance is the sum of all Bitcoin signed to him, similar to how all the fiat cash in Bob’s leather wallet is the sum of all fiat cash given to him. If he wants to combine his two separate BTC, he must do so in another transaction, much like he needs to do if combining two $5 bills into a $10 bill.

In contrast, the account model is like a bank account that automatically maintains user balances, similar to how a bank maintains a single balance amidst spending and receiving funds. When Alice gives Bob 1 ETH, the system now recognizes that Bob’s balance has gone up by 1 ETH and Alice’s has gone down. If Bob already had 1 ETH, then his balance on the blockchain would be 2 ETH. He does not need another exchange to combine them in his account.

<p>&nbsp;</p>

<p align="center">
  <img src="https://blockgeeks.com/wp-content/uploads/2016/09/how-mining-bitcoin-works.png.webp" />
</p>

<p>&nbsp;</p>

## Proof of Work vs Proof of Stake

<p>&nbsp;</p>

[More info](https://blockgeeks.com/guides/proof-of-work-vs-proof-of-stake/)

**Proof of work** is a protocol that has the main goal of deterring cyber-attacks such as a distributed denial-of-service attack (DDoS) which has the purpose of exhausting the resources of a computer system by sending multiple fake requests.

The Proof of work concept existed even before bitcoin, but Satoshi Nakamoto applied this technique to his/her – we still don’t know who Nakamoto really is – digital currency revolutionizing the way traditional transactions are set.

In fact, PoW idea was originally published by Cynthia Dwork and Moni Naor back in 1993, but the term “proof of work” was coined by Markus Jakobsson and Ari Juels in a document published in 1999.

But, returning to date, Proof of work is maybe the biggest idea behind the Nakamoto’s bitcoin white paper – published back in 2008 – because it allows trustless and distributed consensus.

<p>&nbsp;</p>

**Proof of stake** will make the consensus mechanism completely virtual. While the overall process remains the same as proof of work (POW), the method of reaching the end goal is entirely different. In POW, the miners solve cryptographically hard puzzles by using their computational resources.

In POS, instead of miners, there are validators. The validators lock up some of their Ether as a stake in the ecosystem. Following that, the validators bet on the blocks that they feel will be added next to the chain. When the block gets added, the validators get a block reward in proportion to their stake.

<p>&nbsp;</p>

##  Basic Operations 

- How does the Blockchain Work? [Link1](https://medium.com/blockchain-review/how-does-the-blockchain-work-for-dummies-explained-simply-9f94d386e093)

<p>&nbsp;</p>

- How does the Blockchain Work? [Link2](https://onezero.medium.com/how-does-the-blockchain-work-98c8cd01d2ae)

<p>&nbsp;</p>

- How Do Bitcoin Nodes Verify Transactions? [Link](https://smartereum.com/8970/how-do-bitcoin-nodes-verify-transactions/)

A Bitcoin nodes run series of checks on a transaction as it arrives before it is verified. Nodes are built to own transaction pools to verify transactions. The conditions for verification can change from time to time. However, they typically fall within the points listed below.

<p>&nbsp;</p>

What Do Bitcoin Nodes Check Before Verifying a Transaction?

1. They check to see if the data structure and the syntax of the transaction are correct.

2. They check to see if the transaction is above 1 MB.

3. They confirm that the outputs and inputs have values are not be more than 21 million or less than 0.

4. They check the locktime to confirm that it is less than the number allowed.

5. They confirm that the unlocking scripts for the inputs are verified against that of the output.

6. They check to see if the transaction size is more than or up to 100 bytes.

7. They reject any transaction when the value is too low for an empty block.

8. They reject the transactions if the input value is not as high as the output value.

9. They confirm that the input value falls within the required range.

10. They make sure that all Coinbase transactions have a maturity of at least 100 confirmations.

11. The output for each input must exit. If it has been spent, the transaction will be rejected.

12. They confirm that the locking script and the standard format match.

13. They confirm that a matching script exists.

14. The Bitcoin nodes make sure that the signatures are not above the signature limit.

15. They verify that the script for unlocking can push numbers onto the stack.

16. They throw any transaction that is missing into the orphan transaction pool.

The Bitcoin nodes ensure that fraudsters do not infiltrate the system by making sure each transaction meets all the requirements before it is verified. Any transaction that doesn’t meet the requirements is rejected.

<p>&nbsp;</p>

## Beyond Bitcoin and Ethereum

<p>&nbsp;</p>

A Gentle Introduction to Blockchain Technology - [Link](https://bitsonblocks.net/2015/09/09/gentle-introduction-blockchain-technology/)


A Gentle Introduction to Ethereum Technology - [Link](https://bitsonblocks.net/2016/10/02/gentle-introduction-ethereum/)

<p align="center">
  <img src="https://i0.wp.com/bitsonblocks.net/wp-content/uploads/2015/09/bitcoin_approach.jpg?resize=555%2C897&ssl=1
" />
</p>

<p>&nbsp;</p>

Client-server
In the office environment, often data is held on servers, and wherever you log in, you can access the data.  The server holds 100% of the data, and the clients trust that the data is definitive.  Most of the internet is client-server where the website is held on the server, and you are the client when you access it.  This is very efficient, and a traditional model in computing.

Peer-to-peer
In peer-to-peer models, it’s more like a gossip network where each peer has 100% of the data (or as close to it as possible), and updates are shared around.  Peer-to-peer is in some ways less efficient than client-server, as data is replicated many times; once per machine, and each change or addition to the data creates a lot of noisy gossip.  However each peer is more independent, and can continue operating to some extent if it loses connectivity to the rest of the network.  Also peer-to-peer networks are more robust, as there is no central server that can be controlled, so closing down peer-to-peer networks is harder.

<p>&nbsp;</p>


## Public and Private

<p>&nbsp;</p>

On Public and Private Blockchains - [Link](https://blog.ethereum.org/2015/08/07/on-public-and-private-blockchains/)

Over the last year the concept of “private blockchains” has become very popular in the broader blockchain technology discussion. Essentially, instead of having a fully public and uncontrolled network and state machine secured by cryptoeconomics (eg. proof of work, proof of stake), it is also possible to create a system where access permissions are more tightly controlled, with rights to modify or even read the blockchain state restricted to a few users, while still maintaining many kinds of partial guarantees of authenticity and decentralization that blockchains provide. Such systems have been a primary focus of interest from financial institutions, and have in part led to a backlash from those who see such developments as either compromising the whole point of decentralization or being a desperate act of dinosaurish middlemen trying to stay relevant (or simply committing the crime of using a blockchain other than Bitcoin). However, for those who are in this fight simply because they want to figure out how to best serve humanity, or even pursue the more modest goal of serving their customers, what are the practical differences between the two styles?

First, what exactly are the options at hand? To summarize, there are generally three categories of blockchain-like database applications:

Public blockchains: a public blockchain is a blockchain that anyone in the world can read, anyone in the world can send transactions to and expect to see them included if they are valid, and anyone in the world can participate in the consensus process - the process for determining what blocks get added to the chain and what the current state is. As a substitute for centralized or quasi-centralized trust, public blockchains are secured by cryptoeconomics - the combination of economic incentives and cryptographic verification using mechanisms such as proof of work or proof of stake, following a general principle that the degree to which someone can have an influence in the consensus process is proportional to the quantity of economic resources that they can bring to bear. These blockchains are generally considered to be "fully decentralized".
Consortium blockchains: a consortium blockchain is a blockchain where the consensus process is controlled by a pre-selected set of nodes; for example, one might imagine a consortium of 15 financial institutions, each of which operates a node and of which 10 must sign every block in order for the block to be valid. The right to read the blockchain may be public, or restricted to the participants, and there are also hybrid routes such as the root hashes of the blocks being public together with an API that allows members of the public to make a limited number of queries and get back cryptographic proofs of some parts of the blockchain state. These blockchains may be considered "partially decentralized".
Fully private blockchains: a fully private blockchain is a blockchain where write permissions are kept centralized to one organization. Read permissions may be public or restricted to an arbitrary extent. Likely applications include database management, auditing, etc internal to a single company, and so public readability may not be necessary in many cases at all, though in other cases public auditability is desired.

<p>&nbsp;</p>

## What is Cryptocurrency?

Link to article [Link](https://blockgeeks.com/guides/what-is-cryptocurrency/)

Cryptocurrency is an internet-based medium of exchange which uses cryptographical functions to conduct financial transactions. Cryptocurrencies leverage blockchain technology to gain decentralization, transparency, and immutability.

The most important feature of a cryptocurrency is that it is not controlled by any central authority: the decentralized nature of the blockchain makes cryptocurrencies theoretically immune to the old ways of government control and interference.
Cryptocurrencies can be sent directly between two parties via the use of private and public keys.  

These transfers can be done with minimal processing fees, allowing users to avoid the steep fees charged by traditional financial institutions.
Today cryptocurrencies (Buy Crypto) have become a global phenomenon known to most people. In this guide, we are going to tell you all that you need to know about cryptocurrencies and the sheer that they can bring into the global economic system.


<p>&nbsp;</p>

Blockchain and Cryptocurrency
The transaction is known almost immediately by the whole network. But only after a specific amount of time it gets confirmed.

Confirmation is a critical concept in cryptocurrencies. You could say that cryptocurrencies are all about confirmation.

As long as a transaction is unconfirmed, it is pending and can be forged. When a transaction is confirmed, it is set in stone. It is no longer forgeable, it can‘t be reversed, it is part of an immutable record of historical transactions: of the so-called blockchain.

Only miners can confirm transactions. This is their job in a cryptocurrency-network. They take transactions, stamp them as legit and spread them in the network. After a transaction is confirmed by a miner, every node has to add it to its database. It has become part of the blockchain.

For this job, the miners get rewarded with a token of the cryptocurrency, for example with Bitcoins. Since the miner‘s activity is the single most important part of the cryptocurrency-system we should stay for a moment and take a deeper look at it.