projects = [
    # ===== 主展示：GitHub 真实项目（深做 case study） =====
    {
        'slug': 'mnist-gen-compare',
        'featured': True,
        'year': 2025,
        'icon': '🎨',
        'category': {'en': 'Generative AI', 'zh': '生成式 AI'},
        'title': {'en': 'MNIST Generation: DCGAN vs DDPM', 'zh': 'MNIST 生成：DCGAN 对比 DDPM'},
        'summary': {
            'en': 'Trained and compared conditional DCGAN and DDPM on MNIST, with an interactive Flask web app.',
            'zh': '训练并对比条件 DCGAN 与 DDPM，配套可交互的 Flask 网页应用。',
        },
        'stack': ['Python', 'PyTorch', 'DCGAN', 'DDPM', 'Flask'],
        'github_url': 'https://github.com/Danielyhzhao/MNISTGenCompare',
        'cover': 'mnist_cover.png',
        'gallery': ['mnist_dcgan.png', 'mnist_ddpm.png', 'mnist_curve_dcgan.png', 'mnist_curve_ddpm.png'],
        'case_study': {
            'problem': {
                'en': 'Understand the quality and stability trade-offs between GANs and diffusion models via a concrete comparison.',
                'zh': '通过具体对比，理解 GAN 与扩散模型在生成质量与训练稳定性上的权衡。',
            },
            'data': {
                'en': 'MNIST handwritten digit dataset.',
                'zh': 'MNIST 手写数字数据集。',
            },
            'method': {
                'en': 'Trained conditional DCGAN and conditional DDPM; compared generation quality with metrics.',
                'zh': '训练条件 DCGAN 与条件 DDPM，用指标对比生成质量。',
            },
            'result': {
                'en': 'Delivered an interactive Flask app to generate MNIST images with pre-trained models, plus a metrics comparison.',
                'zh': '交付可交互的 Flask 应用，用预训练模型生成 MNIST 图像，并附指标对比。',
            },
            'insight': {
                'en': 'Diffusion models trade slower sampling for higher stability and fidelity than GANs.',
                'zh': '扩散模型以更慢的采样换取比 GAN 更高的稳定性和保真度。',
            },
        },
    },
    {
        'slug': 'dual-llm',
        'featured': True,
        'year': 2025,
        'icon': '🤖',
        'category': {'en': 'LLM Engineering', 'zh': '大语言模型工程'},
        'title': {'en': 'Dual-LLM Code Tutoring System', 'zh': '双 LLM 代码辅导系统'},
        'summary': {
            'en': 'An adversarial dual-LLM loop that analyzes student code and generates feedback, with a web UI.',
            'zh': '对抗式双 LLM 循环分析学生代码并生成反馈，配套 Web 界面。',
        },
        'stack': ['Python', 'LLM', 'DeepSeek API', 'Web UI'],
        'github_url': 'https://github.com/Danielyhzhao/Dual_LLM',
        'cover': 'dual_llm_cover.png',
        'gallery': ['dual_llm_cover.png'],
        'case_study': {
            'problem': {
                'en': 'Code feedback is hard to automate and personalize for students.',
                'zh': '学生代码反馈难以自动化和个性化。',
            },
            'data': {
                'en': 'Student-submitted code attempts.',
                'zh': '学生提交的代码。',
            },
            'method': {
                'en': 'LLM-1 acts as examiner generating tests; LLM-2 acts as mentor generating suggestions and reflection prompts.',
                'zh': 'LLM-1 作为考官生成测试用例，LLM-2 作为导师生成建议与反思提示。',
            },
            'result': {
                'en': 'Built a working adversarial review loop with a web UI.',
                'zh': '构建可用的对抗式审查循环，并配有 Web 界面。',
            },
            'insight': {
                'en': 'Adversarial LLM collaboration improves the specificity and quality of code feedback.',
                'zh': '对抗式 LLM 协作提升了代码反馈的针对性与质量。',
            },
        },
    },
    {
        'slug': 'car-racing-rl',
        'featured': True,
        'year': 2025,
        'icon': '🏎️',
        'category': {'en': 'Reinforcement Learning', 'zh': '强化学习'},
        'title': {'en': 'Car Racing: Q-Learning vs DQN', 'zh': '赛车竞速：Q-Learning 对比 DQN'},
        'summary': {
            'en': 'Multi-agent racing simulation comparing Q-Learning and DQN agents, rendered in real time.',
            'zh': '多智能体赛车仿真，对比 Q-Learning 与 DQN，实时渲染。',
        },
        'stack': ['Python', 'Reinforcement Learning', 'Q-Learning', 'DQN', 'Pygame'],
        'github_url': 'https://github.com/Danielyhzhao/Car-Racing-Q-learning-vs-DQN',
        'cover': 'racing_cover.png',
        'gallery': ['racing_learning.png', 'racing_roc.png', 'racing_train.png'],
        'case_study': {
            'problem': {
                'en': 'Compare how value-based RL algorithms perform in a dynamic environment.',
                'zh': '对比基于价值的强化学习算法在动态环境中的表现。',
            },
            'data': {
                'en': 'A dynamic two-car racing environment built with Pygame.',
                'zh': '用 Pygame 构建的动态双车竞速环境。',
            },
            'method': {
                'en': 'Trained Q-Learning and DQN agents side by side on the same track.',
                'zh': '在同一赛道并排训练 Q-Learning 与 DQN 智能体。',
            },
            'result': {
                'en': 'Real-time simulation with Matplotlib training curves for both agents.',
                'zh': '实时仿真，并用 Matplotlib 可视化两个智能体的训练曲线。',
            },
            'insight': {
                'en': 'DQN handles larger state spaces better, while Q-Learning is simpler but limited by a Q-table.',
                'zh': 'DQN 更适合大状态空间，Q-Learning 更简单但受 Q 表容量限制。',
            },
        },
    },
    {
        'slug': 'sentiment-analysis',
        'featured': True,
        'year': 2025,
        'icon': '💬',
        'category': {'en': 'NLP', 'zh': '自然语言处理'},
        'title': {'en': 'Social Media Sentiment Analysis', 'zh': '社交媒体情感语义分析'},
        'summary': {
            'en': 'BiLSTM + BERT sentiment classification with data preprocessing, training, and a real-time web interface.',
            'zh': '基于 BiLSTM 与 BERT 的情感分类，含数据预处理、训练与实时 Web 界面。',
        },
        'stack': ['Python', 'BERT', 'BiLSTM', 'Flask'],
        'github_url': 'https://github.com/Jackiee02/SentimentAnalysisSystem',
        'cover': 'sentiment_cover.png',
        'gallery': ['sentiment_platform.png', 'sentiment_heatmap.png', 'sentiment_wordcloud.png', 'sentiment_trends.png'],
        'case_study': {
            'problem': {
                'en': 'Analyze sentiment tendencies in social media text to track public opinion and customer feedback.',
                'zh': '分析社交媒体文本的情感倾向，追踪舆情与客户反馈。',
            },
            'data': {
                'en': 'Social media text data, cleaned and tokenized with a built vocabulary.',
                'zh': '社交媒体文本数据，经清洗、分词并构建词表。',
            },
            'method': {
                'en': 'Trained and compared BiLSTM and BERT-based Transformer models for classification.',
                'zh': '训练并对比 BiLSTM 与基于 BERT 的 Transformer 模型进行分类。',
            },
            'result': {
                'en': 'Delivered a web interface for real-time sentiment prediction, with training and evaluation.',
                'zh': '提供实时情感预测的 Web 界面，并完成训练与评估。',
            },
            'insight': {
                'en': 'Deep learning models significantly improve sentiment classification, enabling public-opinion tracking.',
                'zh': '深度学习模型显著提升情感分类效果，可支撑舆情追踪。',
            },
        },
    },
    {
        'slug': 'diabetes-detection',
        'featured': True,
        'year': 2025,
        'icon': '🩺',
        'category': {'en': 'Machine Learning', 'zh': '机器学习'},
        'title': {'en': 'Early Diabetes Detection', 'zh': '机器学习早期糖尿病检测'},
        'summary': {
            'en': 'Multi-model comparison (LR, RF, GBM, SVM, NN, XGBoost) for diabetes risk prediction at 94.15% accuracy / 0.9716 ROC-AUC.',
            'zh': '多模型对比（LR/RF/GBM/SVM/NN/XGBoost）预测糖尿病风险，达 94.15% 准确率 / 0.9716 ROC-AUC。',
        },
        'stack': ['Python', 'Scikit-learn', 'XGBoost', 'ML'],
        'github_url': 'https://github.com/ANDREWZHU-06/CDS524-Machine-Learning-Group11-Project',
        'cover': 'diabetes_cover.png',
        'gallery': ['diabetes_roc.png', 'diabetes_cm.png', 'diabetes_feature.png', 'diabetes_dist.png'],
        'case_study': {
            'problem': {
                'en': 'Predict diabetes risk from clinical and demographic data to support early intervention.',
                'zh': '基于临床与人口学数据预测糖尿病风险，辅助早期干预。',
            },
            'data': {
                'en': 'Clinical and demographic health data.',
                'zh': '临床与人口学健康数据。',
            },
            'method': {
                'en': 'Compared Logistic Regression, Random Forest, Gradient Boosting, SVM, Neural Networks, and XGBoost, with feature selection.',
                'zh': '对比逻辑回归、随机森林、梯度提升、SVM、神经网络与 XGBoost，并做特征选择。',
            },
            'result': {
                'en': 'Achieved 94.15% accuracy and 0.9716 ROC-AUC; deployed a Streamlit app with real-time prediction.',
                'zh': '达 94.15% 准确率和 0.9716 ROC-AUC；部署了带实时预测的 Streamlit 应用。',
            },
            'insight': {
                'en': 'Feature selection and multi-model comparison identified the best-performing model for early screening.',
                'zh': '特征选择与多模型对比选出了最适合早期筛查的最优模型。',
            },
        },
    },
    # ===== 辅助展示：其他 GitHub 真实项目（简列） =====
    {
        'slug': 'fake-news-detection',
        'featured': False,
        'year': 2025,
        'icon': '📰',
        'category': {'en': 'NLP', 'zh': '自然语言处理'},
        'title': {'en': 'Fake News Detection', 'zh': '假新闻检测'},
        'summary': {
            'en': 'LSTM & BiLSTM with 24 hyperparameter combos, Gradio web app, ROC/PR evaluation.',
            'zh': 'LSTM 与 BiLSTM，24 组超参数对比，Gradio 网页应用，ROC/PR 评估。',
        },
        'stack': ['Python', 'LSTM', 'BiLSTM', 'Gradio'],
        'github_url': 'https://github.com/Jackiee02/FakeNewsDetectionSystem',
        'cover': 'fakenews_cover.png',
        'gallery': ['fakenews_f1.png', 'fakenews_loss.png'],
    },
]
