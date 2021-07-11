from django.db import models

# Create your models here.

class Post(models.Model):
	blog_title = models.CharField(max_length=300)
	blog_date = models.DateTimeField(auto_now=False, auto_now_add=False)
	blog_text = models.TextField(max_length=300)
	blog_image = models.ImageField(upload_to='blog_images/')
	