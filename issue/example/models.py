from django.db import models


class IssueModel(models.Model):
    title = models.CharField(max_length=10)
    file = models.FileField(blank=True, null=True)
