from django.db import models

class sched(models.Model):
    scheduleId = models.AutoField(primary_key=True, editable=False)
    shipId = models.CharField(max_length=20, default='001')
    vessel = models.CharField(max_length=20, default='starhorse')
    origin = models.CharField(max_length=20, default="Lucena")
    destination = models.CharField(max_length=20, default="Marinduque")
    date = models.CharField(max_length=20, default='DD/MM/YYYY')
    time = models.CharField(max_length=10, default='12:00')
    seats = models.IntegerField(default=1)
    vehicles = models.IntegerField(default=1)
    price = models.IntegerField(default=0)
    status = models.CharField(max_length=20, default="open")
# Create your models here.
