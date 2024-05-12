from django.urls import path
from . import views

urlpatterns = [
    path('', views.schedule, name ="schedule"),
    path('make/', views.make, name = 'make'),
    path('make/delete/<int:pk>', views.deleteData, name='delete'),
    path('make/update/<int:pk>', views.update, name = 'update'),
    path('search/', views.search_me, name ='search'),
]
