from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import YourTurnAppSerializer
from yourturnapp.models import Project


@api_view(['GET'])
def get_route(request):
    route = [
        {'GET': '/api/yourturnapp'},
        {'GET': '/api/yourturnapp/id'},
        {'GET': '/api/yourturnapp/id/vote'},

        {'POST': '/api/users/token'},
        {'POST': '/api/users/token/refresh'},

    ]
    return Response(route)


@api_view(['GET'])
def get_projects(request):
    projects = Project.objects.all()
    serializer = YourTurnAppSerializer(projects, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_project(request, pk):
    project = Project.objects.get(id=pk)
    serializer = YourTurnAppSerializer(project, many=False)
    return Response(serializer.data)
