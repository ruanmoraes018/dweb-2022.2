import requests
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from datetime import datetime
from .models import RotaViagem, DiaSemana
from .forms import RotaViagemForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Motorista, Passageiro, Custom, RotaViagem
from django.contrib import messages
from django.http.response import HttpResponse
from rolepermissions.roles import assign_role
from django.contrib.auth.hashers import make_password
import django
django.setup()


def cadastro_motorista(request):
    password = request.POST.get('senha')
    confirmar_senha = request.POST.get('confirmar_senha')
    if request.method == 'POST' and password == confirmar_senha:
        username = request.POST.get('username')
        nome_completo = request.POST.get('nome_completo')
        nome_preferencia = request.POST.get('nome_preferencia')
        cnh = request.POST.get('cnh')
        cpf = request.POST.get('cpf')
        telefone = request.POST.get('telefone')
        email = request.POST.get('email')
        placa = request.POST.get('placa')
        renavam = request.POST.get('renavam')
        chassi = request.POST.get('chassi')
        cep = request.POST.get('cep')
        logradouro = request.POST.get('logradouro')
        numero_residencia = request.POST.get('numero_residencia')
        bairro = request.POST.get('bairro')
        cidade = request.POST.get('cidade')
        estado = request.POST.get('estado')
        password = request.POST.get('senha')
        novo_user = Custom.objects.create_user(
            username=username,
            email=email,
            password=password,
            is_motorista=True)
        novo_motorista = Motorista(
            user=novo_user,
            username=username,
            email=email,
            password=make_password(password),
            nome_completo=nome_completo,
            nome_preferencia=nome_preferencia,
            cnh=cnh,
            cpf=cpf,
            telefone=telefone,
            placa=placa,
            renavam=renavam,
            chassi=chassi,
            cep=cep,
            logradouro=logradouro,
            numero_residencia=numero_residencia,
            bairro=bairro,
            cidade=cidade,
            estado=estado,)
        novo_motorista.save()
        assign_role(novo_motorista, 'motorista')
        messages.success(request, 'Cadastro realizado com sucesso!')
        return redirect(login_motorista)
    else:
        return render(request, 'cadastro_motoristas.html')


def cadastro_passageiro(request):
    password = request.POST.get('senha')
    confirmar_senha = request.POST.get('confirmar_senha')
    if request.method == 'POST' and password == confirmar_senha:
        username = request.POST.get('username')
        nome_completo = request.POST.get('nome_completo')
        nome_preferencia = request.POST.get('nome_preferencia')
        cpf = request.POST.get('cpf')
        telefone = request.POST.get('telefone')
        email = request.POST.get('email')
        cep = request.POST.get('cep')
        logradouro = request.POST.get('logradouro')
        numero_residencia = request.POST.get('numero_residencia')
        bairro = request.POST.get('bairro')
        cidade = request.POST.get('cidade')
        estado = request.POST.get('estado')
        password = request.POST.get('senha')
        novo_usuario = Custom.objects.create_user(
            username=username,
            email=email,
            password=password,
            is_passageiro=True)
        novo_passageiro = Passageiro(
            user=novo_usuario,
            username=username,
            email=email,
            password=make_password(password),
            nome_completo=nome_completo,
            nome_preferencia=nome_preferencia,
            cpf=cpf,
            telefone=telefone,
            cep=cep,
            logradouro=logradouro,
            numero_residencia=numero_residencia,
            bairro=bairro,
            cidade=cidade,
            estado=estado)
        novo_passageiro.save()
        assign_role(novo_passageiro, 'passageiro')
        messages.success(request, 'Cadastro realizado com sucesso!')
        return redirect(login_passageiro)
    else:
        return render(request, 'cadastro_usuarios.html')


def login_motorista(request):
    if request.method == "GET":
        return render(request, 'login_motorista.html')
    else:
        email = request.POST.get('email')
        password = request.POST.get('senha')
        user = authenticate(request, email=email, password=password,
                            backend='usuario.backends.MotoristaBackend')
        if user is not None:
            if user.is_active and hasattr(user, 'motorista'):
                login(request, user)
                return redirect(pagina_motorista)
            else:
                messages.add_message(request, messages.WARNING, 'Este usuário não é um motorista cadastrado.')
        else:
            messages.add_message(request, messages.ERROR, 'Email e senha inválidos.')
    return render(request, 'login_motorista.html')


def login_passageiro(request):
    if request.method == "GET":
        return render(request, 'login_usuario.html')
    else:
        email = request.POST.get('email')
        password = request.POST.get('senha')
        passageiro = authenticate(
            request, email=email, password=password, backend='usuario.backends.PassageiroBackend')
        if passageiro is not None:
            if passageiro.is_active and hasattr(passageiro, 'passageiro'):
                login(request, passageiro)
                return redirect(pagina_passageiro)
            else:
                messages.add_message(request, messages.WARNING, 'Este usuário não é um passageiro cadastrado.')
        else:
            messages.add_message(request, messages.ERROR, 'Email e senha inválidos.')
    return render(request, 'login_usuario.html')


@login_required(login_url='login/motorista')
def criar_rota(request):
    if request.method == 'POST':
        form = RotaViagemForm(request.POST)
        if form.is_valid():
            rota = form.save(commit=False)
            rota.motorista = request.user.motorista
            horario_ida_str = form.cleaned_data['horario_ida'].strftime(
                '%Y-%m-%dT%H:%M:%S%z')
            horario_ida = datetime.fromisoformat(horario_ida_str)
            rota.horario_ida = horario_ida
            rota.tipo_veiculo = request.POST.get('tipo_veiculo')
            rota.save()
            dias_semana = form.cleaned_data['dias_semana']
            for dia_nome in dias_semana:
                dia, _ = DiaSemana.objects.get_or_create(nome=dia_nome)
                rota.dias_semana.add(dia)
            messages.success(request, "Rota cadastrada com sucesso!")
            return redirect(lista_rotas)
    else:
        form = RotaViagemForm()
    return render(request, 'criar_rota.html', {'form': form})


@login_required(login_url='login/motorista')
def lista_rotas(request):
    rotas = RotaViagem.objects.filter(motorista=request.user.motorista)
    return render(request, 'lista_rotas.html', {'rotas': rotas})


@login_required(login_url='login/motorista')
def atualizar_rota(request, id):
    rota = get_object_or_404(RotaViagem, id=id)
    if request.method == 'POST':
        form = RotaViagemForm(request.POST or None,
                              request.FILES or None, instance=rota)
        if form.is_valid():
            rota = form.save(commit=False)
            rota.motorista = request.user.motorista
            horario_ida_str = form.cleaned_data['horario_ida'].strftime(
                '%Y-%m-%dT%H:%M:%S%z')
            horario_ida = datetime.fromisoformat(horario_ida_str)
            rota.horario_ida = horario_ida
            rota.tipo_veiculo = request.POST.get('tipo_veiculo')
            rota.save()
            dias_semana = form.cleaned_data['dias_semana']
            rota.dias_semana.clear()
            for dia_nome in dias_semana:
                dia, _ = DiaSemana.objects.get_or_create(nome=dia_nome)
                rota.dias_semana.add(dia)
            messages.success(request, "Rota atualizada com sucesso!")
            return redirect('lista_rotas')
    else:
        form = RotaViagemForm(instance=rota)
    return render(request, 'atualizar_rota.html', {'form': form, 'rota': rota})


@login_required(login_url='login/motorista')
def deletar_rota(request, id):
    rota = get_object_or_404(
        RotaViagem, pk=id, motorista=request.user.motorista)
    dias_em_comum = []
    for dia in rota.dias_semana.all():
        rotas_com_dia = RotaViagem.objects.filter(
            dias_semana=dia).exclude(pk=rota.pk)
        if rotas_com_dia.exists():
            dias_em_comum.append(dia)
    if request.method == 'POST':
        if 'confirmar' in request.POST:
            for dia in dias_em_comum:
                rota.dias_semana.remove(dia)
            rota.delete()
            messages.success(request, 'Rota deletada com sucesso.')
            return redirect('lista_rotas')
        else:
            return redirect('lista_rotas')
    else:
        context = {'rota': rota, 'dias_em_comum': dias_em_comum}
        return render(request, 'deletar_rota.html', context)


@login_required(login_url='login/motorista')
def menu_motorista(request):
    motorista = request.user.motorista
    rotas = RotaViagem.objects.filter(motorista=motorista)
    return render(request, 'menu_motorista.html', {'motorista': motorista, 'rotas': rotas})


@login_required(login_url='login/passageiro')
def menu_passageiro(request):
    passageiro = request.user.passageiro
    return render(request, 'menu_passageiro.html', {'passageiro': passageiro})


@login_required(login_url='login')
def logout_view(request):
    logout(request)
    return redirect(menu)


def portfolio(request):
    return render(request, 'portfolio.html')


def home(request):
    return render(request, 'home.html')


def menu(request):
    exibir_h3 = True
    return render(request, 'menu.html', {'exibir_h3': exibir_h3})


def pesquisa(request):
    if request.method == 'POST':
        origem = request.POST.get('end_inicial')
        destino = request.POST.get('end_final')
        api_key = '2inWVROkYfeGcxFvh3ueKhAjYeL7XPmG'
        dia_semana_nome = request.POST.get('dia_da_semana')
        dia_semana_obj = get_object_or_404(
            DiaSemana, nome__iexact=dia_semana_nome)
        rotas = RotaViagem.objects.filter(
            origem__icontains=origem,
            destino__icontains=destino,
            dias_semana=dia_semana_obj)
        for rota in rotas:
            origem_lat, origem_lng = obter_coordenadas(rota.origem, api_key)
            destino_lat, destino_lng = obter_coordenadas(rota.destino, api_key)
            if origem_lat is None or origem_lng is None or destino_lat is None or destino_lng is None:
                return JsonResponse({'error': 'Falha ao obter as coordenadas de origem e destino'})
            url = f'https://api.tomtom.com/routing/1/calculateRoute/{origem_lat},{origem_lng}:{destino_lat},{destino_lng}/json?key={api_key}'
            response = requests.get(url)
            try:
                data = response.json()
                if 'routes' in data and data['routes']:
                    route = data['routes'][0]
                    summary = route['summary']
                    distance = summary['lengthInMeters']
                    duration = summary['travelTimeInSeconds']
                    distancia_km = distance / 1000
                    duracao_horas = duration // 3600
                    duracao_minutos = (duration % 3600) // 60
                    rota.distancia_km = distancia_km
                    rota.duracao_horas = duracao_horas
                    rota.duracao_minutos = duracao_minutos
                    return redirect('resultados0', origem=origem, destino=destino)
                else:
                    return JsonResponse({'error': 'Falha ao calcular a rota'})
            except ValueError:
                return JsonResponse({'error': 'Erro ao processar a resposta da API'})
    return render(request, 'pesquisa.html')


def obter_coordenadas(endereco, api_key):
    url = f'https://api.tomtom.com/search/2/geocode/{endereco}.json?key={api_key}'
    response = requests.get(url)
    try:
        data = response.json()
        results = data.get('results', [])
        if results:
            result = results[0]
            position = result.get('position')
            lat = position.get('lat')
            lon = position.get('lon')
            return lat, lon
    except ValueError:
        pass
    return None, None


def calcular_rota(lat_origem, lng_origem, lat_destino, lng_destino, api_key):
    url = f'https://api.tomtom.com/routing/1/calculateRoute/{lat_origem},{lng_origem}:{lat_destino},{lng_destino}/json?key={api_key}'
    response = requests.get(url)
    try:
        data = response.json()
        if 'routes' in data and data['routes']:
            route = data['routes'][0]
            summary = route['summary']
            distance = summary['lengthInMeters']
            duration = summary['travelTimeInSeconds']
            distancia_km = round(distance / 1000, 2)
            duracao_horas = duration // 3600
            duracao_minutos = (duration % 3600) // 60
            return distancia_km, duracao_horas, duracao_minutos
        else:
            return None, None, None
    except ValueError:
        return None, None, None


def resultados0(request):
    origem = request.GET.get('end_inicial')
    destino = request.GET.get('end_final')
    dias_semana = request.GET.get('dia_da_semana')
    distancia_km = request.GET.get('distancia_km')
    duracao_horas = request.GET.get('duracao_horas')
    duracao_minutos = request.GET.get('duracao_minutos')
    api_key = '2inWVROkYfeGcxFvh3ueKhAjYeL7XPmG'
    lat_origem, lng_origem = obter_coordenadas(origem, api_key)
    lat_destino, lng_destino = obter_coordenadas(destino, api_key)
    distancia_km, duracao_horas, duracao_minutos = calcular_rota(
        lat_origem, lng_origem, lat_destino, lng_destino, api_key)
    if lat_origem is None or lng_origem is None or lat_destino is None or lng_destino is None:
        return JsonResponse({'error': 'Falha ao obter as coordenadas de origem e destino'})
    rotas = RotaViagem.objects.filter(
        origem__icontains=origem,
        destino__icontains=destino,
        dias_semana__nome=dias_semana)
    lat_origem = str(lat_origem).replace(',', '.')
    lng_origem = str(lng_origem).replace(',', '.')
    lat_destino = str(lat_destino).replace(',', '.')
    lng_destino = str(lng_destino).replace(',', '.')
    context = {
        'rotas': rotas,
        'distancia_km': distancia_km,
        'duracao_horas': duracao_horas,
        'duracao_minutos': duracao_minutos,
        'lat_origem': lat_origem,
        'lng_origem': lng_origem,
        'lat_destino': lat_destino,
        'lng_destino': lng_destino, }
    return render(request, 'resultados0.html', context)


def rotas_por_motorista(request, motorista_id):
    try:
        motorista = Motorista.objects.get(id=motorista_id)
        rotas = RotaViagem.objects.filter(motorista=motorista)
        context = {'rotas': rotas}
        return render(request, 'rotas.html', context)
    except Motorista.DoesNotExist:
        return render(request, 'erro.html')


@login_required(login_url='login/passageiro')
def resultados1(request):
    origem = request.GET.get('end_inicial')
    destino = request.GET.get('end_final')
    dias_semana = request.GET.get('dia_da_semana')
    api_key = '2inWVROkYfeGcxFvh3ueKhAjYeL7XPmG'
    passageiro = Passageiro.objects.get(user=request.user)
    nome_passageiro = passageiro.nome_preferencia
    rotas = RotaViagem.objects.filter(
        origem__icontains=origem,
        destino__icontains=destino,
        dias_semana__nome=dias_semana,)
    context = {'rotas': []}
    for rota in rotas:
        print(rota.origem, rota.destino)
        nome_motorista = rota.motorista.nome_preferencia
        nome_origem = rota.origem
        nome_destino = rota.destino
        hora_partida = rota.horario_ida
        valor_rota = rota.preco
        tipo_veiculo = rota.tipo_veiculo
        mensagem = f"Olá, {nome_motorista}. Me chamo {nome_passageiro}, gostaria de saber mais informações e meios de pagamento da rota: {nome_origem}/{nome_destino}, saindo às {hora_partida} e valor de R$ {valor_rota} de {tipo_veiculo}! Esta mensagem foi criada através da Aplicação TokenTravel!"
        phone_number = rota.motorista.telefone
        lat_origem, lng_origem = obter_coordenadas(origem, api_key)
        lat_destino, lng_destino = obter_coordenadas(destino, api_key)
        distancia_km, duracao_horas, duracao_minutos = calcular_rota(
            lat_origem, lng_origem, lat_destino, lng_destino, api_key)
        if lat_origem is None or lng_origem is None or lat_destino is None or lng_destino is None:
            return JsonResponse({'error': 'Falha ao obter as coordenadas de origem e destino'})
        lat_origem = str(lat_origem).replace(',', '.')
        lng_origem = str(lng_origem).replace(',', '.')
        lat_destino = str(lat_destino).replace(',', '.')
        lng_destino = str(lng_destino).replace(',', '.')
        context['rotas'].append({
            'rota': rota,
            'distancia_km': distancia_km,
            'duracao_horas': duracao_horas,
            'duracao_minutos': duracao_minutos,
            'phone_number': phone_number,
            'mensagem': mensagem,
            'lat_origem': lat_origem,
            'lng_origem': lng_origem,
            'lat_destino': lat_destino,
            'lng_destino': lng_destino, })
    if not context['rotas']:
        return render(request, 'resultados1.html')
    return render(request, 'resultados1.html', context)


@login_required(login_url='login/motorista')
def pagina_motorista(request):
    exibir_turu = True
    return render(request, 'pagina_motorista.html', {'exibir_turu': exibir_turu})


@login_required(login_url='login/passageiro')
def pagina_passageiro(request):
    exibir_foto = True
    return render(request, 'pagina_passageiro.html', {'exibir_foto': exibir_foto})
