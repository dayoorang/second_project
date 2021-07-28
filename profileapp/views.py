from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from profileapp.forms import ProfileCreationForm
from profileapp.models import Profile


class ProfileCreationView(CreateView):
    model = Profile
    form_class = ProfileCreationForm
    template_name = 'profileapp/create.html'
    success_url = reverse_lazy('first_app:hello_world')


    def form_valid(self, form): # 다 검증이 완료된후 실행되는 함수.. FBV 에서는 form.is_valid() 인듯..
        form.instance.user = self.request.user # form 안에 것들을 저장할 그때당시의 user / form.user X
        return super().form_valid(form)

class ProfileUpdateView(UpdateView):
    model = Profile
    form_class = ProfileCreationForm
    context_object_name = 'target_profile'
    success_url = reverse_lazy('first_app:hello_world')
    template_name = 'profileapp/update.html'
