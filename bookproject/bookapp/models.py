from django.db import models

# Create your models here.
class Book(models.Model):
    title=models.CharField(max_length=250)
    author=models.CharField(max_length=250)
    genre=models.CharField(max_length=250)
    publication_date=models.DateField()
    avilability=models.BooleanField(default=True)

    def __str__(self):
        return self.title