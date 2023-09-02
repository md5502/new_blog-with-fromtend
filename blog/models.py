from django.db import models
from django.contrib.auth.models import User
from user.models import UserProfile
import uuid

# Create your models here.
class Post(models.Model):
    PUBLISH_CH = (
        ('P', 'Published'),
        ('D', 'Draft')
    )
    title = models.CharField(max_length=200)
    body = models.TextField()
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    status = models.CharField(max_length=1, choices=PUBLISH_CH, default=PUBLISH_CH[1][1])
    tags = models.ManyToManyField('Tag', blank=True)
    image = models.ImageField(null=True, blank=True, upload_to='post-images', default='post-images/default.png')

    created = models.DateTimeField(auto_now_add=True)
    id = models.CharField(unique=True, primary_key=True, default=uuid.uuid4, editable=False, max_length=200)

    def __str__(self):
        return self.title
    

class Tag(models.Model):
    name=models.CharField(max_length=120, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.CharField(unique=True, primary_key=True, default=uuid.uuid4, editable=False, max_length=200)

    def __str__(self):
        return self.name

class Comment(models.Model):
    body = models.TextField()
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    id = models.CharField(unique=True, primary_key=True, default=uuid.uuid4, editable=False, max_length=200)

    def __str__(self):
        return str(self.body)

    