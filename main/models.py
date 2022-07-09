from django.db import models
from simple_history.models import HistoricalRecords

# Create your models here.

class Order(models.Model):
  # date = models.DateTimeField(blank=True)
  products = models.TextField()
  # courier = models.ForeignKey("Courier", on_delete=models.CASCADE, blank=True)
  # person = models.ForeignKey("Customer", on_delete=models.CASCADE, blank=True)
  # is_delivered = models.BooleanField(blank=True)
  history = HistoricalRecords()

  def __str__(self):
      return 'Заказ ' + str(self.id)
  

class Courier(models.Model):
  name = models.CharField(max_length=30)
  middlename = models.CharField(max_length=40, blank=True)
  surname = models.CharField(max_length=40)
  phone = models.CharField(max_length=20)
  is_working = models.BooleanField()
  history = HistoricalRecords()

  def __str__(self):
      return self.name + ' ' + self.surname

class Customer(models.Model):
  name = models.CharField(max_length=30)
  middlename = models.CharField(max_length=40, blank=True)
  surname = models.CharField(max_length=40)
  email = models.CharField(max_length=30)
  phone = models.CharField(max_length=20)
  address = models.CharField(max_length=100)
  history = HistoricalRecords()

  # def __str__(self):
      # return self.name + ' ' + self.surname