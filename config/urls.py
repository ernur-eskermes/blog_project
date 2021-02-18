from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

from django.urls import path, include

from users import views as userView
from django.contrib.auth import views as authViews 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('reg/', userView.register, name='registartion-page'),
    path('login/', authViews.LoginView.as_view(template_name='users/login.html'), name='login-page'),
    path('logout/', authViews.LogoutView.as_view(template_name='users/logout.html'), name='logout-page'),
    path('profile/', userView.profile, name='profile-page'),
    path('', include('blog.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    