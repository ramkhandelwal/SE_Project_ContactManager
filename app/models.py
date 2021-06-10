from django.db import models

# Create your models here.
from django.utils.timezone import datetime
from django.contrib.auth.models import User

class Contact(models.Model):
    manager = models.ForeignKey(User, on_delete=models.CASCADE,default=None,null = True , blank = True)
    name = models.CharField(max_length=20,null = True , blank = True)
    email = models.EmailField(max_length=100,null = True , blank = True)
    phone = models.IntegerField(null = True , blank = True)
    info = models.CharField(max_length=30,null = True , blank = True)
    gender = models.CharField(max_length=50, choices=(
        ('male', 'Male'),
        ('female', 'Female'),
    ))
    image = models.ImageField(upload_to='images/', blank=True,null = True)
    date_added = models.DateTimeField(default=datetime.now)

    def __str__(self):
        if(self.name):
            return self.name
        elif (self.email):
            return self.email
        elif (self.phone):
            return self.phone
        elif (self.info):
            return self.info
        elif(self.gender):
            return self.gender
        

    class Meta:
        ordering = ['-id']
