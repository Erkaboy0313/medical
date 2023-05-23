from django.db import models

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=200,null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    image = models.ImageField(upload_to='news/',null=True,blank=True)

    class Meta:
        verbose_name_plural = 'News'

    def __str__(self):
        return self.title