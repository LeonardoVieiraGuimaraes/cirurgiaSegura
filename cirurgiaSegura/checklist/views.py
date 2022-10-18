from django.views.generic import TemplateView

# Create your views here.
from django.http import HttpResponse


class IndexView(TemplateView):
    template_name = 'index.html'


# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")
