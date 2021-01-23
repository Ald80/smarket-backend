from django.db import models

# Create your models here.
class Usuario(models.Model):
    nome = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nome

class Tarefa(models.Model):
    descricao = models.CharField(max_length=250)
    estado = models.BooleanField(default=False)
    user = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return "%s %s %s" % (self.descricao, self.estado, self.user)