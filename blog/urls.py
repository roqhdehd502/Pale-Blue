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
from django.urls import path, re_path
from blog import views

app_name = 'blog'

urlpatterns = [
    # Example :  /blog/
    path('', views.PostLV.as_view(), name='index'), # URL 요청을 처리할 뷰 클래스를 PostLV로 지정

    # Example : /blog/post/ (same as /blog/)
    path('post/', views.PostLV.as_view(), name='post_list'),

    # Example : /blog/post/django-example/
    path('post/<int:pk>', views.PostDV.as_view(), name='post_detail'), # 고유 글번호를 이용한 처리
    #re_path(r'^post/(?P<slug>[-\w]+)/$', views.PostDV.as_view(), name='post_detail'), 한글을 고려한 슬러그처리

    # Example : /blog/post/99/like
    path('post/<int:pk>/like/', views.like_post, name='like_post', ),  # 추천 처리

    # Example : /blog/archive/
    path('archive/', views.PostAV.as_view(), name='post_archive'),

    # Example : /blog/archive/2019/
    path('archive/<int:year>/', views.PostYAV.as_view(), name='post_year_archive'),

    # Example : /blog/archive/2019/nov/
    path('archive/<int:year>/<str:month>/', views.PostMAV.as_view(), name='post_month_archive'),

    # Example : /blog/archive/2019/nov/10
    path('archive/<int:year>/<str:month>/<int:day>/', views.PostDAV.as_view(), name='post_day_archive'),

    # Example : /blog/archive/today/
    path('archive/today/', views.PostTAV.as_view(), name='post_today_archive'),

    # Example : /blog/tag/
    path('tag/', views.TagCloudTV.as_view(), name='tag_cloud'),

    # Example : /blog/tag/tagname/
    path('tag/<str:tag>/', views.TaggedObjectLV.as_view(), name='tagged_object_list'),

    # Example : /blog/search/
    path('search/', views.SearchFormView.as_view(), name='search'),

    # Example : /blog/add/
    path('add/', views.PostCreateView.as_view(), name='add',),

    # Example : /blog/change/
    path('change/', views.PostChangeLV.as_view(), name='change',),

    # Example : /blog/99/update/
    path('<int:pk>/update/', views.PostUpdateView.as_view(), name='update',),

    # Example : /blog/99/delete/
    path('<int:pk>/delete/', views.PostDeleteView.as_view(), name='delete',),
]