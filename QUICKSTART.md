# Filoz Blog - Quick Start Guide

## What's Been Set Up

Your fully decentralized Hugo blog is ready! Here's what's configured:

- ✅ Hugo Extended v0.139.3+ installed
- ✅ Custom FilOz branding and layouts
- ✅ Hugo configuration (hugo.yaml) with all features enabled
- ✅ GitHub Actions workflow for automated Filecoin deployment
- ✅ DNSLink integration via deSEC (deblog.filoz.org)
- ✅ Comprehensive README.md with full documentation

**Live site**: https://deblog-filoz-org.ipns.dweb.link/

## Quick Start

### 1. Test Locally

```bash
# Start development server
hugo server -D

# Open browser to http://localhost:1313
```

### 2. Build Site

```bash
# Production build
hugo --gc --minify

# Output will be in ./public/
```

### 3. Setup Filecoin Pin CLI

```bash
# Install globally
npm install -g filecoin-pin

# Get testnet tokens
# 1. Visit https://faucet.calibration.fildev.network/
# 2. Get test FIL for your Ethereum address
# 3. Get USDFC stablecoin from dedicated faucet

# Configure payments (one-time setup)
export PRIVATE_KEY=0x...  # Your funded private key
filecoin-pin payments setup --auto

# Test local pinning
filecoin-pin add ./public/

# Note the CID returned
```

### 4. GitHub Setup

```bash
# Create new GitHub repository
gh repo create filoz-blog --public

# Add remote
git remote add origin https://github.com/YOUR_USERNAME/filoz-blog.git

# Commit everything
git add .
git commit -m "Initial commit: Hugo blog with Filecoin PDP integration"

# Push to GitHub
git branch -M master
git push -u origin master
```

### 5. Configure GitHub Secrets

1. Go to your GitHub repo
2. Settings > Secrets and variables > Actions
3. Add these repository secrets:
   - **FILECOIN_PRIVATE_KEY**: Your Ethereum private key (with test FIL and USDFC)
   - **DESEC_TOKEN**: Your deSEC API token (for DNSLink updates)

### 6. Automatic Deployment

Every push to `master` branch automatically:
1. Builds Hugo site with minification
2. Pins to Filecoin PDP (provider ID 2)
3. Generates new CID
4. Updates DNSLink TXT record via deSEC
5. Comments on commit with all access URLs

**Primary access** (automatically updated):
- `https://deblog-filoz-org.ipns.dweb.link/` (recommended - has SSL)
- `https://dweb.link/ipns/deblog.filoz.org`
- `https://ipfs.io/ipns/deblog.filoz.org`

**Direct CID access** (specific version):
- `https://ipfs.io/ipfs/<CID>`
- `https://dweb.link/ipfs/<CID>`
- `https://<CID>.ipfs.dweb.link`

**Deployment time**: 3-5 minutes from push to live

## Workflow

### Adding New Posts

```bash
# Create new post
hugo new content/posts/my-new-post.md

# Edit the file
# Set draft: false when ready

# Add images to static/images/
# Reference as /images/filename.jpg in markdown

# Preview locally
hugo server -D

# Commit and push
git add .
git commit -m "Add new post: My New Post"
git push

# GitHub Actions will automatically deploy to Filecoin
```

## File Structure

```
filoz-blog/
├── .github/workflows/deploy.yaml  # Auto-deployment with DNSLink
├── content/posts/                 # Your blog posts (markdown)
├── layouts/                       # Custom Hugo layouts
├── assets/css/extended/           # Custom CSS overrides
├── static/images/                 # Images (stored on Filecoin)
├── static/hero*.json              # Lottie animations
├── hugo.yaml                      # Site configuration
├── README.md                      # Full documentation
└── QUICKSTART.md                  # This file
```

## Key Files to Customize

- **hugo.yaml** - Site title, description, social links, menu
- **content/posts/** - Your blog posts (markdown files)
- **static/images/** - Your images
- **layouts/** - Custom templates (optional)
- **assets/css/extended/custom.css** - Custom styling (optional)

## Troubleshooting

**Hugo version issues:**
```bash
hugo version  # Should be v0.139.3 or higher (Extended)
```

**Theme not found:**
```bash
git submodule update --init --recursive
```

**Build fails:**
```bash
rm -rf public/ resources/ .hugo_build.lock
hugo --gc --minify
```

**Filecoin Pin fails:**
```bash
# Check balance on Calibration testnet
# Reconfigure payments
filecoin-pin payments setup --auto
```

## Important Notes

- **Filecoin Pin CLI is ALPHA** (Calibration testnet only as of November 2025)
- Each deployment creates a new CID (immutable content addressing)
- **DNSLink automatically updates** to point to latest CID
- Content propagates to IPFS gateways in 2-5 minutes
- Provider ID 2 has reliable IPNI advertisement success

## Support

- Hugo Docs: https://gohugo.io/documentation/
- Filecoin Docs: https://docs.filecoin.io/
- Issues: Check README.md Troubleshooting section

---

**Ready to blog on Filecoin!** 🚀
