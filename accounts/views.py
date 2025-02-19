from math import log
from django.shortcuts import redirect, render
from .forms import Signupform, ProfileForm, UserForm
from django.contrib.auth import authenticate,login
from .models import Profile

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = Signupform(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username,password=password)
            login(request,user)
            return redirect('/accounts/profile/')
    else:
        form = Signupform()
    return render(request,'registration/signup.html',{'form':form})


def profile(request):
    profile = Profile.objects.get(user=request.user)
    
    return render(request,'accounts/profile.html',{'profile':profile})


def profile_edit(request):
    if request.user.is_authenticated :
        if request.method == 'POST':
            userform = UserForm(request.POST,instance=request.user)
            profileform = ProfileForm(request.POST,request.FILES,instance=request.user.profile)
            if userform.is_valid() and profileform.is_valid():
                userform.save()
                profile = profileform.save(commit=False)
                profile.user = request.user
                profileform.save()
                return redirect('/accounts/profile')

        else:
            userform = UserForm(instance=request.user)
            profileform = ProfileForm(instance=request.user.profile)

        context = {'userform':userform,'profileform':profileform}
        return render(request,'accounts/profile_edit.html',context)
    else:
        return redirect('login')
