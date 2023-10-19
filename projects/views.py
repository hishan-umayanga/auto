from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Project
from .forms import ProjectForm



# Create your views here.

from django.http import HttpResponse



#create projects web page requesting function (this function will display projects html file store in template folder)
def projects(request):

    projects = Project.objects.all()
    context = {'projects':projects}
    return render(request, 'project/projects.html',context)

def project(request, pk):
    projectObj = Project.objects.get(id=pk)
    return render(request, 'project/single-project.html',{'project':projectObj})


#to create a project
@login_required(login_url="login")
def createProject(request):
    form = ProjectForm()

 #form data 

    if request.method == 'POST':
         form = ProjectForm(request.POST, request.FILES)
         if form.is_valid():
             form.save()
             return redirect('projects')

    context = {'form': form}
    return render(request, 'project/project_form.html', context)


#update the project
@login_required(login_url="login")
def updateProject(request, pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)

    if request.method == 'POST':
         form = ProjectForm(request.POST, request.FILES, instance=project)
         if form.is_valid():
             form.save()
             return redirect('projects')

    context = {'form': form}
    return render(request, 'project/project_form.html', context)


#delete the project
@login_required(login_url="login")
def deleteProject(request, pk):
    project = Project.objects.get(id = pk)
    if request.method == 'POST':
        project.delete()
        return redirect('projects')
    context = {'object': project}
    return render(request, 'project/delete_template.html', context)