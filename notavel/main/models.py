from django.contrib.auth.password_validation import validate_password
from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm, PasswordInput


class Professor(models.Model):
    primeiro_nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=150)
    email = models.EmailField(max_length=180)
    senha = models.CharField(max_length=20, validators=[validate_password])
    def __str__(self):
        return self.primeiro_nome

    def __fullName__(self):
        return self.primeiro_nome + self.sobrenome


class Turma(models.Model):
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    aluno = models.ForeignKey(User, on_delete=models.CASCADE)
    materia = models.CharField(max_length=150)

class ProfessorForm(ModelForm):

    
    class Meta:
        model = Professor
        widgets = {
            'senha': PasswordInput()
        }
        help_text = {
            'senha': ("Colocar senha com nó minimo 8 caracteres"),
        }
        fields = ['primeiro_nome','sobrenome','email','senha']
