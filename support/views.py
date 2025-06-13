#from django.shortcuts import render
#def index(request):
    #return render(request, 'services/index.html')
# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("Welcome to the Support page!")