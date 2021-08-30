from django.db import models
from api.utils import constants

from api.accounts.models.user import User


class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    value = models.IntegerField(choices=constants.VOTE_VALUE_CHOICES)

    class Meta:
        abstract = True
