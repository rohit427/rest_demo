from rest_framework import serializers
from .models import User, UserProfile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name',)


class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = UserProfile
        fields = ('user', 'programme', 'discipline',)

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create(**user_data)
        user_profile_Object = UserProfile.objects.create(
            user=user, **validated_data)
        return user_profile_Object

    def update(self, instance, validated_data):
        user_data = validated_data.pop('user')
        user = instance.user

        instance.programme = validated_data.get(
            'programme', instance.programme)
        instance.discipline = validated_data.get(
            'discipline', instance.discipline)

        instance.save()

        user.username = user_data.get('username', user.username)
        user.email = user_data.get('email', user.email)
        user.first_name = user_data.get('first_name', user.first_name)
        user.last_name = user_data.get('last_name', user.last_name)

        user.save()

        return instance
