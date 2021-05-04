from news.models import Author, Category, Post, PostCategory, Comment
from django.contrib.auth.models import User
from django.db import models
user1 = User.objects.get(id=1)
user2 = User.objects.get(id=2)
author1 = Author.objects.get(id=1)
author2 = Author.objects.get(id=2)
category1 = Category.objects.get(id=1)
category2 = Category.objects.get(id=2)
category3 = Category.objects.get(id=3)
category4 = Category.objects.get(id=4)
article1 = Post.objects.get(id=1)
article2 = Post.objects.get(id=2)
news1 = Post.objects.get(id=3)
comment1 = Comment.objects.get(id=1)
comment2 = Comment.objects.get(id=2)
comment3 = Comment.objects.get(id=3)
comment4 = Comment.objects.get(id=4)
author1.update_rating()
