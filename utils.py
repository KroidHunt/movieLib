from rest_framework_simplejwt.authentication import JWTAuthentication

JWTAuthenticator = JWTAuthentication()


def get_user_from_token(request):
    result = JWTAuthenticator.authenticate(request)
    if result is not None:
        user = result[0]
        return user
    return None


def get_serializer_error(serializer):
    error = tuple(tuple(serializer.errors.values())[0].values())[0][0]
    return error
