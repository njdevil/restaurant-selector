# Restaurant Selector v0.1
# https://github.com/njdevil/restaurant-selector
# &copy;2013 Modular Programming Systems Inc
# released as GPL 3

from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$|index|index.html','fueled.restaurant.views.index'),
    url(r'^random/$','fueled.restaurant.views.index'),
    url(r'^restaurant/(?P<restaurant>.*)/$','fueled.restaurant.views.show_restaurant'),
    url(r'^login/$','fueled.restaurant.views.userlogin'),
    url(r'^logout/$','fueled.restaurant.views.userlogout'),
    url(r'^user/(?P<username>.*)/$','fueled.restaurant.views.user_profile'),
    url(r'^add/restaurant/$','fueled.restaurant.views.add_restaurant'),
    url(r'^add/user/$','fueled.restaurant.views.add_user'),
    url(r'^add/group/$','fueled.restaurant.views.add_group'),

    url(r'^admin/', include(admin.site.urls)),
)
