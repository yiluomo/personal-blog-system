from rest_framework import serializers
from .models import UserInfo, Carousel, Work, Hobby, Game, GameScreenshot, Music, Anime, AnimeScreenshot
import json

class UserInfoSerializer(serializers.ModelSerializer):
    resume_list = serializers.SerializerMethodField()
    contact_list = serializers.SerializerMethodField()

    class Meta:
        model = UserInfo
        fields = ['id', 'avatar', 'name', 'intro', 'resume', 'resume_list', 'contact', 'contact_list', 'update_time']

    def get_resume_list(self, obj):
        return obj.get_resume_list()

    def get_contact_list(self, obj):
        return obj.get_contact_list()


class CarouselSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carousel
        fields = ['id', 'image', 'sort', 'is_show']


class WorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Work
        fields = ['id', 'title', 'cover_image', 'desc', 'link', 'create_time']


class HobbySerializer(serializers.ModelSerializer):
    class Meta:
        model = Hobby
        fields = ['id', 'name', 'hobby_type', 'icon', 'desc']


class GameScreenshotSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameScreenshot
        fields = ['id', 'image', 'desc']


class GameSerializer(serializers.ModelSerializer):
    screenshots = GameScreenshotSerializer(many=True, read_only=True)
    
    class Meta:
        model = Game
        fields = ['id', 'name', 'cover', 'desc', 'play_time', 'rating', 'screenshots', 'create_time']


class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = ['id', 'title', 'artist', 'album', 'cover', 'audio_url', 'duration', 'create_time']


class AnimeScreenshotSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnimeScreenshot
        fields = ['id', 'image', 'desc']


class AnimeSerializer(serializers.ModelSerializer):
    screenshots = AnimeScreenshotSerializer(many=True, read_only=True)
    
    class Meta:
        model = Anime
        fields = ['id', 'name', 'cover', 'desc', 'year', 'rating', 'status', 'screenshots', 'create_time']
