from rest_framework_simplejwt.tokens import RefreshToken
from mainapp.models import CustomUser


class TokenService:

    def create_token(self, user: CustomUser) -> (str, str):
        """
        @user take the user instance.
        @response -> return refresh token and access token.
        """
        refresh = RefreshToken.for_user(user)
        return str(refresh), str(refresh.access_token)
