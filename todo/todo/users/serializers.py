from rest_framework import serializers
from drf_dynamic_fields import DynamicFieldsMixin

from todo.users.models import User
from todo.tasks.serializers import TaskSerializer


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ['email', 'is_staff', 'full_name', 'role', 'profile']


class UserWithTasksSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    tasks = TaskSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'email', 'tasks']
