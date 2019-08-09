from rest_framework.serializers import ModelSerializer

from todo.tasks.models import Task


class TaskSerializer(ModelSerializer):

    class Meta:
        model = Task
        exclude = []
        read_only_fields = ['created', 'modified']
