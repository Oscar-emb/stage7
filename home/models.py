from django.db import models

# Create your models here.
class People(models.Model):
    name = models.CharField(max_length=1000)

    def __str__(self):
        return self.name

class Doctor(models.Model):
    doctor = models.CharField(max_length=10000)
    # A doctor can have many patients so we leave this as a one to many relationship
    users = models.ForeignKey(People, on_delete=models.CASCADE)

    def __str__(self):
        return self.doctor

class Address(models.Model):
    address = models.CharField(max_length=10000)
    # Many people living together could have the same address so we equally leave this as a one to many relationship
    user = models.ForeignKey(People, on_delete=models.CASCADE)

    def __str__(self):
        return self.address

class Bio(models.Model):
    bio = models.CharField(max_length=10000)
    # No two people can be sharing the same bio so we leave this as a one to one relationship
    users = models.OneToOneField(People, on_delete=models.CASCADE)

    def __str__(self):
        return self.bio

class Product(models.Model):
    price = models.CharField(max_length=5000, default=" ")
    brand = models.CharField(max_length=2000, default=" ")
    user = models.OneToOneField(People, on_delete = models.CASCADE)

    def __str__(self):
        return self.brand