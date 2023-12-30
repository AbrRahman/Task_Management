from django.db import models
from category.models import CategoryModel
class TaskModel(models.Model):
    task_title=models.CharField(max_length=200)
    task_description =models.CharField(max_length=300)
    category=models.ManyToManyField(CategoryModel)
    is_completed=models.BooleanField(default=False)
    task_assign_date=models.DateField()

    def __str__(self) -> str:
        return self.task_title
   

