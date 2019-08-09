from django.utils.safestring import mark_safe

from todo.core.mixins import BaseAdminMixin


class HistoryAdminMixin(BaseAdminMixin):

    def path_url(self, obj):
        return mark_safe(self.get_href(obj.path, "Download", target='_blank'))
    path_url.short_description = 'Path'
