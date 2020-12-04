from django.db import models


# Create your models here.
class Post(models.Model):
    blog_title = models.CharField(max_length=150)
    blog_date = models.DateTimeField()
    blog_text = models.TextField(max_length=300)
    blog_image = models.ImageField(upload_to='blog_image/')

    def get_summary(self):
        return self.blog_text[:70]
