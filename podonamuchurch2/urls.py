from django.conf.urls import patterns, include, url
from finance.views import index, report_member, report_income, report_budget, report_total, some_view
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^index/$', index),
                       url(r'^report/member/$', report_member),
                       url(r'^report/income/$', report_income),
                       url(r'^report/budget/$', report_budget),
                       url(r'^report/total/$', report_total),
                       url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^some_view/$', some_view),
)
