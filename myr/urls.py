from django.conf.urls import patterns, include, url

urlpatterns = patterns("myr.views",
    url(r"^$",                           "index",       name='home'),
    url(r"^index/$",                     "index",       name='index'),
    url(r"^about/$",                     "about",       name='about'),
    url(r"^calendar/$",                  "calendar",    name='calendar'),
    url(r"^archive/$",                   "archive",     name='archive'),
    url(r"^detail/(post|event)/(\d+)/$", "detail"),
)
