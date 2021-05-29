from django.views.generic import ListView, \
    DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.shortcuts import render
from .models import Post
from .filters import PostFilter
from .forms import PostForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.contrib.auth.models import Group, User
from django.contrib.auth.decorators import login_required

class NewsList(ListView):
    model = Post
    template_name = 'news.html'
    context_object_name = 'news'
    queryset = Post.objects.order_by('-id')
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())
        return context


class NewsSearch(ListView):
    model = Post
    template_name = 'search.html'
    context_object_name = 'news'
    ordering = ['-Post_time']
    # paginate_by = 1  # поставим постраничный вывод в один элемент

    def get_filter(self):
        return PostFilter(self.request.GET, queryset=super().get_queryset())

    def get_queryset(self):
        return self.get_filter().qs

    def get_context_data(self,**kwargs):  # забираем отфильтрованные объекты переопределяя метод get_context_data у наследуемого класса (привет полиморфизм, мы скучали!!!)
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET,
                        queryset=self.get_queryset())  # вписываем наш фильтр в контекст
        return context


class NewsCreate(CreateView):
    template_name = 'create_news.html'
    form_class = PostForm

class NewEdit(LoginRequiredMixin,TemplateView):
    template_name = 'create_news.html'
    form_class = PostForm

    # метод get_object мы используем вместо queryset, чтобы получить информацию об объекте который мы собираемся редактировать
    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)

class NewDelete(DeleteView):
    template_name = 'delete_news.html'
    queryset = Post.objects.all()
    success_url = '/news/'

class ProtectedView(LoginRequiredMixin, TemplateView):
    template_name = 'detail_news.html'

class NewDetailView(DetailView):
    template_name = 'detail_news.html'
    queryset = Post.objects.all()

@login_required
def upgradeMe(request):
    user = request.user
    author_group = Group.objects.get(name='authors')
    if not request.user.groups.filter(name='authors').exists():
        author_group.user_set.add(user)
    return redirect('/news')