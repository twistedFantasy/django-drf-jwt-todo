from django.db import models
from model_utils.choices import Choices

from todo.users.models import User
from todo.tasks.models import Task
from todo.core.models import BaseModel
from todo.core.helpers import cleanup


CATEGORY = Choices(
    ('programming_language', 'Programming Language'), ('database', 'Database'),
    ('cloud_technology', 'Cloud Technology'), ('testing_tool', 'Testing Tool'),
    ('frameworks', 'Frameworks'), ('other', 'Other'),
)


class Tag(BaseModel):
    name = models.CharField('Name', max_length=64, unique=True)
    category = models.CharField('Category', max_length=32, null=True, blank=True, default=None, choices=CATEGORY,
        db_index=True)

    class Meta:
        app_label = 'tags'
        verbose_name_plural = 'Tags'
        ordering = ['name']

    def __str__(self):
        return f'{self.name} (tag {self.id})'

    def save(self, *args, **kwargs):
        self.name = cleanup(self.name)
        super().save(*args, **kwargs)


class TaskTagModel(BaseModel):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    notes = models.TextField('Notes', null=True, blank=True)

    class Meta:
        app_label = 'tags'
        verbose_name_plural = 'TaskTag'
        unique_together = ('task', 'tag')
        ordering = ['task']

    def __str__(self):
        return f'{self.tag}-{self.task}'
