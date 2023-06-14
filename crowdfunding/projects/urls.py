from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    path('projects/', views.ProjectList.as_view(), name="project-list"),
    path('projects/<int:pk>/', views.ProjectDetail.as_view()),
    path('pledges/', views.PledgeList.as_view(), name="pledge-list"),
    path('pledges/<int:pk>/', views.PledgeDetail.as_view(), name='pledge-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
