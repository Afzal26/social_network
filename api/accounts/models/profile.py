from django.db import models

from api.accounts.models.user import User


class Profile(models.Model):
    image = models.ImageField(blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.email
