from django.contrib import admin


class QuoteTopicAdmin(admin.ModelAdmin):
    readonly_fields = ('slug',)


class QuoteAdmin(admin.ModelAdmin):
    list_display = ('speaker', 'truncated',)
