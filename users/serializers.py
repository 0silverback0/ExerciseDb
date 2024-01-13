from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer

class UserCreateSerializer(BaseUserRegistrationSerializer):
    class Meta(BaseUserRegistrationSerializer.Meta):
        model = 'users.User'  # Update with your user model
        fields = ('id', 'email', 'username', 'password', 'password_confirm')
