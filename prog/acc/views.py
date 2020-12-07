from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


# Create your views here.
def hello(request):
    return render(request, "acc/hello.html")
