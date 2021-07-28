from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView

from profileapp.decorators import profile_ownership_required
from profileapp.forms import ProfileCreationForm
from profileapp.models import Profile


@method_decorator(login_required,'get')
@method_decorator(login_required,'post')
class ProfileCreationView(CreateView):
    model = Profile
    form_class = ProfileCreationForm
    template_name = 'profileapp/create.html'
    # success_url = reverse_lazy('first_app:hello_world')


    def form_valid(self, form): # 다 검증이 완료된후 실행되는 함수.. FBV 에서는 form.is_valid() 인듯..
        form.instance.user = self.request.user # form 안에 것들을 저장할 그때당시의 user / form.user X
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('first_app:detail', kwargs={'pk': self.object.user.pk})


@method_decorator(profile_ownership_required,'get')
@method_decorator(profile_ownership_required,'post')
class ProfileUpdateView(UpdateView):
    model = Profile
    form_class = ProfileCreationForm
    context_object_name = 'target_profile'
    # success_url = reverse_lazy('first_app:hello_world')
    template_name = 'profileapp/update.html'

    def get_success_url(self):
        return reverse('first_app:detail', kwargs={'pk':self.object.user.pk})
