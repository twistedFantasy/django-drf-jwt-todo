from todo.users.models import User

from rest_framework.filters import BaseFilterBackend


class UserFilterBackend(BaseFilterBackend):
    field = 'user_id'

    def filter_queryset(self, request, queryset, view):
        user_id = get_user_id(request)
        if user_id:
            return queryset.filter(**{'%s' % self.field: user_id})
        return queryset


def get_user_id(request):
    data = request.query_params
    if request.user.is_staff:
        if data.get('user_id'):
            user = User.objects.get(id=data.get('user_id'))
            return user.id
        return
    return request.user.id
