"""
URL configuration for loja_de_carros project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from carros.views import (
    criar_marca,
    deletar_carro,
    detalhes_carro,
    editar_carro,
    gerenciar_carros,
    lista_carros,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", lista_carros, name="lista_carros"),
    path("carro/<int:carro_id>/", detalhes_carro, name="detalhes_carro"),
    path("gerenciar_carros/", gerenciar_carros, name="gerenciar_carros"),
    path("editar_carro/<int:carro_id>/", editar_carro, name="editar_carro"),
    path("deletar_carro/<int:carro_id>/", deletar_carro, name="deletar_carro"),
    path("criar_marca/", criar_marca, name="criar_marca"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
