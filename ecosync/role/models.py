from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid
from django.db import models
from django.contrib.auth.models import User
import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid

# --------------------------------------------------------------------------------User and role management-------------------------------------------------------------------------------------------
class User(AbstractUser):
    ROLES = (
        ("admin", "System Admin"),
        ("sts_manager", "STS Manager"),
        ("landfill_manager", "Landfill Manager"),
        ("unassigned", "Unassigned"),
    )

    user_id = models.AutoField(primary_key=True)
    id = models.UUIDField(default=uuid.uuid4, editable=False)
    role = models.CharField(max_length=20, choices=ROLES, default="unassigned")
    groups = models.ManyToManyField("auth.Group", related_name="custom_user_groups")
    user_permissions = models.ManyToManyField(
        "auth.Permission", related_name="custom_user_permissions"
    )

    def __str__(self):
        return str(self.user_id)

    class Meta:
        permissions = [
            ("view_user_roles", "Can view user roles"),
            ("change_user_roles", "Can change user roles"),
        ]


# --------------------------------------------------------------------------------Data Entry Views-------------------------------------------------------------------------------------------


class Vehicle(models.Model):
    vehicle_id = models.AutoField(primary_key=True)
    registration_number = models.CharField(max_length=100, unique=True)
    VEHICLE_TYPE_CHOICES = [
        ("open_truck", "Open Truck"),
        ("dump_truck", "Dump Truck"),
        ("compactor", "Compactor"),
        ("container_carrier", "Container Carrier"),
    ]
    type = models.CharField(max_length=20, choices=VEHICLE_TYPE_CHOICES)
    CAPACITY_CHOICES = [(3, "3 Ton"), (5, "5 Ton"), (7, "7 Ton") , (15, "15 Ton")]
    capacity = models.IntegerField(choices=CAPACITY_CHOICES)
    fuel_cost_loaded = models.DecimalField(max_digits=10, decimal_places=2)
    fuel_cost_unloaded = models.DecimalField(max_digits=10, decimal_places=2)


class STS(models.Model):
    sts_id = models.AutoField(primary_key=True)
    ward_number = models.IntegerField()
    capacity = models.IntegerField()
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)

    


class Landfill(models.Model):
    landfill_id = models.AutoField(primary_key=True)
    capacity = models.IntegerField()
    operational_timespan = models.CharField(max_length=100)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)


class STSManager(models.Model):
    sts_manager_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False
    )
    sts = models.ForeignKey(STS, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.email


class LandfillManager(models.Model):
    landfill_manager_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False
    )
    landfill = models.ForeignKey(Landfill, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.email


class STSEntry(models.Model):
    entry_id = models.AutoField(primary_key=True)
    sts = models.ForeignKey(STS, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    sts_manager = models.ForeignKey(STSManager, on_delete=models.CASCADE)
    weight_of_waste = models.IntegerField()
    time_of_arrival = models.DateTimeField()
    time_of_departure = models.DateTimeField()


class LandfillEntry(models.Model):
    entry_id = models.AutoField(primary_key=True)
    landfill = models.ForeignKey(Landfill, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    landfill_manager = models.ForeignKey(LandfillManager, on_delete=models.CASCADE)
    weight_of_waste = models.IntegerField()
    time_of_arrival = models.DateTimeField()
    time_of_departure = models.DateTimeField()
