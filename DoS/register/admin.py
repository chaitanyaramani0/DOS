from django.contrib import admin
from .models import User,Individual,Bulk,Industrial,Commercial
# Register your models here.

admin.site.register(User)
admin.site.register(Industrial)
admin.site.register(Individual)
admin.site.register(Bulk)
admin.site.register(Commercial)
