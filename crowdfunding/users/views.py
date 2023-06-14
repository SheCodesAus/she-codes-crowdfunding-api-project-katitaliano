from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import CustomUser
from .serializers import CustomUserSerializer, ChangePasswordSerializer

class CustomUserList(APIView):
    """
    A view for handling list operations (GET and POST) on CustomUser objects.
    """

    def get(self, request):
        """
        Handles GET request to retrieve a list of all CustomUser objects.
        """
        users = CustomUser.objects.all()
        serializer = CustomUserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        """
        Handles POST request to create a new CustomUser object.
        """
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class CustomUserDetail(APIView):
    """
    A view for handling detail operations (GET) on CustomUser objects.
    """

    def get_object(self, pk):
        """
        Helper method to retrieve a CustomUser object by primary key (pk).
        """
        try:
            return CustomUser.objects.get(pk=pk)
        except CustomUser.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        """
        Handles GET request to retrieve details of a specific CustomUser object by primary key (pk).
        """
        user = self.get_object(pk)
        serializer = CustomUserSerializer(user)
        return Response(serializer.data)
    
    def put(self, request, pk):
        """
        Handles PUT request to update a specific CustomUser object by primary key (pk).
        """
        user = self.get_object(pk)
        serializer = CustomUserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, pk):
        """
        Handles DELETE request to delete a specific CustomUser object by primary key (pk).
        """
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ChangePasswordView(generics.UpdateAPIView):
    """
    A view for handling updating the password of a CustomUser object.
    """

    queryset = CustomUser.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = ChangePasswordSerializer

"""
    CustomUserList: Handles list operations (GET and POST) on CustomUser objects using the APIView class from Django REST framework. It defines get and post methods to handle GET and POST requests respectively, with appropriate serialization and error handling.

    CustomUserDetail: Handles detail operations (GET) on CustomUser objects using the APIView class from Django REST framework. It defines a get_object helper method to retrieve a CustomUser object by primary key (pk), and a get method to handle GET requests to retrieve details of a specific CustomUser object by primary key (pk).

    The put method handles the PUT request to update the details of a specific CustomUser object by primary key (pk). It first retrieves the CustomUser object using the get_object helper method, then validates and saves the updated data using the CustomUserSerializer. If the data is valid, it returns the serialized data in the response.

    The delete method handles the DELETE request to delete a specific CustomUser object by primary key (pk). It retrieves the CustomUser object using the get_object helper method, then calls the delete() method on the object to delete it from the database. It returns a response with HTTP status code 204 NO CONTENT to indicate a successful deletion.

    ChangePasswordView: Handles updating the password of a CustomUser object using the UpdateAPIView class from Django REST framework. It inherits from generics.UpdateAPIView, and specifies the queryset, permission classes, and serializer class to be used for updating the password of a CustomUser object.
"""