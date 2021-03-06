from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.views.generic.list import MultipleObjectMixin

from accountsapp.models import NewModel
from accountsapp.forms import AccountCreationForm
from articleapp.models import Article
from decorators import account_ownership_required


# @login_required
# def hello_world(request):
#     if request.method == 'POST':
#         temp = request.POST.get('input_text')
#         new_model = NewModel()
#         new_model.text = temp
#         new_model.save()
#
#         data_list = NewModel.objects.all()
#
#         return HttpResponseRedirect(reverse('first_app:hello_world'))
#     else:
#         data_list = NewModel.objects.all()
#
#         return render(request, 'accountsapp/hello_world.html',
#                       context={'data_list': data_list})


class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('articleapp:list')
    template_name = 'accountsapp/create.html'

class AccountDetailView(DetailView, MultipleObjectMixin):
    model = User
    context_object_name = 'target_user'
    template_name = 'accountsapp/detail.html'

    paginate_by = 20

    def get_context_data(self, **kwargs):
        article_list = Article.objects.filter(writer=self.object)
        return super().get_context_data(object_list=article_list,**kwargs)


has_ownership = [login_required, account_ownership_required]

@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountUpdateView(UpdateView):
    model = User
    form_class = AccountCreationForm
    context_object_name = 'target_user'
    success_url = reverse_lazy('articleapp:list')
    template_name = 'accountsapp/update.html'

    def get_success_url(self):
        return reverse('first_app:detail', kwargs= {'pk': self.object.pk})

@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('articleapp:list')
    template_name = 'accountsapp/delete.html'


