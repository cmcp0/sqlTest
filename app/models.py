from django.db import models

# Create your models here.

class Usuario(models.Model):
    """docstring for Usuario."""
    Id_Usuario = models.BigAutoField(primary_key=True)
    Token = models.CharField(max_length = 32)
    Nombre = models.CharField(max_length = 50)
    Usuario = models.CharField(max_length = 50)
    Clave = models.CharField(max_length = 32)
    Perfil = models.CharField(max_length = 2)
    Estado = models.CharField(max_length = 1)

    # def __init__(self, arg):
    #     super(Usuario, self).__init__()
    #     self.arg = arg
