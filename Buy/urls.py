from django.conf.urls import url
from django.urls import path
from Buy import views

urlpatterns = [
	path(r'',views.index,name='index'),
	path(r'match1/',views.match1,name='match1'),
	path(r'match2/',views.match2,name='match2'),
]
