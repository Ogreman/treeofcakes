from django.conf.urls import patterns, include, url
from core.views import AboutPageView, HomePageView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', HomePageView.as_view(), name='home'),
    url(r'^about/$', AboutPageView.as_view(), name='about'),

    url(r'^blog/', include('blog.urls')),
    url(r'^recipes/', include('recipes.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
