from django.db import models
from django.utils.translation import ugettext_lazy as _
# Create your models here.

# From : Es quien envia la notificacion es un String
# To : Es a quien se envia la notificacion puede ser un usuario otra x cosa String
# type_notification : Es el tipo de notificacion, puede ser mensaje, compra o venta, etc., String
# message : Es la informacion que llevara el mensaje se recomienda que sea corta y precisa, String
# send_date : Es la fecha en que se envio la notificacion es tipo Date
# notification_status : Es para saber si el usuario ya visualizo la notificacion es un booleano
class Notification(models.Model):
	to = models.CharField(max_length=50, verbose_name=_('To'))
	_from = models.CharField(max_length=50, verbose_name=_('From'))
	activity = models.CharField(max_length=15, 
		verbose_name=_('Activity'))
	message = models.CharField(max_length=100, 
		verbose_name=_('Message'))
	title = models.CharField(max_length=20, 
		verbose_name=_('Title'))
	send_date = models.DateTimeField(auto_now=True)
	notification_status = models.BooleanField(verbose_name=_('Notification status'))
	class Meta:
		verbose_name = _('Message')
		verbose_name_plural = _('Messages')
	def __unicode__(self):
		return '%s: %s' %(self.title, self.message)

# user : Para identificar el usuario que se encuentra conectado, String
# status: Indica si el usuario se encuentra conectado o no, Boolean
# conexion_date : Indica el ultimo momento de conexion que tubo el usuario
class StatusUserNotification(models.Model):
	user = models.CharField(max_length=50, verbose_name=_('User'))
	status = models.BooleanField(verbose_name=_('Status'))
	conexion_date = models.DateTimeField(auto_now=True)
	class Meta:
		verbose_name = _('State')
		verbose_name_plural = _('Status')
	def __unicode__(self):
		return '%s' %(self.status)