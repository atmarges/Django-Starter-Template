from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.shortcuts import reverse
# from django.utils.translation import ugettext_lazy as _

from .misc import get_date_dir


class User(AbstractUser):
    avatar = models.ImageField(upload_to=get_date_dir(pre='img/avatar/'),
                               default='img/avatar/avatar.jpg')

    class Meta:
        app_label = 'core'


# class Object(models.Model):

#     name = models.CharField(max_length=50)

#     class Meta:
#         verbose_name = _("object")
#         verbose_name_plural = _("objects")

#     def __str__(self):
#         return self.name

#     def get_absolute_url(self):
#         return reverse("object_detail", kwargs={"pk": self.pk})
