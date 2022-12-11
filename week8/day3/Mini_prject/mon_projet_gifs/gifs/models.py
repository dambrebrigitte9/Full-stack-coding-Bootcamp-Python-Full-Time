from django.db import models

# Create your models here.
class gifs(models.Model):
    titre= models.CharField(max_length=30)
    url=models.URLField(max_length=40, default="admin@default.com")
    uploader_name =models.CharField(max_length=30)
    created_at = models.DateField(auto_now_add=True)

    
    
    def __str__(self):
        return self.titre

class catégorie(models.Model):
    nom= models.CharField(max_length=30)
    gif = models.ManyToManyField(gifs)

    def __str__(self):
        return self.nom

