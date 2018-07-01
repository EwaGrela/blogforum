from django.urls import path
from . import views

urlpatterns = [
    path('', views.BlogList.as_view(), name ="blog_list"),
    path('<int:pk>', views.BlogDetail.as_view(), name='blog_detail'),
    path('posts/', views.PostList.as_view(), name="post_list"),
    path('posts/<int:pk>', views.PostDetail.as_view(), name = "post_detail")
]
