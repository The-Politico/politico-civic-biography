from django.contrib import admin
from biography.models import Biography, IdeologyCategory

from .biography import BiographyAdmin

admin.site.register(Biography, BiographyAdmin)
admin.site.register(IdeologyCategory)
