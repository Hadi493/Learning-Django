from django.utils import timezone # type: ignore
from django.db import models # type: ignore

# Create your models here.
class agentLists(models.Model):
    POSITIONS_TYPES = [
        ('NS', 'Network Security'),
        ('AS', 'Application Security'),
        ('IS', 'Incident Response'),
        ('IAM', 'Identity and Access Management'),
        ('CR', 'Cryptography'),
        ('CG', 'Compliance and Governance'),
        ('TI', 'Threat Intelligence'),
    ]

    name = models.CharField(max_length=20)
    profile_image = models.ImageField(upload_to='imgs/')
    age = models.IntegerField()
    positions = models.CharField(max_length=30, choices=POSITIONS_TYPES)
    date_added = models.DateTimeField(default=timezone.now)
    description = models.TextField(default='')


    def __str__(self):
        return self.name

