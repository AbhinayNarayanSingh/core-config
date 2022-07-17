from rest_framework import serializers
# from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User


# serializers.ModelSerializer


class UserSerializer(serializers.ModelSerializer):
    _id = serializers.SerializerMethodField(read_only=True)
    isAdmin = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ['_id',  'email', 'name', 'isAdmin']

    def get__id(self, obj):
        return obj.id

    def get_isAdmin(self, obj):
        return obj.is_staff



class UserSerializerWithToken(UserSerializer):
    access = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = [ '_id', 'email', 'name', 'isAdmin', 'access']

    def get_access(self, obj):
        token = RefreshToken.for_user(obj)
        return str(token.access_token)