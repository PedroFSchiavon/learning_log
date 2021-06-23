'''Define padrões de URL para learning_logs'''
from django.conf.urls import url
from . import views

urlpatterns = [
    # Página inicial
    url(r'^$', views.index, name='index'),

    # Mostra todos assuntos
    url(r'^topics/$', views.topics, name='topics'),
    # Página de um único assunto
    url(r'^topics/(?P<topic_id>\d+)$', views.topic, name='topic'),


]