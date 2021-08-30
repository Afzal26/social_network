from rest_framework import serializers
from api.accounts.serializers.user import UserSerializer
from api.credits.models.wallet import Wallet


class WalletSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Wallet
        fields = '__all__'
