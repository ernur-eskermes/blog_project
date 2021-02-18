from .models import Comment, Post
from django import forms

from ckeditor_uploader.widgets import CKEditorUploadingWidget


class PostForm(forms.ModelForm):
	text = forms.CharField(label='Текст', widget=CKEditorUploadingWidget())
	class Meta:
		model = Post
		fields = ['image', 'title', 'text']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class PostAdminForm(forms.ModelForm):
    text = forms.CharField(label='Текст', widget=CKEditorUploadingWidget())
    class Meta:
        model = Post
        fields = '__all__'        
