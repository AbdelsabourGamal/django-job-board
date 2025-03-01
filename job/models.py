from django.db import models
from django.contrib.auth.models import User

# Create your models here.
job_type = (
    ('full time','full time'),
    ('part time','part time'),
)

def image_upload(instance,filename):
    imagename,exetention = filename.split('.')
    return "jobs/%s.%s"%(instance.id,exetention)

class Job(models.Model):
    def save(self,*args,**kwargs):
        self.slug = self.title
        super(Job,self).save(*args,**kwargs)

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    #location
    job_type = models.CharField(max_length=15,choices=job_type)
    description = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    category = models.ForeignKey('Catecory',on_delete=models.CASCADE)
    experince = models.IntegerField(default=1)
    image = models.ImageField(upload_to=image_upload)
    slug = models.SlugField(null=True,blank=True)

    def __str__(self):
        return self.title

class Catecory(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Apply(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    website = models.URLField()
    cv = models.FileField(upload_to='apply')
    cover_letter = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name