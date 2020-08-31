from django import forms
from Social import models

class PostForm(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ['content', 'image']

class PostComment(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = ['content']  
