from django.http import HttpResponse, JsonResponse
from rest_framework import status, generics
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from social_core.backends import username

from .serializers import CustomUserSerializer, UserSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import NewUser
from django.core import serializers


class CustomUserCreate(APIView):
    permission_classes = [AllowAny]

    def post(self, request, format='json'):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class UserProfile(APIView):
#     permission_classes = [IsAuthenticated]
#     serializer_class = CustomUserSerializer
#
#     def post(self, request, format='json'):
#         item = NewUser.objects.get(username=request.user)
#         print("==========================")
#         print(item)
#         print(item.username)
#         print(item.email)
#         print("==========================")
#         return Response(item)


# class UserProfile(generics.RetrieveAPIView):
#     permission_classes = [IsAuthenticated]
#
#     def get(self, request, *args, **kwargs):
#         data = NewUser.objects.get(username=request.user)
#         responseData = {
#             'username': data.username,
#             'email': data.email,
#
#         }
#         return JsonResponse(responseData)


class UserProfile(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = username

    def get_object(self):
        queryset = NewUser.objects.get(username=self.request.user.username)
        return queryset
