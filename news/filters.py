from django_filters import FilterSet
from .models import Post

class PostFilter(FilterSet):
    class Meta:
        model = Post
        fields = {'author': ['exact'],

                  'Post_rating': ['gt'],
                  'Post_time': ['lt'],
                  'Post_title': ['icontains'],
                  'Post_type':['exact'],
                  'Post_category':['exact']
                  }