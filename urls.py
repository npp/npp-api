from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    (r'^search/(?P<source>\w+)/$', 'npp.data.views.source_search'),
    (r'^result/(?P<source>\w+)/$', 'npp.data.views.result'),
    # Example:
    # (r'^npp/', include('npp.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('django.views.generic.simple',
    (r'^$', 'direct_to_template', {'template': 'data/index.html'}),
    (r'^sandbox/$', 'direct_to_template', {'template': 'sandbox/index.html'}),
    (r'^api/', include('npp.api.urls')),
    (r'^search/$', 'direct_to_template', {'template':'data/search_index.html'}),
)