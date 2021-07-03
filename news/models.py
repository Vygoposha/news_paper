from django.db import models
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView
# import datetime


class Author(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name = 'Пользователь')
    author_rating = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.author.get_username()}'

    def update_rating(self):
        post_author = Post.objects.filter(author = self.id, Post_type = self.author)
        total_post_rating = 0
        for post in post_author:
            total_post_rating += post.Post_rating * 3

        total_author_comment_rating = 0
        for comments in Comment.objects.filter(user = self.author):
            total_author_comment_rating += comments.comment_rating

        total_author_post_rating = 0
        for comments in Comment.objects.filter(post = post_author):
            total_author_post_rating += comments.comment_rating

        self.author_rating = total_post_rating + total_author_comment_rating + total_author_post_rating
        self.save()


class Category(models.Model):
    category_name = models.CharField(max_length=64, unique=True)
    subscribers = models.ManyToManyField(User, null=True)

    def __str__(self):
        return f'{self.category_name}'

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Post(models.Model):
    news = 'Новость'
    article = 'Статья'
    Posts = [
        (news, 'Новость'),
        (article, 'Статья')
    ]
    Post_type = models.CharField(max_length=20, choices= Posts, default=news)
    Post_time = models.DateTimeField(auto_now_add=True, verbose_name = 'Дата публикации')
    Post_title = models.CharField(max_length=255, verbose_name = 'Заголовок')
    Post_text = models.TextField()
    Post_rating = models.IntegerField(default=0)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name = 'Автор')
    Post_category = models.ManyToManyField(Category, through='PostCategory')

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"

    def __str__(self):
        return f'{self.Post_title.title()}: {self.Post_text[:20]}'

    def get_absolute_url(self):  # добавим абсолютный путь чтобы после создания нас перебрасывало на страницу с товаром
        return f'/news/post/{self.id}'

    def like(self):
        self.Post_rating += 1
        self.save()

    def dislike(self):
        self.Post_rating -= 1
        self.save()

    def preview(self):
        return str(self.Post_text)[:124],'...'


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete= models.CASCADE)

    def __str__(self):
        return f'{self.category}'


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_text = models.TextField()
    date_time = models.DateTimeField(auto_now_add=True)
    comment_rating = models.IntegerField(default=0)

    def like(self):
        self.comment_rating += 1
        self.save()

    def dislike(self):
        self.comment_rating -= 1
        self.save()

    def __str__(self):
        return self.comment_text
