from django.contrib.auth.models import User

from rest_framework.serializers import ModelSerializer

from user_profile.models import UserProfile


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')


class UserProfileCreateSerializer(ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = UserProfile
        fields = ('user',)

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user_serializer = UserSerializer.create(UserSerializer(), validated_data=user_data)
        user_profile = UserProfile.objects.create(user=user_serializer)
        return user_profile


class UserProfileSerializer(ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = UserProfile
        fields = ('user',)
