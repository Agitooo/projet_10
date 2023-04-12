from rest_framework.permissions import BasePermission

from projects.models import Project, Contributor, Issue, Comment


class ProjectPermissions(BasePermission):

    def has_permission(self, request, view):
        if request.method == 'POST':
            return True
        elif request.method == 'GET':
            # projects = Project.objects.filter(author=request.user)
            contributors = Project.objects.filter(contributor_project__user=request.user)
            if len(contributors) > 0:
                return True
            else:
                return False
        else:
            return False


class ProjectDetailPermissions(BasePermission):

    def has_permission(self, request, view):
        project_pk = view.kwargs['project_pk']
        project = Project.objects.get(pk=project_pk)
        if request.method in ['GET', 'PUT']:
            projects = Project.objects.filter(contributor_project__user=request.user)
            if project in projects:
                return True
            else:
                return False
        elif request.method == 'DELETE':
            if project.author == request.user:
                return True
            else:
                return False
        else:
            return False


class ContributorPermissions(BasePermission):

    def has_permission(self, request, view):
        project_pk = view.kwargs['project_pk']
        project = Project.objects.get(pk=project_pk)
        if request.method in ['GET', 'POST']:
            projects = Project.objects.filter(contributor_project__user=request.user)
            if project in projects:
                return True
            else:
                return False
        elif request.method == 'DELETE':
            if project.author == request.user:
                return True
            else:
                return False
        else:
            return False


class IssuePermissions(BasePermission):

    def has_permission(self, request, view):
        if request.method in ['GET', 'POST']:
            project_pk = view.kwargs['project_pk']
            project = Project.objects.get(pk=project_pk)
            projects = Project.objects.filter(contributor_project__user=request.user)
            if project in projects:
                return True
            else:
                return False
        elif request.method in ['DELETE', 'PUT']:
            issue_pk = view.kwargs['issue_pk']
            issue = Issue.objects.get(pk=issue_pk)
            if issue.auth == request.user:
                return True
            else:
                return False
        else:
            return False


class CommentPermissions(BasePermission):

    def has_permission(self, request, view):
        if request.method in ['GET', 'POST']:
            project_pk = view.kwargs['project_pk']
            project = Project.objects.get(pk=project_pk)
            projects = Project.objects.filter(contributor_project__user=request.user)
            if project in projects:
                return True
            else:
                return False
        else:
            return False


class CommentDetailPermissions(BasePermission):

    def has_permission(self, request, view):
        if request.method == 'GET':
            project_pk = view.kwargs['project_pk']
            project = Project.objects.get(pk=project_pk)
            projects = Project.objects.filter(contributor_project__user=request.user)
            if project in projects:
                return True
            else:
                return False
        elif request.method in ['DELETE', 'PUT']:
            comment_pk = view.kwargs['comment_pk']
            comment = Comment.objects.get(pk=comment_pk)
            if comment.author == request.user:
                return True
            else:
                return False
        else:
            return False
