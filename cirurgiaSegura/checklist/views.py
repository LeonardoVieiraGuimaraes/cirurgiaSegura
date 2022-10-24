# from dataclasses import field
# from multiprocessing.sharedctypes import Value
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from .models import PacienteCirurgia, SalaEsperaCC, AntesInicisaoC, AntesUsuarioSSC


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


class SalaEsperaCCCreateView(CreateView):
    model = SalaEsperaCC
    fields = ['pulseriaIdentificacao', 'jejum', 'inicioJ', 'triconomiaRealizada', 'realizouBanho', 'preparoIntestinal',
              'semProtese', 'sitioCirurgico', 'alergiasConhecidas', 'qualAC', 'riscoViaA', 'equipamentoDisponivelRVA', 'riscoPerdaSa', 'equipamentosAnestesiaTF', 'caixasInstrumentaisCPE', 'formularioIdentificacao', 'relatorioEnfermagem', 'fichaSinaisV', 'exameLaboratI', 'consentimentoCirurgico', 'consentimentoAnestesico', 'avaliaçaoPreA']
    template_name = 'forms/form02.html'

    success_url = reverse_lazy('index')


class AntesInicisaoCCreateView(CreateView):
    model = AntesInicisaoC
    fields = ['pacienteCirurgiaAIC', 'todosProfissionaisCNF', 'cirurgiaoAnestesistaEEC', 'antibioticoProfilaticoAU', 'examesImagemD',
              'revisaoCirurgiaoECDP', 'qualRCECDP', 'revisaoAnestesistaAPERU', 'revisaoEnfermagemICEC', 'palcaBisturiP', 'equipamentoTestadoF']
    template_name = 'forms/form03.html'

    success_url = reverse_lazy('index')


class AntesUsuarioSSCCreateView(CreateView):
    model = AntesUsuarioSSC
    fields = ['pacienteCirurgiaAUSSC', 'instrumentaisAntes', 'compressasAntes', 'agulhasAntes', 'laminaBisturiAntes',
              'instrumentaisDepois', 'compressasDepois', 'agulhasDepois', 'laminaBisturiDepois', 'RegistoCompletoPIRLP', 'houveAglumPMEI', 'QualHAPMEI', 'altaConfirmadaAE']
    template_name = 'forms/form04.html'

    success_url = reverse_lazy('index')

# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")


# class DadosUsuarioCreateView(CreateView):
#     model = DadosUsuario
#     fields = ['nome', 'dataNascimento', 'prontuario', 'nomeMae',
#               'cirurgiaProposta', 'cirurgiaRealizada', 'salaCirurgia', 'dataCirurugia', 'modalidade']
#     template_name = 'forms/form01.html'

#     success_url = reverse_lazy('index')
