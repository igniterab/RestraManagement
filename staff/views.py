from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import StaffUser
from .serialiser import StaffUserSerializer
from django.http import Http404



class StaffUserView(APIView):

    """
    List all StaffUser, or create a new StaffUser.
    """
    query = StaffUser.objects.all()
    serializer_class = StaffUserSerializer

    def get(self, request, format=None):
        serializer = self.serializer_class(self.query, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs): 
        serializer = self.serializer_class(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors)

        serializer.save()
        return Response(serializer.data)
