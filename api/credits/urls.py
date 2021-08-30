from django.urls import path
from .views.invitation import InvitationView
from .views.transfer import TransferView
from .views.wallet import WalletDetail

urlpatterns = [

    # Invitations
    path('invitations', InvitationView.as_view()),

    # Transfers
    path('transfers', TransferView.as_view()),

    # Wallets
    path('wallets/<user_id>', WalletDetail.as_view()),

]
