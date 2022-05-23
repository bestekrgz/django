from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from .serializers import YourTurnAppSerializer
from yourturnapp.models import Project, Review


@api_view(['GET'])
def get_route(request):
    routes = [
        {'GET': '/api/yourturnapp'},
        {'GET': '/api/yourturnapp/id'},
        {'GET': '/api/yourturnapp/id/vote'},

        {'POST': '/api/users/token'},
        {'POST': '/api/users/token/refresh'},

    ]
    return Response(routes)


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


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def view_vote(request, pk):
    project = Project.objects.get(id=pk)
    user = request.user.profile
    data = request.data
    review, created = Review.objects.get_or_create(
        owner=user,
        project=project,

    )
    review.value = data['value']
    review.save()
    project.vote_count
    serializer = YourTurnAppSerializer(project, many=False)
    return Response(serializer.data)
