from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$|index|index.html','fueled.restaurant.views.show_restaurant'),
    url(r'^restaurant/(?P<restaurant>.*)/edit/$','fueled.restaurant.views.edit_restaurant'),
    #url(r'^restaurant/(?P<restaurant>.*)/$','fueled.restaurant.views.show_restaurant'),
    url(r'^restaurant/add/$','fueled.restaurant.views.add_restaurant'),
    # Examples:
    # url(r'^$', 'fueled.views.home', name='home'),
    # url(r'^fueled/', include('fueled.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
