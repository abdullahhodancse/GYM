from django.contrib import admin
from branches.models.branch import Branch

@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = ("name", "phone_number", "created_at")
    search_fields = ("name", "phone_number")
    list_filter = ("created_at",)
    ordering = ("-created_at",)