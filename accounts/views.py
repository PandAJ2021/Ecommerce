from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import RegisterSerializer
from .models import User
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated


class UserRegisterView(APIView):

    def post(self, request):
        ser_data = RegisterSerializer(data=request.data)
        if ser_data.is_valid():
            ser_data.save()
            return Response(data=ser_data.data, status=status.HTTP_201_CREATED)
        return Response(data=ser_data.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLogoutView(APIView):
    permission_classes = [IsAuthenticated,]

    def post(self, request):
        try:
            token = RefreshToken(token=request.data['refresh'])
            token.blacklist()
            return Response({'detail':'Logged out successful'}, status=status.HTTP_205_RESET_CONTENT)
        except Exception as err:
            return Response({'error':str(err)}, status=status.HTTP_400_BAD_REQUEST)
