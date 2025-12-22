# Quick Start Guide

Get your Astro portfolio running in 5 minutes!

## ⚡ Super Quick Start

```bash
# 1. Install dependencies
npm install

# 2. Run development server
npm run dev

# 3. Open browser
# Visit http://localhost:4321
```

That's it! Your portfolio is running locally.

## 📝 First Things to Update

### 1. Your Profile (2 minutes)

Open `src/data.ts` and update:

```typescript
export const PROFILE = {
  name: 'Your Name',              // ← Change this
  title: 'Your Title',            // ← Change this
  institution: 'Your School',     // ← Change this
  email: 'your@email.com',        // ← Change this
  github: 'https://github.com/username',  // ← Change this
  // ... update other fields
};
```

### 2. Your Photo (1 minute)

Replace `public/images/img1.jpg` with your photo.

### 3. Your Papers (3 minutes)

In `src/data.ts`, update the `PAPERS` array:

```typescript
export const PAPERS = [
  {
    title: 'Your Paper',
    authors: 'You, Others',
    venue: 'CVPR',
    year: 2024,
    abstract: 'What your paper does...',
    pdf_link: 'https://...',
    code_link: 'https://github.com/...',
  },
];
```

### 4. Your News (1 minute)

In `src/data.ts`, update the `NEWS` array:

```typescript
export const NEWS = [
  { date: 'Dec 2024', text: 'Your news item' },
];
```

## 🔄 Common Tasks

### Adding a Blog Post

Create `src/content/blog/my-post.md`:

```markdown
---
title: "My Blog Post"
date: "2024-12-20"
excerpt: "Brief description"
tags: ["AI", "Research"]
---

Your content here...
```

### Changing Colors

Edit `public/style.css`:

```css
:root {
    --primary-color: #5b9cf5;  /* Change to your color */
}
```

### Adding a Project

In `src/data.ts`:

```typescript
export const PROJECTS = [
  {
    title: 'Cool Project',
    description: 'What it does',
    tags: ['PyTorch', 'CV'],
    github_link: 'https://...',
    date: '2024'
  },
];
```

## 🚀 Deploy to GitHub Pages

```bash
# 1. Create repository on GitHub (username.github.io)

# 2. Push your code
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/username/username.github.io.git
git push -u origin main

# 3. Enable GitHub Pages
# Go to Settings → Pages → Source: GitHub Actions

# Done! Your site is live! ✨
```

## 📂 File Structure Cheat Sheet

```
portfolio-astro/
├── src/
│   ├── data.ts           ← Edit your profile/papers/news
│   ├── pages/
│   │   ├── index.astro   ← Home page
│   │   ├── research.astro
│   │   └── blog/...      ← Blog posts
│   └── content/blog/     ← Write blog posts here
├── public/
│   ├── style.css         ← Edit colors/styling
│   └── images/           ← Add images here
└── astro.config.mjs      ← Site config
```

## 🎯 Development Workflow

```bash
# Start dev server
npm run dev

# Make changes to files
# See changes instantly in browser!

# When ready to deploy:
npm run build    # Build for production
git add .
git commit -m "Update content"
git push         # Automatic deployment!
```

## 🆘 Need Help?

1. Check `README.md` for detailed info
2. See `MIGRATION.md` to understand Flask → Astro differences
3. Read `DEPLOYMENT.md` for deployment options

## 💡 Pro Tips

- Use `npm run dev` while editing - changes appear instantly!
- Test mobile view: `npm run dev` then resize your browser
- Preview production build: `npm run build && npm run preview`
- Your CSS file from Flask works perfectly - no changes needed!

## ✅ Checklist

- [ ] Updated profile in `src/data.ts`
- [ ] Replaced photo in `public/images/`
- [ ] Updated papers list
- [ ] Updated news items
- [ ] Tested locally with `npm run dev`
- [ ] Ready to deploy!

## 🎉 You're Ready!

Your modern, fast portfolio is ready to share with the world.

Happy coding! 🚀
