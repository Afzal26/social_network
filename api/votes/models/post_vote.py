from django.db import models
from api.posts.models.post import Post
from api.votes.models.vote import Vote


class PostVote(Vote):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    class Meta:
        default_related_name = 'post_votes'
        unique_together = ('post', 'user')

    def __str__(self):
        return f'post: {self.post.id} - value: {self.value}'
