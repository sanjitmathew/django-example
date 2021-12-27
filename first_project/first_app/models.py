from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserInfo(models.Model):
    """ Information about the User """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pic = models.ImageField(upload_to='pics', blank=True)

    def __str__(self):
        return self.user.username


class Topic(models.Model):
    """ Topic of the webiste """

    topic = models.CharField(max_length=264, unique=True)

    def __str__(self):
        return self.topic


class WebPage(models.Model):
    """ Details of the webpage """

    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    name = models.CharField(max_length=264, unique=True)
    url = models.URLField(unique=True)

    def __str__(self):
        return self.name


class AccessRecord(models.Model):
    """ Access details of the webpage """

    name = models.ForeignKey(WebPage, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return str(self.date)
