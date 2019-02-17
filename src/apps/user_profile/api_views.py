from rest_framework import generics, status
from rest_framework.decorators import action
from rest_framework.response import Response

from user_profile.models import UserProfile
from user_profile.serializers import (
    UserProfileCreateSerializer,
    UserProfileSerializer,
)


class UserProfileCreateAPIView(generics.CreateAPIView):
    serializer_class = UserProfileCreateSerializer

    @action(methods=['post'], detail=False)
    def post(self, request):
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class UserProfileListAPIView(generics.ListAPIView):
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()
