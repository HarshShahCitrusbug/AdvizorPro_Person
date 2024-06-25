from django.contrib import admin
from core.models import (
    Brokers,
    BrokersLinkedInProfileData,
    BrokerScrappingData,
)

admin.site.register(Brokers, admin.ModelAdmin)
admin.site.register(BrokersLinkedInProfileData, admin.ModelAdmin)
admin.site.register(BrokerScrappingData, admin.ModelAdmin)
