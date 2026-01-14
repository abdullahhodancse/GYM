from rest_framework import generics, permissions, status
from rest_framework.response import Response

from accounts.models.member import Member
from accounts.models.manager import Manager
from accounts.models.trainer import Trainer
from accounts.models.custome_user import User
from rest_framework.exceptions import ValidationError


from accounts.api.serializers.general.trainer import TrainerSerializer
from accounts.api.serializers.general.member import MemberSerializer
from accounts.api.serializers.general.manager import ManagerSerializer







def get_serializer_and_profile(user):
    if user.role == "manager":
        serializer_class = ManagerSerializer
        try:
            profile = Manager.objects.get(user=user)
        except Manager.DoesNotExist:
            raise ValidationError("Manager profile not created yet")

    elif user.role == "trainer":
        serializer_class = TrainerSerializer
        try:
            profile = Trainer.objects.get(user=user)
        except Trainer.DoesNotExist:
            raise ValidationError("Trainer profile not created yet")

    elif user.role == "member":
        serializer_class = MemberSerializer
        try:
            profile = Member.objects.get(user=user)
        except Member.DoesNotExist:
            raise ValidationError("Member profile not created yet")

    else:
        raise ValidationError("Invalid role")

    return serializer_class, profile


#get profile
class ProfileRetrieveView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = request.user

        serializer_class, profile = get_serializer_and_profile(user)
        serializer = serializer_class(profile)

        return Response({
            "role": user.role,
            "profile": serializer.data
        })


# update profile
class ProfileUpdateView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request, *args, **kwargs):
        return self.update_profile(request)

    def patch(self, request, *args, **kwargs):
        return self.update_profile(request)

    def update_profile(self, request):
        user = request.user

        serializer_class, profile = get_serializer_and_profile(user)

        serializer = serializer_class(profile, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({
                "role": user.role,
                "profile": serializer.data
            })

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)