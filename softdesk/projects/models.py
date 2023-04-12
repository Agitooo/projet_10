from django.conf import settings
from softdesk.settings import AUTH_USER_MODEL
from django.db import models
from django.contrib.auth.models import AbstractUser


class Project(models.Model):
    TYPE_BACK = 1
    TYPE_FRONT = 2
    TYPE_IOS = 3
    TYPE_ANDROID = 4

    TYPE = [
        (TYPE_BACK, 'back-end'),
        (TYPE_FRONT, 'front-end'),
        (TYPE_IOS, 'iOS'),
        (TYPE_ANDROID, 'Android'),
    ]

    title = models.CharField(max_length=128)
    description = models.TextField(max_length=2048)
    type = models.PositiveSmallIntegerField(choices=TYPE, default=TYPE_FRONT)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='project_author')
    objects = models.Manager()

    class Meta:
        verbose_name = "project"
        verbose_name_plural = "projects"

    def __str__(self):
        return self.title


class Contributor(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='contributor_user')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='contributor_project')
    # permission = models.ChoiceField() ??
    role = models.CharField(max_length=128)
    objects = models.Manager()

    class Meta:
        verbose_name = "contributeur"
        verbose_name_plural = "contributeurs"

    def __str__(self):
        return f"{self.user.last_name} {self.user.first_name} - {self.project.title} : {self.role}"


class Issue(models.Model):
    PRIORITY_LOW = 1
    PRIORITY_MEDIUM = 2
    PRIORITY_HIGH = 3

    PRIORITY = [
        (PRIORITY_LOW, 'faible'),
        (PRIORITY_MEDIUM, 'moyenne'),
        (PRIORITY_HIGH, 'haute'),
    ]

    STATUS_A_FAIRE = 1
    STATUS_EN_COURS = 2
    STATUS_TERMINE = 3

    STATUS = [
        (STATUS_A_FAIRE, 'a faire'),
        (STATUS_EN_COURS, 'en cours'),
        (STATUS_TERMINE, 'terminé'),
    ]

    TAG_BUG = 1
    TAG_AMELIORATION = 2
    TAG_TACHE = 3

    TAG = [
        (TAG_BUG, 'bug'),
        (TAG_AMELIORATION, 'amélioration'),
        (TAG_TACHE, 'tâche'),
    ]

    title = models.CharField(max_length=128)
    desc = models.CharField(max_length=2048)
    tag = models.SmallIntegerField(choices=TAG, default=TAG_BUG)
    priority = models.PositiveSmallIntegerField(choices=PRIORITY, default=PRIORITY_LOW)
    project = models.ForeignKey(Project, on_delete=models.DO_NOTHING, related_name='issue_project')
    status = models.SmallIntegerField(choices=STATUS, default=STATUS_A_FAIRE)
    auth = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='issue_author')
    assignee = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='issue_assigne')
    created_time = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

    class Meta:
        verbose_name = "issue"
        verbose_name_plural = "issues"

    def __str__(self):
        return f"{self.project.title} : {self.title} - {self.status}"


class Comment(models.Model):
    description = models.TextField(max_length=2048)
    author = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comment_author')
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE, related_name='comment_issue')
    created_time = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

    class Meta:
        verbose_name = "comment"
        verbose_name_plural = "comments"

    def __str__(self):
        return f"{self.issue.id} : {self.author.last_name} {self.author.first_name}"
