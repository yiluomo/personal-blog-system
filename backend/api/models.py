from django.db import models
import json

class UserInfo(models.Model):
    avatar = models.ImageField(upload_to='avatars/', verbose_name='头像')
    name = models.CharField(max_length=100, verbose_name='姓名')
    intro = models.TextField(verbose_name='简介')
    resume = models.TextField(verbose_name='简历(JSON格式)', help_text='格式: [{"type":"education","content":"..."},{"type":"work","content":"..."}]')
    contact = models.TextField(verbose_name='联系方式(JSON格式)', help_text='格式: [{"type":"email","icon":"fa-envelope","url":"mailto:xxx","text":"xxx"}]')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        db_table = 'user_info'
        verbose_name = '个人信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    def get_resume_list(self):
        try:
            return json.loads(self.resume)
        except:
            return []

    def get_contact_list(self):
        try:
            return json.loads(self.contact)
        except:
            return []


class Carousel(models.Model):
    image = models.ImageField(upload_to='carousel/', verbose_name='轮播图')
    sort = models.IntegerField(default=0, verbose_name='排序')
    is_show = models.BooleanField(default=True, verbose_name='是否显示')

    class Meta:
        db_table = 'carousel'
        verbose_name = '轮播图'
        verbose_name_plural = verbose_name
        ordering = ['sort']

    def __str__(self):
        return f'轮播图 {self.sort}'


class Work(models.Model):
    title = models.CharField(max_length=200, verbose_name='标题')
    cover_image = models.ImageField(upload_to='works/', verbose_name='封面图')
    desc = models.TextField(verbose_name='描述')
    link = models.URLField(blank=True, verbose_name='链接')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        db_table = 'works'
        verbose_name = '作品'
        verbose_name_plural = verbose_name
        ordering = ['-create_time']

    def __str__(self):
        return self.title


class Hobby(models.Model):
    HOBBY_TYPES = [
        ('game', '游戏'),
        ('music', '音乐'),
        ('anime', '动漫'),
    ]
    
    name = models.CharField(max_length=100, verbose_name='名称')
    hobby_type = models.CharField(max_length=20, choices=HOBBY_TYPES, verbose_name='类型')
    icon = models.CharField(max_length=50, verbose_name='图标类名', help_text='FontAwesome图标类名，如: fa-gamepad')
    desc = models.TextField(verbose_name='描述')

    class Meta:
        db_table = 'hobbies'
        verbose_name = '爱好分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f'{self.get_hobby_type_display()} - {self.name}'


class Game(models.Model):
    name = models.CharField(max_length=200, verbose_name='游戏名称')
    cover = models.ImageField(upload_to='games/covers/', verbose_name='游戏封面')
    desc = models.TextField(verbose_name='游戏描述')
    play_time = models.CharField(max_length=100, blank=True, verbose_name='游玩时长', help_text='如: 200小时')
    rating = models.IntegerField(default=5, verbose_name='评分', help_text='1-5星')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='添加时间')

    class Meta:
        db_table = 'games'
        verbose_name = '游戏'
        verbose_name_plural = verbose_name
        ordering = ['-create_time']

    def __str__(self):
        return self.name


class GameScreenshot(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='screenshots', verbose_name='所属游戏')
    image = models.ImageField(upload_to='games/screenshots/', verbose_name='截图')
    desc = models.CharField(max_length=200, blank=True, verbose_name='描述')

    class Meta:
        db_table = 'game_screenshots'
        verbose_name = '游戏截图'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f'{self.game.name} - 截图'


class Music(models.Model):
    title = models.CharField(max_length=200, verbose_name='歌曲名称')
    artist = models.CharField(max_length=200, verbose_name='艺术家')
    album = models.CharField(max_length=200, blank=True, verbose_name='专辑')
    cover = models.ImageField(upload_to='music/covers/', verbose_name='封面图')
    audio_url = models.URLField(verbose_name='音频链接', help_text='网易云音乐外链或其他音频URL')
    duration = models.CharField(max_length=20, verbose_name='时长', help_text='如: 03:45')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='添加时间')

    class Meta:
        db_table = 'music'
        verbose_name = '音乐'
        verbose_name_plural = verbose_name
        ordering = ['-create_time']

    def __str__(self):
        return f'{self.title} - {self.artist}'


class Anime(models.Model):
    name = models.CharField(max_length=200, verbose_name='动漫名称')
    cover = models.ImageField(upload_to='anime/covers/', verbose_name='封面图')
    desc = models.TextField(verbose_name='简介')
    year = models.IntegerField(verbose_name='年份')
    rating = models.IntegerField(default=5, verbose_name='评分', help_text='1-5星')
    status = models.CharField(max_length=50, blank=True, verbose_name='状态', help_text='如: 已完结、连载中')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='添加时间')

    class Meta:
        db_table = 'anime'
        verbose_name = '动漫'
        verbose_name_plural = verbose_name
        ordering = ['-create_time']

    def __str__(self):
        return self.name


class AnimeScreenshot(models.Model):
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE, related_name='screenshots', verbose_name='所属动漫')
    image = models.ImageField(upload_to='anime/screenshots/', verbose_name='截图')
    desc = models.CharField(max_length=200, blank=True, verbose_name='描述')

    class Meta:
        db_table = 'anime_screenshots'
        verbose_name = '动漫截图'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f'{self.anime.name} - 截图'
