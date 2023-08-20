

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

    
class UserLogin(APIView):

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            refresh = RefreshToken.for_user(user)
            response_data = {
                "message": "Logged in Successfully!..",
                'refresh': str(refresh),
                'access': str(refresh.access_token)
            }
            return Response(response_data, status=status.HTTP_200_OK)
        else:
            return Response({"details":"Incorrect credentials"}, status=status.HTTP_400_BAD_REQUEST)
    
    
            