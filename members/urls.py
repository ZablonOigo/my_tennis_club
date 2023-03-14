from django.urls import path

from . import views
app_name = 'members'
urlpatterns=[
    path('',views.index,name='index'),
    path('detail/<int:id>/', views.detail, name='detail'),
    path('search', views.search, name='search'),
]