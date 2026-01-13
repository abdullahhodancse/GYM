from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from accounts.models.custome_user import User



@admin.register(User)
class UserAdmin(BaseUserAdmin):
    ordering = ("email",)

    list_display = (
        "email",
        "role",
        "branch",
        "is_active",
        "is_staff",
    )

    list_filter = (
        "role",
        "branch",
        "is_active",
        "is_staff",
    )

    search_fields = ("email",)

    fieldsets = (
        ("Login Info", {
            "fields": ("email", "password")
        }),
        ("Role & Branch", {
            "fields": ("role", "branch")
        }),
        ("Permissions", {
            "fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")
        }),
        ("Important Dates", {
            "fields": ("last_login",)
        }),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email",
                "password1",
                "password2",
                "role",
                "branch",
                "is_active",
                "is_staff",
            ),
        }),
    )

    filter_horizontal = ("groups", "user_permissions")
