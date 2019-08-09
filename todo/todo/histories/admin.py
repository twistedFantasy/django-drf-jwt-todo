from django import forms
from django.contrib import admin

from todo.histories.models import History
from todo.histories.mixins import HistoryAdminMixin
from todo.core.codemirror2 import json_widget, python_widget


JSON_WIDGET = json_widget(readonly=False)
PYTHON_WIDGET = python_widget(readonly=True)


class HistoryForm(forms.ModelForm):
    params = forms.CharField(required=False, widget=JSON_WIDGET)
    msg = forms.CharField(required=False, widget=PYTHON_WIDGET)


@admin.register(History)
class HistoryAdmin(admin.ModelAdmin, HistoryAdminMixin):
    form = HistoryForm
    list_display = ['id', 'status']
    list_filter = ['status']
    readonly_fields = ['path_url', 'task_id', 'created', 'modified']
    fieldsets = [
        (None, {'fields': ['status', 'path_url', 'params', 'msg', 'task_id']}),
        ('System', {'classes': ['collapse'], 'fields': ['created', 'modified']}),
    ]
    ordering = ['-id']
    filter_horizontal = []
