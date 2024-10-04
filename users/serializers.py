from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from users.models import CustomUser

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])

    class Meta:
        model = CustomUser
        fields = ('phone', 'full_name', 'password')

    def create(self, validated_data):
        user = CustomUser.objects.create(
            username=validated_data['phone'],  # 'phone' ni username sifatida qo'shamiz
            phone=validated_data['phone'],
            full_name=validated_data['full_name']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
