from django.conf.urls import patterns, url 
from tutorial_app import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
	url(r'^about/', views.about, name='about'),
	url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.category, name='category'),
	url(r'^add-category/', views.add_category, name="add-category"),
	url(r'^category/(?P<category_name_slug>[\w\-]+)/add-page/$', views.add_page, name='add-page'),
	url(r'^register/$',views.register,name='register'),
	url(r'^login/$',views.user_login, name='login')
	)