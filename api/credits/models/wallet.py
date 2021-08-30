from django.db import models

from api.accounts.models.user import User


class Wallet(models.Model):
    balance = models.IntegerField(default=0)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.email
