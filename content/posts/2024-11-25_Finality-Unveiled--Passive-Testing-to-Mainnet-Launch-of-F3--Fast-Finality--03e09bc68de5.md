---
title: 'Finality Unveiled: Passive Testing to Mainnet Launch of F3 (Fast Finality)'
description: Jennifer Wang (@jennijuju) · Follow  & Orjan Roren (@Phi-rjan) · Follow
date: '2024-11-25T20:56:17.347Z'
categories: []
keywords: []
slug: finality-unveiled-passive-testing-to-mainnet-launch-of-f3-fast-finality-03e09bc68de5
---

![](/images/1__CMBf6ba698Cbrpo7Llpm3w.png)

Jennifer Wang ([@jennijuju](https://twitter.com/_jennijuju)) & Orjan Roren ([@Phi-rjan](https://x.com/OrjanRoren)) · [Chinese Translation](https://mp.weixin.qq.com/s/Ou-HOcFM8UXb89cl5EcdOQ)

**Fast Finality (**[**FIP0086: Fast Finality in Filecoin (F3)**](https://github.com/filecoin-project/FIPs/blob/master/FIPS/fip-0086.md)**) is one of the most transformative upgrades to the Filecoin consensus layer since the mainnet launch. After nearly two years of intensive research and development, F3 is now almost ready for mainnet deployment, promising groundbreaking improvements for the entire ecosystem! By reducing finality time from 900 epochs to just around 2, F3 introduces substantial benefits across the board:**

*   **Faster transaction confirmation**: Token holders and Dapp users will see transactions finalized in minutes, not hours.
*   **Enhanced cross-chain experiences**: Oracles and bridges will finalize transactions and state changes faster. Imagine a future where Dapps can seamlessly publish storage deals to Filecoin from other chains and receive confirmation within minutes once the data is successfully stored on Filecoin!
*   **More efficient light clients**: Node operators like RPC providers and storage providers can use resource-light clients, improving accessibility.
*   **Streamlined Storage Provider Onboarding:** F3 simplifies provider storage onboarding without requiring additional hardware or operational changes. Storage providers utilizing SP clients like Lotus Miner, Venus, or Curio or participating in the [Ramo network](https://x.com/ramo_io) can significantly enhance their onboarding efficiency. With fast finality reducing publish storage deal times by over 2 minutes, providers can achieve faster data onboarding pipelines and deliver improved SLA performance to their clients.
*   and more!

Changing the consensus protocol of a live network is non-trivial, and the change has undergone rigorous audits/testing and numerous rounds of testing in the Calibration network to ensure a smooth and safe transition to Mainnet. While F3 was initially targeted for the network version 24 upgrade, late-stage trials identified two critical issues; more details can be found [here](https://github.com/filecoin-project/core-devs/discussions/150#discussioncomment-11164504). These issues have now been resolved, and the fixes are being validated on Calibration.

### **Next Steps**

The F3 team is now progressing to the final phase of readiness testing on Mainnet. This includes deploying the updated protocol under production traffic and following the [launch testing plan](https://github.com/filecoin-project/go-f3/issues/213). We’ve also published two F3 monitor dashboards ([Mainnet](https://grafana.f3.eng.filoz.org/public/mainnet), [Calibration Testnet](https://grafana.f3.eng.filoz.org/public/calibnet)) for the community to track progress, monitor tipset finalization, node performance, and more to provide more visibility. To get the latest testing updates, subscribe to [this discussion](https://github.com/filecoin-project/lotus/discussions/12287) or join #fil-fast-finality slack channel.

### **A Note for Node Operators**

As we enter the final passive testing phase on Mainnet, it’s important to understand F3’s bandwidth usage patterns. These patterns are predominantly driven by two key factors:

1.  **Message Volume**: F3 needs to hear from participants controlling at least 66% of the network’s power to make decisions.
2.  **Message Size**: Messages grow larger when there are more tipsets to process.

#### **👋🔔 Expected Bandwidth usage during Bootstrap**

During the bootstrap phase, F3 must finalize all epochs since the last finality — approximately 900 epochs. This extended chain finalization causes a temporary spike in bandwidth usage, typically lasting 5–10 minutes, before stabilizing to baseline levels.

#### Other Known High-Bandwidth Scenarios

F3 reaches finality in what’s called an `Instance`: think of an instance as a meeting where everyone shows up to decide on something. For the meeting to adjourn, at least 66% of the attendees must participate. After F3 bootstraps, each instance typically contains a few epochs worth of tipsets in normal operation. This is because F3, as the name suggests, is _fast finality, a_nd in the vast majority of cases, it finalises tipsets within 2 epochs of their incarnation.

There are however cases where F3 finalisation can lag behind the chain progresses, i.e. the “meeting” as it were takes too long to adjourn, for example due to lack of participation or network connectivity issues. Because the Filecoin chain keeps growing, the instances that come after the one that took longer will now have a longer chain to finalise. The longer chain means there will be larger messages since every message exchanged as part of an F3 instance contains the information about the chain being finalised. The larger messages would then lead to a spike in bandwidth usage. Once the F3 instance catches up with the chain, i.e. goes back to finalising tipsets within the few latest epochs, the bandwidth use drops down to the baseline.

If you notice unexpectedly high bandwidth usage for a prolonged length of time linked to F3 testing, please collect logs from your implementation, especially logs from the `f3/gpbft` and `f3/certexchange` log levels and share them in the `[#fil-fast-finality](https://filecoinproject.slack.com/archives/C0556MSR945)` Slack channel. The F3 team actively monitors performance and will work with you to investigate and implement mitigations for any issues.

### **🏁 F3 Launch**

While we will continue collecting data on the soundness of the F3 implementation through passive testing over the next 2–4 weeks, our current plan is to launch F3 with [**nv25**](https://github.com/filecoin-project/core-devs/discussions/183).

Although we’re waiting on final data to confirm F3’s readiness — the F3 team plans to propose an off-cycle nv25 upgrade to FIL-implementers and core devs. If no critical issues arise during this last phase of testing, here’s what we want to propose for the F3 launch:

*   **Early Dec, 2024** - Releases with the Calibration nv25 upgrade & deploy final F3 code (F3 is already active and running)
*   **Mid Dec, 2024**\- Client releases with the Mainnet nv25/F3-activation epoch set
*   **Jan, 2025** - Mainnet nv25/F3-activation

We will keep you informed as we progress and provide updates to the community if there are any changes to the schedule. Thank you for your support as we move toward this exciting upgrade!

P.S: Subscribe to FilOz [Blog](https://medium.com/@filoz) & [Twitter](https://x.com/_FilOz) to get the latest updates of _Finality Unveiled_.

P.P.S: Special thanks to the other F3 core implementers: [Kubuxu](https://github.com/Kubuxu), [Masih](https://github.com/masih), [Stebalien](https://github.com/stebalien), [Anorth](https://github.com/anorth), [BigLep](https://github.com/biglep); other [Lotus](https://github.com/filecoin-project/lotus) implementers like [rvagg](https://github.com/rvagg), and [Forest](https://github.com/ChainSafe/forest) implementers Hailong & [ruseinov](https://github.com/ruseinov) for the hard work to bring F3 to real life. 💙

### Additional Resources

*   [How F3 is Transforming the Filecoin Network](https://www.fil.org/blog/how-f3-is-transforming-the-filecoin-network) — Filecoin Foundation
*   [Fast Finality: Simplifying Bridges to Other Networks](https://www.youtube.com/watch?v=UpLnwT8e6cI) — Masih Derkani
*   [F3 and GossipBFT: Fast finality on longest-chain protocols](https://research.protocol.ai/talks/f3-and-gossipbft-fast-finality-on-longest-chain-protocols/) — Protocol Labs Research
*   Github: [https://github.com/filecoin-project/go-f3](https://github.com/filecoin-project/go-f3)
*   Slack: [#fil-fast-finality](https://filecoinproject.slack.com/archives/C0556MSR945)