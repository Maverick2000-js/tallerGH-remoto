from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.listar_cuentas, name='listar_cuentas'),
    path('registrar_cuenta/', views.registrar_cuenta, name='registrar_cuenta'),
    path('eliminar_cuenta/<int:id>/', views.eliminar_cuenta, name='eliminar_cuenta'),
    path('actualizar_cuenta/<int:id>/', views.actualizar_cuenta, name='actualizar_cuenta'),
]

