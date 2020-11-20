from django.urls import include, path
from . import views

urlpatterns = [
    path('welcome', views.welcome),
    path('libros', views.get_libros),
    path('libros/add', views.add_libro),
    path('libros/update/<int:libro_id>', views.update_libro),
    path('libros/delete/<int:libro_id>', views.delete_libro),
]
