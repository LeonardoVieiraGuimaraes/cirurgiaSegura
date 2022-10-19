from django.urls import path

from .views import IndexView, BaseView, DadosUsuarioCreateView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('cadastrar/', BaseView.as_view(), name='form01'),
    path('cadastrar/usuario/', DadosUsuarioCreateView.as_view(), name='usuario'),
]
