from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import OurRegistration, UserUpdateForm, ProfileAvatar
from blog.models import Post


def register(request):   
    if request.method == 'POST':
        form = OurRegistration(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Пользователь {username} был успешно зарегестрирован. Войдите!")
            return redirect('login-page')
    else:        
        form = OurRegistration()
    return render(request, 'users/registration.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        avatar_form = ProfileAvatar(request.POST, request.FILES, instance=request.user)
        update_form = UserUpdateForm(request.POST, instance=request.user.profile)
        if update_form.is_valid() and avatar_form.is_valid():
            update_form.save()
            avatar_form.save()

            messages.success(request, 'Данные пользователя изменены')
            return redirect('profile-page')
    else:
        avatar_form = ProfileAvatar(instance=request.user.profile)
        update_form = UserUpdateForm(instance=request.user)    

    posts = Post.objects.filter(author__username=request.user)

    return render(request, 'users/profile.html', {'avatar_form': avatar_form, 'update_form': update_form, 'posts': posts})
