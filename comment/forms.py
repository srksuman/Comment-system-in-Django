from django.db import models
from django.forms import fields, widgets
from .models import Post,Comment
from django import forms
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','description']
        widgets ={
            'title':forms.TextInput(attrs={'class':'form-control'}),
            
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name','comments']
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'comments':forms.TextInput(attrs={'class':'form-control'}),

        }
