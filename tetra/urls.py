from django.conf.urls           import patterns, include, url
from django.contrib.auth.views  import login, logout

urlpatterns = patterns("tetra.views",
    url(r"^login/$",            login,      name='login'),
    url(r"^logout/$",           logout,     name='logout'),
    url(r"^register/$",         "register", name='register'),
)
