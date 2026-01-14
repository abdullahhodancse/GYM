from django.contrib import admin
from accounts.models.manager import Manager


@admin.register(Manager)
class ManagerAdmin(admin.ModelAdmin):
    list_display = ('user', 'branch', 'phone_number')   # list view 
    search_fields = ('user__email', 'branch__name')     # search bar
    list_filter = ('branch',)                            # filter sidebar