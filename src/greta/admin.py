from django.contrib import admin
from guardian.admin import GuardedModelAdmin

from .models import Repository


class RepositoryAdmin(GuardedModelAdmin):
    list_display = ('name', 'forked_from', 'description', 'default_branch')


admin.site.register(Repository, RepositoryAdmin)
