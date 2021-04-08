from django.db import models

# Create your models here.

class Visita(models.Model):
    email = models.EmailField()
    timestamp_in = models.DateTimeField(auto_now_add=True)
    timestamp_out = models.DateTimeField(blank=True, null=True)
    comment = models.CharField(max_length=140, blank=True)

    def __str__(self):
        return self.email