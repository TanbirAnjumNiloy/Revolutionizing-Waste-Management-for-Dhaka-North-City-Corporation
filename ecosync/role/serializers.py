# serializers.py

from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework import serializers
from django.contrib.auth.models import Group
from .models import (
    Vehicle,
    STS,
    Landfill,
    STSManager,
    LandfillManager,
    STSEntry,
    LandfillEntry,
)

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    groups = serializers.PrimaryKeyRelatedField(queryset=Group.objects.all(), required=False, many=True)

    class Meta:
        model = User
        fields = "__all__"


    


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = "__all__"


class STSSerializer(serializers.ModelSerializer):
    class Meta:
        model = STS
        fields = "__all__"


class LandfillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Landfill
        fields = "__all__"


class STSManagerSerializer(serializers.ModelSerializer):
    manager_email = serializers.CharField(source="user.email", read_only=True)

    class Meta:
        model = STSManager
        fields = ("sts_manager_id", "sts", "manager_email")


class LandfillManagerSerializer(serializers.ModelSerializer):
    manager_email = serializers.CharField(source="user.email", read_only=True)

    class Meta:
        model = LandfillManager
        fields = ("landfill_manager_id", "landfill", "manager_email")


class STSEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = STSEntry
        fields = "__all__"


class LandfillEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = LandfillEntry
        fields = "__all__"
