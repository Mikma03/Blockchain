# Table of contents

<p>&nbsp;</p>

1. [Public-key](#Public-key)


<p>&nbsp;</p>

# Public-key

<p>&nbsp;</p>

>[Link](https://www.globalsign.com/en/ssl-information-center/what-is-public-key-cryptography)


<p>&nbsp;</p>



 Public-key cryptography, or asymmetric cryptography, is an encryption scheme that uses two mathematically related, but not identical, keys - a public key and a private key. Unlike symmetric key algorithms that rely on one key to both encrypt and decrypt, each key performs a unique function. The public key is used to encrypt and the private key is used to decrypt.

It is computationally infeasible to compute the private key based on the public key. Because of this, public keys can be freely shared, allowing users an easy and convenient method for encrypting content and verifying digital signatures, and private keys can be kept secret, ensuring only the owners of the private keys can decrypt content and create digital signatures.

Since public keys need to be shared but are too big to be easily remembered, they are stored on digital certificates for secure transport and sharing. Since private keys are not shared, they are simply stored in the software or operating system you use, or on hardware (e.g., USB token, hardware security module) containing drivers that allow it to be used with your software or operating system.

<p>&nbsp;</p>

**Security Benefits of Encryption**

Assuming the individual’s private key has not been compromised, encrypting data and messages offers the following security benefits.

Confidentiality - because the content is encrypted with an individual’s public key, it can only be decrypted with the individual’s private key, ensuring only the intended recipient can decrypt and view the contents/li>
Integrity - part of the decryption process involves verifying that the contents of the original encrypted message and the new decrypted match, so even the slightest change to the original content would cause the decryption process to fail
<p>&nbsp;</p>

> [Asymmetric Encryption - Simply explained](https://www.youtube.com/watch?v=AQDCe585Lnc&ab_channel=SimplyExplained)

<p>&nbsp;</p>
Asymmetric cryptography, also known as public-key cryptography, is a process that uses a pair of related keys -- one public key and one private key -- to encrypt and decrypt a message and protect it from unauthorized access or use.

A public key is a cryptographic key that can be used by any person to encrypt a message so that it can only be decrypted by the intended recipient with their private key. A private key -- also known as a secret key -- is shared only with key's initiator.

When someone wants to send an encrypted message, they can pull the intended recipient's public key from a public directory and use it to encrypt the message before sending it. The recipient of the message can then decrypt the message using their related private key.

If the sender encrypts the message using their private key, the message can be decrypted only using that sender's public key, thus authenticating the sender. These encryption and decryption processes happen automatically; users do not need to physically lock and unlock the message.

Many protocols rely on asymmetric cryptography, including the transport layer security (TLS) and secure sockets layer (SSL) protocols, which make HTTPS possible.

The encryption process is also used in software programs that need to establish a secure connection over an insecure network, such as browsers over the internet, or that need to validate a digital signature.

Increased data security is the primary benefit of asymmetric cryptography. It is the most secure encryption process because users are never required to reveal or share their private keys, thus decreasing the chances of a cybercriminal discovering a user's private key during transmission.

<p>&nbsp;</p>

> [Public Key Cryptography](https://www.youtube.com/watch?v=GSIDS_lvRv4&ab_channel=Computerphile)

<p>&nbsp;</p>


>[Elliptic Curve Cryptography: A Basic Introduction](https://qvault.io/cryptography/elliptic-curve-cryptography/)

<p>&nbsp;</p>

# Hashing

- Hashing is generating a value or values from a string of text using a mathematical function.

- Hashing is one way to enable security during the process of message transmission when the message is intended for a particular recipient only. A formula generates the hash, which helps to protect the security of the transmission against tampering.

Cryptographic hash functions
A cryptographic hash function is a special class of hash functions that has various properties making it ideal for cryptography. There are certain properties that a cryptographic hash function needs to have in order to be considered secure. Let’s run through them one by one.

Property 1: Deterministic

This means that no matter how many times you parse through a particular input through a hash function you will always get the same result. This is critical because if you get different hashes every single time it will be impossible to keep track of the input.

Property 2: Quick Computation

The hash function should be capable of returning the hash of input quickly. If the process isn’t fast enough then the system simply won’t be efficient.

Property 3: Pre-Image Resistance

What pre-image resistance states are that given H(A) it is infeasible to determine A, where A is the input and H(A) is the output hash. Notice the use of the word “infeasible” instead of “impossible”. We already know that it is not impossible to determine the original input from its hash value. Let’s take an example.

Suppose you are rolling a dice and the output is the hash of the number that comes up from the dice. How will you be able to determine what the original number was? It’s simple all that you have to do is to find out the hashes of all numbers from 1-6 and compare. Since hash functions are deterministic, the hash of a particular input will always be the same, so you can simply compare the hashes and find out the original input.

But this only works when the given amount of data is very less. What happens when you have a huge amount of data? Suppose you are dealing with a 128-bit hash. The only method that you have to find the original input is by using the “brute-force method”. The brute-force method basically means that you have to pick up a random input, hash it and then compare the output with the target hash and repeat until you find a match.

> [What is Hashing on the Blockchain?](https://www.youtube.com/watch?v=IGSB9zoSx70&ab_channel=Blockgeeks)


# Transaction Integrity 

>[Link](https://hbr.org/2017/03/how-safe-are-blockchains-it-depends)



Blockchain, the distributed ledger technology underlying bitcoin, may prove to be far more valuable than the currency it supports. But it’s only as valuable as it is secure. As we begin to put distributed ledger technology into practice, it’s important to make sure that the initial conditions we’re setting up aren’t setting us up for security issues later on.

To understand the inherent security risks in blockchain technology, it’s important to understand the difference between public and private blockchains.

One of the first decisions to make when establishing a private blockchain is about the network architecture of the system. Blockchains achieve consensus on their ledger, the list of verified transactions, through communication, and communication is required to write and approve new transactions. This communication occurs between nodes, each of which maintains a copy of the ledger and informs the other nodes of new information: newly submitted or newly verified transactions. Private blockchain operators can control who is allowed to operate a node, as well as how those nodes are connected; a node with more connections will receive information faster. Likewise, nodes may be required to maintain a certain number of connections to be considered active. A node that restricts the transmission of information, or transmits incorrect information, must be identifiable and circumventable to maintain the integrity of the system. A private blockchain underlying commodities trading may grant more-central positions in the network to established trading partners, and may require new nodes to maintain a connection to one of these central nodes as a security measure to ensure it behaves as expected

>[Link](https://infospectives.co.uk/blockchains-embedding-integrity/)

While the implications are huge, there are key things it was never designed to do. It does not check the identity of asset owners before a first transaction is submitted. It just maintains the relationship between asset owner and transactions over time. Initially validating an individual’s entitlement to transact, and their ownership of referenced assets stored outside the blockchain, happens independently.

In other words; If trading Bitcoins, you might be doing business with a drug baron. If that doesn’t send your moral compass into a spin, you can rest assured that the drug baron possesses the currency promised and can’t pretend the trade didn’t happen.
In this Lawfare podcast Nick Weaver (senior staff researcher at the International Computer Science Institute in Berkeley, California and staunch Bitcoin sceptic), gives his own take on Bitcoin basics, and whether it’s really an historic financial opportunity, massive criminal problem, or something else entirely: a waste of everyone’s time and money.

He argues (to protect everyone from fraud), electronic transactions need to be reversible, which Bitcoin transactions are not…without the private keys. He talks a lot about Chinese domination of Bitcoin generation and Chinese coal being burned to power what he dubs “useless work” a.k.a hash generation.

Bitcoin enforces decreasing production returns (currently 25 Bitcoins, plus transaction fees) to combat mining monopolies. The bitcoin protocol specifies that the reward for adding a block will be halved approximately every four years (here’s a counter point for the environmental – if not political and fraud – concerns). Eventually, the Bitcoin reward will decrease to zero – transaction fees will be all folk get – and the limit of 21 million bitcoins will be reached in around 2140. That doesn’t however combat ponzi schemes (where Bitcoin investors are paid returns out of money invested by others, rather than any actual earnings), another key theme in the podcast.

Nick’s primary argument is that criminals see opportunities for returns far beyond Bitcoin market value (due to the anonymous and therefore criminal-friendly aspects of exchange), so racing to reap and control coins through production offers dark opportunities that justify a loss-making investment in production means. Together with potential for market instability (including DDoSing or spamming to disrupt transactions), he argues Bitcoin will never evolve into a value-stabilised competitive currency. Instead it will die a death through breaking or being regulated out of existence…and so what? According to Weaver only criminals, crypto/techno anarchists, and a few misguided venture capitalists will really mourn it.
As I said earlier on, blockchain (as distinct from Bitcoin), is just plumbing. Digitally innovative and game-changing plumbing, but plumbing nonetheless…