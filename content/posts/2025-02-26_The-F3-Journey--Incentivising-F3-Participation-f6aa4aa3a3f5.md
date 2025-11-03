---
title: 'The F3 Journey: Incentivising F3 Participation'
description: Orjan Roren (@Phi-rjan) · Chinese Translation
date: '2025-02-26T14:16:33.808Z'
categories: []
keywords: []
slug: the-f3-journey-incentivising-f3-participation-f6aa4aa3a3f5
---

![](/images/1__nkAqKrT4oufMS8NnTpZ15w.png)

Orjan Roren ([@Phi-rjan](https://x.com/OrjanRoren)) · [Chinese Translation](https://mp.weixin.qq.com/s/QQFjyjV82wc0-qMzk_qV9w)

In our previous [F3 Journey update](https://medium.com/@filoz/the-f3-journey-delegated-authority-for-faster-mainnet-activation-of-f3-98f9aa69eb0c), we shared how we’re speeding up the activation of Fast Finality (F3) on the Filecoin mainnet. Today, we’re excited to explore another key development: the incentives designed to drive participation and ensure everyone benefits from F3.

F3 is a game-changer for Filecoin. It’s designed to make the network faster and more reliable by ensuring that transactions are finalized quickly and securely. For F3 to reach its full potential and speed, we need every Storage Provider (SP) on board. The good news? We’re already seeing incredible momentum — in the latest passive testing round on Mainnet (from nv24), 80% of the network’s power was participating 👏. After F3 has been activated on Mainnet and successfully been running for an extended period of time, the F3 team intends to ensure that the participation rate is always the highest. That’s where incentives come in.

### 🚧 The Challenge: Why Network-Wide Participation Matters

Imagine F3 as a team sport. The more players on the field, the stronger and more dynamic the game becomes. If only a few players show up, the game slows down, there are gaps on the field, and the experience isn’t as good for everyone. Similarly, F3 needs full participation from SPs to deliver optimal benefits, such as consistent, fast finality and a smooth user experience for builders, exchanges, and storage providers.

Low participation can prevent F3 from finalising recent epochs, causing it to lag behind the chain head. This creates inconsistent finalization times and reduces the network’s reliability. This inconsistency poses significant challenges for applications building on top of the F3 APIs and Filecoin — whether they’re storage and client solutions, exchanges, or other services. They need a stable, predictable environment to create great applications and user experience.

That’s why maintaining high participation is crucial. With strong participation, F3 can deliver its core benefits: consistent fast finality, reliable transaction confirmation, and a robust foundation for the entire Filecoin ecosystem.

![](/images/1__lM3caynX5Nf09Hl6XSWxTw.png)

### 💡 The Proposal: Ensuring Participation through Rewards

The proposal introduces a thoughtful adjustment to mining rewards that maintains total rewards while incentivizing F3 participation. The key change? Up to 10% of mining rewards would be tied to F3 participation, verified through on-chain finality certificates.

The rewards system for F3 is built on three main principles:

1.  **Transparent Verification**: Participation is verified through finality certificates posted on-chain. These certificates contain aggregated BLS signatures from participating validators, creating an immutable record of who participated and when.
2.  **Fair Distribution**: Rewards are split between two groups:  
    a. Validators who sign the F3 certificates (participation rewards)  
    b. Validators who include these certificates in their blocks (inclusion rewards)
3.  **Efficient Allocation**: The reward per signature is proportional to each validator’s network power, ensuring fair distribution. A validator’s signature representing 1% of network power receives 1% of the available certificate rewards.

**📝 As an example, when a certificate is included in a block:**

*   The participating signers share (1-α) × 10% of the rewards, based on their power.  
    \- The final number for α has not yet been defined, but is suggested to be in the low double digit %.
*   The validator including the certificate receives α × 10% of the rewards.  
    \- The final number for α has not yet been defined, but is suggested to be in the low double digit %.
*   The remaining 90% stays tied to traditional block production.

This structure creates a balanced incentive: validators are motivated to gather as many signatures as possible (maximizing network participation) while also maintaining timely certificate submission (ensuring network efficiency). SPs will continue to receive the same amount of block rewards as before this proposal, assuming they are participating in F3’s finality certificates and including the signatures of others.

### 🗺️ The Roadmap: What’s Next?

This proposal is currently being discussed in the [Filecoin Improvement Proposal (FIP) repository](https://github.com/filecoin-project/FIPs/discussions/1106), and we’re eager to hear feedback from the community. Once F3 is activated on the mainnet, we’ll work more on implementing this reward system.

During our passive testing phase, we observed that 80% of the network’s power has already participated, meaning this change will be seamless for most. Our focus now is on enhancing bandwidth capabilities and ensuring F3 is activated on the mainnet after network version 25, which is scheduled to happen in [early April 2025](https://github.com/filecoin-project/community/discussions/74#discussioncomment-11369195). We aim to activate F3 4-weeks after this, provided the passive testing continues to yield positive results.

Before F3 activation, we will publish a blog post to help everyone prepare for activation. Our priority is to ensure the F3 system remains stable over extended periods before we shift focus back to the incentives proposal. In the meantime, we would love to hear your thoughts and feedback.

See you in the next instalment 👋