from django.urls import path

from . import views
from .views import SearchView
app_name = 'members'
urlpatterns=[
    path('',views.index,name='index'),
    path('detail/<int:id>/', views.detail, name='detail'),
    path('search/', SearchView.as_view(), name='search'),
    path('register/', views.register, name='register'),
    path('delete/<int:id>/',views.delete_member,name='delete'),
    path('update/<int:id>/',views.update_member, name='update')
]