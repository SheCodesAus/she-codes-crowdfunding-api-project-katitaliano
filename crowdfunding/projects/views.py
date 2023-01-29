from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from rest_framework import status, generics, permissions

from .models import Project, Pledge
from .serializers import ProjectSerializer, PledgeSerializer, ProjectDetailSerializer
from .permissions import IsOwnerOrReadOnly
from datetime import datetime, timedelta

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

    # def post(self, request):
    #     serializer = ProjectSerializer(data=request.data)
    #     if serializer.is_valid():
    #         start_date = datetime.now()
    #         end_date = datetime.now() - timedelta(days=365)
    #         projects_annual = Project.objects.filter(owner=request.user, date_created=range(start_date,end_date)).count()
    #         print(projects_annual)
    #         if  int(projects_annual) <3:
    #             serializer.save(owner=request.user)
    #             return Response(serializer.data, status=status.HTTP_201_CREATED)
    #         else:
    #             return Response(detail= "You have reached your project limit for the last year")
    #     return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)



class ProjectDetail(APIView):
    permission_classes = [
          permissions.IsAuthenticatedOrReadOnly,
          IsOwnerOrReadOnly
    ]

    def get_object(self, pk):
        try:
            project = Project.objects.get(pk=pk)
            self.check_object_permissions(self.request, project)
            return project
        except Project.DoesNotExist:
            raise Http404


    def get(self, request, pk):
        project = self.get_object(pk)
        serializer = ProjectDetailSerializer(project)
        return Response(serializer.data)

    def put(self, request, pk):
          project = self.get_object(pk)
          data = request.data
          serializer = ProjectDetailSerializer(
               instance=project,
               data=data,
                 partial=True
          )
          if serializer.is_valid():
               serializer.save()
               return Response(serializer.data)
          return Response(serializer.errors)


class PledgeList(generics.ListCreateAPIView):
    queryset = Pledge.objects.all()
    serializer_class = PledgeSerializer

    def perform_create(self, serializer):
        serializer.save(supporter=self.request.user)

# class PledgeDetail(generics.RetrieveUpdateDestroyAPIView):
# this will be for editing/deleting pledges
