from django.contrib import admin

# Register your models here.
from .models import ClientDetail,ClientOffer,ClientBooking

admin.site.register(ClientDetail)
admin.site.register(ClientOffer)
admin.site.register(ClientBooking)
