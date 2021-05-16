"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from bookmark.views import BookmarkLV, BookmarkDV # 뷰 모듈의 관련 클래스 임포트

app_name = 'bookmark'

urlpatterns = [
    path('', BookmarkLV.as_view(), name='index'), # 해당 url을 처리할 뷰 클래스를 BookmarkLV로 지정
    path('<int:pk>/', BookmarkDV.as_view(), name='detail'), # 해당 url을 처리할 뷰 클래스를 BookmarkDV로 지정
]
