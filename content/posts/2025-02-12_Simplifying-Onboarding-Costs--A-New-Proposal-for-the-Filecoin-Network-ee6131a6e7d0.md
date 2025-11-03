---
title: 'Simplifying Onboarding Costs: A New Proposal for the Filecoin Network'
description: Irene Giacomelli (@Irene_2911) - Follow
date: '2025-02-12T17:52:34.424Z'
categories: []
keywords: []
slug: simplifying-onboarding-costs-a-new-proposal-for-the-filecoin-network-ee6131a6e7d0
---

![](/images/1__f4uUnfOTGFw__tJLKz__qoQQ.png)

Irene Giacomelli ([@Irene\_2911](https://twitter.com/Irene_2911)) · [Chinese Translation](https://mp.weixin.qq.com/s/B4XRVf8vcDkDn2lhNnFRQA)

### 🚀 The Proposal: Simplifying Costs, Enhancing Efficiency

Filecoin’s economic model has evolved alongside its growth, balancing efficiency, scalability, and sustainability. In response to community feedback and operational insights, we are excited to introduce **FIP-0100**, a pivotal proposal that reshapes how Filecoin handles storage onboarding costs while driving network efficiency. This FIP proposes to:

*   **Remove the Batch Balancer:** Eliminate the batch fee from all precommit and provecommit methods.
*   **Introduce a Per-Sector Fee:** Replace the batch balancer with a stable, predictable mechanism to support long-term economic sustainability.
*   **Eliminate Gas-Limited Constraints:** Simplify protocol operations by removing outdated restrictions.

This proposal reflects insights from extensive discussions on better aligning value accrual and addressing the urgency of gas fee unblocking.

### 🔍 Why Change? The Current Challenges

The current batch balancer mechanism was designed to stabilise Filecoin’s economy, but it presents significant challenges:

*   **Inefficient Batching and Proof Aggregation:** Precommit batching and proof aggregation for provecommit only make economic sense when base fees are high, creating a barrier to efficient gas usage.
*   **Complex Cost Structures:** The batch balancer relies on fluctuating gas fees, making it difficult for Storage Providers (SPs) to predict costs.
*   **Outdated Constraints:** Initially designed before proper gas accounting, protocol limits now unnecessarily restrict growth.

These inefficiencies misalign incentives, discouraging optimisations that could reduce gas costs and improve network performance. Community discussions, including the [**Idea Pitch: Filecoin Value Accrual and Long Term Offering**](https://www.youtube.com/watch?v=2jKS1oLV0V4) session at FDS5 Bangkok, 2025, have emphasised the need for a more effective approach.

### 💡 The FIP-0100 Solution: A Three-Part Approach

#### 1\. Removing the Batch Balancer

By eliminating the batch fee:

*   **Precommit Batching Becomes Rational:** Without the fee, SPs are incentivised to batch sectors more frequently, significantly reducing gas usage.
*   **Proof Aggregation is Optimized:** Removing aggregation fees enables broader adoption, enhancing scalability and onboarding speed.

**Example Savings:**

*   Precommit batching for 4 sectors reduces gas per sector from **16.7M to 4.6M (3.6x savings).**
*   Provecommit aggregation reduces gas per sector from **267.5M to 129.3M (2x savings).**

#### 2\. Introducing a Per-Sector Fee

Replacing the batch balancer with a per-sector fee ensures predictable, stable costs:

*   **Daily Payments:** Fees are paid daily, preventing significant upfront costs that could hinder onboarding.
*   **Aligned with Network Growth:** The fee adjusts based on circulating supply, supporting economic stability.
*   **Cap for High-Growth Scenarios:** Payments are capped to prevent excessive costs during rapid network expansion.

#### 3\. Removing Gas-Limited Constraints

Outdated protocol constraints, like batch size limits, are no longer necessary. Removing them will:

*   **Simplify Protocol Design:** Reduces unnecessary code complexity.
*   **Enhance Flexibility:** Allows the network to scale without artificial bottlenecks.

### 📊 The Economic Impact: Balancing Costs and Growth

FIP-0100 fundamentally shifts how Filecoin captures value:

*   **Decouples Gas Fees from Service Fees:** Gas fees cover execution; per-sector fees capture the value of storage auditing.
*   **Predictable Costs for SPs:** Simplifies cost modelling, making it easier to plan and operate.
*   **Supports Sustainable Growth:** Network revenue aligns with storage demand, not just gas usage.

We expect a **~30% reduction in onboarding gas units**, leading to lower base fees and more efficient storage growth.

### 🗘️ Design Principles

Our onboarding fee design prioritises:

**Simplify the system to improve predictability**

*   Introducing a per-sector fee should help reduce the likelihood of network shocks caused by unpredictable base fee volatility.
*   Service Providers should be able to reason about future fees, rewards, and ROI.
*   A simpler system is easier to maintain, requiring fewer manual updates.

**Capturing Network Value:** Fees will scale with network demand, reflecting added ecosystem value.

**Avoiding** **Bottlenecks**: The new model will ensure we have higher onboarding capacity with respect current system.

### 🚀 What’s Next? The Path to Implementation

*   **Community Feedback:** Please engage with the proposal on the [FIP discussion forum](https://github.com/filecoin-project/FIPs/discussions/1092).
*   **Network Upgrade:** This FIP requires protocol changes to be rolled out in a future network version (targeting nv25).
*   **Ongoing Optimization:** This change paves the way for future enhancements in onboarding and proof mechanisms.

### 🤝 Join the Discussion

**FIP-0100** is a critical step toward a more efficient, sustainable Filecoin network. Your feedback is essential as we refine and implement these changes.

*   [Read the full FIP](https://github.com/filecoin-project/FIPs/blob/836ead8309bee5ffa216cc07bf4ae6b61425a700/FIPS/fip-removeBatchBalancer.md)
*   Review the original FIP discussions [#1092](https://github.com/filecoin-project/FIPs/discussions/1092) & [#1105](https://github.com/filecoin-project/FIPs/discussions/1105)
*   Share your thoughts and follow updates on [Filecoin Slack](https://filecoin.io/slack).

Let’s build a stronger, more scalable Filecoin together. 🚀