from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('view/<int:my_id>', views.history, name="view"),
    path('delete/', views.delete, name="delete"),
    path('deleteData/<int:my_id>', views.delete_data, name="delete_data"),
    path('update/', views.update, name="update"),
    path('updateData/<int:my_id>', views.update_data, name="update_data"),
    path('about/', views.about, name='about'),
    # path('insert/', views.insert_data, name="insert"),
]
