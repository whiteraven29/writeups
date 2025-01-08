from django.urls import path
from .views import PostListCreateView, PostDetailView, CommentListCreateView, PostLikeView, PostUnlikeView

urlpatterns = [
    path('posts/', PostListCreateView.as_view(), name='post-list-create'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('comments/', CommentListCreateView.as_view(), name='comment-list-create'),
    path('<int:post_id>/like/', PostLikeView.as_view(), name='post-like'),
    path('<int:post_id>/unlike/', PostUnlikeView.as_view(), name='post-unlike'),
]
