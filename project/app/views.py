from django.shortcuts import render
from .models import User
from django.http import JsonResponse

# Create your views here.
def home(request):
    return render(request, 'users/home.html')

def users(request):
    if request.method == 'POST':
        # Lógica para processar dados POST (se necessário)
        new_user = User()
        new_user.nome = request.POST.get('nome')
        new_user.idade = request.POST.get('idade')
        new_user.save()
        
        # Responda com sucesso para requisições AJAX
        return JsonResponse({'status': 'success'})
    else:
        # Lógica para solicitações GET
        # Pode ser apenas renderizar o template sem processar dados adicionais
        usuarios = {
            'usuarios': User.objects.all()
        }
        return render(request, 'users/listUrsers.html', usuarios)