from django.db import models

# Create your models here.
class categorie(models.Model):
    nom= models.CharField(max_length=30)
    url=models.URLField(max_length=40, default="admin@default.com")
   
    
    
    def __str__(self):
        return self.nom

class todo(models.Model):
    titre= models.CharField(max_length=30)
    detail= models.CharField(max_length=30)
    has_been_done =models.CharField(default=False)
    date_creation = models.DateField(auto_now_add=True)
    date_completion = models.DateField(auto_now_add=True)
    deadline_date  = models.DateField(auto_now_add=True)
    catégorie = models.ForeignKey(categorie, on_delete=models.CASCADE)




    
    
    def __str__(self):
        return self.titre