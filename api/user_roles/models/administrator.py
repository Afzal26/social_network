from django.db import models

from api.accounts.models.user import User
from api.general.created_modified import CreatedModified


class Administrator(CreatedModified):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.email
