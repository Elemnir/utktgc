from quill.models import Tag, Thread, Post, PostDiff, Member
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

class PostDiffInline(admin.StackedInline):
    model = PostDiff
    extra = 0
    ordering = ("-created",)

class PostAdmin(admin.ModelAdmin):
    class Meta:
        model = Post
    list_display = ["__unicode__", "created", "updated"]
    search_fields = ["creator",]
    inlines = [PostDiffInline]
admin.site.register(Post, PostAdmin)

class MemberAdmin(admin.ModelAdmin):
    class Meta:
        model = Member
admin.site.register(Member, MemberAdmin)


