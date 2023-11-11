from django.shortcuts import render
from .models import User

# Create your views here.
def home(request):
    return render(request, 'users/home.html')

def users(request):
    #salva os dados da tela e enviar para o banco de dados
    usuario = User()
    new_user.nome = request.POST.get('nome')
    new_user.idade = request.POST.get('idade')
    new_user.save()

    #exibir todos os usuarios ja cadastrados em uma nova pagina
    usuarios = {
        'usuarios': User.objects.all()
    }

    #retornar o dados dos usuarios para a pagina de listagem de usuarios
    return render(request, 'users/listUrsers.html', usuarios)