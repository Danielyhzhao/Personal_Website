from flask import Flask, render_template, redirect, url_for, g, abort
from content.projects import projects
from content.translations import T
from content.news import news
from blog import get_all_posts, get_post

app = Flask(__name__)
LANGS = {'en', 'zh'}


@app.url_defaults
def add_lang(endpoint, values):
    values.setdefault('lang', g.get('lang', 'en'))


@app.url_value_preprocessor
def pull_lang(endpoint, values):
    if values is not None:
        lang = values.pop('lang', 'en')
    else:
        lang = 'en'
    if lang not in LANGS:
        abort(404)
    g.lang = lang


@app.context_processor
def inject_globals():
    lang = g.get('lang', 'en')
    return dict(lang=lang, t=lambda key: T[lang].get(key, key))


@app.route('/')
def index():
    return redirect(url_for('home', lang='en'))


@app.route('/<lang>/')
def home():
    featured = [p for p in projects if p['featured']]
    return render_template('index.html', projects=featured, news=news)


@app.route('/<lang>/projects/')
def project_list():
    return render_template('projects.html', projects=projects)


@app.route('/<lang>/projects/<slug>/')
def project_detail(slug):
    project = next((p for p in projects if p['slug'] == slug), None)
    if not project:
        abort(404)
    return render_template('project_detail.html', project=project)


@app.route('/<lang>/blog/')
def blog_list():
    return render_template('blog.html', posts=get_all_posts())


@app.route('/<lang>/blog/<slug>/')
def blog_post(slug):
    post = get_post(slug)
    if post is None:
        abort(404)
    return render_template('blog_post.html', post=post)


@app.route('/<lang>/contact/')
def contact():
    return render_template('contact.html')


@app.errorhandler(404)
def not_found(e):
    return render_template('error.html', code=404,
                           msg_en='Page not found.',
                           msg_zh='页面不存在。'), 404


@app.errorhandler(500)
def server_error(e):
    return render_template('error.html', code=500,
                           msg_en='Something went wrong on our end.',
                           msg_zh='服务器出了点问题。'), 500


if __name__ == '__main__':
    app.run(debug=True)
