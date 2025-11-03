---
title: 'The PDP Journey: An In-Depth Look at How PDP Works'
description: Orjan Roren (@Phi-rjan) · Follow
date: '2025-03-06T14:35:26.759Z'
categories: []
keywords: []
slug: the-pdp-journey-an-in-depth-look-at-how-pdp-works-4b6079f4baad
---

![](/images/1__8gWfzmTPnq05WaaTNfvzmA.png)

Orjan Roren (@Phi-rjan) · [Follow](https://x.com/OrjanRoren)

Welcome to the second instalment of the “The PDP Journey" series! In our [previous blog post](https://medium.com/@filoz/the-pdp-journey-a-refresher-on-proof-of-data-possession-and-its-path-to-mainnet-e6b481d9ad9a), we brought you a refresher on Proof of Data Possession (PDP) and outlined its path to Mainnet.

Today, we’re diving deeper into the mechanics of PDP, starting with the fundamental concepts, walking you through the PDP workflow between clients and providers, and exploring how the proving system handles successful operations and failures.

### 📦 What is a ProofSet?

So let us start with one of the basic building blocks in PDP, called a ProofSet. You can think of a ProofSet as a:

*   **Dynamic Container**: An appendable container can grow or shrink over time as data is added or removed.
*   **Client-Provider Relationship**: Each ProofSet is specific to a single client-provider relationship for security reasons.
*   **Unified Proving**: Proofs are performed over a single ProofSet, with random sampling used to verify data possession in the ProofSet.

The beauty of ProofSets is their flexibility. They can accommodate data of any size, and the PDP contracts don’t impose restrictions on data formatting (though implementation software might pad data to power-of-two sizes).

Whether you’re storing tiny pieces of data or massive files, ProofSets handle it all, and multiple pieces can even be aggregated into a single root. At the abstract level, a ProofSet is simply an array of Merkle roots, providing a clean and efficient data structure for verification.

![](/images/0__FipxIi8kuWpLJx79.gif)

### 🏗️ The PDP Architecture: Contracts Working Together

The current PDP architecture consists of two main smart contracts:

#### The Verifier Contract

This is where the action happens. The verifier contract contains the list of all ProofSets and receives proof submissions from storage providers. While there’s no limit to how many ProofSets it can manage, it implements a sybil burn fee to prevent spam.

Importantly, this contract does not hold user funds, focusing solely on verification functions.

#### The Listener Contract

The listener contract handles the business logic. It processes fault detection and management while listening for other operations including adding roots, proving, rolling over periods, and deletions. The listener can also be programmed to implement additional logic, such as payment requirements, making it the flexible, business-oriented component of the architecture.

The separation of concerns allows for a clean contract architecture where verification and business logic remain distinct. While the current architecture focuses on these two core contracts, the modular design of PDP enables future expansion with specialized contracts for payments, permissions, slashing mechanisms, or other functionality as the PDP ecosystem matures.

### 🧩 Modular by Design

In the initial phase, we expect most services will leverage the audited PDP verifier contract, which is supported by existing PDP storage provider software. This allows services to focus on building unique value propositions while relying on a secure verification core.

However, the ultimate power of PDP architecture lies in its flexibility. While FilOz is deploying one implementation of the PDP proof, the architecture empowers other services and application builders to create their own set of customized PDP proof/verification contracts. This means you can:

*   **Tailor Parameters**: Adjust challenge frequency, proof requirements, and fault tolerance thresholds
*   **Define SLAs**: Create service level agreements that match your specific use cases
*   **Implement SLIs**: Establish custom service level indicators for performance monitoring
*   **Expand Offerings**: Develop specialized storage solutions for different market needs

This flexibility doesn’t just benefit service providers wanting to deploy their own contracts — it enriches the entire Filecoin L1 ecosystem by expanding the range of offerings available to clients.

### ⚙️ How Proving Works in PDP

The proving mechanism in PDP is relatively simple:

*   **Daily Challenges**: Every 24 hours, the ProofSet is challenged.
*   **Chain-Provided Randomness**: The blockchain supplies the randomness for selecting which leaves to challenge
*   **Lightweight Sampling**: Five merkle proofs are requested per challenge, and that is regardless of the ProofSet size.
*   **Efficient Verification**: Each leaf node challenged is 32 bytes in size (160 bytes total per challenge)
*   **CPU-Friendly**: The proving process uses SHA hashing, which can be efficiently performed on a CPU without specialized hardware.

![](/images/0__qrCMkpJJBuPXfdFH.jpg)

This approach provides sufficient security guarantees for onboarders while keeping the proving process extremely lightweight and accessible for SPs.

### ❓ What Happens When Proofs Fail?

So what actually happens when a proof fails in PDP? Let us examine two potential scenarios:

#### Scenario 1: Inability to prove but the System Operational

If a storage provider’s disk fails or data becomes inaccessible, the PDP storage provider recognizes it cannot find or verify the proof. It then sends a “next proving period” message without submitting a proof. This effectively communicates the failure, and the listener contract responds by emitting an event indicating a fault for the specific SP on the ProofSet.

#### Scenario 2: Complete System Failure

If a storage provider’s machine goes down entirely, no explicit fault communication occurs since no cron mechanism exists. In this case, onboarders detect the failure through the absence of a proof. When the SP eventually comes back online, it submits a “next proving period” message acknowledging the fault period for which it was down, before continuing with new challenges.

### 🔄 The PDP Workflow: Client-Provider Interactions

At its core, PDP operates through a straightforward workflow between clients (data onboarders or owners) and providers (storage providers). The current implementation is designed primarily for established relationships, where onboarders already know which storage providers they want to work with.

Currently, no on-chain discovery mechanism exists for matching unknown clients with providers. The system relies on pre-existing relationships, with clients identifying storage providers they want to work with and then setting up a ProofSets between them accordingly.

Future plans include the addition of a payments contract and potentially an automatic protocol for connecting PDP storage providers with clients, but these features are still being planned.

### 🔐 Contract Ownership and Governance

![](/images/0__YvuhorHDDJ0GaQ__T.jpg)

FilOz members currently hold the keys to the PDP verifier and listener contracts. Both the PDP verifier and PDP listener contracts are “Ownable Upgradable” contracts. These are standard interfaces in the EVM development community, allowing for upgrading the code of the contracts after deployment. These contracts have ownership keys that can 1) upgrade the code of the contract and 2) update the owning key for the contract. Since the verifier contract doesn’t hold funds, this arrangement poses minimal security risk at present. The long-term plan for contract governance includes two potential paths:

1.  Distributing upgrade keys to the main parties involved in using PDP
2.  Removing ownership entirely, making the contract immutable

Option 2 would prevent further upgrades to the verifier contract. However, new functionality could still be added through the listener contract or by deploying complementary contracts for slashing, payments, and other features.

### 🔮 Looking Ahead

As PDP continues its journey toward Mainnet deployment, the architecture and mechanisms described here form the foundation designed to verify data possession without the computational overhead of PoRep efficiently. This makes PDP particularly valuable for hot storage scenarios where data needs to be frequently accessed.

Those interested in participating more actively can join us on the [#fil-pdp](https://filecoinproject.slack.com/archives/C0717TGU7V2) channel on [Filecoin Slack](https://filecoin.io/slack), where you can ask questions and engage with the development team.

See you in the next update! 👋