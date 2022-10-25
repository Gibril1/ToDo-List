from django.urls import path
from . import views

urlpatterns = [
    path('', views.list, name='todo-home'),
    path('update/<int:pk>', views.update, name='todo-update'),
    path('delete/<int:pk>', views.delete, name='todo-delete'),
]