from django.db import models

# Create your models here.
class Technology(models.Model):
    images=models.CharField(max_length=50)
    tachnology=models.CharField(max_length=50)
    description=models.CharField(max_length=500)
    def __str__(self):
        return self.tachnology


class ResumeTech(models.Model):
    images=models.CharField(max_length=50)
    tachnology=models.CharField(max_length=50)
    title=models.CharField(max_length=100)
    side_show=models.CharField(max_length=5)
    working_timeline=models.CharField(max_length=20)
    def __str__(self):
        return self.working_timeline



class Project(models.Model):
    project_name=models.CharField(max_length=50)
    delay_time=models.CharField(max_length=50)
    images=models.ImageField(upload_to='projects/photo/')
    filter_id=models.CharField(max_length=20, blank=True)
    def __str__(self):
        return self.project_name




class Review(models.Model):
    customer_name=models.CharField(max_length=50)
    description=models.CharField(max_length=50)
    images=models.ImageField(upload_to='projects/photo/')
    profession=models.CharField(max_length=20, blank=True)
    def __str__(self):
        return self.customer_name





class Blog(models.Model):
    writer_name=models.CharField(max_length=50)
    description=models.CharField(max_length=500)
    image=models.ImageField(upload_to='projects/photo/')
    profession=models.CharField(max_length=20, blank=True)
    blog_name=models.CharField(max_length=50, blank=True)
    date_of_post=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.writer_name
