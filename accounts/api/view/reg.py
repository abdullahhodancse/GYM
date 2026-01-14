from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import login
from accounts.api.serializers.reg import UserRegisterSerializer


class RegisterView(generics.CreateAPIView):
    serializer_class = UserRegisterSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = serializer.save()

            # after reg auto login
            login(request, user)

            # JWT Tocken
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)

            
            return Response({
                "message": "Registration successful",
                "access_token": access_token,
                "user": {
                    "email": user.email,
                    "role": user.role
                }
            }, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({
                "error": str(e),
                "details": serializer.errors if 'serializer' in locals() else "Validation failed"
            }, status=status.HTTP_400_BAD_REQUEST)