from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.db.models import Q  
from django.http import HttpResponseRedirect

from .models import Post, Comment
from .forms import CommentForm, PostForm


class HomeListView(ListView):          
    model = Post                           
    template_name = 'blog/home.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.order_by('-date')[:3]

    def get_context_data(self, **kwargs):
        ctx = super(HomeListView, self).get_context_data(**kwargs)
        ctx['title'] = 'Главная страница'
        return ctx


class BlogListView(ListView):           
    model = Post                           
    template_name = 'blog/blog.html'
    context_object_name = 'posts'
    paginate_by = 3
 
    def get_queryset(self):             
        query = self.request.GET.get('q')
        if query:
            object_list = Post.objects.filter(
            Q(title__icontains=query) |
            Q(text__icontains=query)
            )
        else:
            object_list = Post.objects.order_by('-date')
        return object_list

    def get_context_data(self, **kwargs): 
        ctx = super(BlogListView, self).get_context_data(**kwargs)
        ctx['title'] = 'Cтраница блога'
        return ctx          


class BlogCreateView(CreateView):    
    template_name = 'blog/post_new.html'
    form_class = PostForm

    def form_valid(self, form):         
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):  
        ctx = super(BlogCreateView, self).get_context_data(**kwargs)
        ctx['title'] = 'Создать новый пость'
        return ctx   


class BlogUpdateView(UpdateView):        
    model = Post
    template_name = 'blog/post_edit.html'
    form_class = PostForm

    def form_valid(self, form):       
        form.instance.author = self.request.user 
        return super().form_valid(form)

    def get_context_data(self, **kwargs):  
        ctx = super(BlogUpdateView, self).get_context_data(**kwargs)
        ctx['title'] = 'Редактирование поста'
        return ctx     


class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('home-page')

    def get_context_data(self, **kwargs):
        ctx = super(BlogDeleteView, self).get_context_data(**kwargs)
        ctx['title'] = 'Удаление поста'
        return ctx 


class BlogDetailView(DetailView):       
    model = Post                          
    template_name = 'blog/single.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        ctx = super(BlogDetailView, self).get_context_data(**kwargs)
        ctx['title'] = f'Пость - {self.object.title}'
        ctx['comment_form'] = CommentForm()
        ctx['comments'] = Comment.objects.filter(post=self.object)
        try:
            comment = Comment.objects.get(user=self.request.user, post=self.object)
        except Comment.DoesNotExist:
            comment = None
        ctx['comment'] = comment
        return ctx 


@login_required
def comment_create(request, post_pk):
    if request.POST:
        form = CommentForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.user = request.user
            data.post = Post.objects.get(id=post_pk)
            data.save()
            return redirect(request.META.get('HTTP_REFERER'))

