from django.shortcuts import render

import job
from .models import Job
from django.core.paginator import Paginator
from .forms import Applyform, Addform
from django.contrib.auth.decorators import login_required
from .filters import JobFilter

# Create your views here.
def job_list(request):
    job_list = Job.objects.all()
    filter = JobFilter(request.GET, queryset=job_list)
    job_list = filter.qs

    paginator = Paginator(job_list, 3)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        'jobs':page_obj,
        'filter':filter
    }
    return render(request,'job/job_list.html',context)

@login_required
def job_detail(request,slug):
    job_detail = Job.objects.get(slug=slug)
    
    if request.method == 'POST':
        form = Applyform(request.POST,request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.job = job_detail
            form.save()
    else:
        form = Applyform()

    context = {
        'job':job_detail,
        'form':form,
    }
    return render(request,'job/job_detail.html',context)

@login_required
def add_job(request):
    if request.method == 'POST':
        form = Addform(request.POST,request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.owner = request.user 
            form.save()
    else:
        form = Addform()
    context = {'form':form}
    return render(request,'job/add_job.html',context)

