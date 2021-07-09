from django.urls import path

from .views import *

urlpatterns = [
    path('estabelecimentos/<latitude>/<longitude>', EstabelecimentoList.as_view()),

]
