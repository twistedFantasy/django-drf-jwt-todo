from django.contrib import admin

from todo.tasks.models import Task
from todo.tags.models import TaskTagModel


class TaskTagInline(admin.TabularInline):
    model = TaskTagModel
    extra = 1


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['name', 'type', 'is_completed', 'modified']
    list_filter = ['type', 'is_completed']
    search_fields = ['name']
    readonly_fields = ['created', 'modified']
    fieldsets = [
        (None, {'fields': ['name', 'type', 'is_completed']}),
        ('Details', {'fields': ['user', 'description', 'start_date', 'end_date', 'analyzer_date']}),
        ('System', {'classes': ['collapse'], 'fields': ['created', 'modified']}),
    ]
    add_fieldsets = [
        (None, {
            'classes': ['wide'],
            'fields': ['email', 'password1', 'password2']}
         ),
    ]
    inlines = [TaskTagInline]
    ordering = ['-modified']
    filter_horizontal = []
