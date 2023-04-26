from django.views import generic
from .models import *


class IndexView(generic.ListView):
    template_name = "main/index.html"
    context_object_name = "produto"

    def get_queryset(self):
        return Produto.objects.all



#class DetailView(generic.DetailView):
#    template_name = "polls/detail.html"

