from django.db import models
from froala_editor.fields import FroalaField

# Create your models here.
class UserBlog(models.Model):
    user = models.CharField(max_length=200,null=True)
    title = models.CharField(max_length=200,null=True)
    content = FroalaField()
    slug = models.SlugField(max_length=1000,null=True)
    image = models.ImageField(upload_to="blog/", null = True)
    created_at = models.DateTimeField(auto_now_add=True)
    upload_to = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.user
