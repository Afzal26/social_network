from django.db import models
from api.accounts.models.user import User
from api.general.created_modified import CreatedModified


class PrivateMessage(CreatedModified):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_private_messages')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_private_messages')
    subject = models.CharField(max_length=255)
    body = models.TextField()

    class Meta:
        default_related_name = 'private_messages'

    def __str__(self):
        return self.subject
