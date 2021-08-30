from django.urls import path

from .views.post_vote import PostVoteView, PostVoteDetail

urlpatterns = [

    # Post votes
    path('post_votes', PostVoteView.as_view()),
    path('post_votes/<post_vote_id>', PostVoteDetail.as_view()),

]
