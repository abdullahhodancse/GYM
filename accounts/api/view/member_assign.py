# accounts/api/view/assign_member.py
from rest_framework import generics, status
from rest_framework.response import Response
from accounts.api.serializers.member.member_assign import AssignMemberToBranchSerializer
from permissions.manager_permission import IsManager

class AssignMemberToBranchView(generics.CreateAPIView):
    serializer_class = AssignMemberToBranchSerializer
    permission_classes = [IsManager]


    def create(self, request, *args, **kwargs):  # Handle POST request to assign a member to a branch.
        serializer = self.get_serializer(
            data=request.data,
            context={"request": request}
        )
        serializer.is_valid(raise_exception=True) #  Initialize serializer with request context
        member = serializer.save()

        return Response({
            "message": "Member assigned to your branch successfully",
            "member_id": member.id,
            "branch": member.branch.name
        }, status=status.HTTP_200_OK)
