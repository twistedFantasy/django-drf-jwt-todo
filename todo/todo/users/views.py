from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST

from todo.users.models import User
from todo.users.permissions import UserCustomIsAllowedMethodOrStaff, IsCurrentUserOrStaff
from todo.users.filters import UserFilter, UserBornAfterFilterBackend
from todo.users.serializers import ChangePasswordSerializer, StaffUserSerializer, UserSerializer, \
    StaffUserWithTasksSerializer, UserWithTasksSerializer
from todo.core.filters import ObjectFieldFilterBackend
from todo.core.helpers import true


class ChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request, *args, **kwargs):
        serializer = ChangePasswordSerializer(data=request.data)

        if serializer.is_valid():
            old_password = serializer.data['old_password']
            new_password = serializer.data['new_password']
            if not self.request.user.check_password(old_password):
                return Response({"old_password": ["Wrong password"]}, status=HTTP_400_BAD_REQUEST)
            if new_password == old_password:
                return Response({"new_password": ["Password should be different"]}, status=HTTP_400_BAD_REQUEST)
            self.request.user.set_password(serializer.data['new_password'])
            self.request.user.save(update_fields=['password'])
            return Response(status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated, UserCustomIsAllowedMethodOrStaff, IsCurrentUserOrStaff]
    filter_backends = [
        ObjectFieldFilterBackend, UserBornAfterFilterBackend, SearchFilter, OrderingFilter, DjangoFilterBackend
    ]
    filterset_class = UserFilter
    search_fields = ['email', 'full_name']
    ordering_fields = ['email', 'full_name']
    ordering = ['email']

    def get_serializer_class(self):
        if 'tasks' not in self.request.query_params or true(self.request.query_params.get('tasks')):
            return StaffUserWithTasksSerializer if self.request.user.is_staff else UserWithTasksSerializer
        return StaffUserSerializer if self.request.user.is_staff else UserSerializer
