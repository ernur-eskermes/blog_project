from django.contrib import admin
from .models import Post, Comment
from .forms import PostAdminForm


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	list_display = ('title', 'author', 'date')
	form = PostAdminForm


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('body', 'created', 'active')
    list_filter = ('active', 'created')
