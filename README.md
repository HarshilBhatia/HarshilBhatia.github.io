# Portfolio Website Template

A clean, professional portfolio website built with Flask to showcase your research papers and projects.

## Features

- 🎨 Modern, responsive design
- 📱 Mobile-friendly navigation bar
- 📄 Easy-to-update paper and project sections
- 🔗 Automatic linking to PDFs, GitHub, demos
- 📊 Organized CV page
- 🎯 Simple Python data structure for content management

## Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Run the Server

```bash
python app.py
```

Visit `http://localhost:5000` in your browser.

## How to Add Content

### Adding Papers

Open `app.py` and add to the `PAPERS` list:

```python
PAPERS = [
    {
        'title': 'Your Paper Title',
        'authors': 'Your Name, Co-Author',
        'venue': 'CVPR 2024',
        'year': 2024,
        'abstract': 'Brief description of the paper...',
        'pdf_link': 'https://arxiv.org/pdf/...',
        'project_link': 'https://yourproject.com',
        'code_link': 'https://github.com/yourusername/repo',
        'image': 'static/images/paper_thumbnail.jpg'  # Optional
    },
    # Add more papers...
]
```

### Adding Projects

In `app.py`, add to the `PROJECTS` list:

```python
PROJECTS = [
    {
        'title': 'Cool Project Name',
        'description': 'What does this project do? What technologies?',
        'tags': ['PyTorch', 'Computer Vision', '3D'],
        'github_link': 'https://github.com/yourusername/project',
        'demo_link': 'https://demo.com',  # Optional
        'image': 'static/images/project_thumbnail.jpg',  # Optional
        'date': '2024'
    },
    # Add more projects...
]
```

### Updating Your Profile

Edit the `PROFILE` dictionary in `app.py`:

```python
PROFILE = {
    'name': 'Your Name',
    'title': 'Your Title',
    'institution': 'Your Institution',
    'email': 'your.email@example.com',
    'github': 'https://github.com/yourusername',
    'linkedin': 'https://linkedin.com/in/yourprofile',
    'scholar': 'https://scholar.google.com/yourprofile',
    'bio': 'Your bio text here...'
}
```

### Customizing Your CV

Edit `templates/cv.html` to add your:
- Education history
- Work experience
- Skills
- Awards/Publications

## Project Structure

```
portfolio_website/
├── app.py                  # Main Flask app (edit this to add papers/projects)
├── requirements.txt        # Python dependencies
├── templates/
│   ├── base.html          # Base template with navbar
│   ├── index.html         # Home page
│   ├── research.html      # Research papers page
│   ├── projects.html      # Projects page
│   └── cv.html            # CV page
├── static/
│   ├── css/
│   │   └── style.css      # Styling (customize colors here)
│   └── images/            # Put your images here
└── README.md
```

## Customization

### Changing Colors

Edit the CSS variables in `static/css/style.css`:

```css
:root {
    --primary-color: #2563eb;      /* Main accent color */
    --secondary-color: #1e40af;    /* Hover states */
    --text-color: #1f2937;         /* Main text */
    --text-light: #6b7280;         /* Secondary text */
}
```

### Adding Images

1. Put images in `static/images/`
2. Reference them in your paper/project entries:
   ```python
   'image': 'static/images/my_project.jpg'
   ```

## Deployment

### Option 1: Deploy to PythonAnywhere (Free)
1. Create account at pythonanywhere.com
2. Upload files
3. Configure web app with Flask

### Option 2: Deploy to Heroku
```bash
# Add Procfile
echo "web: python app.py" > Procfile

# Add runtime.txt
echo "python-3.11.0" > runtime.txt

# Deploy
heroku create
git push heroku main
```

### Option 3: Deploy to Render
1. Connect your GitHub repo
2. Add build command: `pip install -r requirements.txt`
3. Add start command: `python app.py`

## Tips

- Keep abstracts concise (2-3 sentences)
- Use high-quality thumbnails (recommended: 400x300px)
- Test on mobile devices
- Add Google Analytics if you want to track visits
- Update your papers/projects regularly

## License

Feel free to use this template for your own portfolio!
