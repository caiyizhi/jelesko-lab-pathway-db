from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^jelesko_web/', include('jelesko_web.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs'
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/(.*)', admin.site.root),
    (r'^search/', include('jelesko_web.blast_fasta.urls')),

    # DO NOT USE IN PRODUCTION SITE
    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve',
           {'document_root': '/Users/caiyizhi/django_data', 'show_indexes': True}),
)
