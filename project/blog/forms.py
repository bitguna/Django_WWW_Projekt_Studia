from django.db.models import fields
from django.utils import timezone
from django import forms
from .models import  Post, Comment

class PostForm(forms.ModelForm):
    class Meta: 
        model = Post
        fields = ("title","text") 

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("text",)