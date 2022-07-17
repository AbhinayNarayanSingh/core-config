from rest_framework import serializers
from .models import *
from user.models import User
from user.serializers import UserSerializer


class CompanySerializer (serializers.ModelSerializer) :

    class Meta:
        model = Company
        fields = "__all__"


class PrimaryGroupSerializer (serializers.ModelSerializer) :

    class Meta:
        model = PrimaryGroup
        fields = ["name"]


class GroupSerializer (serializers.ModelSerializer) :
    under = PrimaryGroupSerializer(many=False)

    class Meta:
        model = Group
        fields = ["id", "name", "under"]


class LedgerSerializer (serializers.ModelSerializer) :

    class Meta:
        model = Ledger
        fields = "__all__"


class JournalSerializer (serializers.ModelSerializer) :

    class Meta:
        model = Journal
        fields = "__all__"