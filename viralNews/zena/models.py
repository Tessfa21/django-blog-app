from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
class New(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    detail = models.TextField()
    image = models.ImageField(upload_to='news_images/', default='default.jpg')
    link = models.CharField(max_length=1000, default='')
    publisher = models.CharField(max_length=300, default='')
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()
    
    def __str__(self):
        return self.title




# class ABC(models.Model):
#     # f1
#     # f2

# model form 

