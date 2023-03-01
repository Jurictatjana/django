from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=200)
    year = models.IntegerField()

#funkcija koja mijenja prikaz stringa na admin stranici
    def __str__(self):
        return f'{self.title} from {self.year}'