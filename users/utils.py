from .models import Profile, Skill
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def pagination_profiles(request, profile, results):
    page = request.GET.get('page')

    paginator = Paginator(profile, results)
    try:
        profile = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        profile = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        profile = paginator.page(page)

    left_index = (int(page) - 4)
    if left_index < 1:
        left_index = 1

    right_index = (int(page) + 5)
    if right_index > paginator.num_pages + 1:
        right_index = paginator.num_pages + 1
    custom_range = range(left_index, right_index)

    return profile, custom_range

def search_user(request):
    search_query = ''
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    skills = Skill.objects.filter(skill_name__icontains=search_query)

    profile = Profile.objects.distinct().filter(Q(name__icontains=search_query) | Q(username__icontains=search_query) |
                                                Q(location__icontains=search_query) | Q(skill__in=skills))
    return profile, search_query
