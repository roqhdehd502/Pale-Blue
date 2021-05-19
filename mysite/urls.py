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
from mysite.views import HomeView, UserCreateView, UserCreateDoneTV
from django.conf.urls.static import static # 정적 파일처리 모듈
from django.conf import settings # setting.py에서 정의한 항목들을 담고 있는 객체를 가져오는 모듈

#from bookmark.views import BookmarkLV, BookmarkDV # 뷰 모듈의 관련 클래스 임포트

urlpatterns = [
    # path(): route, view 2개의 필수 인자와 kwargs, name 2개의 선택 인자를 받는데 여기서, name 인자값은 템플릿 파일에서 사용
    path('admin/', admin.site.urls), # Admin 사이트에 대한 url 정의
    path('', HomeView.as_view(), name='home'), # 홈 페이지
    path('bookmark/', include('bookmark.urls')), # 북마크 페이지
    path('blog/', include('blog.urls')), # 블로그 페이지
    path('photo/', include('photo.urls')), # 사진 페이지
    path('accounts/', include('django.contrib.auth.urls')), # 장고의 URLconf 가져오기
    path('accounts/register/', UserCreateView.as_view(), name='register'), # 가입처리 URL
    path('accounts/register/done/', UserCreateDoneTV.as_view(), name='register_done'), # 계정생성완료 URL
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) # 기존 URL패턴에 static() 함수가 반환하는 URL 패턴을 추가
