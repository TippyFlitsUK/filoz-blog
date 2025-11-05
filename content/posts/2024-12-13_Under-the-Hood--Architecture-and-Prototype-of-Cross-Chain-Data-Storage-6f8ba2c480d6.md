---
title: 'Under the Hood: Architecture and Prototype of Cross-Chain Data Storage'
description: zenground0 · Follow
date: '2024-12-13T19:43:40.122Z'
categories: []
keywords: []
slug: under-the-hood-architecture-and-prototype-of-cross-chain-data-storage-6f8ba2c480d6
featured_image: /images/1__sg__HkoNSHEAN0ubpDIovUg.png
---

![](/images/1__sg__HkoNSHEAN0ubpDIovUg.png)

zenground0 · [Follow](https://github.com/zenground0)

In our previous post, [exporting Filecoin’s Value to Multichain](https://medium.com/@filoz/exporting-filecoins-value-to-multichain-part-i-a554ed4434a1), we explored how **cross-chain deals** make Filecoin’s decentralized storage accessible from any blockchain. But how does this magic happen under the hood? In this post, we’ll take a closer look at the prototype architecture that powers cross-chain data storage, breaking it down into clear steps for builders, storage providers, and curious readers alike. Ready to get technical? Let’s dive in!

### The Core Idea: Seamless Integration Across Chains

At its heart, this prototype bridges two blockchain networks:

1.  The **Filecoin network** is where the storage and proof of data reside.
2.  A **“cross-chain network”** represents any other blockchain where users can initiate storage deals.

The architecture connects these networks with three key components:

*   **Smart contracts** to handle offers, payments, and proofs.
*   **XChain connector nodes** to aggregate data and interact with Filecoin storage providers.
*   **Bridges** to securely send proofs between the chains.

![](/images/1__d10pFHzMRBv6mMOx4Z7Wbw.gif)

### Architecture Overview

#### Smart Contracts

*   **On-Ramp (Cross-Chain Network):** Receives storage offers and payments from users. Holds funds in escrow until proofs are verified.
*   **Oracle (Cross-Chain Network):** Receives proofs from the Filecoin network and validates them for the on-ramp contract.
*   **Prover (Filecoin Network):** Tracks storage deals and sends notifications when data is successfully stored.

#### XChain Connector Node

This is the “middleman” that facilitates the interaction:

*   **XChain Client:** Sends storage deals and payments to the on-ramp contract and helps to route the data transfer between end user & aggregate.
*   **XChain Aggregator:** Combines smaller offers into larger batches, optimizing costs for Filecoin storage providers.
*   **XChain Buffer:** Temporarily holds data before transferring it to Filecoin.

#### Bridges

*   Handles proof transfers from Filecoin to the cross-chain network. In the prototype, we use the **Axelar network** for this step.

![](/images/1__y6hbgacU7twDwg8ig5ACjg.gif)

### Step-by-Step Workflow

#### 1\. Client Makes an Offer

Users prepare their data for storage (e.g., formatting it into CAR files) and send a transaction to post a storage deal to the on-ramp contract. This transaction includes:

*   A data reference (e.g., CommP hash).
*   Payment in ERC20 tokens.
*   Metadata, like the data size and location.

#### 2\. Data Aggregation

XChain nodes listen for new deals, aggregate smaller deals into larger batches, and create proofs of aggregation. After aggregation, the data is sent to Filecoin storage providers to initiate the deal-making process. Once the deal is successfully made on Filecoin, the Prover contract tracks it. It sends a DealNotify signal back to the Oracle contract on the cross-chain network, confirming the storage and enabling the on-ramp contract to release payments.

![](/images/1__069swe8bVeqofC2yGjwBIg.gif)

#### 3\. Bridging Proofs

The Prover contract is notified when a deal is successfully made on Filecoin. This notification identifies the originating source chain and sends proof of storage back to the correct cross-chain network via the Axelar bridge. The Oracle on the cross-chain network validates the proof and signals the on-ramp contract to release payment to the storage provider.

![](/images/1__Hyapt8FqnQkHN6RWrenJDA.gif)

### Prototype Highlights

You can find the source code of these contracts in the [onramp contract GH repo](https://github.com/ZenGround0/onramp-contracts). This prototype demonstrates two groundbreaking features:

1.  **Small Data Deals:** Aggregating smaller deals into batches makes it cost-effective for users to store even small amounts of data on Filecoin.
2.  **ERC20 Payments:** Users can pay for storage in tokens native to their blockchain, increasing flexibility and accessibility.

### What Makes This Exciting for Builders?

The modular nature of this prototype offers immense flexibility. Builders can:

*   Integrate only the components they need, such as aggregation or ERC20 payments.
*   Adapt the system to build advanced storage applications, like auctions or pay-as-you-go models.

For example, a decentralized video platform could use this system to allow users to store and pay for small video files directly from its native blockchain.

### Eastore: Expanding Filecoin’s Reach with Simplified Storage Solutions

As highlighted in this blog series, enabling seamless access to Filecoin’s decentralized storage is crucial for improving user experience and ecosystem adoption. Eastore exemplifies this vision by simplifying the onboarding of small files to Filecoin and extending its utility across multichain environments. With integrations like [FIL-Builders](https://x.com/FILBuilders) already underway and interest from networks such as [Linear](https://x.com/linear), [Eastore](https://x.com/EastoreWeb3) is paving the way for decentralized storage solutions to become more accessible and interoperable. Discover more about their innovative approach in their demo below.

### Next Up: Overcoming Challenges and Exploring Future Applications

This prototype is just the beginning. In our final post, we’ll discuss challenges like bridging latency, potential improvements, and how cross-chain deals can pave the way for advanced applications like true storage markets and repair networks.

Stay tuned!