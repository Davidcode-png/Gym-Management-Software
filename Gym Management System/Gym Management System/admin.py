from django.contrib import admin
# from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User
from django.contrib.auth.models import Group

# class ProfileInLine(admin.StackedInline):
#     model = Profile
#     can_delete = False

# class UserAdmin(BaseUserAdmin):
#     # list_display = ('username','email','full_name',
#     #                 'gym_name')
#     inlines = (ProfileInLine,) 

class PersonAdmin(admin.ModelAdmin):
    list_display = ('username','full_name', 'email','gym_name')

admin.site.unregister(Group)
admin.site.register(User,PersonAdmin)
