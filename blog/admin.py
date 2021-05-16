from django.contrib import admin
from blog.models import Post

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin): # Post 클래스가 Admin 사이트에서 어떤 모습으로 보여줄지를 정의하는 클래스
    list_display = ('id', 'title', 'modify_dt') # Post 객체를 보여줄 때, id와 title, modify_dt를 화면에 출력하라고 지정
    list_filter = ('modify_dt',) # modify_dt 컬럼을 사용하는 필터 사이드바를 보여주도록 지정
    search_fields = ('title', 'content') # 검색박스를 표시하고, 입력된 단어는 title과 content 컬러에서 검색하도록 지정
    prepopulated_fields = {'slug': ('title',)} # slug 필드는 title 필드를 사용해 Key : Value 값으로 미리 채워지도록 지정