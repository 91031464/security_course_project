from django.db import models

# Create your models here.

class About(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=2000)

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.title
