import os
import frontmatter
import markdown

BLOG_DIR = os.path.join(os.path.dirname(__file__), 'content', 'blog')


def get_all_posts():
    posts = []
    for f in os.listdir(BLOG_DIR):
        if f.endswith('.md'):
            post = frontmatter.load(os.path.join(BLOG_DIR, f))
            posts.append({
                'slug': f[:-3],
                'title': post.get('title'),
                'date': post.get('date'),
                'description': post.get('description'),
                'tags': post.get('tags', []),
            })
    return sorted(posts, key=lambda p: p['date'], reverse=True)


def get_post(slug):
    path = os.path.join(BLOG_DIR, f'{slug}.md')
    if not os.path.exists(path):
        return None
    post = frontmatter.load(path)
    return {
        'meta': post.metadata,
        'html': markdown.markdown(post.content, extensions=['fenced_code', 'tables']),
    }
