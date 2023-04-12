"""softdesk URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from projects.views import ProjectsAPIView, ProjectsDetailAPIView, ContributorsAPIView, \
    IssuesAPIView, CommentsAPIView, CommentsDetailAPIView
from users.views import MyObtainTokenPairView, SignupAPIView

app_name = "project"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("signup/", SignupAPIView.as_view()),
    path("login/", MyObtainTokenPairView.as_view()),
    path("projects/", ProjectsAPIView.as_view()),
    path("projects/<int:project_pk>/", ProjectsDetailAPIView.as_view()),
    path("projects/<int:project_pk>/users/", ContributorsAPIView.as_view()),
    path("projects/<int:project_pk>/users/<int:user_pk>/", ContributorsAPIView.as_view()),
    path("projects/<int:project_pk>/issues/", IssuesAPIView.as_view()),
    path("projects/<int:project_pk>/issues/<int:issue_pk>/", IssuesAPIView.as_view()),
    path("projects/<int:project_pk>/issues/<int:issue_pk>/comments/", CommentsAPIView.as_view()),
    path("projects/<int:project_pk>/issues/<int:issue_pk>/comments/<int:comment_pk>/", CommentsDetailAPIView.as_view()),
]
