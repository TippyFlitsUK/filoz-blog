---
title: 'PoRep, PDP, Proof of Delivery: Different Proofs for Different Use Cases'
description: Luca Nizzardo (@luca_nizzardo) - Follow
date: '2024-07-29T14:46:58.320Z'
categories: []
keywords: []
slug: porep-pdp-proof-of-delivery-different-proofs-for-different-use-cases-e6daede195fb
---

![](/images/1__ycc__JGSdqG8JstYHFvB8IQ.jpeg)

Luca Nizzardo (@luca\_nizzardo) — [Follow](https://twitter.com/luca_nizzardo)

Proof of Replication (PoRep) ensures that data is encoded in an incompressible way, which is crucial for building storage-based consensus \[2\].

However, empowering storage-based consensus is not the sole aim of a decentralized storage network like Filecoin. Different use cases require different key features, which are often orthogonal and challenging to achieve with a single tool. For instance, faster retrieval and economic incentives for retrieval (or penalties for missing retrieval) are other features a storage network should target in the long run.

One way to accommodate different user needs and preserve network security is to employ different proofs targeting different use cases.

In this blog post, we explore what can be seen as a storage trilemma:

*   Persistent storage guarantees
*   Provably enabled efficient retrieval
*   Provable guaranteed retrieval.

Each functionality comes at a cost, which can be “paid” to accommodate different user needs.

#### PoRep: Persistent Storage Guarantee for Storage-Based Consensus

Proof of Replication probabilistically ensures that after a preprocessing step, a piece of data is encoded in a unique and incompressible way. Thus, it is impossible for a malicious entity to fake a storage claim. This is crucial when consensus power is represented by the amount of storage a storage provider claims and proves. Moreover, PoRep ensures that data can be replicated within the network by having distinct encodings of the same data.

Nevertheless, persistent storage and replicated storage guarantees come at a cost: the preprocessing step is somewhat expensive (both in terms of cost and time) for both encoding and decoding. While this is not an issue when targeting network security and cold storage (i.e., encoding happening once, decoding happening with low frequency), it is not ideal when data needs to be decoded frequently and when users need efficient retrieval.

#### PDP: Periodical Data Access Guarantee to Provably Enable Efficient Retrieval

Proof of Data Possession (PDP) probabilistically ensures that a piece of data is accessible at a given point in time. It does not need a heavy preprocessing/encoding step and can be performed on clear data. Every time a proving step is performed, it ensures that the data is accessible at that point in time. Periodical data access is guaranteed if that check is repeated with some frequency.

If a client requires efficient data retrieval, PDP can be used to ensure that a copy of the data is periodically accessible and can be efficiently served by a storage provider (SP). In this sense, PDP is a useful add-on for targeting efficient retrievals.

However, PDP cannot replace PoRep for building storage-based consensus. PDP does not ensure replication of the same data or guarantee incompressibility in a decentralized network, where a malicious entity could act as both a Storage Provider and a Client.

Finally, while PDP can prove that efficient retrieval is possible, it does not guarantee that retrieval will be ensured. A malicious storage provider can still deny the retrieval service. Nonetheless, PDP eliminates the need for an expensive decoding step to access the data.

#### Proof of Delivery: Data Retrieval via Trusted Entity

Classical results from information theory show that proof of delivery is impossible without a trusted third party. It is impossible to build a protocol involving a client and a storage provider only, which ensures data delivery. On one hand, a malicious storage provider can always deny providing the retrieval service, while on the other hand, a malicious client can always deny the receipt of the data.

The way to overcome this limitation is the introduction of a trusted third party, which can be represented by, for instance, a consortium that resolves disputes between SP and Client. This is, for instance, the case of the Retriev Protocol \[5\]. Proof of delivery protocols provide higher guarantees at the price of a less lightweight protocol setup.

#### No Perfect Proof for all, but a Specific Proof for Each Use Case

In conclusion, each use case has its own optimal proof system, depending on the specific application requirements. Selecting the most suitable proof system for each use case ensures that individual needs are met effectively. The coexistence of different proof systems in Filecoin allows for a broader range of storage options, accommodating a wider set of applications and addressing diverse needs for both clients and storage providers.

#### **What’s Next?**

The FilOz team is currently focusing on PDP to augment the Filecoin offer and target hot storage, check out the recent talk from [Filecoin Dev Summit Brussels](https://www.fildev.io/). To follow our work, join the [#fil-pdp](https://filecoinproject.slack.com/archives/C0717TGU7V2) channel on Slack!

> **References**

> \[1\] Tight Proofs of Space and Replication  
> [https://eprint.iacr.org/2018/702](https://eprint.iacr.org/2018/702)

> \[2\] Filecoin Proof of Useful Space  
> [https://drive.google.com/file/d/1notObdkPT1BCztgspIpzSUAzWSrM8h81/view](https://drive.google.com/file/d/1notObdkPT1BCztgspIpzSUAzWSrM8h81/view)

> \[3\] Limits on the security of coin flips when half the processors are faulty  
> [https://dl.acm.org/doi/10.1145/12130.12168](https://dl.acm.org/doi/10.1145/12130.12168)

> \[4\] Provable Data Possession at Untrusted Stores  
> [https://eprint.iacr.org/2007/202](https://eprint.iacr.org/2007/202)

> \[5\] Retriev.org project  
> [https://www.retriev.org/#/](https://www.retriev.org/#/)