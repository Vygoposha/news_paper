from django.views.generic import ListView, \
    DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import render
from .models import Post
from .filters import PostFilter
from .forms import PostForm

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
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     # context['time_now'] = datetime.utcnow()  # добавим переменную текущей даты time_now
    #     context['object_list'] = context['object_list'][1].Post_title  # добавим ещё одну пустую переменную, чтобы на её примере посмотреть работу другого фильтра
    #     # print(context)
    #     return context


# class NewsDetail(DetailView):
#     model = Post
#     template_name = 'new.html'
#     context_object_name = 'new'
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#     #     context['time_now'] = datetime.utcnow()  # добавим переменную текущей даты time_now
#         context['Title'] = context['object'].Post_title  # добавим ещё одну пустую переменную, чтобы на её примере посмотреть работу другого фильтра
#         context['Text'] = context['object'].Post_text
#         return context

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

class NewEdit(UpdateView):
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

class NewDetailView(DetailView):
    template_name = 'detail_news.html'
    queryset = Post.objects.all()
