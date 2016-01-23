from django.db import models

# Create your models here.
# how the data in the data base is structured

class Join(models.Model):
    email = models.EmailField()
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "Hi %s " %(self.email)