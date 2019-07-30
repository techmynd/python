from django.contrib import admin

# Register your models here.

from .models import Page

# customize admin options and add extra functionality


class PageAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published')
    list_display_links = ('id', 'title')
    # list_filter = ('category',)
    # # we dont have category for pages but you can sort records by filtering them
    list_editable = ('is_published',)
    # search by title and id
    search_fields = ('title', 'id',)
    list_per_page = 25


# model to generate admin for pages
# admin.site.register(Page)
admin.site.register(Page, PageAdmin)
