from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from .utils import search_project, pagination_project
from django.contrib import messages
from django.core import paginator


def projects(request):
    project_get, search_query = search_project(request)
    project_get, custom_range = pagination_project(request, project_get, 6)
    context = {'projects': project_get, 'search_query': search_query, 'custom_range': custom_range}
    return render(request, 'yourturnapp/projects.html', context)


def project(request, pk):
    project_object = Project.objects.get(id=pk)
    form = ReviewForm()

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        review = form.save(commit=False)
        review.project = project_object
        review.owner = request.user.profile
        review.save()
        project_object.vote_count
        messages.success(request, 'Review submitted successfully!')
        return redirect('project', pk=project_object.id)
    context = {'project': project_object, 'form': form}
    return render(request, 'yourturnapp/single-project.html', context)


@login_required(login_url='login')
def create_project(request):
    profile = request.user.profile
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.project_owner = profile
            project.save()
            return redirect('account')
    context = {'form': form}
    return render(request, 'project_form.html', context)


@login_required(login_url='login')
def update_project(request, pk):
    profile = request.user.profile
    project_get = profile.project_set.get(id=pk)
    form = ProjectForm(instance=project_get)

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project_get)
        if form.is_valid():
            form.save()
            return redirect('account')
    context = {'form': form}
    return render(request, 'project_form.html', context)


@login_required(login_url='login')
def delete_project(request, pk):
    profile = request.user.profile
    project_get = profile.project_set.get(id=pk)
    if request.method == 'POST':
        project_get.delete()
        return redirect('account')
    context = {'object': project_get}
    return render(request, 'delete_template.html', context)
