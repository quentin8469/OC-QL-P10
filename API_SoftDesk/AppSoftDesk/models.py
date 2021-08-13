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

    title = models.CharField(max_length=150)
    description = models.CharField(max_length=150)
    type = models.CharField(max_length=7, choices=TYPE_CHOICES, default='Web')
    author_user_id = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'


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

    user_id = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    projet_id = models.ForeignKey(to=Projects, on_delete=models.CASCADE, blank=True, null=True)
    permission = models.CharField(max_length=50, choices=perm_list, default='restricted')
    role = models.CharField(max_length=150, choices=role_list, default="")

    class Meta:
        verbose_name = 'Contributor'
        verbose_name_plural = 'Contributors'


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

    title = models.CharField(max_length=150)
    description = models.CharField(max_length=150)
    tag = models.CharField(max_length=150, choices=TAG_CHOICES, default='')
    priority = models.CharField(max_length=150, choices=PRIORITY_CHOICES, default='')
    project_id = models.ForeignKey(to=Projects, on_delete=models.CASCADE, blank=True, null=True)
    status = models.CharField(max_length=150, choices=STATUS_CHOICES, default='')
    author_user_id = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='author_id',
                                       blank=True, null=True)
    assignee_user_id = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                                         related_name='assignee_id', blank=True, null=True)
    created_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Issue'
        verbose_name_plural = 'Issues'


class Comments(models.Model):
    """
    Objet Comments
    """

    description = models.CharField(max_length=150)
    author_user_id = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    issue_id = models.ForeignKey(to=Issues, on_delete=models.CASCADE, blank=True, null=True)
    created_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

