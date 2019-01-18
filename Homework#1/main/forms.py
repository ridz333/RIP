from django import forms
from .models import Blog, ImagesForBlog

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title','description')

class ImagesForBlogForm(forms.ModelForm):
    class Meta:
        model = ImagesForBlog
        fields = ('image','blog')