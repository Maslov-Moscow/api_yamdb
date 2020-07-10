from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.views import TitleViewSet
from api.views import GenreViewSet
from api.views import CategoryViewSet
from api.views import ReviewViewSet
from api.views import CommentViewSet


router = DefaultRouter()
router.register('titles', TitleViewSet, basename='titles')
router.register('genres', GenreViewSet)
router.register('categories', CategoryViewSet)
router.register(r'titles/(?P<title_id>\d+)/reviews', ReviewViewSet)
router.register(r'titles/(\d+)/reviews/(?P<review_id>\d+)/comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
