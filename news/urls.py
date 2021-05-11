from django.urls import path
from .views import NewsList, NewsSearch, \
    NewsCreate, NewEdit, NewDelete, NewDetailView  # импортируем наше представление

urlpatterns = [
    # path — означает путь. В данном случае путь ко всем товарам у нас останется пустым, позже станет ясно почему
    path('', NewsList.as_view()),
    # т.к. сам по себе это класс, то нам надо представить этот класс в виде view. Для этого вызываем метод as_view
    path('<int:pk>/', NewDetailView.as_view(), name = 'detail_news'),
    path('search/', NewsSearch.as_view()),
    path('add/', NewsCreate.as_view(), name ='create_news'),
    path('<int:pk>/edit/', NewEdit.as_view(), name ='edit_news'),
    path('<int:pk>/delete/', NewDelete.as_view(), name ='delete_news')
]
    # pk — это первичный ключ товара, который будет выводиться у нас в шаблон