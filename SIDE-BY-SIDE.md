# Side-by-Side Comparison: Flask vs Astro

This document shows your Flask code next to the equivalent Astro code to help you understand the conversion.

## 📁 File Organization

### Flask
```
flask_portfolio/
├── app.py              # Routes + data
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── research.html
│   └── blog.html
├── static/
│   └── css/style.css
└── posts/              # Blog markdown files
```

### Astro
```
portfolio-astro/
├── src/
│   ├── data.ts         # Data only
│   ├── layouts/
│   │   └── Layout.astro    # = base.html
│   ├── pages/
│   │   ├── index.astro     # = index.html + route
│   │   ├── research.astro  # = research.html + route
│   │   └── blog.astro      # = blog.html + route
│   └── content/blog/   # Blog markdown files
└── public/
    └── style.css       # Same CSS!
```

## 🔀 Routing

### Flask
```python
# app.py
@app.route('/')
def index():
    return render_template('index.html', 
                         profile=PROFILE, 
                         papers=PAPERS)

@app.route('/research')
def research():
    return render_template('research.html', 
                         papers=PAPERS)

@app.route('/blog/<slug>')
def blog_post(slug):
    post = get_post_by_slug(slug)
    return render_template('post.html', post=post)
```

### Astro
```
# File system routing
src/pages/index.astro       → /
src/pages/research.astro    → /research
src/pages/blog/[slug].astro → /blog/:slug

# No Python functions needed!
# Data imported directly in component
```

## 📊 Data Definition

### Flask
```python
# app.py or data.py
PAPERS = [
    {
        'title': 'CARFF',
        'authors': 'J. Yang, K. Desai, ...',
        'venue': 'ECCV',
        'year': 2024,
    }
]

PROFILE = {
    'name': 'Harshil Bhatia',
    'email': 'harshilb@cs.cmu.edu',
}
```

### Astro
```typescript
// src/data.ts
export const PAPERS = [
  {
    title: 'CARFF',
    authors: 'J. Yang, K. Desai, ...',
    venue: 'ECCV',
    year: 2024,
  }
];

export const PROFILE = {
  name: 'Harshil Bhatia',
  email: 'harshilb@cs.cmu.edu',
};
```

**Difference**: `'key':` → `key:`, quotes on strings only

## 🎨 Templates

### Base Template

**Flask (`templates/base.html`)**
```html
<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}{{ profile.name }}{% endblock %}</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
</head>
<body>
    <nav class="navbar">
        <a href="{{ url_for('index') }}">Home</a>
        <a href="{{ url_for('research') }}">Research</a>
    </nav>
    
    <main>
        {% block content %}{% endblock %}
    </main>
</body>
</html>
```

**Astro (`src/layouts/Layout.astro`)**
```astro
---
interface Props {
  title?: string;
}
const { title = PROFILE.name } = Astro.props;
---

<!DOCTYPE html>
<html>
<head>
    <title>{title}</title>
    <link rel="stylesheet" href="/style.css">
</head>
<body>
    <nav class="navbar">
        <a href="/">Home</a>
        <a href="/research">Research</a>
    </nav>
    
    <main>
        <slot />
    </main>
</body>
</html>
```

**Key Changes**:
- `{{ variable }}` → `{variable}`
- `{% block %}` → `<slot />`
- `url_for()` → direct paths

### Home Page

**Flask (`templates/index.html`)**
```html
{% extends "base.html" %}

{% block content %}
<div class="intro-section">
    <h1>{{ profile.name }}</h1>
    <p>{{ profile.bio|safe }}</p>
</div>

<section>
    <h2>Recent Publications</h2>
    {% for paper in papers[:3] %}
    <div class="paper-item">
        <h3>{{ paper.title }}</h3>
        <p>{{ paper.authors }}</p>
        {% if paper.pdf_link and paper.pdf_link != '#' %}
        <a href="{{ paper.pdf_link }}">PDF</a>
        {% endif %}
    </div>
    {% endfor %}
</section>
{% endblock %}
```

**Astro (`src/pages/index.astro`)**
```astro
---
import Layout from '../layouts/Layout.astro';
import { PROFILE, PAPERS } from '../data';
---

<Layout>
    <div class="intro-section">
        <h1>{PROFILE.name}</h1>
        <p set:html={PROFILE.bio}></p>
    </div>

    <section>
        <h2>Recent Publications</h2>
        {PAPERS.slice(0, 3).map(paper => (
            <div class="paper-item">
                <h3>{paper.title}</h3>
                <p>{paper.authors}</p>
                {paper.pdf_link && paper.pdf_link !== '#' && (
                    <a href={paper.pdf_link}>PDF</a>
                )}
            </div>
        ))}
    </section>
</Layout>
```

**Key Changes**:
- `{% extends %}` → `import Layout`
- `{% for %}` → `.map()`
- `{% if %}` → `&&` operator
- `|safe` → `set:html={}`

## 🔄 Loops

### Flask
```html
{% for paper in papers %}
    <div>{{ paper.title }}</div>
{% endfor %}
```

### Astro
```astro
{papers.map(paper => (
    <div>{paper.title}</div>
))}
```

## ✅ Conditionals

### Flask
```html
{% if profile.github %}
    <a href="{{ profile.github }}">GitHub</a>
{% endif %}

{% if papers %}
    <div>Has papers</div>
{% else %}
    <div>No papers</div>
{% endif %}
```

### Astro
```astro
{PROFILE.github && (
    <a href={PROFILE.github}>GitHub</a>
)}

{papers.length > 0 ? (
    <div>Has papers</div>
) : (
    <div>No papers</div>
)}
```

## 📝 Blog System

### Flask
```python
# Manual markdown parsing
def parse_post(filepath):
    with open(filepath, 'r') as f:
        content = f.read()
    # Parse frontmatter manually
    # Split content
    # Convert markdown to HTML
    return post_data

@app.route('/blog/<slug>')
def blog_post(slug):
    post = get_post_by_slug(slug)
    return render_template('post.html', post=post)
```

### Astro
```astro
---
// Automatic with content collections
import { getCollection } from 'astro:content';

const posts = await getCollection('blog');
// Frontmatter automatically parsed
// Markdown automatically converted
---
```

### Blog Post Format (Identical!)

**Both Flask and Astro**
```markdown
---
title: "My Post"
date: "2024-12-20"
tags: ["AI", "Research"]
excerpt: "Brief description"
---

## Content Here

Your markdown content...
```

## 🏗️ Build Process

### Flask
```python
# build.py
import os
os.environ['FREEZE'] = '1'
from app import freezer

freezer.freeze()
```

```bash
python build.py
# Output: build/ directory
```

### Astro
```bash
npm run build
# Output: dist/ directory
```

## 🚀 Development

### Flask
```bash
python app.py
# http://localhost:5000
# Manual reload
```

### Astro
```bash
npm run dev
# http://localhost:4321
# Hot reload (instant updates!)
```

## 📊 Real Examples from Your Code

### News Section

**Flask (`templates/index.html`)**
```html
{% for item in news %}
<div class="news-item">
    <span class="news-date">{{ item.date }}</span>
    <p>{{ item.text|safe }}</p>
</div>
{% endfor %}
```

**Astro (`src/pages/index.astro`)**
```astro
{NEWS.map(item => (
    <div class="news-item">
        <span class="news-date">{item.date}</span>
        <p set:html={item.text}></p>
    </div>
))}
```

### Paper Links

**Flask**
```html
{% if paper.pdf_link and paper.pdf_link != '#' %}
<a href="{{ paper.pdf_link }}" target="_blank">PDF</a>
{% endif %}
```

**Astro**
```astro
{paper.pdf_link && paper.pdf_link !== '#' && (
    <a href={paper.pdf_link} target="_blank">PDF</a>
)}
```

### External Links

**Flask**
```html
{% if profile.github %}
<li><a href="{{ profile.github }}">GitHub</a></li>
{% endif %}
```

**Astro**
```astro
{PROFILE.github && (
    <li><a href={PROFILE.github}>GitHub</a></li>
)}
```

## 🎯 Common Patterns Summary

| Task | Flask | Astro |
|------|-------|-------|
| Variable | `{{ var }}` | `{var}` |
| Loop | `{% for x in xs %}` | `{xs.map(x => ())}` |
| Conditional | `{% if x %}` | `{x && ()}` |
| HTML safety | `{{ x\|safe }}` | `set:html={x}` |
| Include template | `{% extends %}` | `import Layout` |
| URL building | `{{ url_for('route') }}` | `"/route"` |
| Static files | `url_for('static', ...)` | `"/file.css"` |

## 💡 Tips for Translation

1. **Curly braces**: Single `{}` in Astro vs double `{{}}` in Flask
2. **Loops**: Use `.map()` instead of `{% for %}`
3. **Conditionals**: Use `&&` or ternary `? :` instead of `{% if %}`
4. **Arrays**: Use `.slice()`, `.filter()`, `.map()` (JavaScript methods)
5. **Paths**: Use `/` for root, no `url_for()` needed

## ✨ What Makes Astro Better?

1. **Faster**: Static HTML loads 10x faster
2. **Simpler Deployment**: Just upload files
3. **Hot Reload**: See changes instantly
4. **Type Safety**: TypeScript catches errors
5. **Modern Tooling**: Better DX
6. **SEO**: Better for search engines

## 🎓 Learning Curve

If you know Flask/Jinja2:
- **Easy**: Template syntax (95% similar)
- **Easy**: Data structures (almost identical)
- **Medium**: JavaScript instead of Python
- **Easy**: Deployment (simpler!)

Total learning time: ~1-2 hours to feel comfortable

---

The conversion preserves all your functionality while making it faster, cheaper, and easier to deploy!
