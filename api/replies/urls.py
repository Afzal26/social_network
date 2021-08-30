from django.urls import path

from .views.post_reply import PostReplyView, PostReplyDetail

urlpatterns = [

    # Post replies
    path('post_replies', PostReplyView.as_view()),
    path('post_replies/<post_reply_id>', PostReplyDetail.as_view()),

]
