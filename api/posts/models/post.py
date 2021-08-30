from django.db import models
from api.accounts.models.user import User
from api.general.created_modified import CreatedModified


class Post(CreatedModified):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    body = models.TextField()
    image = models.ImageField(blank=True)

    class Meta:
        default_related_name = 'posts'

    def __str__(self):
        return self.title
