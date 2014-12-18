from quill.models import Tag, Thread, Post, Member
from django.contrib import admin

class TagAdmin(admin.ModelAdmin):
    class Meta:
        model = Tag
admin.site.register(Tag, TagAdmin)

class ThreadAdmin(admin.ModelAdmin):
    class Meta:
        model = Thread
    list_display = ["title", "creator", "created"]
    list_filter = ["creator"]
admin.site.register(Thread, ThreadAdmin)

class PostAdmin(admin.ModelAdmin):
    class Meta:
        model = Post
    list_display = ["title", "thread", "creator", "created"]
    search_fields = ["title", "creator"]
admin.site.register(Post, PostAdmin)

class MemberAdmin(admin.ModelAdmin):
    class Meta:
        model = Member
admin.site.register(Member, MemberAdmin)


