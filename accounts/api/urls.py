from django.urls import path
from rest_framework.routers import DefaultRouter
from accounts.api.view.login import CustomTokenObtainPairView
from accounts.api.view.reg import RegisterView
from accounts.api.view.profile import ProfileRetrieveView,ProfileUpdateView
from accounts.api.view.admin_reg import AdminRegisterView
from accounts.api.view.make_manager import MemberToManagerView
from accounts.api.view.manager_list import ManagerListView
from accounts.api.view.make_trainer import MakeTrainerView
from accounts.api.view.trainer_list import TrainerListView
from accounts.api.view.member_assign import AssignMemberToBranchView
from accounts.api.view.branch_wise_member_list import BranchWiseMemberListView

router = DefaultRouter()
urlpatterns = [
    
    path("reg/", RegisterView.as_view(), name="register"),# User registration endpoint
    path("login/", CustomTokenObtainPairView.as_view(), name="login"),# login endpoint
    path('profile/', ProfileRetrieveView.as_view(), name='profile-get'),# get profile
    path('profile/update/', ProfileUpdateView.as_view(), name='profile-update'),# profile update
    path("admin/register/", AdminRegisterView.as_view(),name = "asmin_reg"), # admin reg endpoind
    path("make_manager/", MemberToManagerView.as_view(), name="member-to-manager"),# member to manager
    path("managers/list/", ManagerListView.as_view(),name="manager_list"), # manager list
    path("make_trainer/", MakeTrainerView.as_view(), name="make-trainer"),#trainer create
    path("trainers_list/", TrainerListView.as_view(), name="trainer-list"),# trainer list
    path("assign_member/", AssignMemberToBranchView.as_view(), name="assign-member"), # assign member to branch
    path("branch_members/", BranchWiseMemberListView.as_view(), name = "branch_wise_member_list"),  # brancch wish member for manager
    path("branch_members/<int:branch_id>/", BranchWiseMemberListView.as_view(), name = "branch_wise_member_list")  # brancch wish member for admin
    


]


