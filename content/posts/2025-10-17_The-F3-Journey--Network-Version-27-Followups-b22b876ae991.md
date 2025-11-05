---
title: 'The F3 Journey: Network Version 27 Followups'
description: Steve Loeppky (@big_lep)
date: '2025-10-17T16:24:41.807Z'
categories: []
keywords: []
slug: the-f3-journey-network-version-27-followups-b22b876ae991
featured_image: /images/1__zycrAzfsaON__I3LKpeMZjA.png
---

![](/images/1__zycrAzfsaON__I3LKpeMZjA.png)

Steve Loeppky (@big\_lep)

With the recently completed [Network Version 27 “Golden Week” upgrade](https://fil.org/blog/announcing-the-filecoin-network-v27-golden-week-upgrade), the whole network is benefiting from F3 improvements that have rolled out since F3 was first activated on Filecoin Mainnet a little over 5 months ago…

#### 🔬 F3 Aware APIs

Various APIs have been updated or added to consult the F3 sub-system for finality while still falling back to Expected Consensus (EC):

*   _Ethereum APIs —_ Ethereum APIs that use `finalized` and `safe`. No client changes are needed. Faster finality is being returned transparently.
*   `ChainGetFinalizedTipSet` — The fully-maintained `/v1` ”JSON-RPC” APIs now have `[ChainGetFinalizedTipSet](https://docs.filecoin.io/reference/json-rpc/chain#chaingetfinalizedtipset)`, which serves as a convenient way to get a finalized tipset to use with other `/v1` APIs.
*   _Experimental_ `_/v2_` _APIs —_ A significant redesign of Filecoin's RPC interface was started for non-Ethereum APIs with important goals of more intuitive interaction patterns, expressiveness with selectors, smaller footprint, future extensibility, and of course, f3 awareness in all relevant APIs. This effort is not complete, but can be used today. Learn more in the [V2 API documentation](https://www.notion.so/Filecoin-V2-APIs-1d0dc41950c1808b914de5966d501658?pvs=21).

Here’s a summary of F3-aware APIs:

![](/images/1__e9qlep__DwHspwFhwS6iRQQ.png)

All of these APIs can be used today in one’s local Lotus node or with [RPC providers](https://docs.filecoin.io/networks/mainnet/rpcs) like Glif nodes.

#### 🔀 F3 Augmented Snapshots

[FRC-0108](https://github.com/filecoin-project/FIPs/blob/master/FRCs/frc-0108.md#frc-0108-filecoin-snapshot-format) expands the Filecoin snapshot format to include F3 finality certificates. Previously, nodes needed to get the F3 finality certificate chain from peers outside of the snapshot, which could take hours. Now the F3 state is bundled with the snapshot, both reducing the time and bandwidth required for new nodes to join the network with fast finality. F3-augmented snapshots are produced and hosted by the Forest infra team ([download links](https://github.com/ChainSafe/forest/issues/5627)). As all node implementations (Lotus, Forest, Venus) support this updated format, [https://forest-archive.chainsafe.dev/latest/mainnet](https://forest-archive.chainsafe.dev/latest/mainnet) switched to it by default on October 7.

#### 💪 Resiliency and performance improvements

There were a couple of cases of F3 stalling to make progress after its April activation ([1](https://github.com/filecoin-project/lotus/issues/13094), [2](https://github.com/filecoin-project/lotus/issues/13208)). These events resulted in a whole set of resiliency and performance improvements within go-f3 that the whole network has now adopted. Now that these improvements have been deployed, they’re already showing their impact in the week after the network upgrade. For example, F3 has been staying within 10 epochs from head.

![](/images/1__kM6iF0eC16zZyLTcnrj2og.png)

#### 📚 Documentation for operators

We wrote an [exchange and RPC providers guide to F3](https://www.notion.so/Exchange-and-RPC-providers-guide-to-F3-Fast-Finality-105dc41950c180c49175e4b3afcc5923?pvs=21) to help infrastructure providers to understand and onboard with F3. [Public dashboards](https://www.notion.so/F3-Operational-Excellence-5cdce4f1aa6e4c398b475f6e690c47fe?pvs=21) have also been updated.

#### 🔒 Security fixes

Multiple fixes were made to secure F3 before the NV27 upgrade. These have now been publicly disclosed given the network is patched with the software updates as part of the network upgrade:

1.  [**Cached Justification Verification Bypass in go-f3**](https://github.com/filecoin-project/go-f3/security/advisories/GHSA-7pq9-rf9p-wcrf)
2.  [**Integer overflow leading to panic go-f3 module**](https://github.com/filecoin-project/go-f3/security/advisories/GHSA-g99p-47x7-mq88)

#### ☑️ Initial powertable CID has been set by default

After F3’s activation in April, there were [followup actions for SPs to take to participate in F3](https://medium.com/@filoz/the-f3-journey-now-that-f3-is-active-on-mainnet-there-are-follow-up-steps-to-take-a13a93268c29). All NV27-compatible node software now has this set by default. We believe this slightly increased F3 participation.

#### 👀 Looking ahead

F3 is not being actively enhanced currently by FilOz, but the ongoing and future workstreams center around:

1.  Adoption — There have already been efforts to support F3 adoption, and the seamless upgrading of `/v1`Ethereum APIs to be “F3 aware” as discussed above certainly helps. But there is more to do, and we’re [tracking partner adoptions here](https://www.notion.so/Adoption-Partner-Tracking-1d2dc41950c1806c967de0cb6290d36b?pvs=21)!
2.  Increase participation — Looking at the last ~30 days, F3 participation below continues to average around 72%. While this is above the 66.6% requirement, it still leaves us more susceptible for stalls ([as we saw during the nv27 upgrade](https://github.com/filecoin-project/lotus/issues/13359)). Tooling has been built to highlight SPs not participating in F3 ([example slack thread](https://filecoinproject.slack.com/archives/C02GQUMFQVA/p1755231004769599)), but the right long term solution is to [incentivize participation](https://github.com/filecoin-project/FIPs/discussions/1106).

![](/images/1__pxSQaH7L6GRJuDYJIADWdA.png)

Thank you to the community for your participation and feedback. As always, please don’t hesitate to reach out at [#fil-fast-finality](https://filecoinproject.slack.com/archives/C0556MSR945) if you have questions! 🙏