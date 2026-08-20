# ===== 首页 Updates 动态（借鉴 sangluisme.github.io 的 News 区块） =====
# kind: 'blog'  -> 博客文章，模板用 url_for('blog_post', slug=slug) 生成链接
# kind: 'github' -> GitHub 仓库更新，url 为仓库地址
news = [
    {
        'date': '2025-04-23',
        'icon': '📝',
        'kind': 'blog',
        'slug': 'dcgan-vs-ddpm',
        'en': 'New blog: DCGAN vs DDPM on MNIST — what I learned.',
        'zh': '新文章：DCGAN 与 DDPM 实战对比复盘。',
    },
    {
        'date': '2025-04-08',
        'icon': '📦',
        'kind': 'github',
        'url': 'https://github.com/Jackiee02/FakeNewsDetectionSystem',
        'en': 'Fake News Detection system open-sourced on GitHub.',
        'zh': '假新闻检测系统已开源到 GitHub。',
    },
    {
        'date': '2025-03-25',
        'icon': '📦',
        'kind': 'github',
        'url': 'https://github.com/Jackiee02/SentimentAnalysisSystem',
        'en': 'Sentiment analysis system open-sourced (team project).',
        'zh': '情感分析系统已开源（团队项目）。',
    },
    {
        'date': '2025-03-10',
        'icon': '📝',
        'kind': 'blog',
        'slug': 'streamlit-deploy-guide',
        'en': 'New blog: Deploying a Streamlit ML app for free.',
        'zh': '新文章：免费部署 Streamlit 机器学习应用。',
    },
]
