from django.shortcuts import render, redirect
from .models import CargaClientes  # Importe o modelo necessário, se houver

from django.shortcuts import render, redirect
from .models import CargaClientes


def criar_carga_clientes(request):
    if request.method == 'POST':
        bateria = request.POST.get('bateria')
        numeracao = request.POST.get('numeracao')
        contato = request.POST.get('contato')
        valor = request.POST.get('valor')
        cliente = request.POST.get('cliente')
        responsavel = request.POST.get('responsavel')

        # Salvar os dados diretamente no banco de dados
        carga_cliente = CargaClientes(
            bateria=bateria,
            numeracao=numeracao,
            contato=contato,
            valor=valor,
            cliente=cliente,
            responsavel=responsavel
        )
        carga_cliente.save()

        return redirect('carga_clientes_lista')  # Redireciona para a lista após salvar
    return render(request, 'carga_clientes_form.html')

from django.shortcuts import render

def baseView(request):
    return render(request, 'base.html')


from .models import Assistencia

def AssistenciaView(request):
    assistencias = Assistencia.objects.all()
    return render(request, 'assistencia_lista.html', {'assistencias': assistencias})


from .models import Emprestimos

def EmprestimosView(request):
    emprestimos = Emprestimos.objects.all()
    return render(request, 'emprestimos_lista.html', {'emprestimos': emprestimos})



from .models import GarantiaSeminova

def GarantiaSeminovaView(request):
    garantia = GarantiaSeminova.objects.all()
    return render(request, 'garantia_lista.html', {'emprestimos': garantia})

