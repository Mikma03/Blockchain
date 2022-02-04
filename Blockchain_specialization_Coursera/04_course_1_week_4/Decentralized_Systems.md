# Table of contents

<p>&nbsp;</p>

1. [Resources](#Resources)

2. [Resources](#Resources)


# Resources

[Blockchain based trust & authentication for
decentralized sensor networks](https://arxiv.org/pdf/1706.01730.pdf)


# Blockchain Consensus Protocols

We hear plenty of talk of how public blockchains are going to change the world, but to function on a global scale, a shared public ledger needs a functional, efficient and secure consensus algorithm.

A consensus algorithm, like bitcoin's proof of work (the one we hear about most often), does two things: it ensures that the next block in a blockchain is the one and only version of the truth, and it keeps powerful adversaries from derailing the system and successfully forking the chain.

In proof of work, miners compete to add the next block (a set of transactions) in the chain by racing to solve a extremely difficult cryptographic puzzle. The first to solve the puzzle, wins the lottery. As a reward for his or her efforts, the miner receives 12.5 newly minted bitcoins – and a small transaction fee.

Yet, although a masterpiece in its own right, bitcoin's proof of work isn't quite perfect.

Common criticisms include that it requires enormous amounts of computational energy, that it does not scale well (transaction confirmation takes about 10-60 minutes) and that the majority of mining is centralized in areas of the world where electricity is cheap.

Bitcoin creator Satoshi Nakamoto woke us up to the potential of the blockchain, but that doesn't mean we can't keep searching for faster, less centralized and more energy-efficient consensus algorithms to carry us into the future.

# Proof of activity

To avoid hyperinflation (what happens when too much of a currency floods the system) bitcoin will only ever produce 21m bitcoins. That means, at some point, the bitcoin block reward subsidy will end and bitcoin miners will only receive transaction fees.

Some have speculated this might cause security issues resulting from a 'tragedy of the commons', where people act in self-interest and spoil the system. So, proof of activity was created as an alternative incentive structure for bitcoin. Proof of activity is a hybrid approach that combines both proof of work and proof of stake.

In proof of activity, mining kicks off in a traditional proof-of-work fashion, with miners racing to solve a cryptographic puzzle. Depending on the implementation, blocks mined do not contain any transactions (they are more like templates), so the winning block will only contain a header and the miner's reward address.

At this point, the system switches to proof of stake. Based on information in the header, a random group of validators is chosen to sign the new block. The more coins in the system a validator owns, the more likely he or she is to be chosen. The template becomes a full-fledged block as soon as all of the validators sign it.

If some of the selected validators are not available to complete the block, then the next winning block is selected, a new group of validators is chosen, and so on, until a block receives the correct amount of signatures. Fees are split between the miner and the validators who signed off on the block.

Criticisms of proof of activity are the same as for both proof of work (too much energy is required to mine blocks) and proof of stake (there is nothing to deter a validator from double signing).

Decred is the only coin right now using a variation of proof of activity.

# Proof of burn

With proof of burn, instead of pouring money into expensive computer equipment, you 'burn' coins by sending them to an address where they are irretrievable. By committing your coins to never-never land, you earn a lifetime privilege to mine on the system based on a random selection process.

Depending on how proof of burn is implemented, miners may burn the native currency or the currency of an alternative chain, like bitcoin. The more coins you burn, the better chance you have of being selected to mine the next block.

Over time, your stake in the system decays, so eventually you will want to burn more coins to increase your odds of being selected in the lottery. (This mimics bitcoin's mining process, where you have to continually invest in more modern computing equipment to maintain hashing power.)

While proof of burn is an interesting alternative to proof of work, the protocol still wastes resources needlessly. Another criticism is that mining power simply goes to those who are willing to burn more money.

The only coin that uses proof of burn is slimcoin, a cryptocurrency based on peercoin. It uses a combination of proof of work, proof of stake and proof of burn, but is only semi-active at this time.

[Review of blockchain consensus mechanisms](https://medium.com/wavesprotocol/review-of-blockchain-consensus-mechanisms-f575afae38f2)

