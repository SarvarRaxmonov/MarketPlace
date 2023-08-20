from django.contrib import admin
from apps.seller.models import Profile, SendInquiry, Country

admin.site.register(Profile)
admin.site.register(SendInquiry)
admin.site.register(Country)
