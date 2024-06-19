from django.contrib import admin
from core.models import Brokers, BrokersLinkedInProfileData

admin.site.register(Brokers, admin.ModelAdmin)
admin.site.register(BrokersLinkedInProfileData, admin.ModelAdmin)
