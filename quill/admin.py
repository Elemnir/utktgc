from quill.models import Tag, Member
from django.contrib import admin

class TagAdmin(admin.ModelAdmin):
    class Meta:
        model = Tag
admin.site.register(Tag, TagAdmin)

class MemberAdmin(admin.ModelAdmin):
    class Meta:
        model = Member
admin.site.register(Member, MemberAdmin)


