from django.forms import ModelForm, BooleanField
from .models import Post

class PostForm(ModelForm):
    check_box = BooleanField(label='Статья цензурна')
    class Meta:
        model = Post
        fields = [
            'Post_title', 'Post_type','author','Post_category','Post_text'
        ]