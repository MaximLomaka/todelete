from django.contrib import admin
from .models import Person, Phone, Education

# Register your models here.
admin.site.register(Person)
admin.site.register(Phone)
admin.site.register(Education)
