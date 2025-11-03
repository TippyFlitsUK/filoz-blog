---
title: Filecoin nv22 Dragon Upgrade AMA Recap
description: Jennifer Wang (@jennijuju) · Follow
date: '2024-06-17T17:30:21.152Z'
categories: []
keywords: []
slug: filecoin-nv22-dragon-upgrade-ama-recap-8c1870518d33
---

![](/images/1__F6pcSvb__YV3Y3xdFXW6iDw.png)

Jennifer Wang (@jennijuju) · [Follow](https://twitter.com/_jennijuju)

April 9th, 2024

> 📣 The next Filecoin network nv22 Dragon 🐉 upgrade is scheduled on April 24th, 2024, at epoch 3855360. More details can be found [here](https://github.com/filecoin-project/community/discussions/74#discussioncomment-8698675), and subscribe to notifications on [statuspage](https://status.filecoin.io/) for Filecoin network status updates!

On March 19th, 2024, the Filecoin community engaged in an Ask Me Anything session with implementers about the upcoming Filecoin Network nv22 upgrade and other implementation updates. We covered topics ranging from Drand, direct data onboarding, built-in actor events, Curio, and more.

_A summary of the answers from the Q&A is below. Some questions and answers have been edited for readability._

**Q: What does the Drand change to quicknet enable for Filecoin?**

Quicknet has a faster period of 3 seconds rather than 30 seconds, allowing for a faster block time in the future, down to 3s instead of the current 30s.  
It enables verification of beacons without keeping the whole beacon history since the previous signature is no longer required, enabling simpler snapshotting/waypoints of the chain. Verification is also slightly faster and is now entirely stateless. The new scheme also allows for time lock encryption, paving the way for time locked mempools to fight MEV and time-locked transactions on Filecoin.

**Q: Are there any estimates on how much lighter the Filecoin headers will be, with the smaller signatures that Drand quicknet has?**

48 bytes per beacon entry vs. 96 bytes (even less if the entire beacon, including randomness and previous signature is stored by mistake).

**Q: Can I use Forest with the Lotus-Miner?**

No, not yet. There are initiatives for Forest in 2024 to tackle this subject.

**Q: Does Direct Data Onboarding (DDO) support on-chain payments?**

If you are using the DDO pipeline, you can choose to notify the f05 builtin actor and leverage the on-chain payment mechanism there. In the future, users can build other programmable storage markets with customized on-chain payment logics.

**Q: How will the new onboarding methods introduced by FIP-0076 affect existing workflows for clients and storage providers?**

*   All existing workflows will still be supported; 0076 doesn’t mandate change
*   FIP-0076/DDO opens up new options for storage providers and clients to negotiate onboarding mechanisms and agreements separated from the market actor, it also allows interaction with the market actor by treating it as a “notified” actor — which may extend to alternative actors in future.
*   Currently, non-market deals will require alternative mechanisms for agreement between client and storage provider, in the future, user-programmed actors can assist in the mediation/market mechanism
*   Boost will be supporting DDO onboarding workflows _for verified data_. Currently non-verified onboarding won’t be supported by Boost but may be added in the future.

**Q: If DDO/FIP-0076 is successful and we see new deal marketplaces pop up that gains traction, what other future enhancements/changes could be made?**

*   The new deal marketplaces could offer many features:
*   deal renewal, transfer, or re-negotiation;
*   deals for data consuming multiple sectors;
*   very long or perpetual deal duration;
*   native support for replication and repair;
*   alternate payment mechanisms;
*   higher efficiency, off-chain or L2 state;
*   and much more.
*   Potential follow-on changes to the core L1 protocol include:
*   re-snap (replacing sector data), separating data lifetime from sector lifetime;
*   multi-sector Fil+ allocations
*   optionally storing a sector unsealed CID on-chain

**Q: What are the benefits of FIP-0083 for storage providers and clients within the Filecoin ecosystem?**

*   This FIP lays the groundwork for built-in Actor events that have been missing in Filecoin. Actor events allow for better introspection and observability of state transitions in Actors and enable Filecoin monitoring and observability tooling to start relying on them as the source of truth for Filecoin activity. This should indirectly benefit clients & SPs as they can then use this better tooling/observability.
*   This FIP will ship with a select subset of events in the VerifReg, Market, and Miner Actor to allow for better introspection of deal, sector, and datacap lifecycle but the goal is to ship more events in subsequent FIPs across all Actors based on user feedback. FIP-0083 is only the first step in the Actor events workstream.

**Q: What is Forest’s roadmap this year? Can I use it as a full chain node?**

Forest can be used as a lightweight RPC node (caveat: only a subset of Lotus’ RPC methods are supported). A detailed roadmap for 2024 will be published soon. It will definitely include RPC completeness so that Forest can be seamlessly swapped with Lotus for API providers.

**Q: Is there a documented specification to potentially interface with Curio (Lotus-Miner v2)?**

There are some documents describing the HarmonyTask scheduler, and a whole bunch of docs describing Curios architecture. Full user documentation is actively being worked on, and will include specs required to interface with Curio.

**Q: When will BLS12–381 pairing precompiles be available on FEVM?**

The availability of BLS12–381 pairing precompiles on the Filecoin EVM (FEVM) is contingent on the progress and acceptance of the FIP discussing this feature here: [https://github.com/filecoin-project/FIPs/discussions/846](https://github.com/filecoin-project/FIPs/discussions/846). As of now, there isn’t a specific timeline provided for when these precompiles will be available.

For builders and stakeholders interested in having this feature implemented, it is recommended to actively participate in the discussion by posting their use cases and expressing their need for BLS12–381 pairing precompiles. This will help core developers and implementers gauge the demand and potentially prioritize its implementation based on the level of community support.

**Q: How do I keep getting visibility into data stored on Filecoin post-DDO, like the information available on** [**filecoin.tools**](http://filecoin.tools/) **or any Filecoin CID checker?**

DDO distinguishes between the data stored in sectors, and any (optional) deals and/or Fil+ claim for that data.

*   The data commitment for each piece can be extracted from either the onboarding messages or the FIP-0083 sector activation events. The size of the non-zero data stored can also be read out of sector state on chain.
*   Deals made with the built-in storage market actor (f05) can be observed in the actor’s chain state. This is the same as today, but DDO introduces the possibility for a sector to have data _without_ any deal. A non-existent deal cannot be observed.
*   Fil+ claims can be observed in the chain state of the built-in verified registry actor (f06). These records include the SP, sector identifier, and data commitment.

We hope and expect existing tools to be updated to reflect the distinction between data and deals, and/or new tools to improve upon them over time.

**Q: What is Curio that’s mentioned above? How is it different from lotus-miner or venus cluster?**

*   Curio is a rewrite of lotus-miner which aims to be much more scalable and highly-available. The new architecture removes all single points of failure, and removes all scaling bottlenecks.
*   Curio storage layout is compatible with lotus-miner, and there is an easy migration path from lotus-miner to Curio which doesn’t require moving of any sector data. Migrating back from Curio to lotus-miner is also possible.
*   No hardware changes are required to switch from lotus-miner to Curio — Curio replaces the centralized lotus-miner process with YugabyteDB (highly-available Postgres-compatible database), and makes each “worker” node make its own decisions, which results in much better scheduling outcomes. Each node in the new system can handle tasks for multiple on-chain Miner Actors with shared pool of resources (this does allow sealing for miner actors which aren’t owned by the operator of the cluster, which in the future may enable SPs with hardware to become (Un)Sealing-as-a-Service providers)
*   Curio will also support SupraSeal fully, enabling >90% reduction in sealing cost.