# Deployment Guide

This guide covers deploying your Astro portfolio to various platforms.

## 🚀 GitHub Pages (Recommended)

GitHub Pages offers free hosting for static sites. Perfect for portfolios!

### Option 1: Automatic Deployment with GitHub Actions (Easiest)

We've included a GitHub Actions workflow that automatically deploys when you push to `main`.

#### Steps:

1. **Push your code to GitHub:**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin https://github.com/HarshilBhatia/HarshilBhatia.github.io.git
   git push -u origin main
   ```

2. **Enable GitHub Pages:**
   - Go to your repository on GitHub
   - Settings → Pages
   - Source: GitHub Actions
   
3. **Configure site URL** in `astro.config.mjs`:
   ```javascript
   export default defineConfig({
     site: 'https://harshilbhatia.github.io',
     base: '/',  // Use '/' for user pages, '/repo-name' for project pages
   });
   ```

4. **Push changes:**
   ```bash
   git add astro.config.mjs
   git commit -m "Configure site URL"
   git push
   ```

5. **Done!** Your site will be live at `https://harshilbhatia.github.io`

The workflow will automatically:
- Install dependencies
- Build your site
- Deploy to GitHub Pages
- Every time you push to `main`!

### Option 2: Manual Deployment

If you prefer manual control:

1. **Build the site:**
   ```bash
   npm run build
   ```

2. **Install gh-pages:**
   ```bash
   npm install -D gh-pages
   ```

3. **Add deploy script to `package.json`:**
   ```json
   "scripts": {
     "deploy": "npm run build && gh-pages -d dist"
   }
   ```

4. **Deploy:**
   ```bash
   npm run deploy
   ```

## 🌐 Netlify

Netlify offers excellent performance and easy setup.

### Steps:

1. **Push to GitHub** (if not already done)

2. **Connect to Netlify:**
   - Go to [netlify.com](https://netlify.com)
   - Click "Add new site" → "Import an existing project"
   - Connect your GitHub account
   - Select your repository

3. **Configure build settings:**
   - Build command: `npm run build`
   - Publish directory: `dist`
   - Click "Deploy site"

4. **Custom domain (optional):**
   - Site settings → Domain management
   - Add your custom domain

### Features:
- ✅ Automatic deployments on push
- ✅ Preview deployments for PRs
- ✅ Free SSL certificates
- ✅ Form handling
- ✅ Serverless functions (if needed)

## ▲ Vercel

Vercel is optimized for modern frameworks like Astro.

### Steps:

1. **Push to GitHub** (if not already done)

2. **Deploy to Vercel:**
   - Go to [vercel.com](https://vercel.com)
   - Click "Add New Project"
   - Import your GitHub repository
   - Vercel auto-detects Astro
   - Click "Deploy"

3. **Done!** Your site is live.

### Features:
- ✅ Auto-deployment on push
- ✅ Preview deployments
- ✅ Analytics
- ✅ Edge network
- ✅ Free SSL

## 🔧 Cloudflare Pages

Fast global CDN with generous free tier.

### Steps:

1. **Push to GitHub**

2. **Create Cloudflare Pages project:**
   - Go to [pages.cloudflare.com](https://pages.cloudflare.com)
   - Connect your GitHub account
   - Select repository

3. **Build settings:**
   - Framework preset: Astro
   - Build command: `npm run build`
   - Build output: `dist`

4. **Deploy**

### Features:
- ✅ Global CDN
- ✅ Unlimited bandwidth
- ✅ Free SSL
- ✅ Analytics

## 📦 Traditional Hosting

For shared hosting or VPS:

### Steps:

1. **Build locally:**
   ```bash
   npm run build
   ```

2. **Upload `dist/` folder:**
   - Use FTP/SFTP
   - Upload entire `dist/` directory
   - Point your domain to this directory

3. **Configure web server:**
   - Make sure index.html is served for directories
   - Set up proper MIME types

## 🔄 Updating Your Site

### With GitHub Actions:
```bash
# Make changes
git add .
git commit -m "Update content"
git push
# Automatic deployment! ✨
```

### With Netlify/Vercel:
```bash
# Make changes
git add .
git commit -m "Update content"
git push
# Automatic deployment! ✨
```

### Manual:
```bash
npm run build
# Upload dist/ folder
```

## 🎯 Recommended: GitHub Pages + Actions

For your portfolio, we recommend GitHub Pages with GitHub Actions because:

1. **Free forever** for public repos
2. **Automatic deployments** - just push!
3. **Perfect for portfolios** - username.github.io
4. **No configuration needed** - we've set it up for you!
5. **Built-in CI/CD** - no external services

## 📝 Pre-deployment Checklist

Before deploying, make sure:

- [ ] Update `site` in `astro.config.mjs`
- [ ] All links work (test with `npm run build && npm run preview`)
- [ ] Images are in `public/images/`
- [ ] Profile data is updated in `src/data.ts`
- [ ] Remove any test/placeholder content
- [ ] Test on mobile (responsive design)
- [ ] Check all blog posts render correctly

## 🐛 Troubleshooting

### 404 on subpages (GitHub Pages)

Update `astro.config.mjs`:
```javascript
base: '/repository-name',  // For project pages
base: '/',                  // For user pages (username.github.io)
```

### Build fails

```bash
# Clear cache
rm -rf node_modules
npm install
npm run build
```

### Images not loading

- Make sure images are in `public/images/`
- Use `/images/filename.jpg` (not `./images/...`)
- Check file names match exactly (case-sensitive!)

### CSS not loading

- CSS should be in `public/style.css`
- Check the `<link>` tag in Layout.astro uses `/style.css`

## 🎉 You're Live!

Once deployed, share your portfolio:
- Add to LinkedIn profile
- Include in email signature
- Share on social media
- Add to your CV

Your professional portfolio is now live and accessible worldwide! 🌍
