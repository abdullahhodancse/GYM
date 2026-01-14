from django.contrib import admin
from workouts.models.workOutTask import WorkOutTask


@admin.register(WorkOutTask)
class WorkOutTaskAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "workplan",
        "sets",
        "reps",
    )

    list_filter = (
        "workplan",
    )

    search_fields = (
        "name",
        "workplan__title",
    )

    ordering = ("workplan", "name")
