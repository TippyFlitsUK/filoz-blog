---
title: "\U0001F4B0 The Power of Aggregation: Real Savings for Storage Providers"
description: Orjan Roren (@Phi-rjan) · Follow
date: '2025-05-27T16:33:10.876Z'
categories: []
keywords: []
slug: the-power-of-aggregation-real-savings-for-storage-providers-87f62aa9b018
featured_image: /images/1__R87j6ogAORsh2eFNL1v__Gw.png
---

![](/images/1__R87j6ogAORsh2eFNL1v__Gw.png)

Orjan Roren (@Phi-rjan) · [Follow](https://x.com/OrjanRoren)

One of the most significant benefits of FIP-100 is the removal of the batch balancer fee that previously made proof aggregation cost-ineffective at normal base-fee levels, and only rational when it was above the batch-balancer fee threshold. With the batch balancer now removed, it is always the optimal strategy to aggregate, and storage providers can fully leverage aggregation to dramatically reduce their gas costs. _Let’s look at some real on-chain examples that showcase these savings:_

![](/images/1__mb9Wl3XhNi89vlcaAdh1Eg.png)

The difference is striking. Storage providers using aggregation are reducing their per-sector gas significantly compared to storage providers that are committing sectors with batching. This translates to substantial FIL savings and helps free up valuable chain bandwidth for the entire network.

### 🔄 Network-Wide Benefits

Since the activation of FIP-100 and network upgrade marked by the red line, we’ve observed an uptick in SPs adopting aggregation strategies:

![](/images/1__BvErqGJbgm__ICKU1FIPJGQ.png)

The network should aim to minimise the number of batched sectors to create a cycle of benefits. Beyond lowering onboarding costs per sector for Storage Providers (SPs), increased aggregation adoption can deliver:

1.  **Stable low base fees:** Less pressure on the blockspace maintains more consistent gas prices at the desired minimum levels.
2.  **Higher potential onboarding rates:** Reduced blockspace usage through aggregation of ProveCommitSectors3 allows for a higher potential daily sector onboarding rate in the network.

### 🌟 Are you configured correctly for Aggregation?

To ensure you’re taking full advantage of these savings, check if you are sending aggregate or batch **ProveCommitSector3** messages to the network:

1\. Navigate to [Filutils.com](https://www.filutils.com/en/), the only explorer that decodes message parameters for you, and search for your `MinerID`:

![](/images/1__UXQsrr3CPPBpRbNlQcLJlg.png)

2\. Once you’re on your MinerID page, scroll down to the “Message List” section. In the drop-down menu on the right side, select to filter by `ProveCommitSectors3` messages:

![](/images/1__06lJmak67nYUNGzXprphEQ.png)

3\. Click on one of the most recent MessageIDs for a ProveCommitSectors3 message from your MinerID and scroll down to the “Others” section. In the “Params” section, if you see `"AggregateProof": null`, this indicates a batch message—you can save significantly by switching to aggregation. If you see `"AggregateProof"` followed by a long string of text, you're already successfully aggregating your ProveCommitSectors3 messages. 👌

![](/images/1__CEovU6gACo4I3u3WeOS0Ww.png)
![](/images/1__FylNBjEuIFZGwBErOP72mg.png)

If you checked your MinerID on [Filutils](https://www.filutils.com/en/), and see that you are submitting batch messages to the network, these are the steps you can take to start aggregating instead:

### Lotus-Miner SPs:

*   Ensure that you have set `AggregateCommits=true` in your lotus-miner’s `config.toml` file.
*   Ensure that you have set `MinCommitBatch = 4` in your lotus-miner’s `config.toml` file.  
    _Ensure that you are only calling the_ `_lotus-miner sectors batching commit_` _command after building up more than 4 sectors. Based on the data from the chain, we have seen aggregated messages as high as 200 sectors, but how many sectors you want to queue up, before aggregating, really comes down to preference._

### Venus SPs:

*   Ensure that you have set Enabled = true and Threshold = 4 in the \[Miners.Commitment.Prove.Batch\] section of the damocles-manager configuration file.

### Curio SPs:

*   Curio has [updated their settings to remove](https://github.com/filecoin-project/curio/pull/492) the previous base-fee threshold for sector aggregation in ProveCommitSectors3.  
    _This change is included in_ [_Curio v1.25.1_](https://github.com/filecoin-project/curio/releases/tag/v1.25.1)_. After updating to this release, your ProveCommitSectors3 messages will automatically be aggregated when you publish more than 4 sectors._

### 🤝 Join the Conversation

We’re excited to see that FIP-100 is reducing the BaseFee in the network by ensuring that it is always optimal to aggregate messages, and that Storage Providers have started to aggregate messages to save more. Join the discussion in the [#fil-tmp-gas-costs-working-group](https://filecoinproject.slack.com/archives/C085VRJK92L) channel on Filecoin Slack. If you have any questions about aggregation, please reach out to your implementation’s help channel.