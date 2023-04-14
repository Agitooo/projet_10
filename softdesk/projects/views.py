from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from projects.permissions import ProjectPermissions, ProjectDetailPermissions, ContributorPermissions, \
    IssuePermissions, CommentPermissions, CommentDetailPermissions

from projects.models import Project, Contributor, Issue, Comment

from projects.serializers import \
    ProjectListSerializer, ProjectDetailSerializer, ProjectInsertSerializer, ProjectUpdateSerializer, \
    ContributorListSerializer, ContributorInsertSerializer, \
    IssueListSerializer, IssueInsertSerializer, IssueUpdateSerializer, \
    CommentListSerializer, CommentDetailSerializer, CommentInsertSerializer, CommentUpdateSerializer


class ProjectsAPIView(APIView):
    permission_classes = [ProjectPermissions]

    def get(self, request):
        projects = Project.objects.filter(contributor_project__user=request.user).order_by('date_created')
        serializer = ProjectListSerializer(projects, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        author = request.user
        serializer = ProjectInsertSerializer(data={**request.data, 'author': author.id})
        if serializer.is_valid():
            project = serializer.save()
            # On ajoute le créateur à la liste des contributeurs automatiquement
            Contributor.objects.create(user=author, project=project, role="créateur")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProjectsDetailAPIView(APIView):
    permission_classes = [ProjectDetailPermissions]

    def get(self, request, project_pk):
        project = Project.objects.filter(pk=project_pk)
        serializer = ProjectDetailSerializer(project, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, project_pk):
        project = Project.objects.filter(pk=project_pk).first()
        serializer = ProjectUpdateSerializer(project, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, project_pk):
        project = Project.objects.filter(pk=project_pk)
        project.delete()
        return Response("Projet supprimé", status=status.HTTP_200_OK)


class ContributorsAPIView(APIView):
    permission_classes = [ContributorPermissions]

    def get(self, request, project_pk):
        contributors = Contributor.objects.filter(project=project_pk)
        serializer = ContributorListSerializer(contributors, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, project_pk):
        serializer = ContributorInsertSerializer(data={**request.data, 'project': project_pk})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, project_pk, user_pk):
        contributors = Contributor.objects.filter(project=project_pk, user=user_pk)
        contributors.delete()
        return Response("Contributeur supprimé", status=status.HTTP_200_OK)


class IssuesAPIView(APIView):
    permission_classes = [IssuePermissions]

    def get(self, request, project_pk):
        issues = Issue.objects.filter(project=project_pk)
        serializer = IssueListSerializer(issues, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, project_pk):
        auth = request.user
        serializer = IssueInsertSerializer(data={**request.data, 'project': project_pk, 'auth': auth.id})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, project_pk, issue_pk):
        issue = Issue.objects.filter(pk=issue_pk).first()
        serializer = IssueUpdateSerializer(issue, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, project_pk, issue_pk):
        issue = Issue.objects.filter(pk=issue_pk)
        issue.delete()
        return Response("Problème supprimé", status=status.HTTP_200_OK)


class CommentsAPIView(APIView):
    permission_classes = [CommentPermissions]

    def get(self, request, project_pk, issue_pk):
        comments = Comment.objects.filter(issue=issue_pk)
        serializer = CommentListSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, project_pk, issue_pk):
        data = {**request.data, 'author': request.user.id, 'issue': issue_pk}
        serializer = CommentInsertSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentsDetailAPIView(APIView):
    permission_classes = [CommentDetailPermissions]

    def get(self, request, project_pk, issue_pk, comment_pk):
        comment = Comment.objects.filter(pk=comment_pk)
        serializer = CommentDetailSerializer(comment, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, project_pk, issue_pk, comment_pk):
        comment = Comment.objects.filter(pk=comment_pk).first()
        data = {**request.data, 'author': comment.author.id, 'issue': issue_pk}
        serializer = CommentUpdateSerializer(comment, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, project_pk, issue_pk, comment_pk):
        comment = Comment.objects.filter(pk=comment_pk)
        comment.delete()
        return Response("Commentaire supprimé", status=status.HTTP_200_OK)

