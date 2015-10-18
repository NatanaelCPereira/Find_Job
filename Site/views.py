from django.shortcuts import render_to_response, get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.core.context_processors import csrf

from django.utils import timezone

#from Site.models import ToUpload


# Create your views here.
def home(request):
	now = timezone.now()
	#print now.today()
	#print now.month()
	#print now.day()
	#clientes = Cliente.objects.all()
	return render_to_response('home.html', {}, context_instance=RequestContext(request))