from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from accountsapp.models import NewModel
from accountsapp.templates.accountsapp.forms import AccountCreationForm

@login_required
def hello_world(request):
    if request.method == 'POST':
        temp = request.POST.get('input_text')
        new_model = NewModel()
        new_model.text = temp
        new_model.save()

        data_list = NewModel.objects.all()

        return HttpResponseRedirect(reverse('first_app:hello_world'))
    else:
        data_list = NewModel.objects.all()

        return render(request, 'accountsapp/hello_world.html',
                      context={'data_list': data_list})


class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('first_app:hello_world')
    template_name = 'accountsapp/create.html'

class AccountDetailView(DetailView):
    model = User
    context_object_name = 'target_user'
    template_name = 'accountsapp/detail.html'


@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class AccountUpdateView(UpdateView):
    model = User
    form_class = AccountCreationForm
    context_object_name = 'target_user'
    success_url = reverse_lazy('first_app:hello_world')
    template_name = 'accountsapp/update.html'

@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('first_app:hello_world')
    template_name = 'accountsapp/delete.html'


