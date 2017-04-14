from django.conf.urls import url
from django.conf import settings
from . import views


urlpatterns = [
    url(r'^$', views.index),
    url(r'^login/$', views.login),
    url(r'^clearsession/$', views.clearsession),
    url(r'^setting/$', views.setting),

    url(r'^staffmember/$', views.staffmember),
    url(r'^add_staffmember_page/$', views.add_staffmember_page),
    url(r'^add_staffmember/$', views.add_staffmember),
    url(r'^delete_staffmember/(?P<member_id>.+)/$', views.delete_staffmember),
    url(r'^edit_staffmember_page/(?P<member_id>.+)/$', views.edit_staffmember_page),
    url(r'^edit_staffmember/(?P<member_id>.+)/$', views.edit_staffmember),
    url(r'^staffmember_detail/(?P<member_id>.+)/$', views.staffmember_detail),

    url(r'^customer/$', views.customer),
    url(r'^add_customer_page/$', views.add_customer_page),
    url(r'^add_customer/$', views.add_customer),
    url(r'^edit_customer_page/(?P<customer_id>.+)/$', views.edit_customer_page),
    url(r'^edit_customer/(?P<customer_id>.+)/$', views.edit_customer),
    url(r'^delete_customer/(?P<customer_id>.+)/$', views.delete_customer),
    url(r'^customer_detail/(?P<customer_id>.+)/$', views.customer_detail),

    url(r'^agentinfo/$', views.agentinfo),
    url(r'^add_agent_page/$', views.add_agent_page),
    url(r'^add_agent/$', views.add_agent),
    url(r'^edit_agent_page/(?P<agent_id>.+)/$', views.edit_agent_page),
    url(r'^edit_agent/(?P<agent_id>.+)/$', views.edit_agent),
    url(r'^delete_agent/(?P<agent_id>.+)/$', views.delete_agent),
    url(r'^agent_detail/(?P<agent_id>.+)/$', views.agent_detail),

    url(r'^plots/$', views.plots),
    url(r'^add_plot/$', views.add_plot),
    url(r'^edit_plot/$', views.edit_plot),
    url(r'^plot_detail/(?P<plot_id>.+)/$', views.plot_detail),
    url(r'^delete_plot/(?P<plot_id>.+)/$', views.delete_plot),

    url(r'^projects/$', views.projects),
    url(r'^add_project/$', views.add_project),
    url(r'^edit_project/$', views.edit_project),
    url(r'^delete_project/(?P<project_id>.+)/$', views.delete_project),


    url(r'^billing/$', views.billing),

    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT,
    }),

]
