from django.conf.urls import url
from django.conf import settings
from . import views


urlpatterns = [
    url(r'^$', views.index),
    url(r'^login/$', views.login),
    url(r'^dashboard/$', views.dashboard),
    url(r'^clearsession/$', views.clearsession),

    url(r'^staffmember/$', views.staffmember),
    url(r'^add_staffmember_page/$', views.add_staffmember_page),
    url(r'^add_staffmember/$', views.add_staffmember),
    url(r'^delete_staffmember/(?P<member_id>.+)/$', views.delete_staffmember),
    url(r'^edit_staffmember_page/(?P<member_id>.+)/$', views.edit_staffmember_page),
    url(r'^edit_staffmember/(?P<member_id>.+)/$', views.edit_staffmember),
    url(r'^staffmember_detail/(?P<member_id>.+)/$', views.staffmember_detail),

    url(r'^add_customer_page/$', views.add_customer_page),
    url(r'^add_customer/$', views.add_customer),

    url(r'^agentinfo/$', views.agentinfo),
    url(r'^add_agent_page/$', views.add_agent_page),
    url(r'^add_agent/$', views.add_agent),
    url(r'^edit_agent_page/(?P<agent_id>.+)/$', views.edit_agent_page),
    url(r'^edit_agent/(?P<agent_id>.+)/$', views.edit_agent),
    url(r'^delete_agent/(?P<agent_id>.+)/$', views.delete_agent),
    url(r'^agent_detail/(?P<agent_id>.+)/$', views.agent_detail),

    url(r'^plots/$', views.plots),

    url(r'^projects/$', views.projects),

    url(r'^billing/$', views.billing),

    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT,
    }),

]
