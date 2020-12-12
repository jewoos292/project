from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView
from django.views.generic.list import MultipleObjectMixin

from articleapp.models import Article
from .decorators import account_ownership_required
from .forms import AccountUpdateForm
from .models import HelloWorld
from django.urls import reverse, reverse_lazy

has_ownership = [account_ownership_required, login_required]


# Create your views here.
@login_required
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


class AccountDetailView(DetailView, MultipleObjectMixin):
    model = User
    context_object_name = 'target_user'
    template_name = "acc/detail.html"
    paginate_by = 25

    def get_context_data(self, **kwargs):
        object_list = Article.objects.filter(writer=self.get_object())
        return super(AccountDetailView, self).get_context_data(object_list=object_list, **kwargs)


@method_decorator(has_ownership, "get")
@method_decorator(has_ownership, "post")
class AccountUpdateView(UpdateView):
    model = User
    form_class = AccountUpdateForm
    context_object_name = 'target_user'
    success_url = reverse_lazy("account:hello")
    template_name = "acc/update.html"


@method_decorator(has_ownership, "get")
@method_decorator(has_ownership, "post")
class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy("account:login")
    template_name = "acc/delete.html"
