from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from smarket import views

router = routers.DefaultRouter()

# baseUrl = 'api/'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuario', views.UsuarioList.as_view()),
    path('usuario/<int:pk>', views.UsuarioDetail.as_view()),
    path('tarefa', views.TarefaList.as_view()),
    path( 'tarefa/<int:pk>', views.TarefaDetail.as_view()),
    path('', include(router.urls)),
]


