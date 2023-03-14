from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return self.name
    
class Publisher(models.Model):
    Nombre = models.CharField(max_length=100)
    Direccion = models.CharField(max_length=200)
    Ciudad = models.CharField(max_length=100)
    Estado_o_Provincia = models.CharField(max_length=100)
    Pais = models.CharField(max_length=100)
    Website = models.URLField()

    def __str__(self):
        return self.Nombre


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher,on_delete=models.CASCADE)
    publication_date = models.DateField()
    def __str__(self):
        return self.title




    