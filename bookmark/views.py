from django.shortcuts import render

from django.views.generic import ListView, DetailView # 클래스형 제네릭 뷰를 사용하기 위해 ListView, DetailView 클래스 임포트
from bookmark.models import Bookmark # 테이블 조회를 위해 모델 클래스를 임포트

from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from mysite.views import OwnerOnlyMixin

# Create your views here.
class BookmarkLV(ListView): # Bookmark 테이블의 레코드 리스트를 보여주기 위한 뷰
    model = Bookmark

class BookmarkDV(DetailView): # Bookmark 테이블의 특정 레코드에 대한 상세 정보를 보여주기 위한 뷰
    model = Bookmark

class BookmarkCreateView(LoginRequiredMixin, CreateView): # 로그인한 상태에서만 북마크를 작성할 수 있는 뷰
    model = Bookmark
    fields = ['title', 'url']
    success_url = reverse_lazy('bookmark:index')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class BookmarkChangeLV(LoginRequiredMixin, ListView): # 로그인한 상태에서만 북마크의 콘텐츠를 변경할 수 있는 뷰
    template_name = 'bookmark/bookmark_change_list.html'

    def get_queryset(self):
        return Bookmark.objects.filter(owner=self.request.user)

class BookmarkUpdateView(OwnerOnlyMixin, UpdateView): # 작성자만 북마크를 수정할 수 있는 뷰
    model = Bookmark
    fields = ['title', 'url']
    success_url = reverse_lazy('bookmark:index')

class BookmarkDeleteView(OwnerOnlyMixin, DeleteView): # 작성자만 북마크를 삭제할 수 있는 뷰
    model = Bookmark
    success_url = reverse_lazy('bookmark:index')