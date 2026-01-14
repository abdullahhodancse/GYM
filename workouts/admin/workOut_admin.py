from django.contrib import admin
from workouts.models.workOut_plan import WorkOutPlan


@admin.register(WorkOutPlan)
class WorkOutPlanAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "created_by",
        "branch",
        "created_at",
    )

    list_filter = (
        "branch",
        "created_by",
        "created_at",
    )

    search_fields = (
        "title",
        "description",
        "created_by__user__email",
    )

    ordering = ("-created_at",)

    readonly_fields = ("created_at",)
