# from dataclasses import field
# from multiprocessing.sharedctypes import Value
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from .models import PacienteCirurgia


# Create your views here.


class IndexView(TemplateView):
    template_name = 'index.html'


# class BaseView(TemplateView):
#     template_name = 'base.html'


class PacienteCirurgiaCreateView(CreateView):
    model = PacienteCirurgia
    fields = ['nome', 'dataNascimento', 'nomeMae', 'prontuario', 'nomeMae',
              'cirurgiaProposta', 'cirurgiaRealizada', 'salaCirugica', 'dataCirurugia', 'modalidade', 'realizouQuimeoterapia', 'quantasSQ']
    template_name = 'forms/form01.html'

    success_url = reverse_lazy('index')

# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")


# class DadosUsuarioCreateView(CreateView):
#     model = DadosUsuario
#     fields = ['nome', 'dataNascimento', 'prontuario', 'nomeMae',
#               'cirurgiaProposta', 'cirurgiaRealizada', 'salaCirurgia', 'dataCirurugia', 'modalidade']
#     template_name = 'forms/form01.html'

#     success_url = reverse_lazy('index')
