"""ublog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include


v1_urlpatterns = [
    path('user/', include('user.api.v1.urls'), name='user'),
    path('category/', include('category.api.v1.urls'), name='category'),
    path('comment/', include('comment.api.v1.urls'), name='comment'),
    path('file/', include('file.api.v1.urls'), name='file'),
    path('tag/', include('tag.api.v1.urls'), name='tag'),
    path('blog/', include('blog.api.v1.urls'), name='blog'),
]


urlpatterns = [
    path('backend/admin/', admin.site.urls),
    path('backend/api/v1/', include(v1_urlpatterns)),
]
