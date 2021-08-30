import uuid
from django.db import models

from api.accounts.models.user import User
from api.general.created_modified import CreatedModified


class Invitation(CreatedModified):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_invitations')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, default=None, null=True,
                                 related_name='received_invitations')
    code = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    class Meta:
        default_related_name = 'invitations'

    def __str__(self):
        return f'{self.code}'
