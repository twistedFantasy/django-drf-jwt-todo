from rest_framework.serializers import ModelSerializer, Serializer, CharField, EmailField

from todo.users.models import User
from todo.tasks.serializers import TaskSerializer


FIELDS = ['id', 'email', 'is_staff', 'full_name']
READ_ONLY_FIELDS = ['id', 'email', 'is_staff']


class ChangePasswordSerializer(Serializer):
    old_password = CharField(required=True)
    new_password = CharField(required=True)


class StaffUserSerializer(ModelSerializer):
    email = EmailField(required=False)

    class Meta:
        model = User
        fields = FIELDS


class UserSerializer(StaffUserSerializer):

    class Meta(StaffUserSerializer.Meta):
        read_only_fields = READ_ONLY_FIELDS


class StaffUserWithTasksSerializer(StaffUserSerializer):
    tasks = TaskSerializer(many=True, read_only=False)

    class Meta(StaffUserSerializer.Meta):
        fields = StaffUserSerializer.Meta.fields + ['tasks']


class UserWithTasksSerializer(StaffUserWithTasksSerializer, UserSerializer):
    tasks = TaskSerializer(many=True, read_only=True)

    class Meta(StaffUserWithTasksSerializer.Meta):
        read_only_fields = READ_ONLY_FIELDS + ['tasks']
