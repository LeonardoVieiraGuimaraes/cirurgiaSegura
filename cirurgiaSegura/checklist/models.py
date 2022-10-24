from unittest.util import _MAX_LENGTH
from django.db import models


# Create your models here.


class PacienteCirurgia(models.Model):
    # Cadastro Paciente
    # Nome do Paciente
    nome = models.CharField(max_length=50)
    # Data de Nascimento Paciente
    dataNascimento = models.DateField()
    # Nome da Mãe do Paciente
    nomeMae = models.CharField(max_length=50)
    # Protuário do Paciente
    prontuario = models.CharField(max_length=15)
# Cadastro para Cirurgia
    # Cirurgia Proposta:
    cirurgiaProposta = models.CharField(max_length=50)
    # Cirurgia Realizada:
    cirurgiaRealizada = models.CharField(max_length=50)
    # Sala Cirurgica:
    salaCirugica = models.CharField(max_length=50)
    # Data da Cirurgia:
    dataCirurugia = models.DateField(max_length=10)
    # Modalidade ( ) Eletiva (  )Urgência
    modalidade = models.CharField(max_length=1)
    # Relizou Quimeoterapia : ( ) N ( ) S Quantas sessões
    realizouQuimeoterapia = models.CharField(max_length=1)
    quantasSQ = models.IntegerField()
    # Realizou Radioterapia: ( ) N ( ) S Quantas sessões:
    realizouRadioterapia = models.CharField(max_length=1)
    quantasRR = models.IntegerField()

    def __str__(self):
        return "{} ({})".format(self.nome, self.prontuario)

# SALA DE ESPERA DO CENTRO  CIRÚRGICO


class SalaEsperaCC(models.Model):

    pacienteCirurgiaSECC = models.ForeignKey(
        PacienteCirurgia, on_delete=models.CASCADE)

    # Usuário informa: pacienteInforma = models.CharField(max_length=50)
    # Pulseira de identificação  ( ) S  (  ) N
    pulseriaIdentificacao = models.CharField(max_length=1)
    # Jejum ( ) S - inicio ______ ( )  N
    jejum = models.CharField(max_length=1)
    inicioJ = models.TimeField()
    # Tricotomia realizada ( ) sim  ( ) não
    triconomiaRealizada = models.CharField(max_length=1)
    # Realizou o banho ( ) sim  ( ) não
    realizouBanho = models.CharField(max_length=1)
    # Preparo Intestinal  ( ) sim  ( )  não ( ) NA
    preparoIntestinal = models.CharField(max_length=1)
    # Sem prótese ( ) sim  ( ) não
    semProtese = models.CharField(max_length=1)
    # Sítio cirúrgico demarcado corretamente? (   ) N  (  ) S   (  ) NA
    sitioCirurgico = models.CharField(max_length=1)
    # Alergias conhecidas? (   )  N (  ) S Qual?
    alergiasConhecidas = models.CharField(max_length=1)
    qualAC = models.CharField(max_length=20)
    # Risco de via aérea difícil/bronco aspiração?   ( ) N (  ) S  há equipamento disponível?
    riscoViaA = models.CharField(max_length=1)
    equipamentoDisponivelRVA = models.IntegerField()
    # Risco de perda sanguínea > 500 mL ou 7mL/Kg em crianças? (    ) N  (   ) S
    riscoPerdaSa = models.CharField(max_length=1)

    # Equipamentos de anestesia testados e funcionante?
    # (    ) Carrinho de Anestesia   (   ) Monitorização          (   ) Suporte de O2
    # (    ) Baraka                  (   ) Circuito de anestesia  (   ) Laringoscópio
    equipamentosAnestesiaTF = models.CharField(max_length=15)
    # Caixas e instrumentais cirúrgicos presentes e estéreis?   (   ) S   (   ) N
    caixasInstrumentaisCPE = models.CharField(max_length=1)

# Prontuário
    # Formulário identificação    (   ) sim    (   ) não
    formularioIdentificacao = models.CharField(max_length=1)
    # Relatório  enfermagem     (   ) sim    (   ) não   (  ) NA
    relatorioEnfermagem = models.CharField(max_length=1)
    # Ficha de sinais vitais        (   ) sim    (   ) não   (  ) NA
    fichaSinaisV = models.CharField(max_length=1)
    # Exame: ( Laborat. Imagens)   (   ) sim    (   ) não
    exameLaboratI = models.CharField(max_length=1)
    # Consentimento  Cirúrgico  (   ) sim    (   ) não
    consentimentoCirurgico = models.CharField(max_length=1)
    # Consentimento  anestésico  (   ) sim    (   ) não
    consentimentoAnestesico = models.CharField(max_length=1)
    # Avaliação pré – anestésica   (   ) sim    (   ) não
    avaliaçaoPreA = models.CharField(max_length=1)

# ANTES DA INICISÃO CIRÚRGICA


class AntesInicisaoC(models.Model):
    pacienteCirurgiaAIC = models.ForeignKey(
        PacienteCirurgia, on_delete=models.CASCADE)

    # Todos os profissionais confirmam nome e função?  (  ) N  (  ) S
    todosProfissionaisCNF = models.CharField(max_length=1)
    # O cirurgião, anestesista e equipe de enfermagem confirmam:
    #   (  ) identificação do paciente  (  ) sitio cirúrgico (  )  procedimento
    cirurgiaoAnestesistaEEC = models.CharField(max_length=15)
    # O antibiótico profilático foi administrado nos últimos 60 min?
    # (    ) NA    (   ) N   (   ) S   Hora:________:_______
    antibioticoProfilaticoAU = models.CharField(max_length=1)
    horaAPAU = models.TimeField()
    # Exames de imagem estão disponíveis? (    ) N   (    ) S
    examesImagemD = models.CharField(max_length=1)
# Antecipação de eventos críticos:
    # Revisão cirurgião: Há etapas críticas durante o procedimento?
    # (  ) N  (  ) S, qual?
    revisaoCirurgiaoECDP = models.CharField(max_length=1)
    qualRCECDP = models.CharField(max_length=15)
    # Revisão anestesista: Há alguma preocupação especifica em relação ao usuário?   (  ) N (  ) S, qual?
    revisaoAnestesistaAPERU = models.CharField(max_length=1)
    # Revisão da enfermagem: Instrumentais cirúrgicos estéreis e conferidos? (  ) N (  ) S
    revisaoEnfermagemICEC = models.CharField(max_length=1)
    # Placa de bisturi posicionado? (  ) N (  ) S (  ) NA
    palcaBisturiP = models.CharField(max_length=1)
    # Equipamento testado e funcionantes?  (  ) N  (  ) S
    equipamentoTestadoF = models.CharField(max_length=1)

    def __str__(self):
        return "{} ({})".format(self.nome, self.prontuario)


# ANTES DO USÚARIO SAIR DA SALA DE CIRÚRGIA  ( contagem )
class AntesUsuarioSSC(models.Model):
    pacienteCirurgiaAUSSC = models.ForeignKey(
        PacienteCirurgia, on_delete=models.CASCADE)

    # 	    Instrumentais Compressas Agulhas Lâmina de bisturi
    # ANTES			-         -         -           -
    # DEPOIS		-		  -         -           -
    instrumentaisAntes = models.IntegerField()
    compressasAntes = models.IntegerField()
    agulhasAntes = models.IntegerField()
    laminaBisturiAntes = models.IntegerField()
    instrumentaisDepois = models.IntegerField()
    compressasDepois = models.IntegerField()
    agulhasDepois = models.IntegerField()
    laminaBisturiDepois = models.IntegerField()
    # Registro completo do procedimento intraoperatório com registro no livro de procedimentos? (   ) S  (   ) N
    RegistoCompletoPIRLP = models.CharField(max_length=1)
    # Houve algum problema com materiais, equipamentos ou instrumentais?
    # (   ) S  (   ) N    Qual?
    houveAglumPMEI = models.CharField(max_length=1)
    QualHAPMEI = models.CharField(max_length=1)
    # Alta confirmada pelo anestesista e enfermagem para:
    # (   )  UTI        (   )  RPA         Hora:
    altaConfirmadaAE = models.CharField(max_length=1)

# class Order(models.Model):
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     email = models.EmailField()
#     address = models.CharField(max_length=250)
#     postal_code = models.CharField(max_length=20)
#     city = models.CharField(max_length=100)
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)
#     paid = models.BooleanField(default=False)


# CHOICES = [('item1', 'item 1'),
#            ('item2', 'item 2')]


# class OrderCreateForm(ModelForm):
#     postal_code = forms.ChoiceField(
#         choices=CHOICES, widget=forms.RadioSelect())

#     class Meta:
#         model = Order
#         fields = ['first_name', 'last_name', 'email',
#                   'address', 'postal_code', 'city']
