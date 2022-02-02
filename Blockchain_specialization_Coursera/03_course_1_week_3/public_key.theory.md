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

