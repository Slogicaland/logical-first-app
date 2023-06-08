from django.db import models

class logical(models.Model):
     Searchbox = models.CharField(max_length=30)
     signup= models.CharField(max_length=30)
     login= models.CharField(max_length=30)
     createpass = models.CharField(max_length=30)
     confirmpass = models.CharField(max_length=30)