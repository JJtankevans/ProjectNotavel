from django.shortcuts import redirect, render
from .forms import RegisterForm
from .models import ProfessorForm



# Create your views here.
def cadastraAluno(response):

    
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
        
        return redirect('/admin')
    else:
        form = RegisterForm()

    return render(response, "main/cadastro.html", {"form" : form})


def cadastraProfessor(response):
    if response.method == "POST":
        pform = ProfessorForm(response.POST)
        if pform.is_valid():
            pform.save()
        return redirect('/admin')
    else:
        pform = ProfessorForm()

    return render(response, "main/cadastroProf.html", {"form": pform})