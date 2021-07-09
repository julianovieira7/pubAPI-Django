from django.db import models


class Estabelecimento(models.Model):
    def __init__(self, nome, latit, longit):
        self.nome = nome
        self.latit = latit
        self.longit = longit

    nome = models.CharField(max_length=100)
    latit = models.FloatField()
    longit = models.FloatField()


    def __repr__(self):
        return self.nome  + ", " +  str(self.latit) + " " + str(self.longit)
