from django.shortcuts import render_to_response, get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.core.context_processors import csrf

from django.utils import timezone

from Site.models import Usuario
#from Site.models import ToUpload


# Create your views here.
def home(request):
	now = timezone.now()
	usuarios = Usuario.objects.all()
	return render_to_response('home.html', {"usuarios":usuarios}, context_instance=RequestContext(request))

def add_usuario(request):
	if request.method == 'POST': # If the form has been submitted...
		nome = request.POST.get('nome','')
		email = request.POST.get('email','')
		link = request.POST.get('link','')
		telefone = request.POST.get('telefone','')
		senha = request.POST.get('senha','')

		dados = Usuario(nome=nome,email=email,link=link,telefone=telefone,senha=senha)
		dados.save()
	return render_to_response('add_usuario.html', {}, context_instance=RequestContext(request))

def ver_usuario(request,id):
	usuario = Usuario.objects.get(id=id)
	editar = bool(request.GET.get("editar"))
	if request.method == 'POST': # If the form has been submitted...
		usuario.nome = request.POST.get('nome','')
		usuario.email = request.POST.get('email','')
		usuario.link = request.POST.get('link','')
		usuario.telefone = request.POST.get('telefone','')
		usuario.senha = request.POST.get('senha','')

		usuario.save()
		return HttpResponseRedirect("http://127.0.0.1:8000/FindJob/usuario/"+str(usuario.id)+"/?editar=")
	return render_to_response('update_usuario.html', {"usuario":usuario, "editar":editar}, context_instance=RequestContext(request))
	
def delete_usuario(request,id):
	usuario = Usuario.objects.get(id=id)
	usuario.delete()
	return HttpResponseRedirect("http://127.0.0.1:8000/FindJob/")
