from django.contrib import admin
from home.models import Doctor, Address, Bio, People
# from home.models import Doctor,Address,Bio, People

# Register your models here.
admin.site.register(Doctor)
admin.site.register(Address)
admin.site.register(Bio)
admin.site.register(People)
