from django.db import models

class addEvent(models.Model):
    event_name=models.CharField(max_length=100)
    date=models.DateField()
    time=models.TimeField()
    location=models.CharField(max_length=100)
    image=models.ImageField(upload_to='eventImages', blank=True)
    is_liked=models.BooleanField(default=False)
    def __str__(self):
        return self.event_name