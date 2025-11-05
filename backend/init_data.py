import os
import django
import json

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog_backend.settings')
django.setup()

from api.models import UserInfo, Carousel, Work, Hobby, Game, Music, Anime

def init_data():
    print("开始初始化数据...")
    
    # 清空现有数据
    UserInfo.objects.all().delete()
    Carousel.objects.all().delete()
    Work.objects.all().delete()
    Hobby.objects.all().delete()
    Game.objects.all().delete()
    Music.objects.all().delete()
    Anime.objects.all().delete()
    
    # 创建个人信息
    resume_data = json.dumps([
        {"type": "education", "content": "XX大学 计算机科学与技术专业 2018-2022"},
        {"type": "work", "content": "XX科技公司 前端开发工程师 2022-至今"}
    ], ensure_ascii=False)
    
    contact_data = json.dumps([
        {"type": "email", "icon": "fa-envelope", "url": "mailto:example@email.com", "text": "example@email.com"},
        {"type": "github", "icon": "fa-github", "url": "https://github.com/username", "text": "GitHub"},
        {"type": "wechat", "icon": "fa-weixin", "url": "#", "text": "微信: your_wechat"}
    ], ensure_ascii=False)
    
    UserInfo.objects.create(
        avatar='avatars/default_avatar.jpg',
        name='张三',
        intro='热爱编程，喜欢探索新技术。专注于前端开发，追求极致的用户体验。',
        resume=resume_data,
        contact=contact_data
    )
    print("✓ 个人信息创建成功")
    
    # 创建轮播图数据
    carousel_data = [
        {'image': 'carousel/slide1.jpg', 'sort': 1},
        {'image': 'carousel/slide2.jpg', 'sort': 2},
        {'image': 'carousel/slide3.jpg', 'sort': 3}
    ]
    
    for item in carousel_data:
        Carousel.objects.create(**item, is_show=True)
    print("✓ 轮播图数据创建成功")
    
    # 创建爱好分类数据
    hobbies_data = [
        {'name': '游戏', 'hobby_type': 'game', 'icon': 'fa-gamepad', 'desc': '喜欢各类游戏，从RPG到FPS，享受游戏带来的乐趣和挑战。'},
        {'name': '音乐', 'hobby_type': 'music', 'icon': 'fa-music', 'desc': '热爱音乐，喜欢听各种风格的歌曲。从古典到流行，从摇滚到电子。'},
        {'name': '动漫', 'hobby_type': 'anime', 'icon': 'fa-film', 'desc': '动漫爱好者，追过很多经典作品。喜欢日漫的画风和故事。'}
    ]
    
    for hobby in hobbies_data:
        Hobby.objects.create(**hobby)
    print("✓ 爱好分类创建成功")
    
    # 创建游戏数据
    games_data = [
        {
            'name': '塞尔达传说：旷野之息',
            'cover': 'games/covers/zelda.jpg',
            'desc': '任天堂开发的开放世界动作冒险游戏，拥有广阔的世界和自由的探索体验。',
            'play_time': '200小时+',
            'rating': 5
        },
        {
            'name': '原神',
            'cover': 'games/covers/genshin.jpg',
            'desc': '米哈游开发的开放世界冒险游戏，精美的画面和丰富的角色系统。',
            'play_time': '500小时+',
            'rating': 5
        },
        {
            'name': '艾尔登法环',
            'cover': 'games/covers/elden.jpg',
            'desc': 'FromSoftware开发的魂系列游戏，充满挑战的战斗和庞大的世界观。',
            'play_time': '150小时',
            'rating': 5
        }
    ]
    
    for game in games_data:
        Game.objects.create(**game)
    print("✓ 游戏数据创建成功")
    
    # 创建音乐数据
    music_data = [
        {
            'title': '夜曲',
            'artist': '周杰伦',
            'album': '十一月的萧邦',
            'cover': 'music/covers/yequ.jpg',
            'audio_url': 'https://music.163.com/#/song?id=123456',
            'duration': '03:45'
        },
        {
            'title': '晴天',
            'artist': '周杰伦',
            'album': '叶惠美',
            'cover': 'music/covers/qingtian.jpg',
            'audio_url': 'https://music.163.com/#/song?id=123457',
            'duration': '04:28'
        },
        {
            'title': '稻香',
            'artist': '周杰伦',
            'album': '魔杰座',
            'cover': 'music/covers/daoxiang.jpg',
            'audio_url': 'https://music.163.com/#/song?id=123458',
            'duration': '03:43'
        }
    ]
    
    for music in music_data:
        Music.objects.create(**music)
    print("✓ 音乐数据创建成功")
    
    # 创建动漫数据
    anime_data = [
        {
            'name': '进击的巨人',
            'cover': 'anime/covers/aot.jpg',
            'desc': '人类与巨人之间的生存战争，充满悬念和反转的史诗级作品。',
            'year': 2013,
            'rating': 5,
            'status': '已完结'
        },
        {
            'name': '鬼灭之刃',
            'cover': 'anime/covers/kimetsu.jpg',
            'desc': '少年为了拯救变成鬼的妹妹而踏上斩鬼之路，精美的战斗画面。',
            'year': 2019,
            'rating': 5,
            'status': '连载中'
        },
        {
            'name': '咒术回战',
            'cover': 'anime/covers/jujutsu.jpg',
            'desc': '现代背景下的咒术师与咒灵的战斗，热血的战斗场面。',
            'year': 2020,
            'rating': 5,
            'status': '连载中'
        }
    ]
    
    for anime in anime_data:
        Anime.objects.create(**anime)
    print("✓ 动漫数据创建成功")
    
    # 创建作品数据
    works_data = [
        {
            'title': '个人博客系统',
            'cover_image': 'works/project1.jpg',
            'desc': '基于Vue3和Django开发的个人博客系统，具有完整的前后端分离架构。',
            'link': 'https://github.com/username/blog'
        },
        {
            'title': '在线商城项目',
            'cover_image': 'works/project2.jpg',
            'desc': '电商平台前端开发，实现了商品展示、购物车、订单管理等核心功能。',
            'link': 'https://github.com/username/shop'
        },
        {
            'title': '数据可视化大屏',
            'cover_image': 'works/project3.jpg',
            'desc': '企业数据可视化展示系统，使用ECharts和D3.js实现各类图表展示。',
            'link': 'https://github.com/username/dashboard'
        }
    ]
    
    for work in works_data:
        Work.objects.create(**work)
    print("✓ 作品数据创建成功")
    
    print("\n" + "="*50)
    print("数据初始化完成！")
    print("="*50)
    print("\n注意：图片字段使用了占位符，请在Django Admin后台上传实际图片。")
    print("\n后台管理地址: http://127.0.0.1:8000/admin")
    print("用户名: admin")
    print("密码: admin123")
    print("\n需要上传的图片类型：")
    print("  - 轮播图: 3张 (1920x1080)")
    print("  - 个人头像: 1张 (300x300)")
    print("  - 作品封面: 3张 (600x400)")
    print("  - 游戏封面: 3张 + 游戏截图")
    print("  - 音乐封面: 3张")
    print("  - 动漫封面: 3张 + 动漫截图")

if __name__ == '__main__':
    init_data()
