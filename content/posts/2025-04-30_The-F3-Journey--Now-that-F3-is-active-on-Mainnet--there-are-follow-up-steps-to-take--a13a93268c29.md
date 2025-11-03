---
title: >-
  The F3 Journey: Now that F3 is active on Mainnet, there are follow-up steps to
  take…
description: Steve Loeppky (@big_lep)
date: '2025-04-30T14:40:34.195Z'
categories: []
keywords: []
slug: the-f3-journey-now-that-f3-is-active-on-mainnet-there-are-follow-up-steps-to-take-a13a93268c29
---

![](/images/1__kF9FKm9uWsc4K2E3o__Zgkg.png)

Steve Loeppky ([@big\_lep](https://x.com/big_lep))

**As of epoch 4919580, F3 is active on Mainnet! Finality is now just a couple of minutes away — a huge step forward for the Filecoin network.**

#### 🎬 **Action Required**

As a result, node operators should set the initial power table CID so that they don’t need to rely on past blockchain state to compute this. Failure to do so will cause nodes without historical state leading up to the bootstrap epoch `2025-04-29T10:00:00Z` to not participate in F3. Setting the initial power table CID can be accomplished via two means:

1.  Upgrade to the [Lotus 1.32.3](https://github.com/filecoin-project/lotus/releases/tag/v1.32.3) on your Lotus Chain Node. This small patch sets the initial power table in the build constants ([diff](https://github.com/filecoin-project/lotus/compare/release/v1.32.2...release/v1.32.3)).  
    _Storage providers only need to upgrade their Lotus chain node to this release._
2.  Set the `F3_INITIAL_POWERTABLE_CID` environment variable to: `export F3_INITIAL_POWERTABLE_CID="bafy2bzacecklgxd2eksmodvhgurqvorkg3wamgqkrunir3al2gchv2cikgmbu"` before starting your node.

#### ❓ **Why is this necessary?**

During the bootstrap process, F3 began its operation at epoch `4918680`, taking the power table from the state at that epoch to start finalising tipsets. The first certificate refers to the above power table by CID, but there can be many first certificates, and their distinguishing factor is which power table they were created by. The above CID is the genesis information of F3 for Filecoin’s Mainnet, and thus the node requires it to distinguish it from any other possible certificate sequence.

As long as the node possesses the full state for epoch `4918680`, it can use that state to begin following the certificate sequence, but without it, the node needs a direction telling it “F3 started with power table with this CID”.

#### ❓ **Why wasn’t this included in the** [**f3 activation contract**](https://github.com/filecoin-project/f3-activation-contract)**, where all the other F3 activation parameters were set?**

The F3 activation contract was designed with the mindset to “have as small a scope as necessary”. As a result, the initial power table CID wasn’t included. In retrospect, it may have been wise for the contract to have a second method to allow the implementers to set-once-and-only-once the power table CID after the bootstrap epoch.

#### ❓ Does the F3 engineering team have the ability to perform any kind of passive testing or parameter adjusting on mainnet?

No, we are back to the permissionless network that we know and love. Per [FRC-0099](https://github.com/filecoin-project/FIPs/blob/master/FRCs/frc-0099.md), the F3 activation contract was a use-once mechanism. Given that the bootstrap epoch has passed, the contract is now immutable.

#### 👀 Looking ahead

With F3 active on Mainnet, it’s time for builders to start planning to take advantage of these new capabilities. The upcoming [Lotus 1.33.0 release](https://github.com/filecoin-project/lotus/issues/13004) (RC1 targeting 2025–05–01) exposes v2 APIs that are F3-aware. Your input on these APIs is welcome in the [#fil-implementers](https://filecoinproject.slack.com/archives/C05P37R9KQD) Slack channel or [this issue](https://github.com/filecoin-project/lotus/issues/12987).

F3 implementers are active on various [post-activation cleanup tasks](https://github.com/orgs/filecoin-project/projects/114/views/2?filterQuery=-status%3AEpic+-milestone%3A%22MX*%22+-milestone%3A%22Milestone+0*%22+-milestone%3A%22Milestone+1*%22+milestone%3A%22M4%3A+Important+optimization+post+activation%22), including [inlining all the activation parameters](https://github.com/filecoin-project/lotus/issues/13052), [removing dead code](https://github.com/filecoin-project/lotus/issues/12971), and [augmenting snapshots with F3 information](https://github.com/filecoin-project/go-f3/issues/480).

As always, please don’t hesitate to reach out in [#fil-fast-finality](https://filecoinproject.slack.com/archives/C0556MSR945) if you have questions! 🙏