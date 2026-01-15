from rest_framework import generics
from accounts.api.serializers.manager.make_manager import MemberToManagerSerializer
from permissions.admin_permission import IsAdmin

class MemberToManagerView(generics.CreateAPIView):
    serializer_class = MemberToManagerSerializer
    permission_classes = [IsAdmin]