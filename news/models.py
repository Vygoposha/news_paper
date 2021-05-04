from django.db import models
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView
# import datetime

# Create your models here.
class Author(models.Model):
    author = models.OneToOneField(User, on_delete= models.CASCADE)
    author_rating = models.IntegerField(default=0)

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


class Post(models.Model):
    news = 'Новость'
    article = 'Статья'
    Posts = [
        (news, 'Новость'),
        (article, 'Статья')
    ]
    Post_type = models.CharField(max_length=20, choices= Posts, default=news)
    Post_time = models.DateTimeField(auto_now_add=True)
    Post_title = models.CharField(max_length=255)
    Post_text = models.TextField()
    Post_rating = models.IntegerField(default=0)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    Post_category = models.ManyToManyField(Category, through='PostCategory')

    def __str__(self):
        return f'{self.Post_title.title()}: {self.Post_text[:20]}'


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
