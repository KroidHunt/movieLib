from rest_framework import views, status, permissions
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.hashers import make_password
from utils import get_serializer_error, get_user_from_token
from .models import UserProfile
from .serializers import CreateUserProfileSerializer, UserProfileSerializer


def create_user_profile(data):
    if 'is_active' in data:
        del data['is_active']
    if 'password' not in data:
        return Response(status=status.HTTP_400_BAD_REQUEST, data={'error': 'password required'})
    data['password'] = make_password(data['password'])
    serializer = CreateUserProfileSerializer(data={'user': data})
    if not serializer.is_valid(raise_exception=False):
        error = get_serializer_error(serializer)
        return Response(error, status=status.HTTP_400_BAD_REQUEST)
    profile = serializer.save()
    refresh = RefreshToken.for_user(profile.user)
    tokens = {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }
    return Response(tokens, status=status.HTTP_201_CREATED)


class UserProfileView(views.APIView):

    def get(self, request):
        user = get_user_from_token(request)
        if user is not None:
            profile = UserProfile.objects.get(user_id=user.id)
            serializer = UserProfileSerializer(profile)
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST, data={'error': 'invalid token'})


class CreateUserProfile(views.APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        data = request.data
        if type(request.data) is not dict:
            data = request.data.dict()
        data['is_superuser'] = False
        data['is_staff'] = False
        return create_user_profile(data)


class CreateSuperUserProfile(views.APIView):

    def post(self, request):
        user = get_user_from_token(request)
        if user is None or user.is_superuser == False:
            return Response(status=status.HTTP_400_BAD_REQUEST, data='User should be an admin to create a new admin profile')
        data = request.data
        if type(request.data) is not dict:
            data = request.data.dict()
        return create_user_profile(data)
