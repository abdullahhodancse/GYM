from django.contrib import admin
from accounts.models.member import Member


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('user', 'branch', 'phone_number')   # list view 
    search_fields = ('user__email', 'branch__name')     # search bar
    list_filter = ('branch',)                            # filter sidebar