# from dataclasses import field
# from multiprocessing.sharedctypes import Value
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, FormView, UpdateView

from .models import Paciente, Cirurgia
from .forms import PacienteForm, CirurgiaForm, SalaEsperaCCForm, AntesInicisaoCForm, AntesUsuarioSSCForm
# from .models import Paciente


# Create your views here.


class IndexView(TemplateView):
    template_name = 'index.html'


# class BaseView(TemplateView):
#     template_name = 'base.html'

###################
class PacienteCreate(CreateView):
    form_class = PacienteForm
    # model = Paciente
    # fields = '__all__'
    # fields = ['nome', 'dataNascimento', 'nomeMae', 'prontuario', 'nomeMae']
    template_name = 'forms/form01.html'

    success_url = reverse_lazy('index')


class CirurgiaCreate(CreateView):
    form_class = CirurgiaForm
    # fields = '__all__'
    # fields = ['cirurgiaProposta', 'cirurgiaRealizada', 'salaCirugica',
    #           'dataCirurugia', 'modalidade', 'realizouQuimeoterapia', 'quantasSQ']
    template_name = 'forms/form02.html'

    success_url = reverse_lazy('index')


class SalaEsperaCCCreate(CreateView):
    form_class = SalaEsperaCCForm
    # fields = '__all__'

    # fields = ['pulseriaIdentificacao', 'jejum', 'inicioJ', 'triconomiaRealizada', 'realizouBanho', 'preparoIntestinal',
    #           'semProtese', 'sitioCirurgico', 'alergiasConhecidas', 'qualAC', 'riscoViaA', 'equipamentoDisponivelRVA', 'riscoPerdaSa', 'equipamentosAnestesiaTF', 'caixasInstrumentaisCPE', 'formularioIdentificacao', 'relatorioEnfermagem', 'fichaSinaisV', 'exameLaboratI', 'consentimentoCirurgico', 'consentimentoAnestesico', 'avaliaçaoPreA']
    template_name = 'forms/form03.html'

    success_url = reverse_lazy('index')


class AntesInicisaoCCreate(CreateView):
    form_class = AntesInicisaoCForm
    # fields = '__all__'
    # fields = ['pacienteCirurgiaAIC', 'todosProfissionaisCNF', 'cirurgiaoAnestesistaEEC', 'antibioticoProfilaticoAU', 'examesImagemD',
    #           'revisaoCirurgiaoECDP', 'qualRCECDP', 'revisaoAnestesistaAPERU', 'revisaoEnfermagemICEC', 'palcaBisturiP', 'equipamentoTestadoF']
    template_name = 'forms/form04.html'

    success_url = reverse_lazy('index')


class AntesUsuarioSSCCreate(CreateView):
    form_class = AntesUsuarioSSCForm
    fields = '__all__'
    # fields = ['pacienteCirurgiaAUSSC', 'instrumentaisAntes', 'compressasAntes', 'agulhasAntes', 'laminaBisturiAntes',
    #           'instrumentaisDepois', 'compressasDepois', 'agulhasDepois', 'laminaBisturiDepois', 'RegistoCompletoPIRLP', 'houveAglumPMEI', 'QualHAPMEI', 'altaConfirmadaAE']
    template_name = 'forms/form05.html'

    success_url = reverse_lazy('index')

# # def index(request):
# #     return HttpResponse("Hello, world. You're at the polls index.")


# # class DadosUsuarioCreateView(CreateView):
# #     model = DadosUsuario
# #     fields = ['nome', 'dataNascimento', 'prontuario', 'nomeMae',
# #               'cirurgiaProposta', 'cirurgiaRealizada', 'salaCirurgia', 'dataCirurugia', 'modalidade']
# #     template_name = 'forms/form01.html'

# #     success_url = reverse_lazy('index')


##############UPDATE##############################


class PacienteUpdate(UpdateView):
    model = Paciente
    # form_class = PacienteForm
    fields = '__all__'
    template_name = 'forms/form01.html'

    success_url = reverse_lazy('index')


class CirurgiaUpdate(UpdateView):
    model = Cirurgia
    fields = '__all__'
    template_name = 'forms/form02.html'

    success_url = reverse_lazy('index')


class SalaEsperaCCUpdate(UpdateView):
    form_class = SalaEsperaCCForm

    template_name = 'forms/form03.html'

    success_url = reverse_lazy('index')


class AntesInicisaoCUpdate(UpdateView):
    form_class = AntesInicisaoCForm
    template_name = 'forms/form04.html'

    success_url = reverse_lazy('index')


class AntesUsuarioSSCUpdate(UpdateView):
    form_class = AntesUsuarioSSCForm

    template_name = 'forms/form05.html'

    success_url = reverse_lazy('index')
