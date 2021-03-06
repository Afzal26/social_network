from rest_framework import serializers
from api.accounts.serializers.user import UserSerializer
from api.user_roles.models.administrator import Administrator
from api.utils import constants
from api.utils.permissions import is_administrator


class AdministratorSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Administrator
        fields = '__all__'


class AdministratorSerializerCreate(serializers.ModelSerializer):

    class Meta:
        model = Administrator
        fields = '__all__'

    def validate(self, data):
        """
        Administrator permissions needed
        """

        if not is_administrator(self.context['request'].user):
            raise serializers.ValidationError(constants.PERMISSION_ADMINISTRATOR_REQUIRED)
        return data
