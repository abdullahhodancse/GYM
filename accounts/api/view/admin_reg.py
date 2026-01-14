from rest_framework import generics, permissions, status
from rest_framework.response import Response
from accounts.api.serializers.admin_reg import AdminRegisterSerializer


class AdminRegisterView(generics.CreateAPIView):
    serializer_class = AdminRegisterSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        return Response({
            "message": "Admin created successfully",
            "email": user.email,
            "role": user.role
        }, status=status.HTTP_201_CREATED)
