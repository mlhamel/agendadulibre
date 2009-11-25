from django.contrib import admin
from agenda.events.models import Event, City, Region

class EventAdmin(admin.ModelAdmin):
    date_hierarchy = 'start_time'

class CityAdmin(admin.ModelAdmin):
    list_filter = ('region',)
    list_display = ('name','region')
    pass

admin.site.register(Event, EventAdmin)
admin.site.register(Region)
admin.site.register(City, CityAdmin)
