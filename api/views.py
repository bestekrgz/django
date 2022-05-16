from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response


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
