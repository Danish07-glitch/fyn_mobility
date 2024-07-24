
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Component, Vehicle, Issue
from .serializers import ComponentSerializer, VehicleSerializer, IssueSerializer



@api_view(['POST'])
def addComponent(request):
    data=request.data
    serializer=ComponentSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)
    



