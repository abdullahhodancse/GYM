from rest_framework import generics
from branches.models.branch import Branch
from branches.api.serializer.create import BranchSerializer
from admin_permission import IsAdmin

class BranchUpdateView(generics.UpdateAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer
    permission_classes = [IsAdmin]
    lookup_field = "id"
