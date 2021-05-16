from django.contrib import admin
from bookmark.models import Bookmark

# Register your models here.
# Bookmark 클래스가 Admin 사이트에서 어떤 모습으로 보여줄지 정의하는 클래스
@admin.register(Bookmark) # 데코레이터를 통해 어드민 사이트에 등록
class BookmarkAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'url')

# register() 함수로도 어드민 사이트에 등록할 수 있다
# admin.site.register(Bookmark, BookmarkAdmin)