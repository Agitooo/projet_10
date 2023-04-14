from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from projects.models import Project, Contributor, Issue, Comment
from users.serializers import UserListSerializer


class ProjectListSerializer(ModelSerializer):
    author = UserListSerializer()

    class Meta:
        model = Project
        fields = [
            'id',
            'title',
            'author',
        ]


class ProjectInsertSerializer(ModelSerializer):

    class Meta:
        model = Project
        fields = [
            'id',
            'type',
            'title',
            'description',
            'author',
            'date_created',
            'date_updated',
        ]


class ProjectUpdateSerializer(ModelSerializer):

    class Meta:
        model = Project
        fields = [
            'id',
            'type',
            'title',
            'description',
            'date_created',
            'date_updated',
        ]


class ProjectDetailSerializer(ModelSerializer):
    author = UserListSerializer()

    class Meta:
        model = Project
        fields = [
            'id',
            'type',
            'title',
            'description',
            'author',
            'date_created',
            'date_updated',
        ]


class ContributorListSerializer(ModelSerializer):
    user = UserListSerializer()
    project = ProjectListSerializer()

    class Meta:
        model = Contributor
        fields = [
            'id',
            'user',
            'project',
            'role',
        ]


class ContributorInsertSerializer(ModelSerializer):

    class Meta:
        model = Contributor
        fields = [
            'id',
            'user',
            'project',
            'role',
        ]


class IssueListSerializer(ModelSerializer):
    auth = UserListSerializer()
    assignee = UserListSerializer()
    project = ProjectListSerializer()

    class Meta:
        model = Issue
        fields = [
            'id',
            'title',
            'desc',
            'tag',
            'priority',
            'project',
            'status',
            'auth',
            'assignee',
            'created_time',
        ]


class IssueInsertSerializer(ModelSerializer):

    class Meta:
        model = Issue
        fields = [
            'id',
            'title',
            'desc',
            'tag',
            'priority',
            'project',
            'status',
            'auth',
            'assignee',
            'created_time',
        ]


class IssueUpdateSerializer(ModelSerializer):

    class Meta:
        model = Issue
        fields = [
            'id',
            'title',
            'desc',
            'tag',
            'priority',
            'status',
            'assignee',
            'created_time',
        ]


class CommentListSerializer(ModelSerializer):
    author = UserListSerializer()
    issue = IssueListSerializer()

    class Meta:
        model = Comment
        fields = [
            'id',
            'description',
            'author',
            'issue',
            'created_time',
        ]


class CommentInsertSerializer(ModelSerializer):

    class Meta:
        model = Comment
        fields = [
            'id',
            'description',
            'author',
            'issue',
            'created_time',
        ]


class CommentUpdateSerializer(ModelSerializer):

    class Meta:
        model = Comment
        fields = [
            'id',
            'description',
            'author',
            'issue',
            'created_time',
        ]


class CommentDetailSerializer(ModelSerializer):
    author = UserListSerializer()
    issue = IssueListSerializer()

    class Meta:
        model = Comment
        fields = [
            'id',
            'description',
            'author',
            'issue',
            'created_time',
        ]
