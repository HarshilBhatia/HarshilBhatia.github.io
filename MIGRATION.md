# Migration Guide: Flask to Astro

This guide helps you understand the differences between your Flask app and the new Astro version.

## Quick Reference

### Flask → Astro Equivalents

| Flask | Astro |
|-------|-------|
| `app.py` | `src/pages/*.astro` |
| `templates/base.html` | `src/layouts/Layout.astro` |
| `templates/index.html` | `src/pages/index.astro` |
| `PAPERS = [...]` in Python | `export const PAPERS = [...]` in `src/data.ts` |
| `{{ variable }}` | `{variable}` |
| `{% for item in items %}` | `{items.map(item => (...))}` |
| `{{ content\|safe }}` | `<div set:html={content} />` |
| Flask-Frozen | Built-in static generation |

## Detailed Comparison

### 1. Routing

**Flask:**
```python
@app.route('/')
def index():
    return render_template('index.html', data=DATA)

@app.route('/research')
def research():
    return render_template('research.html', papers=PAPERS)
```

**Astro:**
- File-based routing: `src/pages/index.astro` → `/`
- File-based routing: `src/pages/research.astro` → `/research`
- Dynamic routes: `src/pages/blog/[slug].astro` → `/blog/*`

### 2. Templates

**Flask (Jinja2):**
```html
{% extends "base.html" %}
{% block content %}
  <h1>{{ profile.name }}</h1>
  {% for paper in papers %}
    <div>{{ paper.title }}</div>
  {% endfor %}
{% endblock %}
```

**Astro:**
```astro
---
import Layout from '../layouts/Layout.astro';
import { PROFILE, PAPERS } from '../data';
---

<Layout>
  <h1>{PROFILE.name}</h1>
  {PAPERS.map(paper => (
    <div>{paper.title}</div>
  ))}
</Layout>
```

### 3. Data Management

**Flask:**
```python
# app.py or data.py
PAPERS = [
    {
        'title': 'Paper Title',
        'authors': 'Author Names',
    }
]
```

**Astro:**
```typescript
// src/data.ts
export const PAPERS = [
  {
    title: 'Paper Title',
    authors: 'Author Names',
  }
];
```

### 4. Blog Posts

**Flask:**
- Manual markdown parsing with frontmatter
- Custom route handlers
- Manual file discovery

**Astro:**
- Built-in content collections
- Automatic frontmatter parsing
- Type-safe with validation
- Automatic route generation

**Example blog post (same in both):**
```markdown
---
title: "My Post"
date: "2024-12-20"
tags: ["AI", "Research"]
---

Content here...
```

### 5. Static Site Generation

**Flask:**
```python
# Uses Flask-Frozen
freezer = Freezer(app)
freezer.freeze()
```

**Astro:**
```bash
# Built-in
npm run build
```

### 6. Development Server

**Flask:**
```bash
python app.py
# http://localhost:5000
```

**Astro:**
```bash
npm run dev
# http://localhost:4321
```

## Where to Find Things

### Data & Configuration

| What | Flask | Astro |
|------|-------|-------|
| Profile info | `app.py` or `data.py` | `src/data.ts` |
| Papers list | `app.py` or `data.py` | `src/data.ts` |
| Projects list | `app.py` or `data.py` | `src/data.ts` |
| Site config | Flask config | `astro.config.mjs` |

### Templates & Pages

| What | Flask | Astro |
|------|-------|-------|
| Base layout | `templates/base.html` | `src/layouts/Layout.astro` |
| Home page | `templates/index.html` | `src/pages/index.astro` |
| Research page | `templates/research.html` | `src/pages/research.astro` |
| Blog listing | `templates/blog.html` | `src/pages/blog.astro` |
| Blog post | `templates/post.html` | `src/pages/blog/[slug].astro` |

### Static Assets

| What | Flask | Astro |
|------|-------|-------|
| CSS | `static/css/style.css` | `public/style.css` |
| Images | `static/images/` | `public/images/` |

## Common Patterns

### Conditional Rendering

**Flask:**
```html
{% if profile.github %}
  <a href="{{ profile.github }}">GitHub</a>
{% endif %}
```

**Astro:**
```astro
{PROFILE.github && (
  <a href={PROFILE.github}>GitHub</a>
)}
```

### Loops

**Flask:**
```html
{% for paper in papers %}
  <div>{{ paper.title }}</div>
{% endfor %}
```

**Astro:**
```astro
{papers.map(paper => (
  <div>{paper.title}</div>
))}
```

### HTML Safety

**Flask:**
```html
{{ content|safe }}
```

**Astro:**
```astro
<div set:html={content} />
```

### URL Building

**Flask:**
```html
<a href="{{ url_for('research') }}">Research</a>
```

**Astro:**
```astro
<a href="/research">Research</a>
```

## Benefits You'll Notice

1. **Speed**: Pages load much faster (static HTML)
2. **No Server**: Just upload the `dist/` folder
3. **Hot Reload**: Changes appear instantly in dev
4. **Type Safety**: TypeScript catches errors
5. **Modern Tooling**: Better DX with Vite
6. **SEO**: Static HTML is easier for search engines

## Migration Checklist

- [x] ✅ All routes converted to pages
- [x] ✅ Data moved to TypeScript
- [x] ✅ Templates converted to Astro components
- [x] ✅ Blog system set up with content collections
- [x] ✅ CSS copied (no changes needed!)
- [x] ✅ Images in public directory
- [x] ✅ Navigation working
- [x] ✅ Mobile responsive

## Next Steps

1. **Install dependencies**: `npm install`
2. **Run dev server**: `npm run dev`
3. **Test all pages**: Click through each page
4. **Add your content**: Update `src/data.ts`
5. **Write blog posts**: Add markdown files to `src/content/blog/`
6. **Deploy**: Run `npm run build` and upload `dist/`

## Need Help?

- Check the [Astro docs](https://docs.astro.build)
- Compare Flask templates with Astro pages side-by-side
- All your data structure is the same, just in TypeScript!

## Tips

- Your CSS works exactly the same ✨
- Data structure is identical (just JS instead of Python)
- Blog posts use the same markdown format
- No learning curve for content editing!
