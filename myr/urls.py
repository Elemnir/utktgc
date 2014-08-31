from django.conf.urls import patterns, include, url

urlpatterns = patterns("myr.views",
    url(r"^$",                           "index",       name='home'),
    url(r"^index/$",                     "index",       name='index'),
    url(r"^about/$",                     "about",       name='about'),
    url(r"^calendar/$",                  "calendar",    name='calendar'),
    url(r"^calendar/(?P<pagenum>\d+)/$", "calendar",    name='calendar_page'),
    url(r"^archive/$",                   "archive",     name='archive'),
    url(r"^archive/(?P<pagenum>\d+)/$",  "archive",     name='archive_page'),
    url(r"^detail/(post|event)/(\d+)/$", "detail"),
)
