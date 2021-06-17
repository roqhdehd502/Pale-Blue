from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.template.context_processors import request
from django.views.generic import ListView, DetailView, TemplateView, FormView
from django.views.generic.dates import ArchiveIndexView, YearArchiveView, MonthArchiveView
from django.views.generic.dates import DayArchiveView, TodayArchiveView

from django.conf import settings
from blog.models import Post

from blog.forms import PostSearchForm
from django.db.models import Q
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.urls import reverse_lazy
from mysite.views import OwnerOnlyMixin
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

# Create your views here.

# List View
class PostLV(ListView):
    model = Post
    template_name = 'blog/post_all.html'
    context_object_name = 'posts'
    paginate_by = 10

# DetailView
class PostDV(DetailView):
    model = Post

    def get_context_data(self, **kwargs): # Disqus앱 가져오기
        context = super().get_context_data(**kwargs)
        context['disqus_short'] = f"{settings.DISQUS_SHORTNAME}" # f-스트링: 문자열에서 특정 부분만 바꾸고 나머지 부분은 일정하다고 할때, 문자열 포매팅을 이용해서 이쁘게 출력
        context['disqus_id'] = f"post-{self.object.id}-{self.object.slug}"
        # context['disqus_url'] = f"{settings.DISQUS_MY_DOMAIN}{self.object.get_absolute_url()}"
        context['disqus_url'] = f"{settings.DISQUS_MY_DOMAIN}{self.object.id}"
        context['disqus_title'] = f"{self.object.slug}"

        return context

# ArchiveView
class PostAV(ArchiveIndexView): # 테이블로부터 객체 리스트를 가져와 날짜 필드를 기준으로 최신 객체를 먼저 출력
    model = Post
    date_field = 'modify_dt'

class PostYAV(YearArchiveView):
    model = Post
    date_field = 'modify_dt'
    make_object_list = True

class PostMAV(MonthArchiveView):
    model = Post
    date_field = 'modify_dt'

class PostDAV(DayArchiveView):
    model = Post
    date_field = 'modify_dt'

class PostTAV(TodayArchiveView):
    model = Post
    date_field = 'modify_dt'

class TagCloudTV(TemplateView):
    template_name = 'taggit/taggit_cloud.html'

class TaggedObjectLV(ListView):
    template_name = 'taggit/taggit_post_list.html'
    model = Post

    def get_queryset(self):
        return Post.objects.filter(tags__name=self.kwargs.get('tag'))

    def get_context_data(self, **kwargs): # **kwargs: 키워드 : 특정값의 딕셔너리 형태로 함수 내부에 값을 전달
        context = super().get_context_data(**kwargs)
        context['tagname'] = self.kwargs['tag']
        return context

# FormView
class SearchFormView(FormView):
    form_class = PostSearchForm
    template_name = 'blog/post_search.html'

    def form_valid(self, form):
        searchWord = form.cleaned_data['search_word']
        post_list = Post.objects.filter(Q(title__icontains=searchWord) # Q필터는 filter() 매소드의 매칭 조건을 다양화 한다
                                       | Q(description__icontains=searchWord)
                                       | Q(content__icontains=searchWord)).distinct()

        context = {}
        context['form'] = form
        context['search_term'] = searchWord
        context['object_list'] = post_list

        return render(self.request, self.template_name, context)

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'slug', 'description', 'content', 'tags', 'category']
    initial = {'slug': 'auto-filling-do-not-input'}
    success_url = reverse_lazy('blog:index')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class PostChangeLV(LoginRequiredMixin, ListView):
    template_name = 'blog/post_change_list.html'

    def get_queryset(self):
        return Post.objects.filter(owner=self.request.user)

class PostUpdateView(OwnerOnlyMixin, UpdateView):
    model = Post
    fields = ['title', 'slug', 'description', 'content', 'tags', 'category']
    success_url = reverse_lazy('blog:index')

class PostDeleteView(OwnerOnlyMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('blog:index')

@login_required(login_url='mysite:login')
def like_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user == post.owner:
        messages.error(request, '본인이 작성한 글은 추천할수 없습니다')
    else:
        post.like.add(request.user)
    return redirect('blog:post_detail', pk=post.id)