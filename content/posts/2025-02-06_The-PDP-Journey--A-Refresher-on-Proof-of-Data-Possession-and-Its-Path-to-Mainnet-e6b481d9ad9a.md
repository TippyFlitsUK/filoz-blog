---
title: >-
  The PDP Journey: A Refresher on Proof of Data Possession and Its Path to
  Mainnet
description: ''
date: '2025-02-06T15:50:33.101Z'
categories: []
keywords: []
slug: the-pdp-journey-a-refresher-on-proof-of-data-possession-and-its-path-to-mainnet-e6b481d9ad9a
featured_image: /images/1__xZnptkLPaBjO5zecjFSdnA.png
---

![](/images/1__xZnptkLPaBjO5zecjFSdnA.png)

Orjan Roren ([@Phi-rjan](https://x.com/OrjanRoren)) · [Chinese Translation](https://mp.weixin.qq.com/s/UWrQ77wrNL5NqZABXVmheg)

In a previous article, [PoRep, PDP, Proof of Delivery: Different Proofs for Different Use Cases](https://medium.com/@filoz/porep-pdp-proof-of-delivery-different-proofs-for-different-use-cases-e6daede195fb), we explored how various proof systems serve distinct purposes in Filecoin’s ecosystem and introduced Proof of Data Possession (PDP). Since then, significant progress has been made in PDP’s development. Today, we’re excited to launch a new blog series — **_The PDP Journey_** — where we'll explore the development of Proof of Data Possession and follow its progress toward Mainnet contract deployment. In this first instalment, we'll provide a refresher on PDP and outline the roadmap for its deployment.

### 💡 What is PDP: A Refresher on Proof of Data Possession

Proof of Data Possession (PDP) is a new component of the Filecoin ecosystem, designed to work alongside Proof of Replication (PoRep). While PoRep ensures that data is securely stored and uniquely encoded, PDP focuses on verifying that data is accessible at specific points in time. Here’s a breakdown of what PDP does:

*   **Periodic Accessibility:** PDP checks that data is available when needed, ensuring it’s stored and accessible at regular intervals.
*   **Efficient Retrieval:** Unlike PoRep, PDP operates on unencoded data, making it faster to retrieve without the need for decoding the data.
*   **Lightweight Verification:** PDP’s proving process is computationally efficient and doesn’t require heavy resources like GPUs.

PDP is particularly useful for applications where data needs to be accessed frequently, such as in hot storage scenarios. It ensures that storage providers maintain accessible copies of data without the overhead of constant decoding. This makes PDP a valuable tool for improving retrieval efficiency on Filecoin.

It’s important to note that while PDP is a supporting element of efficient retrieval, it doesn’t guarantee retrieval; malicious storage providers could still deny service. Additionally, PDP complements, rather than replaces, PoRep, as it does not guarantee data replication or incompressibility — both essential for storage-based consensus.

These benefits are why Filecoin onramps like [Storacha](https://storacha.network/) and [Akave](https://www.akave.ai/) are exploring PDP as one of the first adopters of the PDP protocol on Mainnet.

### 🛣️ The Road Ahead: PDP’s Path to Mainnet

So, what’s next for Proof of Data Possession (PDP)? The contract is live and running on the Calibration network ([link](https://beryx.io/fil/calibration/address/t410flcy3maporace6wt7k2z2x3cf7kt6o2a3putcfra)), and we’re in the final sprint toward Mainnet deployment. You can follow our progress and track the work through our [top-level tracking item](https://github.com/FilOzone/pdp/issues/95). Here’s a high-level outline of the upcoming phases:

**🏃‍♂️February 2025:**

1.  Complete **PDP Contract Engineering** tasks, including finalizing the PDP design document and performing last optimizations.
2.  **Curio-PDP Pipeline**, making it easy for [Curio](https://curiostorage.org/) users to accept PDP deals and enabling the creation of PDP-focused storage providers, along with comprehensive documentation.
3.  **Onramp Integration:** [Storacha](https://storacha.network/) will begin to actively work on integrating PDP into their product, providing real-world data and identifying integration pain points.

**🔍 March 2025:**

1.  Engage an external audit team to review the finalised PDP contract ([link to code](https://github.com/FilOzone/pdp/tree/main/src)), with the audit report to be published and announced in the [tracking issue](https://github.com/FilOzone/pdp/issues/97).
2.  Publish the PDP explorer to monitor and analyze PDP data and storage provider performance.

**🚀 End of March 2025:**

1.  Launch the PDP contract on Mainnet!!!

![](/images/0__iIHWnHj8GrR3DszP.jpg)

### 🤝 Join the Journey: Following PDP’s Development

We’re excited to continue sharing PDP’s journey to Mainnet in this series. Stay tuned as we dive deeper into the PDP contract, its upgradability, and the path to becoming a PDP Storage Provider in our upcoming posts!

For those interested in following the development even more closely, we encourage you to join the [#fil-pdp](https://filecoinproject.slack.com/archives/C0717TGU7V2) channel on [Filecoin Slack](https://filecoin.io/slack).

See you in the next update 👋