from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^$',views.index),
	url(r'^login/$', views.login),
	url(r'^dashboard/$',views.dashboard),
	url(r'^clearsession/$',views.clearsession),
	url(r'^staffmember/$',views.staffmember),
	url(r'^add_staffmember_page/$',views.add_staffmember_page),
	url(r'^add_staffmember/$',views.add_staffmember),
	url(r'^delete_staffmember/(?P<member_id>.+)/$',views.delete_staffmember),
	url(r'^edit_staffmember_page/(?P<member_id>.+)/$',views.edit_staffmember_page),
	url(r'^edit_staffmember/(?P<member_id>.+)/$',views.edit_staffmember),
	url(r'^staffmember_detail/(?P<member_id>.+)/$',views.staffmember_detail),

	url(r'^agentinfo/$',views.agentinfo),
	url(r'^add_agent_page/$',views.add_agent_page),
	

]
