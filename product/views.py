#from django.http import HttpResponse
from django.shortcuts import render
from .models import MainContent

# Create your views here.
def index(request):
    content_list = MainContent.objects.order_by('-pub_date')
    context = {'content_list': content_list}
    return render(request, 'product/content_list.html', context)
    #return HttpResponse("Hello World")