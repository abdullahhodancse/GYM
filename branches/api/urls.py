from django.urls import path
from branches.api.view.create import BranchCreateView
from branches.api.view.list import BranchListView
from branches.api.view.update import BranchUpdateView

urlpatterns = [
    path("create/", BranchCreateView.as_view(), name="branch-create"),
    path("list/", BranchListView.as_view(), name="branch-list"),
    path("update/<int:id>/", BranchUpdateView.as_view(), name="branch-update")
]