from django.contrib import admin
from .models import Post, Category

class PostAdmin(admin.ModelAdmin):
    list_display = ('id','Post_title','author','Post_time')

admin.site.register(Post, PostAdmin)
admin.site.register(Category)

