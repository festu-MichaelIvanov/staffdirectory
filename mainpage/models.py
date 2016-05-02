from django.db import models

class StaffWorker(models.Model):
		WorkerName = models.CharField('Имя',max_length = 25)
		WorkerSecondName = models.CharField('Фамилия',max_length = 25)
		WorkerEmail = models.CharField('Почта',max_length = 25)
		WorkerMobile = models.CharField('Телефон',max_length = 25)
		WorkerPost = models.CharField('Должность',max_length = 25)
		
		def __str__(self):
			 return self.WorkerName + ' ' +self.WorkerSecondName