from django.db import models
from django.utils.timezone import now

# Create your models here.
class Post(models.Model):
    name =  models.CharField(max_length=30)
    description = models.TextField()
    pub_date = models.DateTimeField(default=now, editable=False)
    image = models.ImageField(upload_to='userImages')

