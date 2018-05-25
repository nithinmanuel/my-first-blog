from django.db import models
from django.utils import timezone


class Post(models.Model):
	author = models.ForeignKey('auth.User', on_delete=models.CASCADE) # the idea is we have attributies in the left and rught side we have the models.data type
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def _str_(self):
		   return self.title  

# Create your models here., in the model we just create model with attributes , the entries are here author,title, text are the attributes., the model named post should be like this 