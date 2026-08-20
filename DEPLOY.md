# personal-site 免费上线部署指南

> 适用：`D:\Program\Web_Personal\personal-site`（Flask + 无数据库 + Markdown 博客）
> 本文按推荐度给出三个免费方案，选一个即可。

---

## 0. 上线前准备（三个方案通用）

在项目根目录创建 `.gitignore`，内容：

```text
__pycache__/
*.pyc
.venv/
venv/
server.log
dist/
.reasonix/
.workbuddy/
.DS_Store
```

并确认 `app.py` 末尾的 `app.run(debug=True)` 不在生产使用（可改为 `debug = os.environ.get('FLASK_DEBUG') == '1'`）。

---

## 方案 A：Cloudflare Pages（⭐ 最推荐，永久免费 + 全球 CDN）

适合你的站点（内容驱动、访问量小），**零服务器成本、无限流量、免费 HTTPS + 自定义域名**。

### A1. 本地生成静态站

```powershell
cd D:\Program\Web_Personal\personal-site
D:\Program\Web_Personal\Web_P\Scripts\python.exe build_static.py
```

会生成 `dist/` 目录（24+ 个页面 + static/）。每次改完 `content/` 里的内容后重新运行一次即可。

> 手动预览：双击 `dist/index.html`，或 `python -m http.server 8080 -d dist` 后访问 `http://127.0.0.1:8080`。

### A2. 推到 GitHub

```powershell
cd D:\Program\Web_Personal\personal-site
git init
git add .
git commit -m "init: personal site static build"
git branch -M main
git remote add origin https://github.com/<你的用户名>/<仓库名>.git   # 先在 GitHub 建空仓库
git push -u origin main
```

### A3. 连接 Cloudflare Pages（约 5 分钟）

1. 注册/登录 [dash.cloudflare.com](https://dash.cloudflare.com)（免费）
2. 左侧 **Workers & Pages → Create → Pages → Connect to Git**
3. 授权 GitHub，选择刚才的仓库
4. 构建设置：
   - **Framework preset**: None（或 Static HTML）
   - **Build command**: 留空（dist 已生成好）
   - **Build output directory**: `dist`
5. 点 **Save and Deploy**，等 1 分钟即可获得 `https://<项目名>.pages.dev` 网址

### A4. 绑定自定义域名（可选，需先有域名）

- 域名在 Cloudflare 托管后：Pages → Custom domains → Add，自动配 DNS + 免费 HTTPS
- 域名在别处：先把 NS 改到 Cloudflare，再同上

### A5. 以后更新内容

```powershell
cd D:\Program\Web_Personal\personal-site
D:\Program\Web_Personal\Web_P\Scripts\python.exe build_static.py   # 重新生成
git add .
git commit -m "update content"
git push                      # Cloudflare 自动重新部署
```

---

## 方案 B：Vercel 直接跑 Flask（改造最小）

保留动态渲染，git push 自动部署。

### B1. 加适配文件

项目根新建 `vercel.json`：

```json
{
  "version": 2,
  "builds": [{ "src": "wsgi.py", "use": "@vercel/python" }],
  "routes": [{ "src": "/(.*)", "dest": "wsgi.py" }]
}
```

项目根新建 `wsgi.py`：

```python
import os
os.environ.setdefault('FLASK_DEBUG', '0')
from app import app as application
```

`requirements.txt` 删掉 gunicorn（Vercel 用自带的 WSGI 运行时）：

```text
Flask==3.0.3
Markdown==3.6
python-frontmatter==1.1.0
```

### B2. 部署

```powershell
npm i -g vercel        # 或 winget install vercel
cd D:\Program\Web_Personal\personal-site
vercel                 # 首次登录，选默认即可
vercel --prod
```

得到 `https://<项目>.vercel.app`。以后 `git push` 或 `vercel --prod` 自动更新。

---

## 方案 C：Render（最接近现状，但冷启动慢）

### C1. 项目根新建 `render.yaml`：

```yaml
services:
  - type: web
    name: personal-site
    runtime: python
    buildCommand: pip install -r requirements.txt
    startCommand: gunicorn app:app --bind 0.0.0.0:$PORT
    plan: free
```

### C2. 部署

1. 先把项目推到 GitHub（见 A2，但**不要**提交 dist/，保留 Flask 结构）
2. 注册 [render.com](https://render.com)（免费）→ New → Web Service → 选仓库
3. Render 自动识别 `render.yaml`，点 Create，几分钟后得到 `https://personal-site.onrender.com`

> 免费实例 15 分钟无访问会休眠，首次访问约 30-60 秒冷启动，适合低频个人站。

---

## 上线后检查清单

- [ ] 首页/中英页 200，404 页面正常（不存在 URL 返回 404 而非 500）
- [ ] HTTPS 已生效（地址栏小锁）
- [ ] 静态图片、字体、anim.js 正常加载（F12 Console 无 404）
- [ ] 手机端排版正常（开发者工具切设备模拟）
- [ ] Google Fonts 若加载慢，可下载字体本地化（`static/fonts/` + `@font-face`）
- [ ] `server.log` 未提交；`SECRET_KEY` 用环境变量（若日后加 session）

## 常见问题

| 问题 | 解决 |
|---|---|
| 方案 A 更新后页面没变 | 等 1-2 分钟部署完成，或 Pages → Deployments 看是否失败 |
| 中文字体未本地化 | 方案 A 的 `dist/static` 是复制来的，可手动放字体文件 |
| 需要统计访问量 | Cloudflare 自带 Analytics（免费，无需 JS） |
| 想彻底在国内快速访问 | 免费方案都难保证，需国内服务器（要备案），成本最低的是对象存储+CDN（如腾讯云 COS+CDN 按量付费） |

---

## 最终建议

- **首选方案 A（Cloudflare Pages）**：免费、快、简单，更新流程 = 跑脚本 + push，最适合这个项目。
- 方案 B 适合你还想改代码/加动态功能时。
- 方案 C 只是"能跑"的最低成本选项。
