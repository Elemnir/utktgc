from django.conf.urls           import patterns, include, url
from django.conf                import settings
from django.conf.urls.static    import static
from django.contrib             import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'', include('myr.urls')),
    url(r'^mail/', include('quill.urls')),
    url(r'^accounts/', include('tetra.urls')),
    
    url(r'^accounts/profile/$', 'quill.views.profile'),

    url(r'^admin/', include(admin.site.urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
