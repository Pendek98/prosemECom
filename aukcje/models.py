from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class aukcja(models.Model):
    Nazwa = models.CharField(max_length=200)
    Cena_kt = models.DecimalField(max_digits=10,decimal_places=2)
    Cena_au = models.DecimalField(max_digits=10,decimal_places=2)
    Owner = models.ForeignKey(User,related_name='Owner',on_delete=models.CASCADE)
    Wygrywajacy = models.ForeignKey(User,on_delete=models.CASCADE)
    #Kategorie = [
    #    (Sport, 'Sport'),
    #    (Elektronika, 'Elektronika'),
   #]
   # Kat = models.CharField(max_length=200,choices=Kategorie,default=Sport,)
    Data_Zak = models.DateTimeField()
    ID = models.UUIDField(primary_key = True,editable = False)
    Opis = models.TextField(max_length=1000)
   # Zdjecie = models.ImageField()
    Zakonczona = models.BooleanField(default=False)