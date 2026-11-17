# Personal Website — Daniel Zhao (赵禹皓)

Source code for my bilingual (EN/ZH) personal website: projects, blog posts, and a short bio.

> **Live site:** https://danielyhzhao.github.io/
> **Deploy:** GitHub Pages (static build). A Flask/Vercel deployment option is documented in `DEPLOY.md`.


---

## ✨ Features

- Bilingual pages (`/en/`, `/zh/`)
- Project case studies (problem → data → method → result → insight)
- Markdown blog (`content/blog/*.md`, frontmatter + auto rendering)
- Responsive layout

## 🧱 Tech Stack

| Layer | Tech |
|---|---|
| Backend | Flask 3.0 (Python) |
| Frontend | Plain HTML/CSS/JS (no framework) |
| Blog | Markdown + frontmatter |
| Deploy | Vercel (Flask) / GitHub Pages (static build) |

## 🚀 Run Locally

```powershell
# 1. Install dependencies (Python 3.10+)
pip install -r requirements.txt

# 2. Start the dev server
python -m flask --app app run --port 5000
# Open http://127.0.0.1:5000
```

## 📝 Updating Content

### Add a blog post
Create a new `.md` file in `content/blog/` with frontmatter (`title`, `date`, `description`, `tags`):

```markdown
---
title: Post title
date: 2026-08-20
description: One-line summary
tags: [python, llm]
---

Body (Markdown; code blocks and tables supported)…
```

### Update bio / projects
- Bio copy: `content/translations.py`
- Projects list: `content/projects.py`
- Updates/news: `content/news.py`

## 🌐 Deployment

### Option 1: Vercel (Flask dynamic)
- Repo already includes `vercel.json` + `wsgi.py`; import the repo on [vercel.com](https://vercel.com)
- Pushing to `main` auto-redeploys

### Option 2: GitHub Pages (static)
1. Regenerate the static site: `python build_static.py` (outputs to `dist/`)
2. Publish to the `gh-pages` branch:

```powershell
git checkout --orphan gh-pages
git rm -rf .
cp -r dist/* .
git add -A
git commit -m "deploy: static site"
git push origin gh-pages
git checkout main
```

3. Site URL: `https://danielyhzhao.github.io/Personal_Website/`

> The root user site (https://danielyhzhao.github.io/) is maintained in the
> `danielyhzhao/danielyhzhao.github.io` repo (main branch, built from `dist/`).

## 📁 Project Layout

```
├── app.py               # Flask app (routes / error handlers)
├── blog.py              # Blog loader + Markdown rendering
├── wsgi.py              # WSGI entrypoint (Vercel)
├── vercel.json          # Vercel config
├── build_static.py      # Static site generator (outputs dist/)
├── content/
│   ├── translations.py  # EN/ZH copy
│   ├── projects.py      # Project data
│   ├── news.py          # Updates data
│   └── blog/            # Markdown posts
├── templates/           # Jinja2 templates
├── static/              # CSS/JS/images
└── dist/                # Static build output (git-ignored)
```

## 📄 License

MIT
