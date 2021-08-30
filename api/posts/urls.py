from django.urls import path

from .views.post import PostView, PostDetail

urlpatterns = [

    # Posts
    path('posts', PostView.as_view()),
    path('posts/<post_id>', PostDetail.as_view()),

]
