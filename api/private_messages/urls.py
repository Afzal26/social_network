from django.urls import path

from .views.private_message import PrivateMessageView, PrivateMessageDetail

urlpatterns = [

    # Private messages
    path('private_messages', PrivateMessageView.as_view()),
    path('private_messages<private_message_id>', PrivateMessageDetail.as_view()),

]
