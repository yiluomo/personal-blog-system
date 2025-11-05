from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (UserInfoViewSet, CarouselViewSet, WorkViewSet, HobbyViewSet,
                   GameViewSet, MusicViewSet, AnimeViewSet)

router = DefaultRouter()
router.register(r'userinfo', UserInfoViewSet)
router.register(r'carousel', CarouselViewSet)
router.register(r'works', WorkViewSet)
router.register(r'hobbies', HobbyViewSet)
router.register(r'games', GameViewSet)
router.register(r'music', MusicViewSet)
router.register(r'anime', AnimeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
