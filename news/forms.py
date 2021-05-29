from django.forms import ModelForm, BooleanField
from .models import Post
from allauth.account.forms import SignupForm
from django.contrib.auth.models import Group

class PostForm(ModelForm):
    check_box = BooleanField(label='Статья цензурна')
    class Meta:
        model = Post
        fields = [
            'Post_title', 'Post_type','author','Post_category','Post_text'
        ]

class BasicSignupForm(SignupForm):
    def save(self, requset):
        user = super(BasicSignupForm, self).save(requset)
        basic_group = Group.objects.get(name = 'common')
        basic_group.user_set.add(user)
        return user