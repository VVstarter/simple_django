from django.contrib import admin

from .models import NewsM


class NewsMAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'date')
    list_display_links = ('title', 'content')
    search_fields = ('title', 'content')


admin.site.register(NewsM, NewsMAdmin)