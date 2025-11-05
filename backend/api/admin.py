from django.contrib import admin
from django.utils.html import format_html
from .models import (UserInfo, Carousel, Work, Hobby, Game, GameScreenshot, 
                    Music, Anime, AnimeScreenshot)

@admin.register(UserInfo)
class UserInfoAdmin(admin.ModelAdmin):
    list_display = ['name', 'intro_short', 'avatar_preview', 'update_time']

    def intro_short(self, obj):
        return obj.intro[:50] + '...' if len(obj.intro) > 50 else obj.intro
    intro_short.short_description = '简介'

    def avatar_preview(self, obj):
        if obj.avatar:
            return format_html('<img src="{}" width="50" height="50" style="border-radius: 50%;" />', obj.avatar.url)
        return '-'
    avatar_preview.short_description = '头像预览'


@admin.register(Carousel)
class CarouselAdmin(admin.ModelAdmin):
    list_display = ['id', 'image_preview', 'sort', 'is_show']
    list_editable = ['sort', 'is_show']
    list_filter = ['is_show']

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" />', obj.image.url)
        return '-'
    image_preview.short_description = '图片预览'


@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    list_display = ['title', 'cover_preview', 'desc_short', 'link', 'create_time']
    list_filter = ['create_time']
    search_fields = ['title', 'desc']

    def desc_short(self, obj):
        return obj.desc[:50] + '...' if len(obj.desc) > 50 else obj.desc
    desc_short.short_description = '描述'

    def cover_preview(self, obj):
        if obj.cover_image:
            return format_html('<img src="{}" width="100" />', obj.cover_image.url)
        return '-'
    cover_preview.short_description = '封面预览'


@admin.register(Hobby)
class HobbyAdmin(admin.ModelAdmin):
    list_display = ['name', 'hobby_type', 'icon', 'desc_short']
    list_filter = ['hobby_type']
    search_fields = ['name', 'desc']

    def desc_short(self, obj):
        return obj.desc[:50] + '...' if len(obj.desc) > 50 else obj.desc
    desc_short.short_description = '描述'


# 游戏截图内联
class GameScreenshotInline(admin.TabularInline):
    model = GameScreenshot
    extra = 1
    fields = ['image', 'desc']


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ['name', 'cover_preview', 'rating', 'play_time', 'create_time']
    list_filter = ['rating', 'create_time']
    search_fields = ['name', 'desc']
    inlines = [GameScreenshotInline]

    def cover_preview(self, obj):
        if obj.cover:
            return format_html('<img src="{}" width="100" />', obj.cover.url)
        return '-'
    cover_preview.short_description = '封面预览'


@admin.register(Music)
class MusicAdmin(admin.ModelAdmin):
    list_display = ['title', 'artist', 'album', 'cover_preview', 'duration', 'create_time']
    list_filter = ['create_time']
    search_fields = ['title', 'artist', 'album']

    def cover_preview(self, obj):
        if obj.cover:
            return format_html('<img src="{}" width="60" height="60" style="border-radius: 5px;" />', obj.cover.url)
        return '-'
    cover_preview.short_description = '封面预览'


# 动漫截图内联
class AnimeScreenshotInline(admin.TabularInline):
    model = AnimeScreenshot
    extra = 1
    fields = ['image', 'desc']


@admin.register(Anime)
class AnimeAdmin(admin.ModelAdmin):
    list_display = ['name', 'cover_preview', 'year', 'rating', 'status', 'create_time']
    list_filter = ['year', 'rating', 'create_time']
    search_fields = ['name', 'desc']
    inlines = [AnimeScreenshotInline]

    def cover_preview(self, obj):
        if obj.cover:
            return format_html('<img src="{}" width="80" />', obj.cover.url)
        return '-'
    cover_preview.short_description = '封面预览'
