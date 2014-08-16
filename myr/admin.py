from myr.models import Asset, Post, Event, AboutStatement
from django.contrib import admin

class AssetAdmin(admin.ModelAdmin):
    class Meta:
        model = Asset
admin.site.register(Asset, AssetAdmin)

class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Post', {'fields': ('head',)}),
        ('Body', {'fields': ('body', 'assets')}),
    ]
    list_display = ('head', 'date')
    search_fields = ['head', 'body',]
    ordering = ['-date', 'head']
    actions = []
admin.site.register(Post, PostAdmin)

class EventAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Event', {'fields': ('date', 'name',)}),
        ('Info', {'fields': ('info', 'assets')}),
    ]
    list_display = ('name', 'date')
    search_fields = ['name', 'info',]
    ordering = ['-date', 'name']
    actions = []
admin.site.register(Event, EventAdmin)

class AboutStatementAdmin(admin.ModelAdmin):
    class Meta:
        model = AboutStatement
admin.site.register(AboutStatement, AboutStatementAdmin)
