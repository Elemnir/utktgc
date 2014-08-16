from django.conf.urls import patterns, include, url

urlpatterns = patterns("quill.views",
    url(r"^send/$",     "mailman",  name='mailman'),
)
