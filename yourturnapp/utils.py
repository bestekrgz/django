from .models import Project, Tag
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def pagination_project(request, project_get, results):
    page = request.GET.get('page')

    paginator = Paginator(project_get, results)
    try:
        project_get = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        project_get = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        project_get = paginator.page(page)

    left_index = (int(page) - 4)
    if left_index < 1:
        left_index = 1

    right_index = (int(page) + 5)
    if right_index > paginator.num_pages + 1:
        right_index = paginator.num_pages + 1
    custom_range = range(left_index, right_index)

    return project_get, custom_range


def search_project(request):
    search_query = ''
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
    tags = Tag.objects.filter(name__icontains=search_query)
    project_get = Project.objects.distinct().filter(
        Q(title__icontains=search_query) | Q(description__icontains=search_query) |
        Q(project_owner__name__icontains=search_query) | Q(tags__in=tags))
    return project_get, search_query
