from django.contrib.auth.models import User
from rest_framework import generics, status, response
from .serializers import RegisterSerializer, LoginSerializer, ProfileSerializer
from .models import Profile


class ProfileView(generics.RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()

    serializer_class = RegisterSerializer


class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self,req):
        serializer = self.get_serializer(data=req.data)
        serializer.is_valid(raise_exception=True)
        token = serializer.validated_data
        return response.Response({"token": token.key}, status=status.HTTP_200_OK)
