from django.contrib import admin
from .models import Individual
from .models import Partnership
from .models import LLP
from .models import Limited_Company


# Register your models here.
admin.site.register(Individual)
admin.site.register(Partnership)
admin.site.register(LLP)
admin.site.register(Limited_Company)