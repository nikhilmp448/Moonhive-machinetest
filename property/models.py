from django.db import models
from user.models import Account


class Property(models.Model):
    """
    Represents a real estate property.
    """
    name = models.CharField(max_length=255)
    address = models.TextField()
    location = models.CharField(max_length=255)
    features = models.TextField()


UNIT_TYPE_CHOICES = [('1BHK', '1BHK'), ('2BHK', '2BHK'), ('3BHK', '3BHK'), ('4BHK', '4BHK')]

class Unit(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='units')
    rent_cost = models.DecimalField(max_digits=10, decimal_places=2)
    unit_type = models.CharField(max_length=50, choices=UNIT_TYPE_CHOICES)

    def __str__(self):
        return f"{self.property.name} - {self.unit_type}"

class Tenant(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    document_proofs = models.FileField(upload_to='uploads/')

class RentalInformation(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE,related_name='tenant')
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE,related_name='rentalunit')
    agreement_end_date = models.DateField()
    monthly_rent_date = models.PositiveIntegerField()