from django.db import models




class Receipt(models.Model):
    title = models.CharField(max_length=200)
    start = models.DateTimeField(auto_now_add=True)
    end = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title