from rest_framework import generics
from accounts.models.manager import Manager
from accounts.api.serializers.manager.manager_list import ManagerListSerializer
from permissions.admin_permission import IsAdmin
from pagination import Pagination

class ManagerListView(generics.ListAPIView):
    queryset = Manager.objects.select_related("user", "branch")
    serializer_class = ManagerListSerializer
    permission_classes = [IsAdmin]
    pagination_class = Pagination
