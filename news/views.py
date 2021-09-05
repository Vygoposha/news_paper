from django.views.generic import ListView, \
    DetailView, CreateView, UpdateView, DeleteView, View
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.core.mail import send_mail
from django.template.loader import render_to_string
from .models import Post, Category, Author
from .filters import PostFilter
from .forms import PostForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import Group, User
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMultiAlternatives  # импортируем класс для создание объекта письма с html

from django.http import HttpResponse
from django.views import View
from .tasks import news_create_notify
from datetime import datetime, timedelta





class NewsList(ListView):
    model = Post
    template_name = 'news.html'
    context_object_name = 'news'
    queryset = Post.objects.order_by('-id')
    paginate_by = 10

    def get_query_data(self, **kwargs):
        query = super().get_context_data(**kwargs)
        query['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())
        return query

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_not_authors'] = not self.request.user.groups.filter(name='authors').exists()
        context['is_not_authorized'] = not self.request.user.is_authenticated
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

    def get_index_data(self, **kwargs):
        index = super().get_context_data(**kwargs)
        index['is_not_authorized'] = not self.request.user.groups.filter(name='common').exists()
        return index


class NewsCreate(PermissionRequiredMixin,CreateView):
    template_name = 'create_news.html'
    form_class = PostForm
    permission_required = ('news.add_post',)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_not_authors'] = not self.request.user.groups.filter(name='authors').exists()
        context['is_not_authorized'] = not self.request.user.is_authenticated
        return context



    # def form_valid(self, form):
    #     author = Author.objects.get(author = self.request.user)
    #     form.instance.author = author
    #
    #     form.save()
    #     sub_list = list(form.instance.Post_category.all().values_list('subscribers', flat=True))
    #     news_create_notify.delay(user_id = sub_list, news_id = form.instance.id)
    #     return super().form_valid(form)

class NewEdit(PermissionRequiredMixin,UpdateView):
    template_name = 'create_news.html'
    form_class = PostForm
    permission_required = ('news.change_post',)


    # метод get_object мы используем вместо queryset, чтобы получить информацию об объекте который мы собираемся редактировать
    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_not_authors'] = not self.request.user.groups.filter(name='authors').exists()
        return context

    def get_index_data(self, **kwargs):
        index = super().get_context_data(**kwargs)
        index['is_not_authorized'] = self.request.user.groups.filter(name='common').exists()
        return index


class NewDelete(PermissionRequiredMixin, DeleteView):
    template_name = 'delete_news.html'
    queryset = Post.objects.all()
    permission_required = ('news.delete_post',)
    success_url = '/news/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_not_authors'] = not self.request.user.groups.filter(name='authors').exists()
        return context

    def get_index_data(self, **kwargs):
        index = super().get_context_data(**kwargs)
        index['is_not_authorized'] = not self.request.user.groups.filter(name='common').exists()
        return index


class NewDetailView(LoginRequiredMixin, DetailView):
    template_name = 'detail_news.html'
    queryset = Post.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_not_authors'] = not self.request.user.groups.filter(name='authors').exists()
        context['is_not_authorized'] = not self.request.user.groups.filter(name='common').exists()
        return context




@login_required
def upgradeMe(request):
    user = request.user
    author_group = Group.objects.get(name='authors')
    if not request.user.groups.filter(name='authors').exists():
        author_group.user_set.add(user)
    return redirect('/')


class Subscribe(LoginRequiredMixin, View):
    model = Category

    def post(self, request, *args, **kwargs):
        user = self.request.user

        category = get_object_or_404(Category, id=self.kwargs['pk'])
        if category.subscribers.filter(username=self.request.user).exists():
            category.subscribers.remove(user)
        else:
            category.subscribers.add(user)

        html_content = render_to_string(
            'send_notify.html',
            {
                'category': category,  # словарь со значениями, к которым можно обращаться
                'user': User,
            }
        )

        # в конструкторе уже знакомые нам параметры, да? Называются правда немного по другому, но суть та же.
        msg = EmailMultiAlternatives(
            subject=f'{category.category_name}',
            body='Текст',  # это то же, что и message
            from_email='igor.vigol@yandex.ru',
            to=['dzu960128@gmail.com'],  # это то же, что и recipients_list
        )
        msg.attach_alternative(html_content, "text/html")  # добавляем html

        msg.send()  # отсылаем

        return redirect('/')

class IndexView(View):
    def get(self, request):
        # hello.delay()
        # printer.apply_async([10], countdown = 1)
        return HttpResponse("Hello")

