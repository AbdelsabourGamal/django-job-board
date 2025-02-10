from django.db import models

# Create your models here.
job_type = (
    ('full time','full time'),
    ('part time','part time'),
)
class Job(models.Model):
    title = models.CharField(max_length=100)
    #location
    job_type = models.CharField(max_length=15,choices=job_type)
    description = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    category = models.ForeignKey('Catecory',on_delete=models.CASCADE)
    experince = models.IntegerField(default=1)

    def __str__(self):
        return self.title

class Catecory(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name