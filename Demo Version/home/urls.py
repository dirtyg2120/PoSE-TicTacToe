from django.urls import path
from . import views

urlpatterns = [
	path('homepage', views.index, name='index'),
	path('news', views.newsPage, name='news'),
	path('downloads', views.downloadPage, name='downloads'),
	path('aboutus', views.aboutPage, name='about'),
	path('play', views.playPage, name='play'),
]