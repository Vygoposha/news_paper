from django.urls import path, include
from django.contrib import admin
from .views import NewsList, NewsSearch, IndexView, \
    NewsCreate, NewEdit, NewDelete, NewDetailView, upgradeMe, Subscribe  # импортируем наше представление
from allauth.account.views import LogoutView
from django.views.decorators.cache import cache_page

urlpatterns = [
    # path('', IndexView.as_view()),
    # path — означает путь. В данном случае путь ко всем товарам у нас останется пустым, позже станет ясно почему
    path('', cache_page(60)(NewsList.as_view()), name = 'news'),
    # т.к. сам по себе это класс, то нам надо представить этот класс в виде view. Для этого вызываем метод as_view
    path('<int:pk>/', NewDetailView.as_view(), name = 'detail_news'),
    path('search/', NewsSearch.as_view(), name = 'search'),
    path('add/', NewsCreate.as_view(), name ='create_news'),
    path('<int:pk>/edit/', NewEdit.as_view(), name ='edit_news'),
    path('<int:pk>/delete/', NewDelete.as_view(), name ='delete_news'),
    path('upgrade/', upgradeMe, name = 'upgrade'),
    path('subscribe/<int:pk>/', Subscribe.as_view(), name = 'subscribe'),






]
    # pk — это первичный ключ товара, который будет выводиться у нас в шаблон