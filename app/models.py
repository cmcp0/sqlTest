# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Usuario(models.Model):
    id_usuario = models.AutoField(db_column='Id_Usuario', primary_key=True)  # Field name made lowercase.
    usuario = models.CharField(db_column='Usuario', unique=True, max_length=50)  # Field name made lowercase.
    clave = models.CharField(db_column='Clave', max_length=32)  # Field name made lowercase.
    estado = models.CharField(db_column='Estado', max_length=1)  # Field name made lowercase.

    class Meta:
        db_table = 'Usuario'
