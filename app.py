
# from flask import Flask, render_template
# from datetime import datetime

from flask import Flask, render_template, abort
from datetime import datetime
import os
import markdown
import re
from pathlib import Path

app = Flask(__name__)

from data import * 
# Your projects - easily add new ones here
PROJECTS = [
    {
        'title': 'Cool Project Name',
        'description': 'Detailed description of your project. What problem does it solve? What technologies did you use?',
        'tags': ['PyTorch', 'Computer Vision', '3D'],
        'github_link': 'https://github.com/yourusername/project',
        'demo_link': '#',
        'image': 'static/images/project1.jpg',
        'date': '2024'
    },
    # Add more projects here
]

# Your information

@app.route('/')
def index():
    return render_template('index.html', profile=PROFILE, papers=PAPERS[:3], projects=PROJECTS[:3], news=NEWS)

@app.route('/research')
def research():
    return render_template('research.html', profile=PROFILE, papers=PAPERS)

@app.route('/projects')
def projects():
    return render_template('projects.html', profile=PROFILE, projects=PROJECTS)

@app.route('/cv')
def cv():
    return render_template('cv.html', profile=PROFILE)



# Blog functions
def parse_post(filepath):
    """Parse a markdown post with frontmatter"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Split frontmatter and content
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            frontmatter = parts[1].strip()
            markdown_content = parts[2].strip()
        else:
            frontmatter = ""
            markdown_content = content
    else:
        frontmatter = ""
        markdown_content = content
    
    # Parse frontmatter
    metadata = {}
    for line in frontmatter.split('\n'):
        if ':' in line:
            key, value = line.split(':', 1)
            key = key.strip()
            value = value.strip().strip('"').strip("'")
            
            # Handle tags as list
            if key == 'tags':
                # Remove brackets and split by comma
                value = value.strip('[]').split(',')
                value = [tag.strip().strip('"').strip("'") for tag in value]
            
            metadata[key] = value
    
    # Convert markdown to HTML with extensions
    html_content = markdown.markdown(
        markdown_content, 
        extensions=['fenced_code', 'codehilite', 'tables', 'toc']
    )
    
    # Get slug from filename
    slug = Path(filepath).stem
    
    return {
        'slug': slug,
        'title': metadata.get('title', 'Untitled'),
        'date': metadata.get('date', ''),
        'tags': metadata.get('tags', []),
        'excerpt': metadata.get('excerpt', ''),
        'content': html_content,
        'filepath': filepath
    }

def get_all_posts():
    """Get all blog posts sorted by date (newest first)"""
    posts_dir = Path('posts')
    if not posts_dir.exists():
        return []
    
    posts = []
    for filepath in posts_dir.glob('*.md'):
        try:
            post = parse_post(filepath)
            posts.append(post)
        except Exception as e:
            print(f"Error parsing {filepath}: {e}")
            continue
    
    # Sort by date (newest first)
    posts.sort(key=lambda x: x['date'], reverse=True)
    return posts

def get_post_by_slug(slug):
    """Get a single post by its slug"""
    posts_dir = Path('posts')
    for filepath in posts_dir.glob('*.md'):
        if filepath.stem == slug:
            return parse_post(filepath)
    return None

@app.route('/blog')
def blog():
    posts = get_all_posts()
    return render_template('blog.html', profile=PROFILE, posts=posts)

@app.route('/blog/<slug>')
def blog_post(slug):
    post = get_post_by_slug(slug)
    if post is None:
        abort(404)
    return render_template('post.html', profile=PROFILE, post=post)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)