# -*- coding: utf-8 -*-
"""
build_static.py — 将 Flask 站点静态化为纯 HTML（用于 Cloudflare Pages / GitHub Pages / Netlify）
================================================================================================
用法：D:\\Program\\Web_Personal\\Web_P\\Scripts\\python.exe build_static.py
产物：dist/ 目录（可直接拖入 Cloudflare Pages / 推送到 GitHub Pages 分支）

以后每次更新 content/ 里的内容后，重新运行本脚本再推送即可。
"""
import os
import shutil
import sys

try:
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
except Exception:
    pass

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DIST_DIR = os.path.join(BASE_DIR, 'dist')

# 需要导出的路由（不含 / 重定向）
ROUTES = [
    '/en/', '/zh/',
    '/en/projects/', '/zh/projects/',
    '/en/blog/', '/zh/blog/',
    '/en/contact/', '/zh/contact/',
]


def route_to_path(route: str) -> str:
    """把 URL 路由映射为 dist 下的文件路径（目录式 index.html）"""
    p = route.strip('/')
    if not p:
        return 'index.html'
    return os.path.join(p, 'index.html')


def main():
    sys.path.insert(0, BASE_DIR)
    os.chdir(BASE_DIR)
    import app as appmod  # noqa: E402

    if os.path.exists(DIST_DIR):
        shutil.rmtree(DIST_DIR)
    os.makedirs(DIST_DIR, exist_ok=True)

    client = appmod.app.test_client()

    # 1. 所有项目详情页
    from content.projects import projects
    for proj in projects:
        for lang in ('en', 'zh'):
            ROUTES.append(f'/{lang}/projects/{proj["slug"]}/')

    # 2. 所有博客文章页
    from blog import get_all_posts
    for post in get_all_posts():
        for lang in ('en', 'zh'):
            ROUTES.append(f'/{lang}/blog/{post["slug"]}/')

    # 3. 导出页面
    exported = 0
    for route in ROUTES:
        resp = client.get(route)
        if resp.status_code != 200:
            print(f'[跳过] {route} -> HTTP {resp.status_code}')
            continue
        out = os.path.join(DIST_DIR, route_to_path(route))
        os.makedirs(os.path.dirname(out), exist_ok=True)
        with open(out, 'w', encoding='utf-8') as f:
            f.write(resp.get_data(as_text=True))
        exported += 1
    print(f'[导出] {exported} 个页面')

    # 4. 首页：把英文首页同时作为站点根 index.html（与 Flask 的 / 重定向等价）
    resp = client.get('/en/')
    with open(os.path.join(DIST_DIR, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(resp.get_data(as_text=True))

    # 5. 复制静态资源
    shutil.copytree(os.path.join(BASE_DIR, 'static'), os.path.join(DIST_DIR, 'static'))
    print(f'[静态] static/ 已复制')

    total = sum(len(fs) for _, _, fs in os.walk(DIST_DIR))
    print(f'[完成] dist/ 共 {total} 个文件，大小约 '
          f'{sum(os.path.getsize(os.path.join(r, f)) for r, _, fs in os.walk(DIST_DIR) for f in fs) / 1e6:.1f} MB')
    print('可直接部署：Cloudflare Pages / GitHub Pages / Netlify')


if __name__ == '__main__':
    main()
