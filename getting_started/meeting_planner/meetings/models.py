from django.db import models


# represent table in db (obejts are the rows)
class Meeting(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
