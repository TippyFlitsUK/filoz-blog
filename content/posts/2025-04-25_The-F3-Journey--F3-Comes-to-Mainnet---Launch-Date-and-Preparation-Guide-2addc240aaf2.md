---
title: 'The F3 Journey: F3 Comes to Mainnet - Launch Date and Preparation Guide'
description: Orjan Roren (@Phi-rjan) · Follow
date: '2025-04-25T10:23:52.809Z'
categories: []
keywords: []
slug: the-f3-journey-f3-comes-to-mainnet-launch-date-and-preparation-guide-2addc240aaf2
---

![](/images/1__Cj6eyHK4RYGUdU6D__neLZg.png)

Orjan Roren (@Phi-rjan) · [Follow](https://x.com/OrjanRoren)

After a long time of research, implementation work, and rigorous testing, we’re thrilled to announce that Fast Finality (F3) is being activated on the Filecoin Mainnet! This milestone represents the culmination of a long journey that began with theoretical research on consensus mechanisms, progressed through complex protocol design, survived countless whiteboard sessions and developer hours, with final parameters emerging from extensive passive testing ([nv24](https://github.com/filecoin-project/go-f3/issues/213), [nv25](https://github.com/filecoin-project/go-f3/issues/802)). It will soon become a reality that will transform the Filecoin network!

F3’s story began with early research into how faster finality could be brought to Filecoin’s unique architecture. The first research papers and proof of concept were created by the [ConsensusLab team](https://research.protocol.ai/groups/consensuslab/), followed by the technical specifications and implementations, and then by the recent extensive passive testing at 100% network scale. Each step has built upon the last to create a solution that delivers on the promise of a faster, more reliable transaction finality in Filecoin.

What once seemed like a distant goal is now mere days away from becoming an integral part of the network. This isn’t just a technical upgrade; adding another consensus mechanism to the Filecoin network will empower builders, improve user experiences, and strengthen Filecoin’s position as a cutting-edge decentralized storage infrastructure.

### 🗓️ Mark Your Calendars: F3 Launch Date

**🚀 F3 will be activated on the Filecoin mainnet on 2025–04–29 at 10:00 UTC (epoch 4920480) 🚀**

The F3 activation on Mainnet follows the successful deployment of network version 25 on April 14th, which comes after [extensive passive testing that has consistently demonstrated F3’s readiness for mainnet](https://github.com/filecoin-project/go-f3/issues/802).

After 17 rounds of passive testing after nv25 activated, we have identified four F3 parameter adjustments that played a key role in network stability and performance, which we have adjusted accordingly:

**QualityDeltaMultiplier:** increased from 1 to 8

*   The `QualityDeltaMultiplier` extends the `QUALITY` phase timeout to facilitate better propagation of proposals across the network, while keeping the timeout for other phases unaffected to maintain fast and consistent progress towards finalization.

**Internal pub-sub channel buffer sizes:** the internal buffer sizes for queueing the pub-sub messages prior to processing were increased significantly to eliminate dropping messages before they get to be processed.

*   This helped address a message processing bottleneck, caused by slow calls to fetch the chain state as part of message validation and instance start. Additionally, all F3 messages are processed sequentially to guarantee a consistent state. The increase in buffer size allows for a larger number of messages to be queued up before being processed, which helps to ensure that messages are not dropped and that the system can keep up with the incoming message rate.

**MaxChainLength:** reduced from 100 to 20.

*   The longer the chain, the more state needs to be fetched and validated, which can lead to performance issues, considering the slow response time of interacting with the chain state. The `MaxChainLength` parameter is used to limit the number of tipsets that are picked for each F3 finalization round. By reducing this value, we can reduce the amount of state that needs to be fetched and validated, which can help to improve performance and further aid F3 to keep up with the rate of incoming messages.

**HeadLookback:** set to 4.

*   By setting this value to 4, we can ensure that F3 can finalize blocks that are at least 4 blocks behind the chain head. This contributes to the correctness of F3 in terms of design goals: graceful co-existence with the EC chain.

As we shared our blog post [Delegated Authority for Faster Mainnet Activation of F3](https://medium.com/@filoz/the-f3-journey-delegated-authority-for-faster-mainnet-activation-of-f3-98f9aa69eb0c), we’re able to accelerate the activation timeline on Mainnet thanks to the [delegated authority mechanism](https://github.com/filecoin-project/FIPs/blob/master/FRCs/frc-0099.md) that allowed us to fine-tune parameters and set these parameters through a contract without waiting for an additional network upgrade. (You can follow the activation steps [here](https://github.com/filecoin-project/f3-activation-contract/issues/22).)

### 🔍 What to Expect When F3 gets activated

First of all there are two phases to be aware of when F3 gets activated on `2025-04-29 at 10:00 UTC`.

1.  `The Bootstrap Phase`: Where F3 catches up to the latest state
2.  `The Steady State Phase`: The ongoing finalization of the chain after the initial Bootstrap phase

The Bootstrap is expected to take approximately 1 hour and 30 minutes, and the bandwidth usage during this period is estimated to be **≈500KiB Up and Down**. After the Bootstrap phase has completed, and we are entering the steady state of F3 finalizing the chain, you can expect the bandwidth usage to be around **≈1 MiB Up and Down**.

Here are the metrics we gathered during the bootstrap phase of passive testing round 66 on Mainnet, which has the same parameters as the one that is being activated:

![](/images/1__JoVDo5FXi__VUfTqb__5A50Q.png)
![](/images/1__70MHlEAMF76KLH1mbUrrXg.png)

### 📊 Monitoring F3 Performance

We’ve developed several tools to help you monitor the F3 activation, ensuring that you are participating in F3 and monitoring its performance over time:

**F3 Grafana Dashboard:**

*   After setting up [Grafana dashboards for your Lotus instance](https://lotus.filecoin.io/tutorials/lotus/grafana-dashboard/), you can import the [F3Dashboard.json](https://github.com/filecoin-project/lotus/blob/master/metrics/grafana/F3Dashboard.json) template.

![](/images/1__sGKV7YL7cCh__fA39nwlD6Q.png)

*   One can compare their own node’s metrics to the [F3 Public Dashboard](https://grafana.f3.eng.filoz.org/public/mainnet).

**CLI commands:** `**lotus f3**` and its sub-commands:

*   `lotus f3 status`: Provides a quick overview of F3's operational status, showing whether F3 is running, the current instance, round, phase, and manifest details.
*   `lotus f3 list-miners`: This command lists the minerIDs that are connected to the Lotus node and participating in F3.
*   `lotus f3 powertable`: Sub-commands for interacting with [F3 power tables](https://github.com/filecoin-project/FIPs/blob/master/FIPS/fip-0086.md#power-table-and-consensus-committee).
*   `lotus f3 powertable get`: Retrieves the power table for a specific instance, showing the distribution of power among F3 participants.
*   `lotus f3 powertable get-proportion`: Calculates the total proportion of power for the specified minerIDs, useful for understanding your voting power within the F3 system.
*   `lotus f3 certs`: Sub-commands for managing interactions with [F3 finality certificates](https://github.com/filecoin-project/FIPs/blob/master/FIPS/fip-0086.md#synchronization-of-participants-across-instances).
*   `lotus f3 certs get`: Retrieves a finality certificate for a specific instance (or the latest if none specified).
*   `lotus f3 certs list`: Shows a range of finality certificates, allowing you to track F3's progress over time.
*   `lotus f3 manifest`: Displays the current F3 manifest, which contains the system's configuration parameters, including committee lookback, initial power table, and other critical settings.

### 🤝 Community Support

The F3 team will be providing support during and after the activation period. We encourage all storage providers and node operators that have any questions with regards to any logs or issues that may arise to post and ask in the `#fil-fast-finality` or `#fil-help` channels.

For Storage Providers we also recommend reading through some of the common log messages that you can expect to see after activation, in the [Storage Providers guide to F3 (Fast Finality)](https://filoznotebook.notion.site/The-Storage-Provider-s-Guide-to-F3-Fast-Finality-109dc41950c180319892cf47eeb1b56d) .

### 🗺️ Looking Forward: From Activation to Utilization

The activation of F3 on mainnet represents a significant milestone for Filecoin, though it’s important to understand this is just the beginning of F3’s journey for the user experience. While F3 will be active on the network, users won’t immediately experience its full benefits until ecosystem partners integrate with it through upcoming APIs.

Therefore, our focus in Q2 is getting the API ready and helping users integrate it. Our plan going forward is:

*   **Developing a v2 API in Lotus that leverages F3**: This API foundation is essential for exchanges, explorers, and other services to benefit from the faster finality that F3 brings.
*   **Ethereum-compatible API support for bridges**: Work has already begun on extending the Eth\* API support to incorporate the “finalized” concept, making it easier for bridges and dapps to integrate F3’s finality guarantees.

You can follow along with all these effort [here](https://github.com/filecoin-project/lotus/issues/12987). These integrations will begin rolling out soon with [Lotus v1.33.0](https://github.com/filecoin-project/lotus/issues/13004) (with more follow-ups to come), bringing the tangible benefits of fast finality to the broader Filecoin ecosystem.

We want to express gratitude to the entire Filecoin community for your patience, feedback, and support throughout this journey. 💙 F3 has been made possible by a dedicated group of engineers, researchers, and protocol designers, and we are now looking forward to seeing F3 being implemented in strategic areas in the ecosystem.

See you on the other side of activation 🫡