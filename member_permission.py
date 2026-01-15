from rest_framework.permissions import BasePermission

class IsMember(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and hasattr(request.user, "member")
            and request.user.role == "member"
        )