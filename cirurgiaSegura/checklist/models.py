from django.db import models


# Create your models here.

class DadosUsuario(models.Model):
    nome = models.CharField(max_length=50,  verbose_name='Nome')
    dataNascimento = models.DateField(verbose_name='Data de Nascimento')
    prontuario = models.CharField(max_length=50, verbose_name='Prontuário')
    nomeMae = models.CharField(max_length=50, verbose_name='Nome da Mãe')
    cirurgiaProposta = models.CharField(
        max_length=50, verbose_name='Cirúrgia Proposta')
    cirurgiaRealizada = models.CharField(
        max_length=50, verbose_name='Cirúrgia Realizada')
    salaCirurgia = models.CharField(
        max_length=50, verbose_name='Sala Cirúrgia')
    dataCirurugia = models.DateField(verbose_name='Data da Cirúrgia')

    modalidade = models.CharField(max_length=3)

    def __str__(self):
        return "{} ({})".format(self.nome, self.prontuario)


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
