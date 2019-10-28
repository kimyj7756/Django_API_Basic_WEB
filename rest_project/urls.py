
from django.contrib import admin
from django.urls import path,include
from rest_app import urls
# 오른쪽 상단에 로그인 로그아웃 표시
from rest_framework import urls
# urlpatterns
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('rest_app.urls')),
    
    # 오른쪽 상단에 로그인 로그아웃 표시
    path('api-auth/',include('rest_framework.urls'))
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) 