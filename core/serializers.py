from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer, UserSerializer as BaseUserSerializer
from rest_framework import serializers 

class UserCreateSerializer(BaseUserCreateSerializer):
    email = serializers.EmailField(required=False)  # Make email field not required
    phone_number = serializers.CharField(required=False)
    class Meta(BaseUserCreateSerializer.Meta):
        
        fields = ['id','email','phone_number','username','password']

    def validate(self, attrs):
        email = attrs.get('email')
        phone_number = attrs.get('phone_number')

        if not email and not phone_number:
            raise serializers.ValidationError("You must provide either email or phone number.")

        if email and phone_number:
            raise serializers.ValidationError("Provide either email or phone number, not both.")

        return attrs

class UserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        ref_name = "User 1"     
        fields = ['id','username','email','phone_number']

