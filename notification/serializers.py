import re
from rest_framework import serializers
from .models import User


class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password']

    def validate(self, data):
        password = data.get('password', None)

        # # Validate password has at least one small and capital letter
        # if not re.match(r"^(?=.*[A-Z])(?=.*[a-z]).*", password):
        #     raise serializers.ValidationError(
        #         'A password must contain atleast one small letter and one capital letter.'
        #     )
        # # Validate the password has atleast one number
        # elif not re.match(r"^(?=.*[0-9]).*", password):
        #     raise serializers.ValidationError(
        #         'A password must contain atleast one number.'
        #     )

        return data

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    
    
    
