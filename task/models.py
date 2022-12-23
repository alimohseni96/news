from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class NewID(models.Model):
    new_id = models.CharField(max_length=255)

    def __str__(self):

        return f"{self.new_id}"


class New(models.Model):

    id_new = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    summary = models.CharField(max_length=255)
    date_published = models.DateTimeField()
    url = models.CharField(max_length=255)
    content_html = models.CharField(max_length=255)

    # author = models.CharField(max_length=255)
    # user = models.ForeignKey(User,on_delete= models.CASCADE)

    def __str__(self):

        return f"{self.title}"

