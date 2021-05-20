from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# Bookmark 테이블을 정의하는 클래스
class Bookmark(models.Model):
    title = models.CharField('TITLE', max_length=100, blank=True) # 북마크의 제목
    url = models.URLField('URL', unique=True) # 북마크 경로
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True) # 북마크를 지정한 사용자(기존에 사용자 없이 추가한 것을 고려하여 null값을 허용)

    def __str__(self):
        return "%s %s" %(self.title, self.url)