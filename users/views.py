from django.shortcuts import render
from django.contrib.auth import get_user_model

from rest_framework import generics
#from rest_framework.views import APIView
#from rest_framework.response import Response
from rest_framework import permissions, generics, viewsets

from .models import CustomUser
from .serializers import CustomUserSerializer

User = get_user_model()

class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAdminUser]

#class CustomUserAPIView(generics.ListCreateAPIView):
#    queryset = User.objects.all()
#    serializer_class = CustomUserSerializer
#    permission_classes = [permissions.IsAdminUser]

#class CustomUserAPIView(APIView):
#    def get(self, request):
#        lst = User.objects.all().values()
#        return Response({"users": list(lst)})
