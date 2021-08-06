from django.db import models
from django.conf import settings


# Create your models here.


class Projects(models.Model):
    """
    Objet Projects
    """

    TYPE_CHOICES = [
        ('Web', 'Web'),
        ('iOS', 'iOS'),
        ('Android', 'Android')
    ]

    title = models.CharField(max_length=150, blank=False, null=False)
    description = models.CharField(max_length=150, blank=False, null=False)
    type = models.CharField(max_length=7, choices=TYPE_CHOICES, default='Web')
    author_user_id = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=False, null=False)
    created_time = models.DateTimeField(auto_now_add=True)


class Contributors(models.Model):
    """
    Objet Contributors
    """
    perm_list = [
        ("restricted", "Contributeur"),
        ("all", "Auteur"),
    ]

    role_list = [
        ("author", "Auteur"),
        ("responsable", "Responsable"),
        ("Contributor", "Contributeur"),
    ]

    user_id = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    projet_id = models.ForeignKey(to=Projects, on_delete=models.CASCADE)
    permission = models.CharField(max_length=50, choices=perm_list, blank=False, null=False, default='restricted')
    role = models.CharField(max_length=150, choices=role_list, default="")


class Issues(models.Model):
    """
    Objet Issues
    """
    TAG_CHOICES = [('Bug', 'Bug'),
                   ('Amelioration', 'Amelioration'),
                   ('Tâche', 'Tâche')
                   ]
    PRIORITY_CHOICES = [('Low', 'Faible'),
                        ('Middle', 'Moyenne'),
                        ('High', 'Elevée')
                        ]
    STATUS_CHOICES = [('En cours', 'En cours'),
                      ('Terminée', 'Terminée')
                      ]

    tile = models.CharField(max_length=150, blank=False, null=False)
    description = models.CharField(max_length=150, blank=False, null=False)
    tag = models.CharField(max_length=150, choices=TAG_CHOICES, default='')
    priority = models.CharField(max_length=150, choices=PRIORITY_CHOICES, default='')
    project_id = models.ForeignKey(to=Projects, on_delete=models.CASCADE)
    status = models.CharField(max_length=150, choices=STATUS_CHOICES, default='')
    author_user_id = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='author_id',
                                       null=False)
    assignee_user_id = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                                         related_name='assignee_id')
    created_time = models.DateTimeField(auto_now_add=True)


class Comments(models.Model):
    """
    Objet Comments
    """

    description = models.CharField(max_length=150)
    author_user_id = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=False, null=False)
    issue_id = models.ForeignKey(to=Issues, on_delete=models.CASCADE, blank=False, null=False)
    created_time = models.DateTimeField(auto_now_add=True)
