from django.db import models

class NewRepairForm(models.Model):
    CATEGORIES = (
        ('SAW', 'chainsaw'),
        ('MWR', 'lawnmower'),
        ('WTR', 'weedeater'),
    )
    category = models.CharField(max_length=20, choices=CATEGORIES)
    description = models.CharField(max_length=100)
    serial_number = models.CharField(max_length=100)

    # def __str__(self):
    #     return self.first_name
