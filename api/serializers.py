from rest_framework import serializers
from .models import User,UserProfile
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password','mobile_number']
        extra_kwargs = {
            'password': {'write_only': True}

        }

    def create(self, validated_data):
        password = validated_data.pop('password',None)
        # print("pass", password)
        instance = self.Meta.model(**validated_data)
        # print("instance",instance)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'
