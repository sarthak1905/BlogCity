from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='blog-index'),
    path('home/', views.PostListView.as_view(), name='blog-home'),
    path('user/<str:username>', views.UserPostListView.as_view(template_name='blog/user_post.html'), name='user-posts'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('post/new/', views.PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='blog-about'),
]
