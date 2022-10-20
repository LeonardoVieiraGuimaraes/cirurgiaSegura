from django.urls import path


from .views import IndexView, PacienteCirurgiaCreateView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    # path('cadastrar/', BaseView.as_view(), name='base'),
    path('cadastrar/paciente_cirurgia/',
         PacienteCirurgiaCreateView.as_view(), name='paciente_cirurgia'),
]
