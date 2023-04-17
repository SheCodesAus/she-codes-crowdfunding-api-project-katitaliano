from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from rest_framework import status, generics, permissions

from .models import Project, Pledge
from .serializers import ProjectSerializer, PledgeSerializer, ProjectDetailSerializer
from .permissions import IsOwnerOrReadOnly

class ProjectList(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def get(self, request):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(
                    serializer.data,
                    status=status.HTTP_201_CREATED)
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST)


class ProjectDetail(APIView):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,  # Authorization: user must be authenticated, or request must be read-only
        IsOwnerOrReadOnly  # Authorization: user must be the owner of the project, or request must be read-only
    ]

    # Helper method to get the project object based on the provided primary key (pk)
    def get_object(self, pk):
        try:
            project = Project.objects.get(pk=pk)  # Fetch the project object from the database
            self.check_object_permissions(self.request, project)  # Check object-level permissions
            return project
        except Project.DoesNotExist:
            raise Http404  # Raise HTTP 404 error if the project does not exist

    # Handles HTTP GET request
    def get(self, request, pk):
        project = self.get_object(pk)  # Fetch the project object
        serializer = ProjectDetailSerializer(project)  # Serialize the project object
        return Response(serializer.data)  # Return serialized data as response

    # Handles HTTP PUT request
    def put(self, request, pk):
        project = self.get_object(pk)  # Fetch the project object
        data = request.data  # Get data from request
        serializer = ProjectDetailSerializer(
            instance=project,  # Use the fetched project object as instance
            data=data,  # Use the request data as data
            partial=True  # Allow partial updates
        )
        if serializer.is_valid():  # Check if serializer data is valid
            serializer.save()  # Save the updated object
            return Response(serializer.data)  # Return serialized data as response
        return Response(serializer.errors)  # Return serializer errors as response
    
    # Handles HTTP DELETE request
    def delete(self, request, pk):
        project = self.get_object(pk)  # Fetch the project object
        project.delete()  # Delete the project object
        return Response(status=status.HTTP_204_NO_CONTENT)  # Return HTTP 204 No Content response

class PledgeList(generics.ListCreateAPIView):
    queryset = Pledge.objects.all()
    serializer_class = PledgeSerializer

    def perform_create(self, serializer):
        serializer.save(supporter=self.request.user)

class PledgeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pledge.objects.all()
    serializer_class = PledgeSerializer
    permission_classes = (IsOwnerOrReadOnly,)

# class PledgeDetail(generics.RetrieveUpdateDestroyAPIView):
# this will be for editing/deleting pledges
