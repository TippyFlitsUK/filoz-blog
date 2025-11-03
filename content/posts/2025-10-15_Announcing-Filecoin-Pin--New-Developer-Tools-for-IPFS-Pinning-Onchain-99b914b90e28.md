---
title: 'Announcing Filecoin Pin: New Developer Tools for IPFS Pinning Onchain'
description: >-
  When Filecoin first launched, it had an ambitious goal: to be the incentivized
  persistence layer for IPFS. Changing how we address content…
date: '2025-10-15T15:38:14.425Z'
categories: []
keywords: []
slug: announcing-filecoin-pin-new-developer-tools-for-ipfs-pinning-onchain-99b914b90e28
---

When [Filecoin](http://filecoin.io) first launched, it had an ambitious goal: to be the incentivized persistence layer for [IPFS](http://ipfs.tech). Changing how we address content, IPFS moved from fragile location-based URLs to verifiable content identifiers that never break. But without economic incentives or cryptographic guarantees, IPFS content only lasted as long as someone, somewhere, kept hosting it out of goodwill or individual interest.

Filecoin was designed to answer the question: “Who keeps the data in IPFS around?” The mission was clear — to transform IPFS from “best-effort pinning” or reliance on centralized providers into truly persistent, verifiable storage backed by economic incentives and onchain payments, and audited with cryptographic proofs.

### Bringing IPFS & Filecoin Together

The mission of Filecoin has always been to create a decentralized, efficient, and robust foundation for humanity’s information, **starting with IPFS**.

But until now, connecting these two systems has been anything but simple.

Developers wanting to combine IPFS content addressing with Filecoin’s verifiable storage proofs and incentives faced a maze of specialized storage onboarding flows, third-party vendors, or complex workarounds. A seamless integration of discovery, routing, and delivery at scale remained just out of reach.

**Today, that changes.**

With [Filecoin Pin](https://docs.filecoin.io/builder-cookbook/filecoin-pin), developers can now persist any file or existing IPFS data on the Filecoin network of decentralized and globally distributed storage providers using familiar workflows and IPFS tooling, from the [command line](https://docs.filecoin.io/builder-cookbook/filecoin-pin/filecoin-pin-cli) to [GitHub Actions](https://github.com/filecoin-project/filecoin-pin/tree/master/upload-action). IPFS pins now come with Filecoin’s verifiable storage guarantees and the ability to persist IPFS files with crypto wallet payments — no vendors, workarounds, or KYC dependency on credit cards required. **The decentralized storage stack is finally coming together!**

![](/images/1__S1JiuXJTXvNKREC0RTYeRA.png)

### How Filecoin Pin Works

When you use Filecoin Pin, your IPFS files are persisted on Filecoin. Storage providers must cryptographically prove that they continue to store and serve your data daily, and customers only pay when these storage proofs are successfully delivered and verified onchain. Your data is directly available from Filecoin storage providers throughout the storage period.

![](/images/1__5K2Ub9XpBDV4aArXzYKxew.png)

But verifiable persistence is only part of the equation; a complete storage solution also depends on fast, dependable access to data. Filecoin Pin brings this full circle.

With Filecoin, your data remains portable and sovereign: you can choose providers, audit storage proofs and payments onchain, all without depending on a single company or provider. This is the trustless, economically-incentivized persistence layer that was always meant to complement IPFS.

Filecoin Pin is powered entirely by onchain smart contracts, decentralized storage providers, and common IPFS tooling like the [InterPlanetary Network Indexer (IPNI)](https://docs.cid.contact/) and the [IPFS Gateway](https://about.ipfs.io/). Developers pay for ongoing storage with web3 wallets like [MetaMask](https://metamask.io/), and audit verifiable storage proofs on the [PDP Scan](https://pdp.vxb.ai/calibration) Explorer.

![](/images/1____FGn4EYIAPqOeoOgO28EnQ.png)
![](/images/1__yqsF4uus1whLe2EdcPlHJw.png)
![](/images/1__Dx7ZcHpMLbc__D3L82csKSw.png)

### Getting Started

Today, developers can start building with [Filecoin Pin](https://docs.filecoin.io/builder-cookbook/filecoin-pin) to power their IPFS dApps, workflows, websites, agents, and more!

There are 3 ways to start using Filecoin Pin today:

1.  [Filecoin Pin CLI](https://docs.filecoin.io/builder-cookbook/filecoin-pin/filecoin-pin-cli) — Upload new or existing IPFS files directly to Filecoin via the command line
2.  [Filecoin Pin GitHub Action](https://github.com/filecoin-project/filecoin-pin/blob/master/upload-action/README.md) — Use GitHub Actions to automatically publish websites or build artifacts to IPFS & Filecoin
3.  [Filecoin Pin dApp Demo](https://github.com/filecoin-project/filecoin-pin-website) — Run or fork a simple demo dApp using Filecoin Pin

We can’t wait to see what you build! Here’s a few ideas:

*   Trustless onchain AI agents with fully sovereign data storage & persistence
*   Auto-backup tooling for photos, videos, & large files
*   Personal ENS website publishing flows with built-in wallet-funded pinning
*   NFT onchain preservation Data DAOs
*   Real-time data availability for chain snapshots or historical chain state
*   Daemon sidecars for kubo or helia to pin each new ‘ipfs add’ to Filecoin
*   New p2p collaboration tools with user-pays data persistence

And much **much** more!

Join us in [#fil-foc](https://filecoinproject.slack.com/archives/C07CGTXHHT4?utm_source=filozblog) for all the latest updates and real-time developer support as we build the Filecoin Onchain Cloud together!

### Filecoin Pin in Action

Want to see Filecoin Pin in action? Grab a snack🍿 and follow along with these 🔥🔥🔥 Filecoin Pin walkthroughs!