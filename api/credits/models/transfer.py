from django.db import models

from api.accounts.models.user import User
from api.general.created_modified import CreatedModified


class Transfer(CreatedModified):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_transfers')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_transfers')
    amount = models.IntegerField()

    class Meta:
        default_related_name = 'transfers'

    def __str__(self):
        return f'{self.sender.email} > {self.receiver.email} - {self.amount}'
