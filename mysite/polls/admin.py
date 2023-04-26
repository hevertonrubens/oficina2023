from django.contrib import admin
from .models import Usuario
from .models import empreendedor 
from .models import produtos
from .models import loja

# Register your models here.
admin.site.register(Usuario)
admin.site.register(empreendedor)
admin.site.register(produtos)
admin.site.register(loja)
