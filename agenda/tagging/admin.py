from django.contrib import admin
from agenda.tagging.models import Tag, TaggedItem
from agenda.tagging.forms import TagAdminForm

class TagAdmin(admin.ModelAdmin):
    form = TagAdminForm

admin.site.register(TaggedItem)
admin.site.register(Tag, TagAdmin)




