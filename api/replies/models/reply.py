from django.db import models

from api.accounts.models.user import User
from api.general.created_modified import CreatedModified


class Reply(CreatedModified):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()

    class Meta:
        abstract = True
