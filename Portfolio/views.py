from django.shortcuts import render
from technology.models import Technology,ResumeTech,Project,Review,Blog
def index(request):
    technology=Technology.objects.all()
    resume_tech=ResumeTech.objects.all()
    projects=Project.objects.all()
    reviews=Review.objects.all()
    blogs=Blog.objects.all()
    context={
    'technology':technology,
    'resume_tech':resume_tech,
    'projects':projects,
    'reviews':reviews,
    'blogs':blogs,
    }
    return render(request,'index.html',context)
