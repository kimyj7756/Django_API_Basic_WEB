from rest_framework.routers import DefaultRouter
from django.urls import path,include
from rest_app import views

# 객체 생성
router = DefaultRouter()
router.register('essay',views.PostViewSet)
router.register('album',views.ImageViewSet)
router.register('files',views.FileViewSet)

urlpatterns= [
    path('',include(router.urls))
]
