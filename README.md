# Filoz Blog

A Hugo blog with PaperMod theme, fully deployed to Filecoin PDP (Proof of Data Possession) storage. All content, including images, is stored on decentralized Filecoin storage with cryptographic proof of persistence.

## Features

- **Hugo Static Site Generator** with PaperMod theme
- **Filecoin PDP Storage** - All content pinned to personal storage provider node
- **IPFS Gateway Access** - Accessible via multiple IPFS gateways
- **Automated Deployment** - GitHub Actions CI/CD pipeline
- **Medium Migration** - Tools to migrate posts from Medium with local images
- **Image Optimization** - Scripts to compress and optimize images before pinning
- **Zero CDN Dependencies** - All images stored on Filecoin, not Medium or third-party CDNs

## Architecture

```
Write Post (Markdown)
    ↓
Git Push to GitHub
    ↓
GitHub Actions Trigger
    ↓
Hugo Build (--gc --minify)
    ↓
Filecoin Pin CLI
    ↓
Content Pinned to PDP Node
    ↓
New CID Generated
    ↓
Accessible via IPFS Gateways
```

## Prerequisites

### Local Development

- **Hugo Extended** v0.112.4+ ([installation guide](https://gohugo.io/installation/))
- **Git** for version control
- **Node.js 24+** for Filecoin Pin CLI
- **ImageMagick** (optional, for image optimization)

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

### 4. Install Medium Migration Tool (optional)

```bash
npm install -g medium-2-md
```

### 5. Install ImageMagick (optional, for image optimization)

```bash
# Ubuntu/Debian
sudo apt-get install imagemagick

# macOS
brew install imagemagick
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

## Medium Migration

### Step 1: Export from Medium

1. Go to https://medium.com/me/settings/security
2. Click "Download your information"
3. Download the `medium-export.zip` file
4. Extract it to the project root:

```bash
unzip medium-export.zip
```

### Step 2: Run Migration Script

```bash
./migrate-medium.sh
```

This script will:
- Convert all Medium posts to Hugo-compatible markdown
- Download ALL images from Medium posts
- Save images to `static/images/`
- Update markdown to reference local images
- Add YAML frontmatter with title, date, description, canonical URL

### Step 3: Review Migrated Posts

```bash
ls -la content/posts/
```

Check posts and make any necessary edits.

### Step 4: Optimize Images (Optional)

```bash
./optimize-images.sh
```

This will:
- Resize images to max 1200px width
- Compress JPEGs at 85% quality
- Strip metadata
- Optionally convert to WebP format

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

#### 1. Add GitHub Secret

1. Go to your GitHub repository
2. Settings > Secrets and variables > Actions
3. Click "New repository secret"
4. Name: `FILECOIN_PRIVATE_KEY`
5. Value: Your Ethereum private key (with test FIL and USDFC)

#### 2. Push to GitHub

```bash
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/yourusername/filoz-blog.git
git push -u origin main
```

#### 3. Automatic Deployment

Every push to `main` branch will:
1. Build Hugo site
2. Pin to Filecoin via your PDP node
3. Generate new CID
4. Create deployment artifact
5. Comment on commit with IPFS URLs

### Access Your Deployed Site

After deployment, access your site via IPFS gateways:

- `https://ipfs.io/ipfs/<CID>`
- `https://dweb.link/ipfs/<CID>`
- `https://cloudflare-ipfs.com/ipfs/<CID>`
- `https://<CID>.ipfs.dweb.link`

Find the CID in:
- GitHub Actions run summary
- Commit comments
- Downloaded artifacts (`cid.txt`)

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
├── migrate-medium.sh            # Medium migration script
├── optimize-images.sh           # Image optimization script
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
- **NOT for production use** (as of October 2025)
- Register at [filecoin.cloud](https://filecoin.cloud) for mainnet availability

### Content Addressing

- Each deployment creates a **new CID** (immutable)
- Old CIDs remain accessible (if still pinned)
- Update DNS/links to point to new CID after deployment

### IPFS Gateway Propagation

- Content may take 2-5 minutes to appear on all gateways
- Try different gateways if one is slow
- Direct node access is fastest (if available)

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

### Medium Migration Issues

```bash
# Reinstall medium-2-md
npm uninstall -g medium-2-md
npm install -g medium-2-md

# Increase timeout for slow connections
# Edit migrate-medium.sh and change -t 1000 to -t 2000
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
