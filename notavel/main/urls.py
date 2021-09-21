from django.urls  import path

from . import views

urlpatterns = [
    path("", views.cadastraAluno, name="cadAluno"),
    path("professor/", views.cadastraProfessor, name="cadProfessor")
]