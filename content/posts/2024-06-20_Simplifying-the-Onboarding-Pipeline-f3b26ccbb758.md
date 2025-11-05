---
title: Simplifying the Onboarding Pipeline
description: Irene Giacomelli (@Irene_2911) - Follow
date: '2024-06-20T16:07:58.137Z'
categories: []
keywords: []
slug: simplifying-the-onboarding-pipeline-f3b26ccbb758
featured_image: /images/1__7lwh__xf8chnkS__dKLtmxuw.png
---

![](/images/1__7lwh__xf8chnkS__dKLtmxuw.png)

Irene Giacomelli (@Irene\_2911) — [Follow](https://twitter.com/Irene_2911)

20th June, 2024

### When Two is Too Many!

When Filecoin launched in 2020, Storage Providers (SPs) could only store client data by onboarding deal-native sectors. As a result, deals had to be injected into sectors at sealing time without the possibility of being changed later.

This changed thanks to [FIP0019](https://github.com/filecoin-project/FIPs/blob/master/FIPS/fip-0019.md) (“SnapDeal”) and the introduction of the ReplicaUpdate method, which enabled the possibility of injecting data into existing Committed-Capacity (CC) sectors. [FIP0019](https://github.com/filecoin-project/FIPs/blob/master/FIPS/fip-0019.md) aimed to utilize committed capacity already proven in the network to incorporate deals and envisioned the possibility of enabling flexibility in deal dynamics.

As a result, we currently have two distinct data onboarding pipelines:

*   Sealing a deal-native sector
*   Upgrading a CC sector via SnapDeal

Having these two options introduces complexity and risk, potentially slowing down future protocol development and complicating the SP stack software as well as the onboarding process for new SPs. Therefore, we advocate for selecting a single option to streamline the process.

### Sector Onboarding Made Simple

To determine which option should become the standard and which should be deprecated, we need to consider the following:

*   **Streamlining the Onboarding Process  
    **Onboarding a sector involves several computational steps, such as labelling the DRG graph, constructing Merkle-Tree commitments, and generating SNARKs. These tasks are resource-intensive, requiring specialized hardware and software distinct from those used for storage purposes. If we choose “CC → SnapDeal” as the standard pipeline, all sectors will be onboarded as CC sectors, allowing for the delegation of the entire stack of these steps. Conversely, the deal sector pipeline limits task delegation. While SNARK computation can still be outsourced, other tasks like labelling necessitate data flow between the Service Provider (SP) and the external service provider, adding complexity and cost.
*   **Enhancing Delegation with NI-PoRep  
    **The feasibility and efficiency of delegation will improve significantly with the upcoming addition of NI-PoRep ([FIP0092](https://github.com/filecoin-project/FIPs/blob/master/FIPS/fip-0092.md)) to the Filecoin list of PoReps in the upcoming network upgrades. Current PoRep proofs require interaction with the chain, making trustless delegation impossible. NI-PoRep addresses this issue by eliminating the need for chain interaction. Thus, the “CC → SnapDeal” flow, combined with NI-PoRep, paves the way for a “Sealing-as-a-Service” model. In this scenario, SPs can delegate certain activities to external parties offering competitive services at lower costs while they remain responsible only for storing the sector and eventually snapping data.
*   **Towards a Decentralized Service Market  
    **In the envisioned Sealing-as-a-Service (SaaS) scenario, we can achieve a truly decentralized service market for SPs facilitated by projects such as the introduction of a [SealerID](https://github.com/filecoin-project/FIPs/pull/993). This initiative aims to create a competitive and decentralized market for sealing services, ultimately benefiting the SPs with lower costs and greater efficiency.
*   **Ensuring Feasibility of Future Improvements**  
    The “CC → SnapDeal” flow opens up possibilities for new features. For example, when a sector is onboarded as CC, we have the SectorKey proved on-chain, enabling support for [Re-Snap](https://github.com/filecoin-project/FIPs/discussions/538) (allowing sector data to be replaced more than once). Achieving the same improvements for deal-native sectors is more complex and, therefore, slower. In general, deal sectors add significant code complexity in the miner actor and sector onboarding software because they need to support two different ways of committing to data.

**To appreciate the power of incorporating Re-Snap into Filecoin, let’s consider a simple analogy:**

Using containers or organizers in your garage can be incredibly useful. During the summer, you can store your winter jackets in these containers. When the weather turns colder, you can easily swap out your summer clothes for your winter attire. The convenience of having these containers readily available when needed is invaluable.

In a similar vein, by adding Re-Snap, we are developing a service and marketplace where you, as a data client, can purchase storage containers and utilize them to store your data as required. This flexibility ensures that your storage needs are met efficiently, just as you effortlessly manage seasonal clothing changes in your garage.

### Conclusion: Evolving Filecoin Towards Useful Storage

In conclusion, simplifying the data onboarding process by choosing the “CC → SnapDeal” pipeline as the standard can significantly reduce operational complexity, lower costs, and pave the way for future enhancements. By adopting this streamlined approach, the Filecoin network can more efficiently support new SPs, enhance the feasibility of task delegation, and unlock innovative features that drive the decentralized storage market forward.

At the first [Filecoin Dev Summit](https://www.fildev.io/), [Anorth](https://github.com/anorth) mentioned that updatable storage sectors and being able to move and delete data are essential parts of [an efficient foundation for **useful storage**](https://www.youtube.com/watch?v=7ZnkLWus-xw)**.** Simplifying the protocol is not just a matter of reducing complexity; it is a strategic move toward fostering a more robust, scalable, and user-friendly ecosystem.

### References

*   [https://filecoin.io/blog/posts/cc-sector-upgrade-guidelines-and-modeling/](https://filecoin.io/blog/posts/cc-sector-upgrade-guidelines-and-modeling/)
*   Data and Storage Onboarding Pipeline in Filecoin Workshop: [https://www.youtube.com/watch?v=RCURiEZEMe8](https://www.youtube.com/watch?v=RCURiEZEMe8)
*   Flexible sector and data commitments, support for re-snap and deletion: [https://www.youtube.com/watch?v=7ZnkLWus-xw](https://www.youtube.com/watch?v=7ZnkLWus-xw)