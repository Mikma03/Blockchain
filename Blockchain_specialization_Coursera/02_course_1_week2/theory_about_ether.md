# Table of contents

<p>&nbsp;</p>

1. [Smart Contracts](#Smart-Contracts)

    1.1. [Bitcoin structure](#Bitcoin-structure)

<p>&nbsp;</p>

# Smart Contracts

## What is Ethereum

> [More info](https://ethdocs.org/en/latest/introduction/what-is-ethereum.html)

Ethereum is an open blockchain platform that lets anyone build and use decentralized applications that run on blockchain technology. Like Bitcoin, no one controls or owns Ethereum – it is an open-source project built by many people around the world. But unlike the Bitcoin protocol, Ethereum was designed to be adaptable and flexible. It is easy to create new applications on the Ethereum platform, and with the Homestead release, it is now safe for anyone to use those applications.

<p>&nbsp;</p>

## A next generation blockchain

<p>&nbsp;</p>

Blockchain technology is the technological basis of Bitcoin, first described by its mysterious author Satoshi Nakamoto in his white paper “Bitcoin: A Peer-to-Peer Electronic Cash System”, published in 2008. While the use of blockchains for more general uses was already discussed in the original paper, it was not until a few years later that blockchain technology emerged as a generic term. A blockchain is a distributed computing architecture where every network node executes and records the same transactions, which are grouped into blocks. Only one block can be added at a time, and every block contains a mathematical proof that verifies that it follows in sequence from the previous block. In this way, the blockchain’s “distributed database” is kept in consensus across the whole network. Individual user interactions with the ledger (transactions) are secured by strong cryptography. Nodes that maintain and verify the network are incentivized by mathematically enforced economic incentives coded into the protocol.

In Bitcoin’s case the distributed database is conceived of as a table of account balances, a ledger, and transactions are transfers of the bitcoin token to facilitate trustless finance between individuals. But as bitcoin began attracting greater attention from developers and technologists, novel projects began to use the bitcoin network for purposes other than transfers of value tokens. Many of these took the form of “alt coins” - separate blockchains with cryptocurrencies of their own which improved on the original bitcoin protocol to add new features or capabilities. In late 2013, Ethereum’s inventor Vitalik Buterin proposed that a single blockchain with the capability to be reprogrammed to perform any arbitrarily complex computation could subsume these many other projects.

In 2014, Ethereum founders Vitalik Buterin, Gavin Wood and Jeffrey Wilcke began work on a next-generation blockchain that had the ambitions to implement a general, fully trustless smart contract platform.

<p>&nbsp;</p>

## Ethereum Virtual Machine

<p>&nbsp;</p>

Ethereum is a programmable blockchain. Rather than give users a set of pre-defined operations (e.g. bitcoin transactions), Ethereum allows users to create their own operations of any complexity they wish. In this way, it serves as a platform for many different types of decentralized blockchain applications, including but not limited to cryptocurrencies.

Ethereum in the narrow sense refers to a suite of protocols that define a platform for decentralised applications. At the heart of it is the Ethereum Virtual Machine (“EVM”), which can execute code of arbitrary algorithmic complexity. In computer science terms, Ethereum is “Turing complete”. Developers can create applications that run on the EVM using friendly programming languages modelled on existing languages like JavaScript and Python.

<p>&nbsp;</p>

## Smart conctracts

<p>&nbsp;</p>

>[More info](https://blockgeeks.com/guides/smart-contracts/)

<p>&nbsp;</p>

A smart contract is a computer protocol intended to digitally facilitate, verify, or enforce the negotiation or performance of a contract. Smart contracts allow the performance of credible transactions without third parties.

One of the best things about the blockchain is that, because it is a decentralized system that exists between all permitted parties, there’s no need to pay intermediaries (Middlemen) and it saves you time and conflict. Blockchains have their problems, but they are rated, undeniably, faster, cheaper, and more secure than traditional systems, which is why banks and governments are turning to them.


Smart contracts help you exchange money, property, shares, or anything of value in a transparent, conflict-free way while avoiding the services of a middleman.

The best way to describe smart contracts is to compare the technology to a vending machine. Ordinarily, you would go to a lawyer or a notary, pay them, and wait while you get the document. With smart contracts, you simply drop a bitcoin into the vending machine (i.e. ledger), and your escrow, driver’s license, or whatever drops into your account. More so, smart contracts not only define the rules and penalties around an agreement in the same way that a traditional contract does, but also automatically enforce those obligations. If you are looking for a more detailed walkthrough of smart contracts please check out our blockchain courses on smart contracts.

<p>&nbsp;</p>

**Autonomy** – You’re the one making the agreement; there’s no need to rely on a broker, lawyer or other intermediaries to confirm. Incidentally, this also knocks out the danger of manipulation by a third party, since execution is managed automatically by the network, rather than by one or more, possibly biased, individuals who may err.

**Trust** – Your documents are encrypted on a shared ledger.  There’s no way that someone can say they lost it.

**Backup** – Imagine if your bank lost your savings account. On the blockchain, each and every one of your friends have your back. Your documents are duplicated many times over.

**Safety** – Cryptography, the encryption of websites, keeps your documents safe. There is no hacking. In fact, it would take an abnormally smart hacker to crack the code and infiltrate.

**Speed** – You’d ordinarily have to spend chunks of time and paperwork to manually process documents. Smart contracts use software code to automate tasks, thereby shaving hours off a range of business processes.

**Savings** – Smart contracts save you money since they knock out the presence of an intermediary. You would, for instance, have to pay a notary to witness your transaction.

**Accuracy** – Automated contracts are not only faster and cheaper but also avoid the errors that come from manually filling out heaps of forms.

<p>&nbsp;</p>

## Official docs for smart conctracts

<p>&nbsp;</p>

>[Link to doc](https://docs.soliditylang.org/en/develop/introduction-to-smart-contracts.html)

<p>&nbsp;</p>

# Ethereum Structure

<p>&nbsp;</p>

>[Ethereum Whitepaper](https://ethereum.org/en/whitepaper/)

<p>&nbsp;</p>

>[Tutorials](https://ethereum.org/en/developers/tutorials/)

<p>&nbsp;</p>

# Account Management


<p>&nbsp;</p>

## Accounts

Accounts play a central role in Ethereum. There are two types of accounts: externally owned accounts (EOAs) and contract accounts. Here we focus on externally owned accounts, which will be referred to simply as accounts. Contract accounts will be referred to as contracts and are discussed in detail in Contracts. This generic notion of account subsuming both externally owned accounts and contracts is justified in that these entities are so called state objects. These entities have a state: accounts have balance and contracts have both balance and contract storage. The state of all accounts is the state of the Ethereum network which is updated with every block and which the network really needs to reach a consensus about. Accounts are essential for users to interact with the Ethereum blockchain via transactions.

If we restrict Ethereum to only externally owned accounts and allow only transactions between them, we arrive at an “altcoin” system that is less powerful than bitcoin itself and can only be used to transfer ether.

Accounts represent identities of external agents (e.g., human personas, mining nodes or automated agents). Accounts use public key cryptography to sign transaction so that the EVM can securely validate the identity of a transaction sender.


To provide Ethereum integration for your native applications, the very first thing you should be interested in doing is account management.

Although all current leading Ethereum implementations provide account management built in, it is ill advised to keep accounts in any location that is shared between multiple applications and/or multiple people. The same way you do not entrust your ISP (who is after all your gateway into the internet) with your login credentials; you should not entrust an Ethereum node (who is your gateway into the Ethereum network) with your credentials either.

The proper way to handle user accounts in your native applications is to do client side account management, everything self-contained within your own application. This way you can ensure as fine grained (or as coarse) access permissions to the sensitive data as deemed necessary, without relying on any third party application’s functionality and/or vulnerabilities.

To support this, go-ethereum provides a simple, yet thorough accounts package that gives you all the tools to do properly secured account management via encrypted keystores and passphrase protected accounts. You can leverage all the security of the go-ethereum crypto implementation while at the same time running everything in your own application.

There are a few different ways one can authorize the account manager to execute signing operations, each having its advantages and drawbacks. Since the different methods have wildly different security guarantees, it is essential to be clear on how each works:

- Single authorization: The simplest way to sign a transaction via the account manager is to provide the passphrase of the account every time something needs to be signed, which will ephemerally decrypt the private key, execute the signing operation and immediately throw away the decrypted key. The drawbacks are that the passphrase needs to be queried from the user every time, which can become annoying if done frequently; or the application needs to keep the passphrase in memory, which can have security consequences if not done properly; and depending on the keystore’s configured strength, constantly decrypting keys can result in non-negligible resource requirements.

- Multiple authorizations: A more complex way of signing transactions via the account manager is to unlock the account via its passphrase once, and allow the account manager to cache the decrypted private key, enabling all subsequent signing requests to complete without the passphrase. The lifetime of the cached private key may be managed manually (by explicitly locking the account back up) or automatically (by providing a timeout during unlock). This mechanism is useful for scenarios where the user may need to sign many transactions or the application would need to do so without requiring user input. The crucial aspect to remember is that anyone with access to the account manager can sign transactions while a particular account is unlocked (e.g. application running untrusted code).
<p>&nbsp;</p>

## Keyfiles

<p>&nbsp;</p>

Every account is defined by a pair of keys, a private key and public key. Accounts are indexed by their address which is derived from the public key by taking the last 20 bytes. Every private key/address pair is encoded in a keyfile. Keyfiles are JSON text files which you can open and view in any text editor. The critical component of the keyfile, your account’s private key, is always encrypted, and it is encrypted with the password you enter when you create the account. Keyfiles are found in the keystore subdirectory of your Ethereum node’s data directory. Make sure you backup your keyfiles regularly! See the section Backup and restore accounts for more information.

Creating a key is tantamount to creating an account.

You don’t need to tell anybody else you’re doing it
You don’t need to synchronize with the blockchain
You don’t need to run a client
You don’t even need to be connected to the internet
Of course your new account will not contain any Ether. But it’ll be yours and you can be certain that without your key and your password, nobody else can ever access it.

It is safe to transfer the entire directory or any individual keyfile between Ethereum nodes.

<p>&nbsp;</p>

# Ethereum Operations

<p>&nbsp;</p>

## Gas fee

<p>&nbsp;</p>

>[Info about gas](https://ethereum.stackexchange.com/questions/3/what-is-meant-by-the-term-gas?newreg=3ba3934e1c6547a789bf7cba9884c76e)

<p>&nbsp;</p>

"Gas" is the name for a special unit used in Ethereum. It measures how much "work" an action or set of actions takes to perform: for example, to calculate one Keccak256 cryptographic hash it will take 30 gas each time a hash is calculated, plus a cost of 6 more gas for every 256 bits of data being hashed. Every operation that can be performed by a transaction or contract on the Ethereum platform costs a certain number of gas, with operations that require more computational resources costing more gas than operations that require few computational resources.

The reason gas is important is that it helps to ensure an appropriate fee is being paid by transactions submitted to the network. By requiring that a transaction pay for each operation it performs (or causes a contract to perform), we ensure that network doesn't become bogged down with performing a lot of intensive work that isn't valuable to anyone. This is a different strategy than the Bitcoin transaction fee, which is based only on the size in kilobytes of a transaction. Since Ethereum allows arbitrarily complex computer code to be run, a short length of code can actually result in a lot of computational work being done. So it's important to measure the work done directly instead of just choosing a fee based on the length of a transaction or contract.

So if gas is basically a transaction fee, how do you pay it? This is where it gets a little tricky. Although gas is a unit that things can be measured in, there isn't any actual token for gas. That is, you can't own 1000 gas. Instead, gas exists only inside of the Ethereum virtual machine as a count of how much work is being performed. When it comes to actually paying for the gas, the transaction fee is charged as a certain number of ether, the built-in token on the Ethereum network and the token with which miners are rewarded for producing blocks.

This might seem odd at first. Why don't operations just have a cost measured in ether directly? The answer is that ether, like bitcoins, have a market price that can change rapidly! But the cost of computation doesn't go up or down just because the price of ether changes. So it's helpful to separate out the price of computation from the price of the ether token, so that the cost of an operation doesn't have to be changed every time the market moves.

The terminology here gets a little messy. Operations in the EVM have gas cost, but gas itself also has a gas price measured in terms of ether. Every transaction specifies the gas price it is willing to pay in ether for each unit of gas, allowing the market to decide the relationship between the price of ether and the cost of computing operations (as measured in gas). It's the combination of the two, total gas used multiplied by gas price paid, that results in the total fee paid by a transaction.

As tricky as it is, it's important to understand this distinction, because it results in one of the most confusing things about Ethereum transactions to the initial learner: there is a difference between your transaction running out of gas and your transaction not having a high enough fee. If the gas price I set in my transaction is too low, no one will even bother to run my transaction in the first place. It will simply not be included in the blockchain by miners. But if I provide an acceptable gas price, and then my transaction results in so much computational work that the combined gas costs go past the amount I attached as a fee, that gas counts as "spent" and I don't get it back. The miner will stop processing the transaction, revert any changes it made, but still include it in the blockchain as a "failed transaction", collecting the fees for it. This may seem harsh, but when you realise that the real work for the miner was in performing the computation, you can see that they will never get those resources back either. So it's only fair that you pay them for the work they did, even though your badly designed transaction ran out of gas.

<p>&nbsp;</p>

Providing too big of a fee is also different than providing too much ether. If you set a very high gas price, you will end up paying lots of ether for only a few operations, just like setting a super high transaction fee in bitcoin. You'll definitely be prioritised to the front of the line, but your money is gone. If you provided a normal gas price, however, and just attached more ether than was needed to pay for the gas that your transaction consumed, the excess amount will be refunded back to you. Miners only charge you for the work that they actually do. You can think of the gas price as the hourly wage for the miner, and the gas cost as their timesheet of work performed.

There are a lot of other subtleties to gas, but that should give you the basics! Gas is the key mechanism that makes the complex computations in Ethereum "safe" for the network to work on, because any programs that run out of control will only last as long as the money provided by the people who requested they be run. When the money stops, the miners stop working on it. And the mistakes you make in your program will only affect the people who pay to use it--the rest of the network can't suffer performance issues due to your error. They will simply get a big payday when the performance issues consume all of your ether! Without this critical technique, the idea of a general-purpose blockchain would have been completely impossible.

tl;dr:

- Gas is the way that fees are calculated

- The fees are still paid in ether, though, which is different from gas

- The gas cost is the amount of work that goes into something, like the number of hours of labour, whereas the gas price is like the hourly wage you pay for the work to be done. The combination of the two determines your total transaction fee.

- If your gas price is too low, no one will process your transaction

- If your gas price is fine but the gas cost of your transaction runs "over budget" the transaction fails but still goes into the blockchain, and you don't get the money back for the work that the labourers did.

- This makes sure that nothing runs forever, and that people will be careful about the code that they run. It keeps both miners and users safe from bad code!

<p>&nbsp;</p>

Short:

Gas is the execution fee for every operation made on ethereum. Its price is expressed in ether and it's decided by the miners, which can refuse to process transaction with less than a certain gas price. To get gas you simply need to add ether to your account.

Long:

Ethereum implements on the blockchain an execution environment called the Ethereum Virtual Machine (EVM). When you are running a decentralized application (dApp), every instruction is executed on every node of the network. This has a cost: for every operation that a script can execute there is a specified cost, expressed in number of gas units, that you can see in the EVM specification.

The price of one unit of gas is decided by the miners, currently it is around 5 to 21 GWei (One GWei is 10^9 Wei or 10^-9 Ether). Ethereum uses ether as its internal currency/token. Your accounts holding are expressed in ether. When you deploy a contract, or execute a transaction the gas will be taken from your account balance. You are free to specify a gasprice, or keep the suggest one.

<p>&nbsp;</p>

# Incentive Model

<p>&nbsp;</p>

>[Ether - basic info](https://ethereum.org/en/eth/)


<p>&nbsp;</p>

>[Proof of work and stake](https://blockgeeks.com/guides/proof-of-work-vs-proof-of-stake/)

