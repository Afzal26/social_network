from django.db import models
from api.general.created_modified import CreatedModified

from api.accounts.models.user import User


class Moderator(CreatedModified):
    sponsor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sponsored_moderators')
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.email
