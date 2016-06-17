from django.contrib import admin
from .models import Medicament, User, MedicineType
from .models import Boala


admin.site.register(Medicament)
admin.site.register(User)
admin.site.register(MedicineType)
admin.site.register(Boala)
# Register your models here.
