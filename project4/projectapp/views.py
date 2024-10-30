from django.shortcuts import render,redirect
from .models import Profile, Project, WorkExperience, Education, Certification
from .forms import ProfileForm, ProjectForm, WorkExperienceForm, EducationForm, CertificationForm

def home(request):
    profile=Profile.objects.all()
    project=Project.objects.all()
    work_experience =WorkExperience.objects.all()
    education= Education.objects.all()
    certification=Certification.objects.all()
    return render(request,'home.html',{'Profile':profile,'Project':project,'workExperience':work_experience ,'Education':education,'Certification':certification})











