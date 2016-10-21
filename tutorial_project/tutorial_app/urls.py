from django.conf.urls.static import static
from django.confi import settings

urlpatterns = patterns('',
	# Examples:
	#url(r'^$','tuts718.views.home',name='home')
	#url(r'^blog/',include('blog.urls')),

	url(r'^admin/', include(admin.site.urls)),
	url('r^', include(TuTz718.urls)),
	)
)+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


from django.conf.urls import patterns, url 
from tutorial_app import views
urlpatterns = patterns('',
    url(r'^$', views.index, name='index'))
	url(r'^about/', views.about, name="about")