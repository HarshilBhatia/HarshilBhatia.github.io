# Harshil's Portfolio - Astro Version

A modern, fast portfolio website built with Astro, converted from Flask. Features static site generation, markdown blog support, and excellent performance.

## 🚀 Features

- **Lightning Fast**: Static site generation with Astro
- **Modern Stack**: TypeScript support, component-based architecture
- **Blog Support**: Markdown-based blog with content collections
- **Responsive Design**: Mobile-friendly with dark theme
- **Easy to Update**: Simple data structures for papers, projects, and news
- **SEO Friendly**: Static HTML for better search engine optimization
- **Zero JavaScript** (unless needed): Astro ships minimal JS by default

## 📦 Project Structure

```
portfolio-astro/
├── public/
│   ├── style.css          # Your existing CSS (unchanged!)
│   └── images/            # Profile photos and project images
├── src/
│   ├── content/
│   │   ├── config.ts      # Content collections configuration
│   │   └── blog/          # Blog posts (markdown files)
│   ├── layouts/
│   │   └── Layout.astro   # Base layout (like Flask's base.html)
│   ├── pages/
│   │   ├── index.astro    # Home page
│   │   ├── research.astro # Research page
│   │   ├── projects.astro # Projects page
│   │   ├── cv.astro       # CV page
│   │   ├── blog.astro     # Blog index
│   │   └── blog/
│   │       └── [slug].astro  # Individual blog posts
│   └── data.ts            # Your papers, projects, news data
├── astro.config.mjs       # Astro configuration
├── package.json           # Dependencies
└── tsconfig.json          # TypeScript config
```

## 🛠️ Getting Started

### 1. Install Dependencies

```bash
cd portfolio-astro
npm install
```

### 2. Run Development Server

```bash
npm run dev
```

Visit `http://localhost:4321` in your browser.

### 3. Build for Production

```bash
npm run build
```

The static site will be generated in the `dist/` folder.

### 4. Preview Production Build

```bash
npm run preview
```

## ✏️ How to Update Content

### Adding/Editing Papers

Open `src/data.ts` and modify the `PAPERS` array:

```typescript
export const PAPERS = [
  {
    title: 'Your Paper Title',
    authors: 'Your Name, Co-Author',
    venue: 'CVPR',
    year: 2024,
    abstract: 'Brief description...',
    pdf_link: 'https://arxiv.org/pdf/...',
    project_link: 'https://yourproject.com',
    code_link: 'https://github.com/username/repo',
  },
  // Add more papers...
];
```

### Adding/Editing Projects

In `src/data.ts`, modify the `PROJECTS` array:

```typescript
export const PROJECTS = [
  {
    title: 'Cool Project',
    description: 'What it does...',
    tags: ['PyTorch', 'Computer Vision'],
    github_link: 'https://github.com/username/project',
    demo_link: 'https://demo.com',
    image: '/images/project.jpg',
    date: '2024'
  },
  // Add more projects...
];
```

### Adding News Items

In `src/data.ts`, modify the `NEWS` array:

```typescript
export const NEWS = [
  {
    date: 'Dec 2024',
    text: 'Your news update (can include <a> tags for links)'
  },
  // Add more news...
];
```

### Updating Profile Information

In `src/data.ts`, edit the `PROFILE` object:

```typescript
export const PROFILE = {
  name: 'Your Name',
  title: 'Your Title',
  institution: 'Your Institution',
  email: 'your.email@example.com',
  github: 'https://github.com/username',
  linkedin: 'https://linkedin.com/in/yourprofile',
  scholar: 'https://scholar.google.com/yourprofile',
  photo: '/images/img1.jpg',
  bio: 'Your bio text (can include HTML)...'
};
```

### Writing Blog Posts

Create a new markdown file in `src/content/blog/`:

```markdown
---
title: "Your Blog Post Title"
date: "2024-12-20"
excerpt: "Brief description..."
tags: ["Computer Vision", "Research"]
---

## Your Content Here

Write your blog post in markdown...
```

## 🎨 Customizing Design

### Changing Colors

Edit `public/style.css` and modify the CSS variables:

```css
:root {
    --primary-color: #5b9cf5;      /* Main accent color */
    --text-color: #e8e8e8;         /* Main text */
    --text-light: #a8a8a8;         /* Secondary text */
    --bg-color: #2b2b2b;           /* Background */
    --bg-secondary: #353535;       /* Cards/sections */
    --border-color: #444444;       /* Borders */
}
```

### Adding Images

1. Place images in `public/images/`
2. Reference them in your data: `image: '/images/myimage.jpg'`

## 🚀 Deployment

### Deploy to GitHub Pages

1. Update `astro.config.mjs`:
```javascript
export default defineConfig({
  site: 'https://yourusername.github.io',
  base: '/repository-name',
});
```

2. Build and deploy:
```bash
npm run build
# Copy dist/ folder to your GitHub Pages repository
```

### Deploy to Netlify

1. Connect your GitHub repository to Netlify
2. Build command: `npm run build`
3. Publish directory: `dist`

### Deploy to Vercel

1. Import your GitHub repository
2. Vercel will auto-detect Astro
3. Deploy!

## 📝 Key Differences from Flask Version

### What Changed:
- **Routing**: File-based instead of Python decorators
  - `app.py @app.route('/')` → `src/pages/index.astro`
- **Templates**: Astro components instead of Jinja2
  - `{{ variable }}` → `{variable}`
  - `{% for %}` → `{items.map()}`
- **Data**: TypeScript/JavaScript instead of Python
  - `PAPERS = [...]` in Python → `export const PAPERS = [...]` in TypeScript
- **Blog**: Content collections instead of parsing markdown manually
  - Astro handles frontmatter and rendering automatically
- **Build**: Static site generation instead of Flask server
  - Run `npm run build` to generate static HTML

### What Stayed the Same:
- ✅ All your CSS (100% compatible!)
- ✅ Same design and layout
- ✅ Same data structure for papers/projects
- ✅ Markdown blog posts with frontmatter
- ✅ Same features and functionality

## 🎯 Benefits of Astro Version

1. **Faster Loading**: Static HTML loads instantly
2. **Better SEO**: Search engines love static sites
3. **Easier Deployment**: No Python server needed
4. **Free Hosting**: GitHub Pages, Netlify, Vercel
5. **Better DX**: Hot reload, TypeScript support
6. **Lower Costs**: No server to maintain

## 📚 Learn More

- [Astro Documentation](https://docs.astro.build)
- [Content Collections Guide](https://docs.astro.build/en/guides/content-collections/)
- [Deployment Guide](https://docs.astro.build/en/guides/deploy/)

## 🤝 Contributing

Feel free to customize this template for your own portfolio!

## 📄 License

Free to use for your personal portfolio!
