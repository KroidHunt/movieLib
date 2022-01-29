from rest_framework import serializers
from django.contrib.auth.models import User
from user_profile.models import UserProfile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class CreateUserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = UserProfile
        fields = '__all__'

    def create(self, validated_data):
        user_data = validated_data.get('user')
        user = UserSerializer.create(
            UserSerializer(), validated_data=user_data)
        profile = UserProfile.objects.create(user=user, dp=None)
        return profile


class UserProfileSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    class Meta:
        model = UserProfile
        fields = ['user']
        dept = 1

    def get_user(self, obj):
        user_serialzier = UserSerializer(obj.user)
        data = user_serialzier.data
        del data['password']
        if obj.dp:
            data['dp'] = obj.dp
        else:
            data['dp'] = None
        return data
