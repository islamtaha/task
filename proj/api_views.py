from proj.serializers import UserSerializer
from rest_framework import generics
from django.contrib.auth.models import User

class UserAPIList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer