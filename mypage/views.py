from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView

from mypage.models import MyProfile

# Create your views here.
class MypageMain(LoginRequiredMixin, ListView): # 마이페이지 홈
    model = MyProfile
    template_name = 'mypage/mypage_main.html'
    context_object_name = 'mypage_main'
    #paginate_by = 10

# FormView
# class SearchFormView(FormView):
#     form_class = PostSearchForm
#     template_name = 'blog/post_search.html'
#
#     def form_valid(self, form):
#         searchWord = form.cleaned_data['search_word']
#         post_list = Post.objects.filter(Q(title__icontains=searchWord) # Q필터는 filter() 매소드의 매칭 조건을 다양화 한다
#                                        | Q(description__icontains=searchWord)
#                                        | Q(content__icontains=searchWord)).distinct()
#
#         context = {}
#         context['form'] = form
#         context['search_term'] = searchWord
#         context['object_list'] = post_list
#
#         return render(self.request, self.template_name, context)

# class PostCreateView(LoginRequiredMixin, CreateView):
#     model = Post
#     fields = ['title', 'slug', 'description', 'content', 'tags', 'category']
#     initial = {'slug': 'auto-filling-do-not-input'}
#     success_url = reverse_lazy('blog:index')
#
#     def form_valid(self, form):
#         form.instance.owner = self.request.user
#         return super().form_valid(form)
#
# class PostChangeLV(LoginRequiredMixin, ListView):
#     template_name = 'blog/post_change_list.html'
#
#     def get_queryset(self):
#         return Post.objects.filter(owner=self.request.user)
#
# class PostUpdateView(OwnerOnlyMixin, UpdateView):
#     model = Post
#     fields = ['title', 'slug', 'description', 'content', 'tags', 'category']
#     success_url = reverse_lazy('blog:index')
#
# class PostDeleteView(OwnerOnlyMixin, DeleteView):
#     model = Post
#     success_url = reverse_lazy('blog:index')