from django.views.generic import ListView, DetailView
from .models import Post

class NewsList(ListView):
    model = Post
    template_name = 'news.html'
    context_object_name = 'news'
    queryset = Post.objects.order_by('-id')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['time_now'] = datetime.utcnow()  # добавим переменную текущей даты time_now
        context['object_list'] = context['object_list'][1].Post_title  # добавим ещё одну пустую переменную, чтобы на её примере посмотреть работу другого фильтра
        print(context)
        return context


class NewsDetail(DetailView):
    model = Post
    template_name = 'new.html'
    context_object_name = 'new'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
    #     context['time_now'] = datetime.utcnow()  # добавим переменную текущей даты time_now
        context['Title'] = context['object'].Post_title  # добавим ещё одну пустую переменную, чтобы на её примере посмотреть работу другого фильтра
        context['Text'] = context['object'].Post_text
        return context