from django.contrib import admin
from .user import UserAdmin, User
from .group import Group, GroupAdmin


admin.site.register(User, UserAdmin)
admin.site.register(Group, GroupAdmin)
