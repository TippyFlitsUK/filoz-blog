# Filoz Blog

A fully decentralized Hugo blog with PaperMod theme, deployed to Filecoin PDP (Proof of Data Possession) storage. All content is stored on Filecoin with cryptographic proof of persistence and accessible via DNSLink at **deblog.filoz.org**.

## Quick Access

- **Primary URL**: https://deblog-filoz-org.ipns.dweb.link/
- **Alternative**: https://dweb.link/ipns/deblog.filoz.org
- **Direct CID**: Check GitHub Actions summary after each deployment

## Features

- **Hugo Static Site Generator** with PaperMod theme and custom FilOz branding
- **Filecoin PDP Storage** - All content pinned with daily cryptographic proofs
- **DNSLink** - Human-readable domain via deSEC DNS (deblog.filoz.org)
- **IPFS Gateway Access** - Accessible via multiple IPFS gateways
- **Automated Deployment** - Push to master triggers full CI/CD pipeline
- **Zero CDN Dependencies** - Completely decentralized infrastructure

## Architecture

```
Write Post (Markdown)
    ↓
Git Push to master branch
    ↓
GitHub Actions Trigger
    ↓
Hugo Build (--gc --minify)
    ↓
Filecoin Pin CLI (Provider ID 2)
    ↓
Content Pinned to PDP Node
    ↓
New CID Generated
    ↓
deSEC API Call
    ↓
DNSLink TXT Record Updated
    ↓
Site Accessible:
  - deblog.filoz.org (DNSLink)
  - Direct CID via IPFS gateways
```

## Prerequisites

### Local Development

- **Hugo Extended** v0.112.4+ ([installation guide](https://gohugo.io/installation/))
- **Git** for version control
- **Node.js 24+** for Filecoin Pin CLI

### Filecoin Deployment

- **Filecoin Pin CLI** (`npm install -g filecoin-pin`)
- **Calibration Testnet Tokens**:
  - Test FIL from [Calibration Faucet](https://faucet.calibration.fildev.network/)
  - USDFC stablecoin from dedicated faucet
- **Ethereum-style Private Key** with test funds

## Installation

### 1. Clone Repository

```bash
git clone https://github.com/yourusername/filoz-blog.git
cd filoz-blog
git submodule update --init --recursive
```

### 2. Install Hugo

**Linux:**
```bash
wget https://github.com/gohugoio/hugo/releases/download/v0.139.3/hugo_extended_0.139.3_Linux-64bit.tar.gz
tar -xzf hugo_extended_0.139.3_Linux-64bit.tar.gz
sudo mv hugo /usr/local/bin/
```

**macOS:**
```bash
brew install hugo
```

**Windows:**
Download from [Hugo releases](https://github.com/gohugoio/hugo/releases)

Verify installation:
```bash
hugo version
```

### 3. Install Filecoin Pin CLI (for deployment)

```bash
npm install -g filecoin-pin
```

## Local Development

### Start Development Server

```bash
hugo server -D
```

Open http://localhost:1313 in your browser.

### Create New Post

```bash
hugo new content/posts/my-new-post.md
```

Edit the post in `content/posts/my-new-post.md`:

```markdown
---
title: "My New Post"
date: 2025-11-03T10:00:00Z
draft: false
tags: ["filecoin", "web3"]
---

Your content here...
```

### Build Site

```bash
hugo --gc --minify
```

Output will be in `public/` directory.

## Filecoin Deployment

### Setup (One-time)

#### 1. Get Test Tokens

- Visit [Calibration Faucet](https://faucet.calibration.fildev.network/)
- Get test FIL for your Ethereum address
- Get USDFC stablecoin from dedicated faucet

#### 2. Configure Filecoin Pin

```bash
export PRIVATE_KEY=0x...  # Your funded private key
filecoin-pin payments setup --auto
```

#### 3. Test Local Pinning

```bash
hugo --gc --minify
filecoin-pin add ./public/
```

You'll receive a CID (Content Identifier). Test access:
```
https://ipfs.io/ipfs/<CID>
```

### GitHub Actions Deployment

#### 1. Add GitHub Secrets

1. Go to your GitHub repository
2. Settings > Secrets and variables > Actions
3. Add these secrets:
   - **FILECOIN_PRIVATE_KEY**: Your Ethereum private key (with test FIL and USDFC)
   - **DESEC_TOKEN**: Your deSEC API token (for DNSLink updates)

#### 2. Push to GitHub

```bash
git add .
git commit -m "Initial commit"
git branch -M master
git remote add origin https://github.com/yourusername/filoz-blog.git
git push -u origin master
```

#### 3. Automatic Deployment

Every push to `master` branch automatically:
1. Builds Hugo site with minification
2. Pins to Filecoin PDP (provider ID 2)
3. Generates new CID
4. Updates DNSLink TXT record via deSEC
5. Creates deployment artifacts
6. Comments on commit with all access URLs

**Deployment time**: 3-5 minutes from push to live

### Access Your Deployed Site

**Primary access via DNSLink** (automatically updated):
- `https://deblog-filoz-org.ipns.dweb.link/` (recommended - has SSL)
- `https://dweb.link/ipns/deblog.filoz.org`
- `https://ipfs.io/ipns/deblog.filoz.org`

**Direct CID access** (specific version):
- `https://ipfs.io/ipfs/<CID>`
- `https://dweb.link/ipfs/<CID>`
- `https://<CID>.ipfs.dweb.link`

Find the latest CID in:
- GitHub Actions run summary
- Commit comments
- Downloaded artifacts (`cid.txt` or `ipfs-uri.txt`)

**Note**: DNSLink propagation takes 2-5 minutes after deployment

## Project Structure

```
filoz-blog/
├── .github/
│   └── workflows/
│       └── deploy.yaml          # GitHub Actions workflow
├── archetypes/
│   └── default.md               # Post template
├── content/
│   └── posts/                   # Blog posts (markdown)
├── static/
│   └── images/                  # Images (stored on Filecoin)
├── themes/
│   └── PaperMod/                # Theme (git submodule)
├── hugo.yaml                    # Hugo configuration
└── README.md
```

## Configuration

### Hugo Configuration

Edit `hugo.yaml` to customize:

- **baseURL**: Your domain (or leave for IPFS)
- **title**: Site title
- **params.description**: Site description
- **params.socialIcons**: Social media links
- **menu**: Navigation menu

### Theme Customization

PaperMod theme can be customized via `hugo.yaml` params. See [PaperMod Wiki](https://github.com/adityatelange/hugo-PaperMod/wiki) for options.

## Workflow

### Adding New Content

1. **Write post:**
   ```bash
   hugo new content/posts/my-post.md
   ```

2. **Add images:**
   - Place in `static/images/`
   - Reference as `/images/filename.jpg` in markdown

3. **Preview locally:**
   ```bash
   hugo server -D
   ```

4. **Commit and push:**
   ```bash
   git add .
   git commit -m "Add new post: My Post"
   git push
   ```

5. **Automatic deployment:**
   - GitHub Actions builds and pins to Filecoin
   - New CID generated
   - Access via IPFS gateways

### Updating Existing Content

1. Edit markdown files in `content/posts/`
2. Commit and push changes
3. New CID generated with updated content

## Important Notes

### Filecoin Pin CLI Status

- **Currently ALPHA software** on Calibration testnet
- **NOT for production use** (as of November 2025)
- Register at [filecoin.cloud](https://filecoin.cloud) for mainnet availability

### DNSLink and Content Addressing

- Each deployment creates a **new CID** (immutable content addressing)
- **DNSLink automatically updates** to point to latest CID via deSEC API
- Old CIDs remain accessible via IPFS if still pinned
- DNSLink TXT record: `_dnslink.deblog.filoz.org` → `dnslink=/ipfs/<latest-CID>`

### IPFS Gateway Propagation

- Content may take 2-5 minutes to appear after DNSLink update
- IPNI (InterPlanetary Network Indexer) advertisement ensures discoverability
- Provider ID 2 has reliable IPNI advertisement success
- Try different gateways if one is slow

## Troubleshooting

### Hugo Build Fails

```bash
# Verify Hugo installation
hugo version

# Check for theme issues
git submodule update --init --recursive

# Clean and rebuild
rm -rf public/ resources/
hugo --gc --minify
```

### Filecoin Pin Fails

```bash
# Check CLI version
filecoin-pin --version

# Verify private key is set
echo $PRIVATE_KEY

# Check testnet balance
# Visit Calibration explorer with your address

# Reconfigure payments
filecoin-pin payments setup --auto
```

### Images Not Loading

- Check image paths in markdown: `/images/` not `images/`
- Verify images exist in `static/images/`
- Build and check `public/images/` directory

## Resources

### Documentation

- [Hugo Documentation](https://gohugo.io/documentation/)
- [PaperMod Theme Wiki](https://github.com/adityatelange/hugo-PaperMod/wiki)
- [Filecoin Docs](https://docs.filecoin.io/)
- [Filecoin Pin CLI](https://github.com/filecoin-project/filecoin-pin)

### Community

- [Hugo Discourse](https://discourse.gohugo.io/)
- [Filecoin Slack](https://filecoin.io/slack)
- [IPFS Forum](https://discuss.ipfs.tech/)

## License

MIT License - feel free to use this setup for your own blog.

## Credits

- **Hugo** - Static site generator
- **PaperMod** - Hugo theme by [@adityatelange](https://github.com/adityatelange)
- **Filecoin** - Decentralized storage network
- **IPFS** - InterPlanetary File System

---

Built with Hugo, stored on Filecoin PDP, accessible via IPFS.
