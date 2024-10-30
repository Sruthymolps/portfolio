from django import forms
from .models import Profile, Project, WorkExperience, Education, Certification

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['user','bio', 'skills', 'contact_details']

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'image', 'link']

class WorkExperienceForm(forms.ModelForm):
    class Meta:
        model = WorkExperience
        fields = ['job_title', 'company_name', 'start_date', 'end_date', 'description']

class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ['institution_name', 'degree', 'graduation_year']

class CertificationForm(forms.ModelForm):
    class Meta:
        model = Certification
        fields = ['title', 'issued_by', 'issue_date']
