from rest_framework import serializers
from .models import User
from rest_framework.validators import UniqueValidator


class RegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(required=True ,write_only=True)

    class Meta:
        model = User
        fields = ['name', 'email', 'phone', 'password', 'password2']
        extra_kwargs = {
            'password':{'write_only':True},
            'email':{'validators':[UniqueValidator(queryset=User.objects.all())]},
        }

    def validate_phone(self, value):
        if not value.isdigit():
            raise serializers.ValidationError('Phone number must be numeric.')
        if len(value) != 11:
            raise serializers.ValidationError('Phone number must be exactly 11 digits.')
        return value
    
    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError('Passwords must match.')
        return data
    
    def create(self, validated_data):
        validated_data.pop('password2')
        return User.objects.create_user(**validated_data)


