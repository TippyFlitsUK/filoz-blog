---
title: 'The F3 Journey: Delegated Authority for Faster Mainnet Activation of F3'
description: Orjan Roren (@Phi-rjan) · Chinese Translation
date: '2025-02-04T14:53:27.246Z'
categories: []
keywords: []
slug: the-f3-journey-delegated-authority-for-faster-mainnet-activation-of-f3-98f9aa69eb0c
---

![](/images/1__yirtLz__EiGd2BoXDuaCiIw.png)

Orjan Roren ([@Phi-rjan](https://x.com/OrjanRoren)) · [Chinese Translation](https://mp.weixin.qq.com/s/iz3sGOR6rEuEJBk2mw65zg)

In our [previous](https://medium.com/@filoz/finality-unveiled-passive-testing-to-mainnet-launch-of-f3-fast-finality-03e09bc68de5) `[The F3 Journey](https://medium.com/@filoz/finality-unveiled-passive-testing-to-mainnet-launch-of-f3-fast-finality-03e09bc68de5)` [upda](https://medium.com/@filoz/finality-unveiled-passive-testing-to-mainnet-launch-of-f3-fast-finality-03e09bc68de5)te, we shared insights from our passive testing of Fast Finality (F3) on mainnet and outlined necessary timeline adjustments. Since then, we've made significant progress addressing the challenges identified during testing. We are excited to share a key development that will shape F3's path to be activated on the Filecoin mainnet.

### 🚧 The Challenge: Network Upgrade Bottleneck

One of the key challenges in developing F3 has been its reliance on network upgrades to deploy improvements, as well as the difficulty of finalizing parameters to make Fast Finality truly fast. After our last round of passive testing, we realized that we might be facing a potentially long timeline:

1.  **First Network Upgrade**: To ship critical improvements like message compression and chain hashing to reduce bandwidth usage across all nodes
2.  **Second Network Upgrade**: To deploy the finalized parameters and activation epoch for F3

This two-upgrade process would have pushed F3 activation to mid-2025. Given the significant improvements F3 brings to the network’s speed, finality and usability, we knew we needed a more efficient approach to deliver these benefits sooner while maintaining safety and security. So we put our heads down and started to think about alternative proposals that could speed up F3 activation to mainnet.

![](/images/0__qMJnhHrKgQenlJ5a.jpg)

### 💡 The proposal: Delegated Authority for Parameter Setting

After careful consideration and investigation, the F3 team proposes a new mechanism for faster F3 activation by delegating the authority to set F3 parameters to a smart contract. The approach, detailed in the [FRC for Delegation of Authority for F3 parameter Setting](https://github.com/filecoin-project/FIPs/pull/1112/files), aims to speed up the activation process for F3 while maintaining the network’s security and reliability.

The core idea of the proposal is to transition the parameter-setting process, which previously required an additional network upgrade, to an on-chain contract. This allows parameters to be set after multiple rounds of passive testing following the implementation of critical improvements like message compression and chain hashing in the Filecoin network version 25 upgrade. Consequently, we can bypass the need to wait for network version 26 to activate F3 and instead activate F3 on the mainnet whenever there is consensus among the implementation teams that we have achieved the desired set of parameters that enable F3 to progress quickly and stably in the network.

### ⚙️ The Mechanism: How Delegated Authority Works

The mechanism of the on-chain contract is designed with some key principles in mind:

*   **Controlled Parameter Setting:** Setting the F3 parameters will require full consensus among the Filecoin chain implementations (Lotus, Forest, and Venus).
*   **Transparent Process:** The parameter changes will be visible on-chain, maintaining transparency for the network.
*   **Time-Bound Authority:** The contract will have a limited lifespan, automatically disabling after six months. Additionally, the contract prevents further updates once the set bootstrap epoch has passed, meaning it can only be used once to finalize parameters.

So let us take a more technical dive into what the parameters for activating F3 are and what they mean:

**✍️ Contract Parameters:**

The contract allows for configuring parameters in the F3 manifest. Let’s examine the most important parameters of the contract that will allow us to set the parameters that are most optimal for network performance after a round of passive testing after network version 25 ships:

*   **Bootstrap Epoch:** Specifies the activation time of F3 in Mainnet. The bootstrap epoch can not be set sooner than 72 hours from message transmission. This buffer period allows the network to react in case any issues are discovered late in the process.
*   **EC.HeadLookback:** This parameter defines how many epochs F3 lags behind the expected consensus. For example, if the network is at epoch 100 and **EC.HeadLookback** is set to 10, F3 will be working to finalize up to epoch 90.
*   **CatchUpAlignment:** This parameter sets a waiting period for incoming messages during fast finalization. It helps ensure F3 works properly with real-world network speeds by giving messages enough time to arrive before proceeding.
*   **EC.BaseDecisionBackoffTable:** This parameter controls how long the system should wait before retrying when F3 encounters conflicts. If participants can’t agree on finalizing a chain, the system will pause temporarily before making another attempt.

**📋 Full list of parameters:**

Five additional parameters need to be set:

*   **Expected Consensus Delay Multiplier**
*   **GPBFT Configuration**
*   **Certificate Exchange Configuration**
*   **Chain Exchange Configuration**
*   **PubSub Configuration**

All of these parameters are either related to knobs that need to be tuned to find the right balance between speed, bandwidth usage and performance or configurations that make F3 work with the networking stack in Filecoin and accommodate the large size of mainnet.

You can dive into the technical details of these parameters in the FIP discussion here: [https://github.com/filecoin-project/FIPs/discussions/1102](https://github.com/filecoin-project/FIPs/discussions/1102).

### 🗺️ The Roadmap: Path Forward

The smart contract repository for streamlining F3 activation is now [publicly available](https://github.com/filecoin-project/f3-activation-contract), with the first version’s [source code published](https://github.com/filecoin-project/f3-activation-contract/blob/master/contracts/F3Parameters.sol) and verified on [Sourcify](https://sourcify.dev/#/lookup/0x5341A43bBD1ef7E0290F47127e7605e5e88B5E11):

![](/images/1__AlmuZEgZJdgeyMdD__sFrvg.png)

We welcome community reviews of the contract. Questions and feedback can be posted in the [GitHub discussion](https://github.com/filecoin-project/FIPs/discussions/1102). The progress in establishing and integrating this delegated authority approach is tracked [here](https://github.com/filecoin-project/go-f3/issues/828). With network version 25 deployment starting soon, we expect to finalize all outstanding work items related to optimizing F3 by the end of the week starting 2025–02–03.

In our next post in `The F3 Journey` series, we'll explore the FIP discussion and design considerations for making F3 participation a network requirement in a future upgrade. You can read the proposal here: [https://github.com/filecoin-project/FIPs/discussions/1106](https://github.com/filecoin-project/FIPs/discussions/1106).

Stay tuned!👋