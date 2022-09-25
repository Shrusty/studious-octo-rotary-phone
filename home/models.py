from django.db import models

# Create your models here.
class Contact(models.Model):
    name= models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    phone=models.CharField(max_length=12)
    desc=models.TextField()
    date=models.DateField()

    def __str__(self):
        return self.email

#
class Post(models.Model):
    sno=models.AutoField(primary_key=True)
    title= models.CharField(max_length=250)

    db_image= models.ImageField(null=True, blank=True, upload_to="db_image/")
    slug= models.CharField(max_length=120)
    contents=models.TextField()

    def __str__(self):
        return self.title   