from django.db import models
class CategoryModel(models.Model):
    category_name=models.CharField(max_length=200)
    
    def __str__(self) -> str:
        return self.category_name
   
