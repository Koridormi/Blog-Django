from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.post_list, name = 'post_list'),
    path('create/', views.post_create, name = 'post_create'),
    path('<int:pk>/', views.post_detail, name = 'post_detail'),
    path('<int:pk>/editar/', views.post_update, name = 'post_update'),
    path('<int:pk>/eliminar/', views.post_delete, name = 'post_delete')
]