from django.urls import path
from rest_framework.routers import DefaultRouter
from accounts.api.view.login import CustomTokenObtainPairView
from accounts.api.view.reg import RegisterView
from accounts.api.view.profile import ProfileRetrieveView,ProfileUpdateView
from accounts.api.view.admin_reg import AdminRegisterView
from accounts.api.view.make_manager import MemberToManagerView
from accounts.api.view.manager_list import ManagerListView

router = DefaultRouter()
urlpatterns = [
    
    path("reg/", RegisterView.as_view(), name="register"),# User registration endpoint
    path("login/", CustomTokenObtainPairView.as_view(), name="login"),# login endpoint
    path('profile/', ProfileRetrieveView.as_view(), name='profile-get'),# get profile
    path('profile/update/', ProfileUpdateView.as_view(), name='profile-update'),# profile update
    path("admin/register/", AdminRegisterView.as_view(),name = "asmin_reg"), # admin reg endpoind
    path("make_manager/", MemberToManagerView.as_view(), name="member-to-manager"),# member to manager
    path("managers/list/", ManagerListView.as_view(),name="manager_list") # manager list
    


]


