from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group

from todo.users.models import User


class UserAdmin(BaseUserAdmin):
    list_display = ['email', 'full_name', 'modified']
    list_filter = ['is_staff', 'tags']
    search_fields = ['email', 'full_name']
    readonly_fields = ['created', 'modified']
    fieldsets = [
        (None, {'fields': ['email', 'password']}),
        ('Details', {'fields': ['full_name', 'tags']}),
        ('Permissions', {'fields': ['is_active', 'is_staff', 'is_superuser']}),
        ('System', {'classes': ['collapse'], 'fields': ['created', 'modified']}),
    ]
    add_fieldsets = [
        (None, {
            'classes': ['wide'],
            'fields': ['email', 'password1', 'password2']}
         ),
    ]
    ordering = ['-modified']
    filter_horizontal = []


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
