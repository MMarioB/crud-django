from django.urls import path
from . import views

urlpatterns = [
    path('', views.EstudianteLista.as_view(), name='estudiante_list'),
    path('vista/<int:pk>', views.EstudianteDetalle.as_view(), name='estudiante_details'),
    path('nuevo', views.EstudianteCrear.as_view(), name='estudiante_new'),
    path('editar/<int:pk>', views.EstudianteModificar.as_view(), name='estudiante_edit'),
    path('borrar/<int:pk>', views.EstudianteBorrar.as_view(), name='estudiante_delete'),
]