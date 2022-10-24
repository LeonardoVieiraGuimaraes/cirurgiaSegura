from django.urls import path


from .views import IndexView, PacienteCirurgiaCreateView, SalaEsperaCCCreateView, AntesInicisaoCCreateView, AntesUsuarioSSCCreateView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    # path('cadastrar/', BaseView.as_view(), name='base'),
    path('cadastrar/PacienteCirurgia/',
         PacienteCirurgiaCreateView.as_view(), name='PacienteCirurgia'),
    path('cadastrar/SalaEsperaCC/',
         SalaEsperaCCCreateView.as_view(), name='SalaEsperaCC'),
    path('cadastrar/AntesInicisaoC/',
         AntesInicisaoCCreateView.as_view(), name='AntesInicisaoC'),
    path('cadastrar/AntesUsuarioSSC/',
         AntesUsuarioSSCCreateView.as_view(), name='AntesUsuarioSSC'),

]
