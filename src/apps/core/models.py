from django.db import models
from django.contrib.auth.models import AbstractUser

from .misc import get_date_dir


class User(AbstractUser):
    avatar = models.ImageField(upload_to=get_date_dir(pre='img/avatar/'),
                               default='img/avatar/avatar.jpg')

    class Meta:
        app_label = 'core'
