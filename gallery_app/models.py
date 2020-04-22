from django.db import models

# Create your models here.
class Picture_model(models.Model):
	CHOICES=[('Tulip','Tulip'),
	('Daffodil','Daffodil'),
	('Poppy','Poppy'),
	('Sunflower','Sunflower'),
	('Bluebell','Bluebell'),
	('Rose','Rose'),
	('Snowdrop','Snowdrop'),
	('Cherryblossom','Cherry blossom'),
	('Orchid','Orchid'),
	('Iris','Iris'),
	('Peony','Peony'),
	('Chrysanthemum','Chrysanthemum'),
	('Geranium','Geranium'),
	('Lily','Lily'),
	('Lotus','Lotus'),
	('Waterlily','Water lily'),
	('Dandelion','Dandelion'),
	('Hyacinth','Hyacinth'),
	('Daisy','Daisy'),
	('Crocus','Crocus'),
	]
	name = models.CharField(max_length=100, choices=CHOICES,default='None')
	image = models.ImageField(upload_to='images')

	class Meta:
		verbose_name_plural = "Picture_model"

	def __str__(self):
		return self.get_name_display(),str(self.image)

