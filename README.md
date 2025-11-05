# 樱花主题个人博客

一个基于 Vue3 + Django + MySQL 的樱花主题个人博客项目，具有精美的樱花飘落动画效果和响应式设计。

## 项目特点

- 🌸 樱花主题视觉设计，带有樱花飘落动画效果
- 📱 完全响应式布局，适配PC、平板、手机
- 🎨 精美的UI设计和流畅的交互动画
- 🔧 前后端分离架构，易于维护和扩展
- 📊 Django Admin后台管理，方便数据管理

## 技术栈

### 前端
- Vue 3 (Composition API)
- Vue Router 4
- Axios
- Tailwind CSS
- Anime.js (动画库)
- Font Awesome (图标)

### 后端
- Django 4.2
- Django REST Framework
- MySQL 8.0
- drf-yasg (API文档)

## 项目结构

```
sakura-blog/
├── backend/              # Django 后端
│   ├── blog_backend/     # 项目配置
│   ├── api/              # API应用
│   ├── media/            # 媒体文件
│   ├── requirements.txt  # Python依赖
│   ├── manage.py         # Django管理脚本
│   └── init_data.py      # 数据初始化脚本
├── frontend/             # Vue3 前端
│   ├── src/
│   │   ├── components/   # 组件
│   │   ├── views/        # 页面
│   │   ├── router/       # 路由
│   │   └── utils/        # 工具函数
│   ├── package.json      # Node依赖
│   └── vite.config.js    # Vite配置
└── README.md             # 项目文档
```

## 快速开始

### 环境要求

- Python 3.9+
- Node.js 16+
- MySQL 8.0+
- Anaconda (推荐)

### 1. 数据库配置

```bash
# 登录MySQL
mysql -u root -p

# 创建数据库
CREATE DATABASE blog_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

# 创建用户
CREATE USER 'blog_user'@'localhost' IDENTIFIED BY 'blog_password';

# 授权
GRANT ALL PRIVILEGES ON blog_db.* TO 'blog_user'@'localhost';
FLUSH PRIVILEGES;
```

### 2. 后端配置

```bash
# 创建虚拟环境（使用Anaconda）
conda create -n blog_env python=3.9
conda activate blog_env

# 进入后端目录
cd backend

# 安装依赖
pip install -r requirements.txt

# 数据库迁移
python manage.py makemigrations
python manage.py migrate

# 创建超级用户
python manage.py createsuperuser

# 初始化测试数据
python init_data.py

# 启动后端服务
python manage.py runserver
```

后端服务将运行在 `http://127.0.0.1:8000`

### 3. 前端配置

```bash
# 进入前端目录
cd frontend

# 安装依赖
npm install

# 启动开发服务器
npm run dev
```

前端服务将运行在 `http://localhost:5173`

## 功能模块

### 1. 轮播图模块
- 全屏轮播展示
- 自动切换（5秒间隔）
- 手动切换（按钮/指示器）
- 淡入淡出动画效果

### 2. 个人信息模块
- 头像展示
- 个人简介
- 教育/工作经历
- 联系方式（支持跳转）

### 3. 作品展示模块
- 网格布局展示
- 封面图片
- 作品描述
- 外链跳转

### 4. 爱好展示模块
- 游戏、音乐、动漫三大类
- 图标+描述展示
- 悬停动画效果

### 5. 樱花动画
- 樱花飘落效果
- 随机轨迹和速度
- 性能优化（限制数量）

## 后台管理

访问 `http://127.0.0.1:8000/admin` 进入Django后台管理系统。

### 管理功能
- 个人信息管理（头像、简介、简历、联系方式）
- 轮播图管理（上传图片、排序、显示控制）
- 作品管理（添加/编辑/删除作品）
- 爱好管理（添加/编辑/删除爱好）

### 图片上传说明
初始化数据使用了占位符，需要在后台上传实际图片：
1. 轮播图：建议尺寸 1920x1080，二次元风格图片
2. 头像：建议尺寸 300x300，正方形
3. 作品封面：建议尺寸 600x400

## API文档

访问 `http://127.0.0.1:8000/swagger/` 查看完整的API文档。

### 主要接口
- `GET /api/userinfo/current/` - 获取当前用户信息
- `GET /api/carousel/` - 获取轮播图列表
- `GET /api/works/` - 获取作品列表
- `GET /api/hobbies/` - 获取爱好列表

## 部署说明

### 前端部署
```bash
cd frontend
npm run build
```
将生成的 `dist` 目录部署到静态服务器（如Nginx）。

### 后端部署
1. 修改 `settings.py` 中的配置：
   - `DEBUG = False`
   - 设置 `ALLOWED_HOSTS`
   - 配置生产环境数据库

2. 收集静态文件：
```bash
python manage.py collectstatic
```

3. 使用 Gunicorn 运行：
```bash
pip install gunicorn
gunicorn blog_backend.wsgi:application --bind 0.0.0.0:8000
```

## 常见问题

### 1. 跨域问题
确保 Django `settings.py` 中的 `CORS_ALLOWED_ORIGINS` 包含前端地址。

### 2. 图片无法显示
- 检查 `MEDIA_URL` 和 `MEDIA_ROOT` 配置
- 确保在 `urls.py` 中添加了媒体文件路由
- 前端使用完整URL访问图片

### 3. 数据库连接失败
- 检查MySQL服务是否启动
- 确认数据库用户名和密码正确
- 检查数据库是否已创建

### 4. 樱花动画卡顿
- 减少花瓣数量（修改 `CherryBlossomAnimation.vue`）
- 移动端自动减少到10片

## 开发建议

1. **图片优化**：使用压缩后的图片，提升加载速度
2. **数据备份**：定期备份数据库数据
3. **安全配置**：生产环境修改 `SECRET_KEY` 和数据库密码
4. **性能优化**：启用缓存、CDN加速

## 许可证

MIT License

## 联系方式

如有问题或建议，欢迎联系。

---

**祝你使用愉快！🌸**
