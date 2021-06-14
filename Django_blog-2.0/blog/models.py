from django.db import models
from django.contrib.auth.models import User


STATUS = (
    (0, "Draft"),
    (1, "Publish")
)


class Post(models.Model):
    
    title = models.CharField(max_length=200, unique=True)
    emp_image = models.ImageField(default='SOME STRING' ,upload_to='upload/')
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)


class Form(models.Model):
       contact = models.CharField(max_length=20)
       fname  = models.CharField(max_length=20)
       lname =  models.CharField(max_length=300)
       email=   models.EmailField()
       phone = models.IntegerField()
       iname = models.CharField(max_length=30)
       comment =  models.TextField(max_length=300)


       