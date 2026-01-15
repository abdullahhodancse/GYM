from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import exceptions
from rate_limit import LoginRateThrottle

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    username_field = 'email'
   


    def validate(self, attrs):
        
        email = attrs.get("email") or attrs.get("username")
        password = attrs.get("password")

        if not email:
            raise exceptions.AuthenticationFailed("Email is required")
        if not password:
            raise exceptions.AuthenticationFailed("Password is required")

        from django.contrib.auth import authenticate
        user = authenticate(request=self.context.get('request'), email=email, password=password)

        if not user:
            raise exceptions.AuthenticationFailed('Invalid email or password')
        if not user.is_active:
            raise exceptions.AuthenticationFailed('Account is disabled')

        
        data = super().validate(attrs)

        
        data['user'] = {
            'email': user.email,
            'role': user.role
        }

        return data


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
    throttle_classes = [LoginRateThrottle]