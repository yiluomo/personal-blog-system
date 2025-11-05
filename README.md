# 🌸 樱花主题个人博客

一个基于 **Vue3 + Django + SQLite** 的樱花主题个人博客项目，具有精美的樱花飘落动画效果和完整的内容管理系统。

![樱花博客](https://img.shields.io/badge/Vue-3.3.4-brightgreen) ![Django](https://img.shields.io/badge/Django-5.2.7-green) ![License](https://img.shields.io/badge/license-MIT-blue)

## ✨ 项目特点

- 🌸 **樱花主题** - 独特的樱花飘落动画效果
- 🎮 **游戏展示** - 游戏收藏展示系统，支持截图画廊
- 🎵 **音乐播放器** - 网易云风格的音乐播放器，支持播放列表
- 📺 **动漫展示** - 动漫收藏展示系统，支持截图画廊
- 📱 **响应式设计** - 完美适配PC、平板、手机
- 🎨 **精美UI** - 流畅的交互动画和现代化设计
- 🔧 **易于管理** - Django Admin后台，便捷的内容管理

## 🚀 快速开始

### 环境要求

- Python 3.9+
- Node.js 16+

### 1. 克隆项目

```bash
git clone https://github.com/yiluomo/-.git
cd -
```

### 2. 后端配置

```bash
cd backend

# 安装依赖
pip install -r requirements.txt

# 数据库迁移
python manage.py migrate

# 创建管理员账户
python manage.py createsuperuser

# 初始化测试数据
python init_data.py

# 启动后端服务
python manage.py runserver
```

后端服务：`http://127.0.0.1:8000`  
管理后台：`http://127.0.0.1:8000/admin`

### 3. 前端配置

```bash
cd frontend

# 安装依赖
npm install

# 启动开发服务器
npm run dev
```

前端服务：`http://localhost:5173`

## 📦 功能模块

### 核心功能

| 模块 | 功能描述 |
|------|---------|
| 🖼️ **轮播图** | 全屏轮播展示，自动/手动切换 |
| 👤 **个人信息** | 头像、简介、简历、联系方式展示 |
| 💼 **作品展示** | 作品集展示，支持外链跳转 |
| 🎯 **爱好展示** | 标签页切换展示游戏、音乐、动漫 |

### 扩展功能

#### 🎮 游戏模块
- 游戏卡片网格展示
- 5星评分系统
- 游玩时长显示
- 详情弹窗
- 游戏截图画廊

#### 🎵 音乐模块
- 网易云风格播放器
- 旋转唱片动画
- 唱针摆动效果
- 播放控制（播放/暂停/上下曲）
- 进度条拖动
- 播放列表

#### 📺 动漫模块
- 动漫海报墙展示
- 5星评分系统
- 年份/状态标签
- 详情弹窗
- 精彩截图画廊

## 🎨 技术栈

### 前端
- **Vue 3.3** - 渐进式JavaScript框架
- **Vue Router 4** - 官方路由管理
- **Axios** - HTTP客户端
- **Tailwind CSS** - 实用优先的CSS框架
- **Anime.js** - 轻量级动画库
- **Vite** - 下一代前端构建工具

### 后端
- **Django 5.2** - Python Web框架
- **Django REST Framework** - RESTful API工具包
- **SQLite** - 轻量级数据库
- **Pillow** - Python图像处理库

## 📂 项目结构

```
sakura-blog/
├── backend/                    # Django后端
│   ├── blog_backend/          # 项目配置
│   ├── api/                   # API应用
│   │   ├── models.py          # 数据模型（9个）
│   │   ├── serializers.py     # 序列化器
│   │   ├── views.py           # 视图
│   │   └── admin.py           # 后台管理
│   ├── media/                 # 媒体文件
│   ├── manage.py              # Django管理脚本
│   └── init_data.py           # 数据初始化
│
├── frontend/                  # Vue3前端
│   ├── src/
│   │   ├── components/        # 组件（8个）
│   │   ├── views/             # 页面
│   │   ├── router/            # 路由
│   │   └── utils/             # 工具
│   ├── package.json
│   └── vite.config.js
│
└── README.md
```

## 🔧 后台管理

访问 `http://127.0.0.1:8000/admin` 进入管理后台。

### 管理功能
- ✅ 个人信息管理
- ✅ 轮播图管理
- ✅ 作品管理
- ✅ 游戏管理（含截图）
- ✅ 音乐管理
- ✅ 动漫管理（含截图）

### 图片上传建议

| 类型 | 建议尺寸 | 数量 |
|------|---------|------|
| 轮播图 | 1920x1080 | 3张 |
| 头像 | 300x300 | 1张 |
| 作品封面 | 600x400 | 3-5张 |
| 游戏封面 | 400x600 | 若干 |
| 音乐封面 | 300x300 | 若干 |
| 动漫封面 | 300x420 | 若干 |

## 🌐 API接口

| 接口 | 方法 | 说明 |
|------|------|------|
| `/api/userinfo/current/` | GET | 获取用户信息 |
| `/api/carousel/` | GET | 获取轮播图 |
| `/api/works/` | GET | 获取作品列表 |
| `/api/games/` | GET | 获取游戏列表 |
| `/api/music/` | GET | 获取音乐列表 |
| `/api/anime/` | GET | 获取动漫列表 |

## 🚢 部署

### 前端部署
```bash
cd frontend
npm run build
# 将 dist 目录部署到静态服务器
```

### 后端部署
```bash
# 修改 settings.py
DEBUG = False
ALLOWED_HOSTS = ['your-domain.com']

# 使用 Gunicorn
pip install gunicorn
gunicorn blog_backend.wsgi:application
```

## ❓ 常见问题

<details>
<summary><b>图片无法显示？</b></summary>

确保已在后台上传图片，并且Django服务正在运行。
</details>

<details>
<summary><b>音乐无法播放？</b></summary>

1. 检查音频链接是否有效
2. 确认浏览器允许自动播放
3. 尝试手动点击播放按钮
</details>

<details>
<summary><b>如何修改主题色？</b></summary>

编辑 `frontend/tailwind.config.js` 中的颜色配置。
</details>

## 📝 开发计划

- [ ] 添加文章博客功能
- [ ] 实现评论系统
- [ ] 添加访问统计
- [ ] 实现搜索功能
- [ ] 添加深色模式
- [ ] 实现多语言支持

## 📄 许可证

本项目采用 [MIT](LICENSE) 许可证。

## 🙏 致谢

感谢所有开源项目的贡献者！

---

**如果这个项目对你有帮助，请给个 ⭐️ Star 支持一下！** 🌸
