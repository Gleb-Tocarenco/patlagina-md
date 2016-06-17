from django.contrib import admin
from .models import Medicament, User, MedicineType
from .models import Boala
from .models import MedicamentPharmacy, Farmacie
from .models import Localitate
from .models import Review


admin.site.register(Medicament)
admin.site.register(User)
admin.site.register(MedicineType)
admin.site.register(Boala)
admin.site.register(Farmacie)
admin.site.register(MedicamentPharmacy)
admin.site.register(Localitate)
admin.site.register(Review)
# Register your models here.
