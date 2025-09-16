# ticket_system/urls.py

from django.contrib import admin
from django.urls import path, include  # 'include' é a parte importante aqui

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Esta linha diz: "Qualquer URL que comece com 'api/' deve ser
    # gerenciada pelo arquivo de URLs do nosso app 'api'."
    path('api/', include('api.urls')),
]