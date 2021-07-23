
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accountsapp.urls'))
    path('profiles/', include('profileapp.urls'))

]
