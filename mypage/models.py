from django.db import models
from django.urls import reverse # URL 패턴을 만들어주는 장고 내장 함수
from django.contrib.auth.models import User # 유저 인증 모듈
from blog.models import Post # 커퓨니티 게시판
from photo.models import Album # 앨범 게시판

# Create your models here.
class MyProfile(models.Model): # 유저 프로필
    profile = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='PROFILE', blank=True, null=True) 

    def __str__(self):
        return self.profile

class MyCommunity(models.Model): # 커뮤니티
    community = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='COMMUNITY', blank=True, null=True)

    class Meta:
        ordering = ('community',)

    def __str__(self):
        return self.community

    # def get_absolute_url(self):
    #     return reverse('photo:photo_detail', args=(self.id,))

class MyAlbum(models.Model): # 앨범
    album = models.ForeignKey(Album, on_delete=models.CASCADE, verbose_name='ALBUM', blank=True, null=True)

    class Meta:
        ordering = ('album',)

    def __str__(self):
        return self.album

    # def get_absolute_url(self):
    #     return reverse('photo:album_detail', args=(self.id,))