from rest_framework import generics
from branches.models.branch import Branch
from branches.api.serializer.create import BranchSerializer
from  permissions.admin_permission import IsAdmin

class BranchCreateView(generics.CreateAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer
    permission_classes = [IsAdmin]
