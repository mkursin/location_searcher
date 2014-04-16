from django.contrib import admin

# # Register your models here.
from searcher.models import LocationsByIp
#
#
# # class LocationsIpAdmin(admin.ModelAdmin):
# #     list_display = ('ID', 'IP', 'Latitude', 'Longitude', 'City', 'Region', 'Bistrict')
# #     # search_fields = ('ID', 'Name', 'Key')
# #     # list_filter = ('Key', 'Name',)
#
admin.site.register(LocationsByIp)