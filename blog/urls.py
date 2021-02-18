from django.urls import path
from . import views 

urlpatterns = [
    path('', views.HomeListView.as_view(), name='home-page'),
    path('blog/', views.BlogListView.as_view(), name='blog-page'),
    path('blog/<int:pk>/', views.BlogDetailView.as_view(), name='single-page'),
    path('blog/new/', views.BlogCreateView.as_view(), name='post-new-page'),
    path('blog/<int:pk>/edit/', views.BlogUpdateView.as_view(), name='post-edit-page'),
    path('blog/<int:pk>/delete/', views.BlogDeleteView.as_view(), name='post-delete-page'),

    path('comment-create/<int:post_pk>', views.comment_create, name='comment_create'),
]