from .models import User, Property, Image, Favorite, Inquiry
from django.contrib import admin

admin.site.register(User)
admin.site.register(Property)
admin.site.register(Image)
admin.site.register(Favorite)
admin.site.register(Inquiry)
