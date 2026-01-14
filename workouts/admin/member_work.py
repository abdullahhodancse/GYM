from django.contrib import admin
from workouts.models.memberworkOut import MemberWorkOut


@admin.register(MemberWorkOut)
class MemberWorkOutAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "member",
        "workoutplan",
        "status",
        "due_date",
        "created_at",
    )

    list_filter = (
        "status",
        "due_date",
        "workoutplan",
    )

    search_fields = (
        "member__user__email",
        "workoutplan__title",
    )

    ordering = ("-created_at",)

    readonly_fields = ("created_at",)
