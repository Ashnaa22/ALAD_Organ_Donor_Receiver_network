from logging import PlaceHolder
from django.db import models




class HomePageBody(models.Model):
    id_vision = models.IntegerField(blank=True, null=True )
    title = models.CharField(blank=True, null=True, max_length=20)
    body_img = models.ImageField(upload_to='home_body')
    body_text = models.TextField(blank=True, null=True)
    

    def __str__(self):
        return self.title