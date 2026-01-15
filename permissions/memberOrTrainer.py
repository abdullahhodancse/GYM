# workouts/permissions/is_member_or_trainer.py
from rest_framework.permissions import BasePermission

class IsMemberOrTrainer(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and (
                hasattr(request.user, "member")
                or hasattr(request.user, "trainer")
            )
        )
