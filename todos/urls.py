from django.urls import path
from . import views

app_name = 'todos'
urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<int:todo_pk>/', views.detail, name='detail'),
    path('create/', views.create, name='create'),
    path('update/<int:todo_pk>/', views.update, name='update'),
    path('delete/<int:todo_pk>/', views.delete, name='delete'),
    path('category/', views.category, name='category'),
]