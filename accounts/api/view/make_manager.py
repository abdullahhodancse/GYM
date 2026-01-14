from rest_framework import generics
from accounts.api.serializers.make_manager import MemberToManagerSerializer
from admin_permission import IsAdmin

class MemberToManagerView(generics.CreateAPIView):
    serializer_class = MemberToManagerSerializer
    permission_classes = [IsAdmin]