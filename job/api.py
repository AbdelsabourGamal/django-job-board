# like views
from .models import Job
from .serializers import JobSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def job_list_api(request):
    jobs = Job.objects.all()
    data = JobSerializer(jobs, many=True).data
    return Response({'data':data})

@api_view(['GET'])
def job_detail_api(request,slug):
    jobs = Job.objects.get(slug=slug)
    data = JobSerializer(jobs).data
    return Response({'data':data})