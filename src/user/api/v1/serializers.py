from rest_framework import serializers
from user.models.user import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        exclude = ['password']
