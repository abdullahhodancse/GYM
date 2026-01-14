from django.contrib import admin
from accounts.models.trainer import Trainer


@admin.register(Trainer)
class TrainerAdmin(admin.ModelAdmin):
    list_display = ('user', 'branch', 'phone_number')   # list page columns
    search_fields = ('user__email', 'branch__name')     # search by email / branch
    list_filter = ('branch',)                            # filter by branch
