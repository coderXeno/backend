from django.db import models

# Create your models here.
#model for first graph on landing page
class Todoentriesmodel(models.Model):
    id = models.IntegerField(primary_key=True)
    entry = models.CharField(max_length = 60)

    def __str__(self):
        return self.id
