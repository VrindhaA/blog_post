from django.urls import path
from api.views import PostList, PostDetail,BlogListView

urlpatterns = [
    path('posts/', PostList.as_view()),
    path('post_detail/<int:pk>/', PostDetail.as_view()),
    path('list_blogs/',BlogListView.as_view(),name='blog_list')
]

