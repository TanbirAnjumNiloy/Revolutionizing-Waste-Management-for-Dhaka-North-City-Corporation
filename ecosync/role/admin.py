from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(User)
admin.site.register(Vehicle)
admin.site.register(STS)
admin.site.register(Landfill)
admin.site.register(STSManager)
admin.site.register(LandfillManager)
admin.site.register(STSEntry)
admin.site.register(LandfillEntry)