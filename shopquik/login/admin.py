from django.contrib import admin

# Register your models here.

from .models import Item, List, Store, Aisle, User

admin.site.register(Item)
admin.site.register(List)
admin.site.register(Store)
admin.site.register(Aisle)
admin.site.register(User)