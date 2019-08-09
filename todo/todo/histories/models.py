from django.db import models
from model_utils import Choices

from todo.core.models import BaseModel


STATUS = Choices('pending', 'processing', 'stopped', 'failed', 'completed')
BUSY = [STATUS.pending, STATUS.processing]
DONE = [STATUS.completed]


class History(BaseModel):
    status = models.CharField('Status', max_length=16, choices=STATUS, default=STATUS.pending, db_index=True)
    path = models.CharField('Path', max_length=256, null=True, blank=True)
    params = models.TextField('Params', null=True)
    msg = models.CharField('msg', max_length=256, null=True, blank=True)
    task_id = models.CharField('task_id', max_length=128, null=True)

    class Meta:
        app_label = 'histories'
        verbose_name_plural = 'Histories'
        ordering = ['-id']

    def __str__(self):
        return f'history_{self.id}'
