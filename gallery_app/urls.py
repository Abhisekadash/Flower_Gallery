from django.urls import path
from . import views

urlpatterns=[
	path('',views.main_flower,name='main_flower'),
	path('main/<str:name>/',views.main,name='main'),
	path('upload/<str:name>',views.upload,name='upload'),
	path('remove/<int:images_id>/<str:name>',views.remove,name='remove'),
	path('fullimage/<int:images_id>',views.fullimage,name='fullsize'),
]