from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DetailView

from .models import HelloWorld
from django.urls import reverse, reverse_lazy


# Create your views here.
def hello(request):
    if request.method == "POST":

        temp = request.POST.get("hello_world_input")
        new_hello_world = HelloWorld()
        new_hello_world.text = temp
        new_hello_world.save()

        return HttpResponseRedirect(reverse("account:hello"))
    else:
        hello_world_list = HelloWorld.objects.all()
        return render(request, "acc/hello.html", context={'hello_world_list': hello_world_list})


class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy("account:hello")
    template_name = "acc/create.html"


class AccountDetailView(DetailView):
    model = User
    context_object_name = 'target_user'
    template_name ="acc/detail.html"
