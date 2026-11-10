from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from .forms import CuentaForm

from .models import Cuenta

def listar_cuentas(request):
    cuentas = Cuenta.objects.all()
    return render(request, 'gestionCuentas.html', {'cuentas': cuentas})


def registrar_cuenta(request):
    if request.method == 'POST':
        v_tipocuenta = request.POST.get('txtTipoCuenta')
        v_descripcion = request.POST.get('txtDescripcion')
        v_saldo = request.POST.get('txtSaldo')
        
        Cuenta.objects.create(
            tipocuenta=v_tipocuenta,
            descripcion=v_descripcion,
            saldo=v_saldo
        )
    return redirect('listar_cuentas')


def eliminar_cuenta(request, id):

    cuenta = Cuenta.objects.get(id=id)

    cuenta.delete()
    return redirect('listar_cuentas')

def actualizar_cuenta(request, id):

    cuenta = get_object_or_404(Cuenta, id=id)

    if request.method == 'POST':
        formulario = CuentaForm(request.POST, instance=cuenta)

        if formulario.is_valid():
            formulario.save()
            return redirect('listar_cuentas')

    else:
        formulario = CuentaForm(instance=cuenta)

    return render(request, 'editarCuenta.html', {'formulario': formulario})
    

