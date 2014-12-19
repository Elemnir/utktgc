from django.conf.urls import patterns, include, url

urlpatterns = patterns("quill.views",
    url(r"^mail/send/$",                "mailman",      name='mailman'),
    url(r"^accounts/profile/$",         "profile",      name='profile'),
    url(r"^forum/$",                    "forum",        name='forum'),
    url(r"^forum/(?P<pagenum>\d+)/$",   "forum",        name='forum_page'),
    url(r"^forum/thread/new/$",         "add_thread",   name='add_thread'),
    url(r"^forum/thread/(?P<val>\d+)/$","thread",       name='thread'),
    url(r"^forum/thread/(?P<val>\d+)/(?P<pagenum>\d+)/$",  "thread",   name='thread_page'),
    url(r"^forum/edit/(\d+)/$",         "edit_post",    name='edit_post'),
)
