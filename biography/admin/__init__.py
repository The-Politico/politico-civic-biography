from django.contrib import admin
from biography.models import Biography, QuoteTopic, Quote, IdeologyCategory

from .biography import BiographyAdmin
from .quote import QuoteTopicAdmin, QuoteAdmin

admin.site.register(Biography, BiographyAdmin)
admin.site.register(QuoteTopic, QuoteTopicAdmin)
admin.site.register(Quote, QuoteAdmin)
admin.site.register(IdeologyCategory)
