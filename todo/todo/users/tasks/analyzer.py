from datetime import datetime
from celery import Task

from todo.users.models import User
from todo.core.manage import register


@register()
class Analyzer(Task):
    abstract = False

    def run(self, user_id, *args, **kwargs):
        user = User.objects.get(id=user_id)
        for task in user.tasks.all():
            task.analyzer_date = datetime.now().date()
            task.save(update_fields=['analyzer_date'])


if __name__ == '__main__':
    job = Analyzer()
    job.run()
