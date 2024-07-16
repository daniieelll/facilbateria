
from django.shortcuts import render, redirect
from facil.models import Carga_clientes, Assistencia, Emprestimos, Seminova
from django.http import HttpResponse
from django.urls import reverse

def carga_cliente_view(request):
    if request.method == 'POST':
        cliente = request.POST['cliente']
        bateria = request.POST['bateria']
        numeracao_bateria = request.POST['numeracao_bateria']
        contato = request.POST['contato']
        valor = request.POST['valor']
        responsavel = request.POST.get('responsavel', '')

        Carga_clientes.objects.create(
            cliente=cliente,
            bateria=bateria,
            numeracao_bateria=numeracao_bateria,
            contato=contato,
            valor=valor,
            responsavel=responsavel
        )
        return redirect('carga_clientes')

    if 'toggle_resolvido' in request.GET:
        carga_id = request.GET['toggle_resolvido']
        carga = Carga_clientes.objects.get(id=carga_id)
        carga.resolvido = not carga.resolvido
        carga.save()
        return redirect('carga_clientes')

    query = request.GET.get('cliente')
    if query:
        cargas = Carga_clientes.objects.filter(cliente__icontains=query)
    else:
        cargas = Carga_clientes.objects.all()

    return render(request, 'carga_cliente.html', {'cargas': cargas})


def base_view(request):
    return render(request,'base.html')


def assistencia_view(request):
    if request.method == 'POST':
        cliente = request.POST.get('cliente')
        bateria = request.POST.get('bateria')
        numeracao_bateria = request.POST.get('numeracao_bateria')
        contato = request.POST.get('contato')
        responsavel = request.POST.get('responsavel')
        foto = request.FILES.get('foto')

        assistencia = Assistencia(
            cliente=cliente,
            bateria=bateria,
            numeracao_bateria=numeracao_bateria,
            contato=contato,
            responsavel=responsavel,
            foto=foto
        )
        assistencia.save()
        return redirect('assistencia')  # Redireciona para a mesma página após salvar

    if request.method == 'GET' and 'toggle_resolvido' in request.GET:
        assistencia_id = request.GET.get('toggle_resolvido')
        assistencia = Assistencia.objects.get(id=assistencia_id)
        assistencia.resolvido = not assistencia.resolvido
        assistencia.save()
        return redirect('assistencia')  # Redireciona para a mesma página após marcar como resolvido

    query = request.GET.get('query')
    if query:
        assistencias = Assistencia.objects.filter(cliente__icontains=query)
    else:
        assistencias = Assistencia.objects.all()

    return render(request, 'assistencia.html', {'assistencias': assistencias})



def Emprestimos_view(request):
    if request.method == 'POST':
        cliente = request.POST.get('cliente')
        contato = request.POST.get('contato')
        bateria = request.POST.get('bateria')
        numeracao_bateria = request.POST.get('numeracao_bateria')
        data_emprestimo = request.POST.get('data_emprestimo')
        data_devolucao = request.POST.get('data_devolucao')
        responsavel = request.POST.get('responsavel')

        emprestimos = Emprestimos(
            cliente=cliente,
            contato=contato,
            bateria=bateria,
            numeracao_bateria=numeracao_bateria,
            data_emprestimo=data_emprestimo,
            data_devolucao=data_devolucao,
            responsavel=responsavel
        )
        emprestimo.save()
        return redirect('emprestimos')  # Redireciona para a mesma página após salvar

    if request.method == 'GET' and 'toggle_resolvido' in request.GET:
        emprestimo_id = request.GET.get('toggle_resolvido')
        emprestimo = Emprestimos.objects.get(id=emprestimo_id)
        emprestimo.resolvido = not emprestimo.resolvido
        emprestimo.save()
        return redirect('emprestimos')  # Redireciona para a mesma página após marcar como resolvido

    query = request.GET.get('cliente')
    if query:
        emprestimos = Emprestimos.objects.filter(cliente__icontains=query)
    else:
        emprestimos = Emprestimos.objects.all()

    return render(request, 'emprestimos.html', {'emprestimos': emprestimos})


def garantia_Seminova_view(request):
    query = request.GET.get('cliente')
    if query:
        seminovas = Seminova.objects.filter(cliente__icontains=query)
    else:
        seminovas = Seminova.objects.all()

    if request.method == 'POST':
        cliente = request.POST.get('cliente')
        contato = request.POST.get('contato')
        bateria = request.POST.get('bateria')
        numeracao_bateria = request.POST.get('numeracao_bateria')
        garantia = request.POST.get('garantia')
        data_venda = request.POST.get('data_venda')
        responsavel = request.POST.get('responsavel')
        foto = request.FILES.get('foto')
        tab = request.POST.get('tab', 'seminova')

        Seminova.objects.create(
            cliente=cliente,
            contato=contato,
            bateria=bateria,
            numeracao_bateria=numeracao_bateria,
            garantia=garantia,
            data_venda=data_venda,
            foto=foto,
            responsavel=responsavel
        )
        return redirect(f"{reverse('garantia_seminovas')}?tab={tab}")

    # Lógica para alternar o campo resolvido
    if 'toggle_resolvido' in request.GET:
        seminova_id = request.GET['toggle_resolvido']
        seminova = Seminova.objects.get(id=seminova_id)
        seminova.resolvido = not seminova.resolvido
        seminova.save()
        return redirect(f"{reverse('garantia_seminovas')}?tab=seminova")

    return render(request, 'garantia_seminovas.html', {'seminovas': seminovas})



