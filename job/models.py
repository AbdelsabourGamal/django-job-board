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
    #category = 
    experince = models.IntegerField(default=1)

    def __str__(self):
        return self.title

