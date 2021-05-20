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
#from bookmark.views import BookmarkLV, BookmarkDV # 뷰 모듈의 관련 클래스 임포트
from bookmark import views

app_name = 'bookmark'

urlpatterns = [
    #path('', BookmarkLV.as_view(), name='index'),
    #path('<int:pk>/', BookmarkDV.as_view(), name='detail'),
    path('', views.BookmarkLV.as_view(), name='index'), # 해당 url을 처리할 뷰 클래스를 BookmarkLV로 지정
    path('<int:pk>/', views.BookmarkDV.as_view(), name='detail'), # 해당 url을 처리할 뷰 클래스를 BookmarkDV로 지정

    # Example: /bookmark/add/
    path('add/',
         views.BookmarkCreateView.as_view(), name="add",
        ),

    # Example: /bookmark/change/
    path('change/',
         views.BookmarkChangeLV.as_view(), name="change",
        ),

    # Example: /bookmark/99/update/
    path('<int:pk>/update/',
         views.BookmarkUpdateView.as_view(), name="update",
         ),

    # Example: /bookmark/99/delete/
    path('<int:pk>/delete/',
         views.BookmarkDeleteView.as_view(), name="delete",
         ),
]
