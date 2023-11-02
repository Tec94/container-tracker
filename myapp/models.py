from django.db import models

# Create your models here.

class Warehouse(models.Model):
    CONTAINER_STATUS = [
        ('IN', 'In Warehouse'),
        ('OUT', 'Out of Warehouse'),
    ]

    CONTAINER_LOCATION = [
        ('TX', 'Austin, Texas'),
        ('CA', 'San Francisco, California'),
        ('NY', 'New York City, New York'),
        ('IL', 'Chicago, Illinois'),
        ('WA', 'Seattle, Washington'),
        ('MA', 'Boston, Massachusetts'),
        ('GA', 'Atlanta, Georgia'),
        ('CO', 'Denver, Colorado'),
        ('FL', 'Miami, Florida'),
        ('DC', 'Washington, D.C.'),
        ('PA', 'Philadelphia, Pennsylvania'),
        ('AZ', 'Phoenix, Arizona'),
        ('MI', 'Detroit, Michigan'),
        ('OH', 'Columbus, Ohio'),
    ]

    container_id = models.CharField(max_length=5)
    container_status = models.CharField(max_length=3, choices=CONTAINER_STATUS)
    container_location = models.CharField(max_length=2, choices=CONTAINER_LOCATION)
    container_eta = models.DateField(default='Not Out of Warehouse')

