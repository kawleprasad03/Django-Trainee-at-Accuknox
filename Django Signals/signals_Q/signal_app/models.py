from django.db import models

# Create your models here.
class TestModel(models.Model):
    FirstName = models.CharField(max_length=100)
    LastName = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.FirstName + " " + self.LastName
    
    

