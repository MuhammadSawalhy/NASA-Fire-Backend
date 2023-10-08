# serializers.py

from djoser.serializers import UserCreateSerializer
from users.models import CustomUser

class CustomUserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = CustomUser
        fields = ('id', 'first_name', 'last_name', 'email', 'username', 'password')
