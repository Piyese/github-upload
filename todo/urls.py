from django.urls import path

from . import views

app_name='todo'
urlpatterns=[
    path('',views.home, name='home'),
    path('add/',views.add, name='add'),
    path('delete_item/<int:todo_id>/',views.delete_item, name='delete_item'),
    ]