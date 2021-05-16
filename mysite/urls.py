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
from django.contrib import admin
from django.urls import path, include
from mysite.views import HomeView

#from bookmark.views import BookmarkLV, BookmarkDV # 뷰 모듈의 관련 클래스 임포트

urlpatterns = [
    # path(): route, view 2개의 필수 인자와 kwargs, name 2개의 선택 인자를 받는데 여기서, name 인자값은 템플릿 파일에서 사용
    path('admin/', admin.site.urls), # Admin 사이트에 대한 url 정의
    path('', HomeView.as_view(), name='home'), # 홈 페이지
    path('bookmark/', include('bookmark.urls')), # 북마크 페이지
    path('blog/', include('blog.urls')), # 블로그 페이지

    # class-based views
    #path('bookmark/', BookmarkLV.as_view(), name='index'), # 해당 url을 처리할 뷰 클래스를 BookmarkLV로 지정
    #path('bookmark/<int:pk>/', BookmarkDV.as_view(), name='detail'), # 해당 url을 처리할 뷰 클래스를 BookmarkDV로 지정
]
