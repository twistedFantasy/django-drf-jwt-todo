from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import OrderingFilter

from todo.tasks.models import Task
from todo.tasks.serializers import TaskSerializer
from todo.users.filters import UserFilterBackend


class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [
        OrderingFilter,
        UserFilterBackend,
        DjangoFilterBackend,
    ]
    filter_fields = ['user', 'type', 'is_completed']
