from django.db import models
from django.conf import settings


class Perfil(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL)
	fotografia = models.ImageField(upload_to="users/%Y/%m/%d", blank=True,  default="/userDefault.png")

	def __str__(self):
		return 'Perfil del usuario {} {}'.format(self.user.first_name, self.user.last_name)