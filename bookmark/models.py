from django.db import models

# Create your models here.
# Bookmark 테이블을 정의하는 클래스
class Bookmark(models.Model):
    title = models.CharField('TITLE', max_length=100, blank=True)
    url = models.URLField('URL', unique=True)

    '''def __str__(self):
        return self.title'''
    def __str__(self):
        return "%s %s" %(self.title, self.url)