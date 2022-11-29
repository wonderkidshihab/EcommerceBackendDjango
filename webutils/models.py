from django.db import models

# Create your models here.
class Story(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=250)
    description = models.TextField()
    image = models.ImageField(upload_to='./static/images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    footer_text = models.CharField(max_length=300)

    def __str__(self):
        return self.title
    