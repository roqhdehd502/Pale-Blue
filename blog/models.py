from django.db import models
from django.urls import reverse # URL 패턴을 만들어주는 장고 내장 함수
from taggit.managers import TaggableManager # 태그 매니저
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.
class Post(models.Model):
    title = models.CharField(verbose_name='TITLE', max_length=50) # TITLE이란 별칭의 char타입 50자 제한 필드 변수
    slug = models.SlugField('SLUG', unique=True, allow_unicode=True, help_text='해당 별칭을 지정하세요.') # SLUG란 별칭의 유니크 키 옵션을 가진 문구
    description = models.CharField('DESCRIPTION', max_length=100, blank=True, help_text='내용을 입력하세요.') # 글내용 한 줄 설명
    content = models.TextField('CONTENT') # 글내용
    create_dt = models.DateTimeField('CREATE DATE', auto_now_add=True) # 작성일자
    modify_dt = models.DateTimeField('MODIFY DATE', auto_now=True) # 수정일자
    tags = TaggableManager(blank=True) # 태그
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='OWNER', blank=True, null=True) # 작성자
    category = models.CharField('CATEGORY', max_length=20, null=True) # 카테고리

    class Meta: # 필드 속성 외 필요한 파라미터를 설정하는 내부 클래스
        verbose_name = 'post' # 테이블의 단수 별칭 설정
        verbose_name_plural = 'posts' # 테이블의 복수 별칭 설정
        db_table = 'blog_posts' # 데이터베이스에 저장되는 테이블의 이름
        ordering = ('-modify_dt',) # 모델 객체의 리스트 출력 시 modify_dt 컬럼을 기준으로 내림차순 정렬

    def __str__(self):
        return '[{}] {}'.format(self.title, self.owner)
        #return self.title

    def get_absolute_url(self): # 해당 메소드가 정의된 객체를 지칭하는 URL을 반환
        return reverse('blog:post_detail', args=(self.slug,))

    def get_previous(self): # 메소드 내에서 장고의 내장 함수인 get_privious_by_modify_dt()를 호출
        return self.get_previous_by_modify_dt()

    def get_next(self): # -modify_dt 컬럼을 기준으로 다음 포스트를 반환
        return self.get_next_by_modify_dt()

    def save(self, *args, **kwargs): # 모델 객체의 내용을 데이터베이스에 저장
        self.slug = slugify(self.title, allow_unicode=True)
        super().save(*args, **kwargs)