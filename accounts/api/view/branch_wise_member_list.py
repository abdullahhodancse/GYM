from rest_framework import generics
from accounts.models.member import Member
from accounts.api.serializers.member.branch_wise_member import BranchWiseMemberListSerializer
from permissions.adminOrManager_permission import IsAdminOrManager
from pagination import Pagination

class BranchWiseMemberListView(generics.ListAPIView):
    serializer_class = BranchWiseMemberListSerializer
    permission_classes = [IsAdminOrManager]
    pagination_class = Pagination

    def get_queryset(self):
        user = self.request.user
        queryset = Member.objects.select_related("user", "branch")

        #  Admin logic
        if user.role == "admin":
            branch_id = self.request.query_params.get("branch_id")
            if branch_id:
                return queryset.filter(branch_id=branch_id)
            return queryset # admin gets all member if branch id not provied
         
        #  Manager logic
        return queryset.filter(branch=user.manager.branch)
