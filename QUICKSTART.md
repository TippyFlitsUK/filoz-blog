# Filoz Blog - Quick Start Guide

## What's Been Set Up

Your Hugo blog with Filecoin PDP storage integration is ready! Here's what's configured:

- ✅ Hugo v0.152.2 Extended installed
- ✅ PaperMod theme installed as git submodule
- ✅ Hugo configuration (hugo.yaml) with PaperMod settings
- ✅ Sample welcome post created
- ✅ Medium migration script (migrate-medium.sh)
- ✅ Image optimization script (optimize-images.sh)
- ✅ GitHub Actions workflow for Filecoin deployment
- ✅ Comprehensive README.md with full documentation

## Next Steps

### 1. Migrate Your Medium Posts

```bash
# Download your Medium export from: https://medium.com/me/settings/security
# Extract medium-export.zip to this directory
unzip medium-export.zip

# Run migration script (installs medium-2-md if needed)
npm install -g medium-2-md
./migrate-medium.sh
```

This will:
- Convert all Medium posts to Hugo markdown
- Download ALL images locally to `static/images/`
- Update markdown to reference local images
- Add YAML frontmatter

### 2. (Optional) Optimize Images

```bash
# Install ImageMagick if not already installed
sudo apt-get install imagemagick

# Run optimization
./optimize-images.sh
```

This will resize, compress, and optionally convert images to WebP.

### 3. Test Locally

```bash
# Start development server
hugo server -D

# Open browser to http://localhost:1313
```

### 4. Build Site

```bash
# Production build
hugo --gc --minify

# Output will be in ./public/
```

### 5. Setup Filecoin Pin CLI

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

### 6. GitHub Setup

```bash
# Create new GitHub repository
gh repo create filoz-blog --public

# Add remote
git remote add origin https://github.com/YOUR_USERNAME/filoz-blog.git

# Commit everything
git add .
git commit -m "Initial commit: Hugo blog with Filecoin PDP integration"

# Push to GitHub
git branch -M main
git push -u origin main
```

### 7. Configure GitHub Secrets

1. Go to your GitHub repo
2. Settings > Secrets and variables > Actions
3. Click "New repository secret"
4. Name: `FILECOIN_PRIVATE_KEY`
5. Value: Your Ethereum private key (with test FIL and USDFC)

### 8. Automatic Deployment

Every push to `main` branch will:
1. Build Hugo site
2. Pin to your Filecoin PDP node
3. Generate new CID
4. Comment on commit with IPFS URLs

Access your deployed site at:
- `https://ipfs.io/ipfs/<CID>`
- `https://dweb.link/ipfs/<CID>`
- `https://cloudflare-ipfs.com/ipfs/<CID>`
- `https://<CID>.ipfs.dweb.link`

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
├── .github/workflows/deploy.yaml  # Auto-deployment workflow
├── content/posts/                 # Your blog posts (markdown)
├── static/images/                 # Images (will be on Filecoin)
├── themes/PaperMod/               # Theme (git submodule)
├── hugo.yaml                      # Site configuration
├── migrate-medium.sh              # Medium migration script
├── optimize-images.sh             # Image optimization script
├── README.md                      # Full documentation
└── QUICKSTART.md                  # This file
```

## Key Files to Customize

- **hugo.yaml** - Site title, description, social links, menu
- **content/posts/** - Your blog posts
- **static/images/** - Your images

## Troubleshooting

**Hugo version issues:**
```bash
hugo version  # Should be v0.152.2 or higher
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

- **Filecoin Pin CLI is ALPHA** (Calibration testnet only)
- Each deployment creates a new CID (immutable content)
- Images take 2-5 minutes to propagate across IPFS gateways
- Update DNS/links to point to new CID after each deployment

## Support

- Hugo Docs: https://gohugo.io/documentation/
- PaperMod Wiki: https://github.com/adityatelange/hugo-PaperMod/wiki
- Filecoin Docs: https://docs.filecoin.io/
- Issues: Check README.md Troubleshooting section

---

**Ready to blog on Filecoin!** 🚀
