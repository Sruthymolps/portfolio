from django.contrib import admin

# Register your models here.
from .models import Profile, Project, Education, WorkExperience, Certification



admin.site.register(Profile)
admin.site.register(Project)
admin.site.register(Education)
admin.site.register(WorkExperience)
admin.site.register(Certification)
