from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import UserInfo, Carousel, Work, Hobby, Game, Music, Anime
from .serializers import (UserInfoSerializer, CarouselSerializer, WorkSerializer, 
                         HobbySerializer, GameSerializer, MusicSerializer, AnimeSerializer)

class UserInfoViewSet(viewsets.ModelViewSet):
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer

    @action(detail=False, methods=['get'])
    def current(self, request):
        """获取当前用户信息（默认第一条）"""
        user_info = self.queryset.first()
        if user_info:
            serializer = self.get_serializer(user_info)
            return Response(serializer.data)
        return Response({'error': '未找到用户信息'}, status=404)


class CarouselViewSet(viewsets.ModelViewSet):
    queryset = Carousel.objects.filter(is_show=True)
    serializer_class = CarouselSerializer


class WorkViewSet(viewsets.ModelViewSet):
    queryset = Work.objects.all()
    serializer_class = WorkSerializer


class HobbyViewSet(viewsets.ModelViewSet):
    queryset = Hobby.objects.all()
    serializer_class = HobbySerializer


class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer


class MusicViewSet(viewsets.ModelViewSet):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer


class AnimeViewSet(viewsets.ModelViewSet):
    queryset = Anime.objects.all()
    serializer_class = AnimeSerializer
