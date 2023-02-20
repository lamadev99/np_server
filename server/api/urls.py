from django.urls import path, include
from rest_framework import routers
from api.views import *

router = routers.DefaultRouter()

router.register(r'profile', WriterProfileViewSet)
router.register(r'news', NewsViewSet)
router.register(r'comment', CommentViewSet)
router.register(r'category', CategoryViewSet)
router.register(r'subCategory', SubCategoryViewSet)
router.register(r'page', PageGeneratorViewSet)


urlpatterns = [
    path('', include(router.urls)),
]