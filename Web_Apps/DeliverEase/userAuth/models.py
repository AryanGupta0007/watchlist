from django.db import models

# Create your models here.


# this is the buyer table contains the different details about the buyer
class Buyer(models.Model):
    name = models.CharField(max_length=64)
    email = models.CharField(max_length=64)
    password = models.CharField(max_length=64)
    phone_no = models.CharField(max_length=64)
    address = models.CharField(max_length=64)

    def __repr__(self) -> str:
        return f"{self.name}  {self.id} {self.email} {self.phone_no} " \
               f"{self.email} {self.address}"


# this is the seller table contains the different details about the seller
class Seller(models.Model):
    name = models.CharField(max_length=64)
    email = models.CharField(max_length=64)
    password = models.CharField(max_length=64)
    phone_no = models.CharField(max_length=64)
    address = models.CharField(max_length=100)
    experience = models.CharField(max_length=100)

    def __repr__(self) -> str:
        return f"{self.name}  {self.id} {self.email} {self.experience}" \
               f" {self.phone_no}  {self.address}"
