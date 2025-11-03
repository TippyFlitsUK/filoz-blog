---
title: >-
  Announcing Proof of Data Possession (PDP) on Filecoin: Verifiable Hot Storage
  Has Arrived!
description: 'zenground0 (@zenground0), James Bluett (@TippyFlits)'
date: ''
categories: []
keywords: []
slug: ''
---

![](/images/1__0tFRL0PLpUfikbR16__fzJA.png)

zenground0 ([@zenground0](https://x.com/zenground0)), James Bluett ([@TippyFlits](https://x.com/TippyFlits))

We’re thrilled to unveil **Proof of Data Possession (PDP)**, a game-changing advancement in decentralised hot storage now available on Filecoin! As a core feature of Filecoin Web Services (FWS), PDP dramatically improves how quickly and inexpensively data integrity and accessibility can be verified, making it ideal for hot-storage scenarios.

### 🔎 What Exactly is PDP?

Proof of Data Possession (PDP) is a lightweight cryptographic proof system designed to verify that a storage provider holds a user’s data in an accessible, retrievable, and unsealed state. Unlike traditional storage proofs in Filecoin — such as Proof of Replication (PoRep) and WindowPoSt — that verify sealed storage periodically, PDP enables **continuous, on-demand verification** of unsealed data.

In essence, PDP transforms Filecoin into a trustless environment for hot storage. Clients can schedule random challenges at any time, and storage providers must respond with cryptographic proofs that validate the availability of the actual data. These proofs are efficient, cost-effective, and publicly verifiable without needing to retrieve the full data set.

This unlocks new use cases where frequent access, uptime guarantees, or compliance-grade verification are critical — such as serving web assets, fine-tuning AI models, or supporting real-time analytics.

### 🔥 Hot Storage and PDP

The Filecoin network has long been the gold standard for decentralised, long-term storage. **With PDP, it now rises to meet the moment for hot storage** — data that needs to be available, accessible, and provable at a moment’s notice. This opens the door for dynamic applications like AI training, CDN-style web delivery, developer sandboxes, and low-latency edge computing.

Hot storage use cases demand a different level of reliability and speed. Unlike archival data, hot data must be instantly retrievable — ideally without repeated downloads or expensive redundancy. PDP makes this possible while keeping data verifiable through real-time proof challenges that ensure data is still online, unsealed, and under the provider’s control.

With PDP, storage providers can confidently signal availability, and clients can trust that their data is live and ready — without needing to access the data itself. This changes the game for:

*   **Real-Time Retrieval**: Get immediate confirmation that your data is retrievable right now — not hours or days from now.
*   **Consistent Accessibility**: Critical for developers, content delivery networks, or apps that need always-on access to datasets.
*   **Confidence in Critical Data**: For financial services, research, and other sensitive sectors, the cryptographic certainty of data presence adds an essential layer of trust.Ideal for mission-critical applications where data integrity and rapid retrieval are essential.

### 📦 Smart Contracts and Tools

PDP functionality is now powered by robust, audited smart contracts deployed on Mainnet and Calibration Testnet:

*   **Mainnet PDP Contracts:**
*   **Verifier:** [0x9C65E8E57C98cCc040A3d825556832EA1e9f4Df6](https://filfox.info/en/address/0x9C65E8E57C98cCc040A3d825556832EA1e9f4Df6)
*   **Service:** [0x805370387fA5Bd8053FD8f7B2da4055B9a4f8019](https://filfox.info/en/address/0x805370387fA5Bd8053FD8f7B2da4055B9a4f8019)

  

*   **Calibration Testnet PDP Contracts:**
*   **Verifier:** [0x5A23b7df87f59A291C26A2A1d684AD03Ce9B68DC](https://calibration.filfox.info/en/address/0x5A23b7df87f59A291C26A2A1d684AD03Ce9B68DC)
*   **Service:** [0x6170dE2b09b404776197485F3dc6c968Ef948505](https://calibration.filfox.info/en/address/0x6170dE2b09b404776197485F3dc6c968Ef948505)

All contracts have been thoroughly audited by Zellic to ensure security and [reliability](https://github.com/Zellic/publications/blob/master/Proof%20of%20Data%20Possession%20-%20Zellic%20Audit%20Report.pdf).

### 🛠️Developer & Storage Provider Tools

To get started building or running a PDP-enabled storage provider or client, we recommend reading the following comprehensive setup guides:

*   📘 [](https://docs.curiostorage.org/experimental-features/enable-pdp)[Getting Started with PDP for Filecoin Storage Providers](https://docs.filecoin.io/storage-providers/pdp/prerequisites)
*   📘 [Getting Started with PDP for Storage Clients](https://docs.filecoin.io/storage-providers/pdp/use-pdp)

These guides walk through everything from installing dependencies, building the Curio node and PDPTool, managing PDP services, configuring wallet access, setting up proof sets, and verifying availability.

PDPTool is bundled with Curio and is used by both providers and clients to manage the lifecycle of PDP challenges, proof sets, and file operations.

### 🎥 Watch PDP in Action

Check out our exciting demos to see PDP live:

[PDP Demo — FilZoo](https://www.youtube.com/watch?v=f_9f5pzqumw) — Demonstrates how to inspect data secured by PDP on the Filecoin network and walk through building a simple web app that interacts with it — bringing verifiable storage into your browser in just minutes.

[PDP Demo — DeepSeek R1 Public Dataset](https://www.youtube.com/watch?v=IVkwz7WNHZ8) — Dive into uploading large files to a PDP-enabled storage provider by archiving and verifying the DeepSeek R1 670B parameter model — a powerful example of how PDP can support open, verifiable access to massive AI datasets.

### 🧑‍🚀 Launching the PDP MinerX Program!

We are excited to announce the **PDP MinerX Program** — an established initiative supporting early-adopter Filecoin Storage Providers (SPs) focusing on hot storage and rapid data retrieval. MinerX is more than a pilot — it’s a strategic investment in building a reliable, retrieval-aware network of PDP-capable providers.

Running from April through May 2025, the initial phase of MinerX will onboard at least fifteen geographically diverse SPs, as well as several external clients, to stress-test the PDP stack in real-world conditions. These providers will serve as the foundation for demonstrating verifiable, performant storage on the Filecoin network.

Our goal with MinerX is to ensure PDP launches with a strong community, proven tooling, and trusted infrastructure. It’s the bridge between protocol innovation and production-grade deployment.

If you’re a storage provider looking to lead the charge into verifiable, accessible storage, MinerX is your moment. 

[Click here](https://forms.gle/yX359bPAcNSftVNk6) to apply for the PDP MinerX program.

### 🌌 PDP and Filecoin Web Services (FWS)

PDP is more than just a new proof mechanism — it’s a critical building block of Filecoin Web Services (FWS), Filecoin’s decentralised, modular alternative to traditional cloud providers.

FWS plans to offer a growing suite of interoperable services — including compute, storage, networking, and orchestration — purpose-built for Web3 builders. It’s designed for composability, scalability, and trustlessness, enabling developers to assemble powerful decentralised applications without reinventing the stack.

Within this framework, PDP enables real-time data verifiability, making it the cornerstone of FWS’s hot storage layer. Whether you’re building an AI training pipeline, a retrieval gateway, or a low-latency content platform, PDP ensures that data is available, unsealed, and provably under your control — no downloads required.

Learn more about FWS:

*   [The New Era of AI-Compute: Filecoin Introduces Filecoin Web Services (FWS)](https://medium.com/@FILLiquid/the-new-era-of-ai-compute-filecoin-introduces-filecoin-web-services-fws-b9d73151918e)
*   [Filecoin Web Services: The Future of Decentralized Cloud Services](https://filecointldr.io/article/filecoin-web-services-the-future-of-decentralized-cloud-services)

### 🚩 Get Started with PDP Today

Step into the future of decentralised data with PDP. Whether you’re a developer, storage provider, or application builder, now is the time to integrate verifiable hot storage into your stack.

[Join the MinerX program](https://forms.gle/yX359bPAcNSftVNk6), explore the tooling, and help build a Filecoin network where availability, transparency, and performance are provable — on demand.

Whether you’re running your own PDP service, uploading large AI models, or just experimenting with proof sets through pdptool, this is your opportunity to help define the future of data availability in Web3.

**Stay tuned for more updates, insights, and tutorials!**