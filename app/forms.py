"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from django.db import models
from .models import Comment
from .models import Blog

class BootstrapAuthenticationForm(AuthenticationForm):
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'Логин',}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder': 'Пароль',}))

class FeedbackForm(forms.Form):
    name = forms.CharField(label='Имя', min_length=2, max_length=100)
    email = forms.EmailField(label='ваш e-mail', min_length=7)
    visits = forms.ChoiceField(label='Вы посещали наш музей',
                               choices=(('1','Ни разу'),
                                        ('2','Один раз'),
                                        ('3','Два и более раз')
                                        ),initial=1)
    agree = forms.BooleanField(label='Согласие на обработку персональных данных', required=True)
    message = forms.CharField(label='Ваш отзыв', widget=forms.Textarea(attrs={'rows':12,'cols':20}))

class CommentForm (forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
        labels = {'text': "Комментарий"}

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = {'title', 'description', 'content', 'image',}
        labels = {'title':"Заголовок", 'discription':"Краткое содержание", 'content':"Полное содержание", 'image':"Картинка"}